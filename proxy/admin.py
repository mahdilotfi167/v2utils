from django.contrib import admin

from proxy.models import *
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter,
    StackedPolymorphicInline,
    PolymorphicInlineSupportMixin,
)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


class TransportInline(StackedPolymorphicInline):
    model = Transport

    class WebSocketInline(StackedPolymorphicInline.Child):
        model = WebSocket

    class HttpInline(StackedPolymorphicInline.Child):
        model = Http

    class TcpInline(StackedPolymorphicInline.Child):
        model = Tcp

    class GrpcInline(StackedPolymorphicInline.Child):
        model = Grpc

    child_inlines = (
        WebSocketInline,
        HttpInline,
        TcpInline,
        GrpcInline,
    )


class InboundChildAdmin(PolymorphicChildModelAdmin):
    base_model = Inbound


class InboundAddressInline(admin.TabularInline):
    extra = 1
    model = InboundAddress


@admin.register(Vmess)
class VmessAdmin(PolymorphicInlineSupportMixin, InboundChildAdmin):
    base_model = Vmess
    inlines = (TransportInline, InboundAddressInline)


class FallbackInline(admin.StackedInline):
    model = Fallback


@admin.register(Vless)
class VlessAdmin(PolymorphicInlineSupportMixin, InboundChildAdmin):
    base_model = Vless
    inlines = (TransportInline, FallbackInline, InboundAddressInline)


@admin.register(Inbound)
class InboundAdmin(PolymorphicInlineSupportMixin, PolymorphicParentModelAdmin):
    base_model = Inbound
    child_models = (Vmess, Vless)
    list_filter = (PolymorphicChildModelFilter,)
    list_display = ('tag', 'up', 'down')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'up', 'down')
