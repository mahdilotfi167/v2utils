from django.db import models
from polymorphic.models import PolymorphicModel
from typing import Iterable
from django.conf import settings


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
    sniffing_enabled = models.BooleanField(default=False)
    sniffing_dest_override = models.CharField(max_length=255, blank=True, null=True)
    max = models.PositiveBigIntegerField(null=True, blank=True)
    up = models.PositiveBigIntegerField(default=0)
    down = models.PositiveBigIntegerField(default=0)

    @property
    def protocol(self):
        return self.__class__.__name__.lower()

    def get_client_link(self, user: User) -> str:
        raise NotImplementedError()

    def get_client_json(self, user: User) -> str:
        raise NotImplementedError()

    def _get_sniffing_config(self):
        sniffing = {'enabled': self.sniffing_enabled}
        if self.sniffing_dest_override:
            sniffing['destOverride'] = [do.strip() for do in self.sniffing_dest_override.split(',')]
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

    def get_server_config(self, users: Iterable[User]):
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


class Vmess(Inbound):
    def get_client_link(self, user: User) -> str:
        return ""

    def get_client_json(self, user: User) -> str:
        return ""


class Vless(Inbound):
    decryption = models.CharField(max_length=100, blank=True, null=True)

    def get_client_link(self, user: User) -> str:
        return ""

    def get_client_json(self, user: User) -> str:
        return ""

    def _get_settings_config(self, users: Iterable[User]):
        res = {
            **super()._get_settings_config(users),
            'decryption': self.decryption or 'none',
        }
        if self.fallbacks.exists():
            res['fallbacks'] = [fb.get_server_config() for fb in self.fallbacks.all()]
        return res


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
            'certificateFile': self.cert_path,
            'keyFile': self.key_path,
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
    tls_certificates = models.ManyToManyField(Certificate)
    inbound = models.OneToOneField(Inbound, models.CASCADE, related_name='transport')

    def get_server_config(self):
        stream_settings = dict()
        stream_settings['network'] = self.network
        if self.tls:
            stream_settings['security'] = 'tls'
            certificates = [c.get_server_config() for c in self.tls_certificates.all()]
            alpn = [a.strip() for a in self.tls_alpn.split(',')]
            stream_settings['tlsSettings'] = {
                'certificates': certificates,
                'alpn': alpn,
            }
        else:
            stream_settings['security'] = 'none'
        return stream_settings


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


class Tcp(Transport):
    network = 'tcp'
    accept_proxy_protocol = models.BooleanField(default=False)
    header_type = models.CharField(max_length=100, default="none")
    header_request_path = models.CharField(max_length=255, null=True, blank=True)

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


class Fallback(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    alpn = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    dest = models.CharField(max_length=100)
    xver = models.IntegerField(blank=True, null=True)
    inbound = models.ForeignKey(Vless, on_delete=models.CASCADE, related_name='fallbacks')

    def get_server_config(self):
        res = {'dest': self.dest}
        for field in ['name', 'alpn', 'path', 'xver']:
            value = getattr(self, field)
            if value is not None and value != '':
                res[field] = value
        return res
