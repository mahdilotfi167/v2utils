from django.apps import AppConfig
import subprocess


class ProxyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proxy'

    # def ready(self) -> None:
        # run v2ray
        # subprocess.Popen(['v2ray', '-config', '/etc/v2ray/config.json'])
        # return super().ready()