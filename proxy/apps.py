from django.apps import AppConfig
import os
import sys


class ProxyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proxy'

    def ready(self) -> None:
        if bool(os.environ.get('RUN_MAIN')):
            from proxy.services import start_v2ray, start_scheduler
            # start_v2ray()
            start_scheduler()