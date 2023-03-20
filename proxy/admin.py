from django.contrib import admin

from proxy.models import *
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter


class InboundChildAdmin(PolymorphicChildModelAdmin):
    base_model = Inbound


@admin.register(Vmess)
class VmessAdmin(InboundChildAdmin):
    base_model = Vmess


@admin.register(Vless)
class VlessAdmin(InboundChildAdmin):
    base_model = Vless


@admin.register(Inbound)
class InboundAdmin(PolymorphicParentModelAdmin):
    base_model = Inbound
    child_models = (Vmess, Vless)
    list_filter = (PolymorphicChildModelFilter,)
