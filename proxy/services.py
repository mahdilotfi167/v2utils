from django.utils import timezone
from v2client.v5.api import V2ray
from proxy.models import *
from django.conf import settings
from django.db.models import F, Q, Value, Prefetch
from utils.schedule import Scheduler

v2api: V2ray = None


def generate_inbounds_config():
    enabled_query = (Q(enabled=True) & 
                     (Q(max__isnull=True) | Q(max__gt=F('up') + F('down'))) & 
                     (Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now())))
    return [*settings.INBOUNDS_CONF] + [
        inbound.get_server_config() for inbound in Inbound.objects.filter(
            enabled_query
        ).prefetch_related( # select_related won't work here, because of polymorphic models
            Prefetch('transport', queryset=Transport.objects.all())
        ).prefetch_related(
            'transport__tls_certificates'
        ).prefetch_related(
            Prefetch('group', queryset=Group.objects.filter(enabled_query).order_by('id'))
        ).prefetch_related(
            Prefetch('group__users', queryset=User.objects.filter(enabled_query).order_by('id'))
        ).order_by('id')
    ]


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
    
    
def reset_traffic(queryset):
    queryset.update(
        up=0,
        down=0,
        last_reset=Value(timezone.now()),
    )


def update_traffics():
    global v2api
    user_traffics = v2api.get_user_traffics(reset=True)
    traffics_by_username = dict()
    traffics_by_tag = dict()
    for traffic in user_traffics:
        username, inbound_tag = traffic.email.split('@')
        up, down = traffics_by_username.get(username, (0, 0))
        traffics_by_username[username] = (up + traffic.up, down + traffic.down)
        traffics_by_tag[inbound_tag] = (up + traffic.up, down + traffic.down)
    reset_traffic(User.objects.filter(last_reset__lte=Value(timezone.now()) - F('reset_period')))
    reset_traffic(Group.objects.filter(last_reset__lte=Value(timezone.now()) - F('reset_period')))
    reset_traffic(Inbound.objects.filter(last_reset__lte=Value(timezone.now()) - F('reset_period')))
    for username, traffic in traffics_by_username.items():
        up, down = traffic
        if up or down:
            User.objects.filter(username=username).update(
                up=F('up') + Value(up),
                down=F('down') + Value(down),
            )
    for tag, traffic in traffics_by_tag.items():
        up, down = traffic
        if up or down:
            Inbound.objects.filter(tag=tag).update(
                up=F('up') + Value(up),
                down=F('down') + Value(down),
            )
            Group.objects.filter(inbounds__tag=tag).update(
                up=F('up') + Value(up),
                down=F('down') + Value(down),
            )


def refresh_v2ray():
    global v2api
    update_traffics()
    config = generate_config()
    v2api.refresh_config(config)


def start_scheduler():
    scheduler = Scheduler()
    scheduler.every(15).seconds.do(refresh_v2ray)
    scheduler.run_continuously()
