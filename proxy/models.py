from django.db import models
from polymorphic.models import PolymorphicModel
from typing import Iterable


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    uuid = models.UUIDField(unique=True)
    max = models.PositiveBigIntegerField(null=True, blank=True)
    up = models.PositiveBigIntegerField(default=0)
    down = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.__str__()


class Inbound(PolymorphicModel):
    tag = models.CharField(max_length=100, unique=True)
    listen = models.CharField(max_length=255)
    port = models.PositiveIntegerField(blank=True, null=True)
    settings = models.JSONField(blank=True, null=True)
    streamSettings = models.JSONField(blank=True, null=True)
    sniffing = models.JSONField(blank=True, null=True)
    max = models.PositiveBigIntegerField(null=True, blank=True)
    up = models.PositiveBigIntegerField(default=0)
    down = models.PositiveBigIntegerField(default=0)

    class Meta:
        CONFIG_FIELDS = ["tag", "listen", "port", "settings", "streamSettings", "sniffing"]

    @property
    def protocol(self):
        return self.__class__.__name__.lower()

    def get_client_link(self, user: User) -> str:
        raise NotImplementedError()

    def get_client_json(self, user: User) -> str:
        raise NotImplementedError()

    def get_server_config(self, users: Iterable[User]):
        inbound_data = dict()
        inbound_data["settings"] = {}
        # Set necessary configurations
        for field in self.Meta.CONFIG_FIELDS:
            if getattr(self, field) is not None:
                inbound_data[field] = getattr(self, field)
        # Configure clients
        client_data = list()
        for user in users:
            client_data.append({
                "email": "%s@%s" % (user.username, self.tag),
                "id": str(user.uuid),
            })
        inbound_data["settings"]["clients"] = client_data
        return inbound_data

    def __str__(self):
        return self.tag

    def __repr__(self):
        return self.__str__()


class Vmess(Inbound):
    def get_client_link(self, user: User) -> str:
        return ""

    def get_client_json(self, user: User) -> str:
        return ""


class Vless(Inbound):
    def get_client_link(self, user: User) -> str:
        return ""

    def get_client_json(self, user: User) -> str:
        return ""
