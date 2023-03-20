from v2client.v5.api import V2ray
from v2client.v5.client import Client
from proxy.models import Inbound, User
from django.conf import settings

v2api = None
v2client = None


def generate_config():
    Inbound.objects.all()


def make_inbounds():
    users = User.objects.all()
    inbounds = [*settings.INBOUNDS_CONF]
    inbound_fields = ["tag", "listen", "port", "settings", "streamSettings", "sniffing"]
    for inbound in Inbound.objects.all():
        inbound_data = dict()
        inbound_data["settings"] = {}
        # Set necessary configurations
        for field in inbound_fields:
            if getattr(inbound, field) is not None:
                inbound_data[field] = getattr(inbound, field)
        # Configure clients
        client_data = list()
        for user in users:
            client_data.append({
                "email": "%s@%s" % (user.username, inbound.tag),
                "id": str(user.uuid),
            })
        inbound_data["settings"]["clients"] = client_data
        inbounds.append(inbound_data)
    return inbounds


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
    global v2client
    if v2api is None:
        config = make_config()
        v2api = V2ray(settings.V2RAY_BINARY_PATH, config)
    if v2client is None:
        v2client = Client(settings.API_ADDRESS, settings.API_PORT)

    v2api.start()
