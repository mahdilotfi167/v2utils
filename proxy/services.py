from v2client.v5.api import V2ray
from proxy.models import Inbound, User
from django.conf import settings
from django.db.models import F, Q

v2api = None


def generate_config():
    Inbound.objects.all()


def make_inbounds():
    user_query = Q(enabled=True) & (Q(max__isnull=True) | Q(max__gt=F('up') + F('down')))
    users = User.objects.filter(user_query).order_by('id')
    return [*settings.INBOUNDS_CONF] + [inbound.get_server_config(users) for inbound in
                                        Inbound.objects.all().order_by('id')]


def make_config():
    return {
        "log": settings.LOG_CONF,
        "api": settings.API_CONF,
        "stats": settings.STATS_CONF,
        "policy": settings.POLICY_CONF,
        "inbounds": make_inbounds(),
        "outbounds": settings.OUTBOUNDS_CONF,
        "routing": settings.ROUTING_CONF,
    }


def start_v2ray():
    global v2api
    config = make_config()
    if v2api is None:
        v2api = V2ray(settings.V2RAY_BINARY_PATH, settings.API_ADDRESS, settings.API_PORT)
    v2api.start(config)
