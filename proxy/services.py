from v2client.v5.api import V2ray
from proxy.models import Inbound, User
from django.conf import settings
from django.db.models import F, Q, Value
from utils.schedule import Scheduler

v2api: V2ray


def generate_inbounds_config():
    user_query = Q(enabled=True) & (Q(max__isnull=True) | Q(max__gt=F('up') + F('down')))
    users = User.objects.filter(user_query).order_by('id')
    return [*settings.INBOUNDS_CONF] + [inbound.get_server_config(users) for inbound in
                                        Inbound.objects.all().order_by('id')]


def generate_config():
    return {
        "log": settings.LOG_CONF,
        "api": settings.API_CONF,
        "stats": settings.STATS_CONF,
        "policy": settings.POLICY_CONF,
        "inbounds": generate_inbounds_config(),
        "outbounds": settings.OUTBOUNDS_CONF,
        "routing": settings.ROUTING_CONF,
    }


def start_v2ray():
    global v2api
    config = generate_config()
    if v2api is None:
        v2api = V2ray(settings.V2RAY_BINARY_PATH, settings.API_ADDRESS, settings.API_PORT)
    v2api.start(config)


def update_traffics():
    user_traffics = v2api.get_user_traffics(reset=True)
    traffics_by_username = dict()
    for traffic in user_traffics:
        username, _ = traffic.email.split('@')
        up, down = traffics_by_username.get(username, (0, 0))
        traffics_by_username[username] = (up + traffic.up, down + traffic.down)
    for username, traffic in traffics_by_username.items():
        up, down = traffic
        if not up and not down:
            continue
        User.objects.filter(
            username=username
        ).update(
            up=F('up') + Value(up),
            down=F('down') + Value(down),
        )


def refresh_v2ray():
    update_traffics()
    config = generate_config()
    v2api.refresh_config(config)


def start_scheduler():
    scheduler = Scheduler()
    scheduler.every(20).seconds.do(refresh_v2ray)
    scheduler.run_continuously()
