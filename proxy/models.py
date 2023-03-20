from django.db import models
from polymorphic.models import PolymorphicModel


class User(models.Model):
    username = models.CharField(max_length=100)
    uuid = models.UUIDField()
    max = models.PositiveBigIntegerField(null=True, blank=True)
    up = models.PositiveBigIntegerField(default=0)
    down = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.__str__()


class Inbound(PolymorphicModel):
    key = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, blank=True, null=True)
    listen = models.CharField(max_length=255)
    port = models.PositiveIntegerField(blank=True, null=True)
    settings = models.JSONField(blank=True, null=True)
    streamSettings = models.JSONField(blank=True, null=True)
    sniffing = models.JSONField(blank=True, null=True)
    max = models.PositiveBigIntegerField(null=True, blank=True)
    up = models.PositiveBigIntegerField(default=0)
    down = models.PositiveBigIntegerField(default=0)

    @property
    def protocol(self):
        return self.__class__.__name__.lower()

    def get_link(self, user: User) -> str:
        raise NotImplementedError()

    def get_json(self, user: User) -> str:
        raise NotImplementedError()

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.__str__()


class Vmess(Inbound):
    def get_link(self, user: User) -> str:
        return ""

    def get_json(self, user: User) -> str:
        return ""


class Vless(Inbound):
    def get_link(self, user: User) -> str:
        return ""

    def get_json(self, user: User) -> str:
        return ""
