from django.contrib import admin
from proxy import services
from proxy.models import *
from jet.admin import CompactInline
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicChildModelFilter,
    StackedPolymorphicInline,
    PolymorphicInlineSupportMixin,
)


TRAFFIC_FIELDSETS = (
    'enabled',
    'max',
    'up',
    'down',
    'expires_at',
    'reset_period',
    'last_reset',
)

INBOUND_FIELDSETS = (
    'tag',
    'listen',
    'port',
    'sniffing_enabled',
    'sniffing_dest_override',
    'group',
)


@admin.action
def reset_traffics(modeladmin, request, queryset):
    services.reset_traffic(queryset)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


class AddressInline(admin.TabularInline):
    extra = 1
    model = Address


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'up', 'down')
    readonly_fields = ('up', 'down', 'last_reset')
    inlines = (AddressInline,)
    actions = (reset_traffics,)
    fieldsets = (
        (None, {
            "fields": (
                'title',
            ),
        }),
        ('Traffic', {
            "fields": TRAFFIC_FIELDSETS
        })
    )
    


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


@admin.register(Vmess)
class VmessAdmin(PolymorphicInlineSupportMixin, InboundChildAdmin):
    base_model = Vmess
    inlines = (TransportInline,)
    readonly_fields = ('up', 'down', 'last_reset')
    fieldsets = (
        (None, {
            "fields": (
                *INBOUND_FIELDSETS,
            ),
        }),
        ('Traffic', {
            "fields": TRAFFIC_FIELDSETS
        })
    )
    
    
@admin.register(Trojan)
class TrojanAdmin(PolymorphicInlineSupportMixin, InboundChildAdmin):
    base_model = Trojan
    inlines = (TransportInline,)
    readonly_fields = ('up', 'down', 'last_reset')
    fieldsets = (
        (None, {
            "fields": (
                *INBOUND_FIELDSETS,
            ),
        }),
        ('Traffic', {
            "fields": TRAFFIC_FIELDSETS
        })
    )


class FallbackInline(admin.StackedInline):
    model = Fallback
    extra = 0


@admin.register(Vless)
class VlessAdmin(PolymorphicInlineSupportMixin, InboundChildAdmin):
    base_model = Vless
    inlines = (TransportInline, FallbackInline)
    readonly_fields = ('up', 'down', 'last_reset')
    fieldsets = (
        (None, {
            "fields": (
                *INBOUND_FIELDSETS,
                'decryption',
            ),
        }),
        ('Traffic', {
            "fields": TRAFFIC_FIELDSETS
        })
    )


@admin.register(Inbound)
class InboundAdmin(PolymorphicInlineSupportMixin, PolymorphicParentModelAdmin):
    base_model = Inbound
    actions = (reset_traffics,)
    child_models = (Vmess, Vless, Trojan)
    list_filter = (PolymorphicChildModelFilter,)
    readonly_fields = ('up', 'down', 'last_reset')
    list_display = ('tag', 'up', 'down')
    
    
class MembershipInline(CompactInline):
    model = Membership
    extra = 1
    readonly_fields = ('up', 'down', 'last_reset')
    fieldsets = (
        (None, {
            "fields": (
                'group',
            ),
        }),
        ('Traffic', {
            "fields": TRAFFIC_FIELDSETS
        })
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('up', 'down', 'last_reset')
    actions = (reset_traffics,)
    inlines = (MembershipInline,)
    list_display = ('username', 'up', 'down')
    fieldsets = (
        (None, {
            "fields": (
                'username',
                'uuid',
            ),
        }),
        ('Traffic', {
            "fields": TRAFFIC_FIELDSETS
        })
    )
