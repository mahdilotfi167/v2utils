from .base import BASE_DIR

CERT_FILES_BASE_DIR = BASE_DIR / '.certs'

V2RAY_BINARY_PATH = "/usr/local/bin/v2ray"

API_PORT = 10085
API_ADDRESS = "127.0.0.1"


LOG_BASE_DIR = BASE_DIR / 'logs'
LOG_BASE_DIR.mkdir(parents=True, exist_ok=True)

LOG_CONF = {
    "loglevel": "warning",
    "access": str(LOG_BASE_DIR / 'access.log'),
}

API_CONF = {
    "services": [
        "HandlerService",
        "LoggerService",
        "StatsService",
    ],
    "tag": "api",
}

STATS_CONF = {}

POLICY_CONF = {
    "levels": {
        "0": {
            "statsUserUplink": True,
            "statsUserDownlink": True,
        }
    },
    "system": {
        "statsInboundUplink": True,
        "statsInboundDownlink": True,
        "statsOutboundUplink": True,
        "statsOutboundDownlink": True,
    },
}

INBOUNDS_CONF = [
    {
        "listen": API_ADDRESS,
        "port": API_PORT,
        "protocol": "dokodemo-door",
        "settings": {
            "address": API_ADDRESS,
        },
        "tag": "api",
        "sniffing": None,
    }
]

OUTBOUNDS_CONF = [
    {
        "protocol": "freedom",
        "settings": {},
    },
    {
        "protocol": "blackhole",
        "tag": "blocked",
    },
    {
        "tag": "DNS-Internal",
        "protocol": "dns",
        "settings": {
            "address": "127.0.0.53",
            "port": 53,
        },
    },
]

ROUTING_CONF = {
    "domainStrategy": "AsIs",
    "rules": [
        {
            "inboundTag": [
                "api",
            ],
            "outboundTag": "api",
            "type": "field",
        },
        {
            "type": "field",
            "outboundTag": "blocked",
            "ip": [
                "geoip:private",
            ],
        },
        {
            "type": "field",
            "outboundTag": "blocked",
            "protocol": [
                "bittorrent",
            ],
        },
    ]
}
