from django.apps import AppConfig
import os


class ProxyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proxy'

    def ready(self) -> None:
        from django.conf import settings
        from proxy.services import start_v2ray, start_scheduler
        if bool(os.environ.get('RUN_MAIN')) or settings.IS_PROD:
            start_v2ray()
            start_scheduler()
