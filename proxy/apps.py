from django.apps import AppConfig


class ProxyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proxy'

    def ready(self) -> None:
        from proxy.services import start_v2ray
        start_v2ray()
