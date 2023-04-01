from django.db import models
from polymorphic.models import PolymorphicModel
from typing import Iterable
from django.db.models import Q, F
from django.utils import timezone
from django.conf import settings
from uuid import uuid4
from base64 import b64encode
from json import dumps


class TrafficStats(models.Model):
    enabled = models.BooleanField(default=True)
    max = models.PositiveBigIntegerField(null=True, blank=True)
    up = models.PositiveBigIntegerField(default=0)
    down = models.PositiveBigIntegerField(default=0)
    expires_at = models.DateTimeField(null=True, blank=True)
    last_reset = models.DateTimeField(auto_now_add=True)
    reset_period = models.DurationField(null=True, blank=True)
    
    ENABLED_FILTER = (Q(enabled=True) & 
                     (Q(max__isnull=True) | Q(max__gt=F('up') + F('down'))) & 
                     (Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now())))

    class Meta:
        abstract = True


class Group(TrafficStats):
    title = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField('User', through='Membership', related_name='groups')
    
    def get_client_links(self, user):
        res = []
        for address in self.public_addresses.all():
            res.extend(inbound.get_client_link(address.address, address.port, user) for inbound in self.inbounds.all())
        return res

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class User(TrafficStats):
    username = models.CharField(max_length=100, unique=True)
    uuid = models.UUIDField(unique=True, default=uuid4)
    
    def get_server_links(self):
        res = []
        groups = [membership.group for membership in self.memberships.all()]
        for group in groups:
            res.extend(group.get_client_links(self))
        return res

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.__str__()


class Membership(TrafficStats):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='memberships')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='memberships')

    def __str__(self):
        return self.group.__str__()

    def __repr__(self):
        return self.__str__()


class Inbound(PolymorphicModel, TrafficStats):
    tag = models.CharField(max_length=100, unique=True)
    listen = models.CharField(max_length=255)
    port = models.PositiveIntegerField(blank=True, null=True)
    sniffing_enabled = models.BooleanField(default=False)
    sniffing_dest_override = models.CharField(
        max_length=255, blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='inbounds', blank=True, null=True)
    name = models.CharField(max_length=100, default="", blank=True)
    sni = models.CharField(max_length=255, default="", blank=True)

    @property
    def protocol(self):
        return self.__class__.__name__.lower()

    def get_client_link(self, domain: str, port: int, user: User) -> str:
        raise NotImplementedError()

    def get_client_json(self, user: User) -> str:
        raise NotImplementedError()

    def _get_sniffing_config(self):
        sniffing = {'enabled': self.sniffing_enabled}
        if self.sniffing_dest_override:
            sniffing['destOverride'] = [do.strip()
                                        for do in self.sniffing_dest_override.split(',')]
        return sniffing

    def _get_settings_config(self, users: Iterable[User]):
        clients = list()
        for user in users:
            clients.append({
                "email": "%s@%s" % (user.username, self.tag),
                "id": str(user.uuid),
            })
        return {
            'clients': clients,
        }

    def get_server_config(self):
        users = [
            membership.user for membership in self.group.memberships.all()
        ] if self.group else User.objects.none()

        inbound_config = {'listen': self.listen, 'protocol': self.protocol}

        if self.tag:
            inbound_config['tag'] = self.tag
        if self.port:
            inbound_config['port'] = self.port

        inbound_config['streamSettings'] = self.transport.get_server_config()

        inbound_config["settings"] = self._get_settings_config(users)

        inbound_config['sniffing'] = self._get_sniffing_config()

        return inbound_config

    def __str__(self):
        return self.tag

    def __repr__(self):
        return self.__str__()


class Address(models.Model):
    address = models.CharField(max_length=255)
    port = models.PositiveIntegerField(blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='public_addresses')


class Vmess(Inbound):
    def get_client_link(self, domain: str, port: int, user: User) -> str:
        transport_props = self.transport.get_link_props() if self.transport else {}
        props = {
            "add": domain,
            "aid": "0",
            "host": "",
            "id": str(user.uuid),
            "net": transport_props.get('network', ''),
            "path": transport_props.get('path', '') or transport_props.get('serviceName', ''),
            "port": str(port or self.port),
            "ps": self.name or self.tag,
            "scy": "none",
            "sni": self.sni,
            "alpn": ','.join(transport_props.get('alpn', [])),
            "tls": "tls" if transport_props.get('tls', False) else "",
            "type": transport_props.get('type', ''),
            "v": "2",
        }
        return "vmess://%s" % b64encode(dumps(props).encode('utf-8')).decode('utf-8')

    def get_client_json(self, user: User) -> str:
        return ""


class Vless(Inbound):
    decryption = models.CharField(max_length=100, blank=True, null=True)

    def get_client_link(self, domain: str, port: int, user: User) -> str:
        transport_props = self.transport.get_link_props() if self.transport else {}
        props = {
            'security': 'tls' if transport_props.get('tls', False) else '',
            'type': transport_props.get('network'),
            'serviceName': transport_props.get('serviceName', ''),
            'path': transport_props.get('path', ''),
            'sni': self.sni,
        }
        query = '&'.join("%s=%s" % (k, v) for k, v in props.items() if v)
        return 'vless://%s@%s:%d?%s#%s' % (user.uuid, domain, port or self.port, query, self.name or self.tag)

    def get_client_json(self, user: User) -> str:
        return ""

    def _get_settings_config(self, users: Iterable[User]):
        res = {
            **super()._get_settings_config(users),
            'decryption': self.decryption or 'none',
        }
        if self.fallbacks.exists():
            res['fallbacks'] = [fb.get_server_config()
                                for fb in self.fallbacks.all()]
        return res


class Trojan(Inbound):
    def get_client_link(self, domain: str, port: int, user: User) -> str:
        transport_props = self.transport.get_link_props() if self.transport else {}
        props = {
            'security': 'tls' if transport_props.get('tls', False) else '',
            'type': transport_props.get('network'),
            'serviceName': transport_props.get('serviceName', ''),
            'path': transport_props.get('path', ''),
            'sni': self.sni,
        }
        query = '&'.join("%s=%s" % (k, v) for k, v in props.items() if v)
        return 'trojan://%s@%s:%d?%s#%s' % (user.uuid, domain, port or self.port, query, self.name or self.tag)
    
    def get_client_json(self, user: User) -> str:
        return ""
    
    def _get_settings_config(self, users: Iterable[User]):
        clients = list()
        for user in users:
            clients.append({
                "email": "%s@%s" % (user.username, self.tag),
                "password": str(user.uuid),
            })
        return {
            'clients': clients,
        }


class Certificate(models.Model):
    domain = models.CharField(max_length=255)
    cert = models.TextField()
    key = models.TextField()

    @property
    def base_path(self):
        return settings.CERT_FILES_BASE_DIR / str(self.id)

    @property
    def cert_path(self):
        return self.base_path / 'cert.pem'

    @property
    def key_path(self):
        return self.base_path / 'key.pem'

    def get_server_config(self):
        return {
            'certificateFile': str(self.cert_path),
            'keyFile': str(self.key_path),
        }

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.base_path.mkdir(parents=True, exist_ok=True)
        with open(self.cert_path, 'w') as f:
            f.write(self.cert)
        with open(self.key_path, 'w') as f:
            f.write(self.key)

    def __str__(self):
        return self.domain


class Transport(PolymorphicModel):
    network = ''
    tls = models.BooleanField(default=False)
    tls_alpn = models.CharField(max_length=255, blank=True, null=True)
    tls_certificates = models.ManyToManyField(Certificate, blank=True)
    inbound = models.OneToOneField(
        Inbound, models.CASCADE, related_name='transport')

    def get_server_config(self):
        stream_settings = dict()
        stream_settings['network'] = self.network
        if self.tls:
            stream_settings['security'] = 'tls'
            certificates = [c.get_server_config()
                            for c in self.tls_certificates.all()]
            stream_settings['tlsSettings'] = {
                'certificates': certificates,
                'alpn': self.alpn,
            }
        else:
            stream_settings['security'] = 'none'
        return stream_settings
    
    @property
    def alpn(self):
        if not self.tls_alpn:
            return []
        return [a.strip() for a in self.tls_alpn.split(',')]
    
    def get_link_props(self):
        return {
            "network": self.network,
            "tls": self.tls,
            "alpn": self.alpn,
        }


class WebSocket(Transport):
    network = 'ws'
    accept_proxy_protocol = models.BooleanField(default=False)
    path = models.CharField(max_length=255)

    def get_server_config(self):
        return {
            **super().get_server_config(),
            'wsSettings': {
                'acceptProxyProtocol': self.accept_proxy_protocol,
                'path': self.path,
            },
        }
        
    def get_link_props(self):
        return {
            **super().get_link_props(),
            'path': self.path,
        }


class Http(Transport):
    network = 'h2'
    path = models.CharField(max_length=255)

    def get_server_config(self):
        return {
            **super().get_server_config(),
            'httpSettings': {
                'path': self.path,
            },
        }
        
    def get_link_props(self):
        return {
            **super().get_link_props(),
            'path': self.path,
        }


class Tcp(Transport):
    network = 'tcp'
    accept_proxy_protocol = models.BooleanField(default=False)
    header_type = models.CharField(max_length=100, default="none")
    header_request_path = models.CharField(
        max_length=255, null=True, blank=True)

    def get_server_config(self):
        tcp_settings = {
            'acceptProxyProtocol': self.accept_proxy_protocol,
            'header': {
                'type': self.header_type,
            },
        }
        if self.header_request_path:
            paths = [rp.strip() for rp in self.header_request_path.split(',')]
            tcp_settings['header']['request'] = {'path': paths}
        return {
            **super().get_server_config(),
            'tcpSettings': tcp_settings,
        }
    
    def get_link_props(self):
        return {
            **super().get_link_props(),
            'path': self.header_request_path,
            'type': self.header_type,
        }


class Grpc(Transport):
    network = 'grpc'
    service_name = models.CharField(max_length=255)

    def get_server_config(self):
        return {
            **super().get_server_config(),
            'grpcSettings': {
                'serviceName': self.service_name,
            },
        }

    def get_link_props(self):
        return {
            **super().get_link_props(),
            'serviceName': self.service_name,
        }


class Fallback(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    alpn = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    dest = models.CharField(max_length=100)
    xver = models.IntegerField(blank=True, null=True)
    inbound = models.ForeignKey(
        Vless, on_delete=models.CASCADE, related_name='fallbacks')

    def get_server_config(self):
        res = {'dest': self.dest}
        for field in ['name', 'alpn', 'path', 'xver']:
            value = getattr(self, field)
            if value is not None and value != '':
                res[field] = value
        return res
