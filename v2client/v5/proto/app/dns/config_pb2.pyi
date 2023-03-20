from common.net import address_pb2 as _address_pb2
from common.net import destination_pb2 as _destination_pb2
from app.router.routercommon import common_pb2 as _common_pb2
from app.dns.fakedns import fakedns_pb2 as _fakedns_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CacheDisabled: CacheStrategy
CacheEnabled: CacheStrategy
DESCRIPTOR: _descriptor.FileDescriptor
Disabled: FallbackStrategy
DisabledIfAnyMatch: FallbackStrategy
Enabled: FallbackStrategy
Full: DomainMatchingType
Keyword: DomainMatchingType
Regex: DomainMatchingType
Subdomain: DomainMatchingType
USE_IP: QueryStrategy
USE_IP4: QueryStrategy
USE_IP6: QueryStrategy

class Config(_message.Message):
    __slots__ = ["Hosts", "NameServers", "cache_strategy", "client_ip", "disableCache", "disableFallback", "disableFallbackIfMatch", "domain_matcher", "fake_dns", "fallback_strategy", "name_server", "query_strategy", "static_hosts", "tag"]
    class HostsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _address_pb2.IPOrDomain
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ...) -> None: ...
    CACHE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    DISABLECACHE_FIELD_NUMBER: _ClassVar[int]
    DISABLEFALLBACKIFMATCH_FIELD_NUMBER: _ClassVar[int]
    DISABLEFALLBACK_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MATCHER_FIELD_NUMBER: _ClassVar[int]
    FAKE_DNS_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    Hosts: _containers.MessageMap[str, _address_pb2.IPOrDomain]
    NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
    NAME_SERVER_FIELD_NUMBER: _ClassVar[int]
    NameServers: _containers.RepeatedCompositeFieldContainer[_destination_pb2.Endpoint]
    QUERY_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    STATIC_HOSTS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    cache_strategy: CacheStrategy
    client_ip: bytes
    disableCache: bool
    disableFallback: bool
    disableFallbackIfMatch: bool
    domain_matcher: str
    fake_dns: _fakedns_pb2.FakeDnsPoolMulti
    fallback_strategy: FallbackStrategy
    name_server: _containers.RepeatedCompositeFieldContainer[NameServer]
    query_strategy: QueryStrategy
    static_hosts: _containers.RepeatedCompositeFieldContainer[HostMapping]
    tag: str
    def __init__(self, NameServers: _Optional[_Iterable[_Union[_destination_pb2.Endpoint, _Mapping]]] = ..., name_server: _Optional[_Iterable[_Union[NameServer, _Mapping]]] = ..., Hosts: _Optional[_Mapping[str, _address_pb2.IPOrDomain]] = ..., client_ip: _Optional[bytes] = ..., static_hosts: _Optional[_Iterable[_Union[HostMapping, _Mapping]]] = ..., fake_dns: _Optional[_Union[_fakedns_pb2.FakeDnsPoolMulti, _Mapping]] = ..., tag: _Optional[str] = ..., domain_matcher: _Optional[str] = ..., disableCache: bool = ..., disableFallback: bool = ..., disableFallbackIfMatch: bool = ..., query_strategy: _Optional[_Union[QueryStrategy, str]] = ..., cache_strategy: _Optional[_Union[CacheStrategy, str]] = ..., fallback_strategy: _Optional[_Union[FallbackStrategy, str]] = ...) -> None: ...

class HostMapping(_message.Message):
    __slots__ = ["domain", "ip", "proxied_domain", "type"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PROXIED_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    domain: str
    ip: _containers.RepeatedScalarFieldContainer[bytes]
    proxied_domain: str
    type: DomainMatchingType
    def __init__(self, type: _Optional[_Union[DomainMatchingType, str]] = ..., domain: _Optional[str] = ..., ip: _Optional[_Iterable[bytes]] = ..., proxied_domain: _Optional[str] = ...) -> None: ...

class NameServer(_message.Message):
    __slots__ = ["address", "cache_strategy", "client_ip", "fake_dns", "fallback_strategy", "geoip", "original_rules", "prioritized_domain", "query_strategy", "skipFallback", "tag"]
    class OriginalRule(_message.Message):
        __slots__ = ["rule", "size"]
        RULE_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        rule: str
        size: int
        def __init__(self, rule: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...
    class PriorityDomain(_message.Message):
        __slots__ = ["domain", "type"]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        domain: str
        type: DomainMatchingType
        def __init__(self, type: _Optional[_Union[DomainMatchingType, str]] = ..., domain: _Optional[str] = ...) -> None: ...
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CACHE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    FAKE_DNS_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    GEOIP_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_RULES_FIELD_NUMBER: _ClassVar[int]
    PRIORITIZED_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    QUERY_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SKIPFALLBACK_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    address: _destination_pb2.Endpoint
    cache_strategy: CacheStrategy
    client_ip: bytes
    fake_dns: _fakedns_pb2.FakeDnsPoolMulti
    fallback_strategy: FallbackStrategy
    geoip: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoIP]
    original_rules: _containers.RepeatedCompositeFieldContainer[NameServer.OriginalRule]
    prioritized_domain: _containers.RepeatedCompositeFieldContainer[NameServer.PriorityDomain]
    query_strategy: QueryStrategy
    skipFallback: bool
    tag: str
    def __init__(self, address: _Optional[_Union[_destination_pb2.Endpoint, _Mapping]] = ..., client_ip: _Optional[bytes] = ..., tag: _Optional[str] = ..., prioritized_domain: _Optional[_Iterable[_Union[NameServer.PriorityDomain, _Mapping]]] = ..., geoip: _Optional[_Iterable[_Union[_common_pb2.GeoIP, _Mapping]]] = ..., original_rules: _Optional[_Iterable[_Union[NameServer.OriginalRule, _Mapping]]] = ..., fake_dns: _Optional[_Union[_fakedns_pb2.FakeDnsPoolMulti, _Mapping]] = ..., skipFallback: bool = ..., query_strategy: _Optional[_Union[QueryStrategy, str]] = ..., cache_strategy: _Optional[_Union[CacheStrategy, str]] = ..., fallback_strategy: _Optional[_Union[FallbackStrategy, str]] = ...) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = ["cache_strategy", "client_ip", "disableCache", "disableFallback", "disableFallbackIfMatch", "domain_matcher", "fake_dns", "fallback_strategy", "name_server", "query_strategy", "static_hosts", "tag"]
    CACHE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    DISABLECACHE_FIELD_NUMBER: _ClassVar[int]
    DISABLEFALLBACKIFMATCH_FIELD_NUMBER: _ClassVar[int]
    DISABLEFALLBACK_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MATCHER_FIELD_NUMBER: _ClassVar[int]
    FAKE_DNS_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    NAME_SERVER_FIELD_NUMBER: _ClassVar[int]
    QUERY_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    STATIC_HOSTS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    cache_strategy: CacheStrategy
    client_ip: str
    disableCache: bool
    disableFallback: bool
    disableFallbackIfMatch: bool
    domain_matcher: str
    fake_dns: _fakedns_pb2.FakeDnsPoolMulti
    fallback_strategy: FallbackStrategy
    name_server: _containers.RepeatedCompositeFieldContainer[SimplifiedNameServer]
    query_strategy: QueryStrategy
    static_hosts: _containers.RepeatedCompositeFieldContainer[SimplifiedHostMapping]
    tag: str
    def __init__(self, name_server: _Optional[_Iterable[_Union[SimplifiedNameServer, _Mapping]]] = ..., client_ip: _Optional[str] = ..., static_hosts: _Optional[_Iterable[_Union[SimplifiedHostMapping, _Mapping]]] = ..., fake_dns: _Optional[_Union[_fakedns_pb2.FakeDnsPoolMulti, _Mapping]] = ..., tag: _Optional[str] = ..., domain_matcher: _Optional[str] = ..., disableCache: bool = ..., disableFallback: bool = ..., disableFallbackIfMatch: bool = ..., query_strategy: _Optional[_Union[QueryStrategy, str]] = ..., cache_strategy: _Optional[_Union[CacheStrategy, str]] = ..., fallback_strategy: _Optional[_Union[FallbackStrategy, str]] = ...) -> None: ...

class SimplifiedHostMapping(_message.Message):
    __slots__ = ["domain", "ip", "proxied_domain", "type"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PROXIED_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    domain: str
    ip: _containers.RepeatedScalarFieldContainer[str]
    proxied_domain: str
    type: DomainMatchingType
    def __init__(self, type: _Optional[_Union[DomainMatchingType, str]] = ..., domain: _Optional[str] = ..., ip: _Optional[_Iterable[str]] = ..., proxied_domain: _Optional[str] = ...) -> None: ...

class SimplifiedNameServer(_message.Message):
    __slots__ = ["address", "cache_strategy", "client_ip", "fake_dns", "fallback_strategy", "geoip", "original_rules", "prioritized_domain", "query_strategy", "skipFallback", "tag"]
    class OriginalRule(_message.Message):
        __slots__ = ["rule", "size"]
        RULE_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        rule: str
        size: int
        def __init__(self, rule: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...
    class PriorityDomain(_message.Message):
        __slots__ = ["domain", "type"]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        domain: str
        type: DomainMatchingType
        def __init__(self, type: _Optional[_Union[DomainMatchingType, str]] = ..., domain: _Optional[str] = ...) -> None: ...
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CACHE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    FAKE_DNS_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    GEOIP_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_RULES_FIELD_NUMBER: _ClassVar[int]
    PRIORITIZED_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    QUERY_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SKIPFALLBACK_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    address: _destination_pb2.Endpoint
    cache_strategy: CacheStrategy
    client_ip: str
    fake_dns: _fakedns_pb2.FakeDnsPoolMulti
    fallback_strategy: FallbackStrategy
    geoip: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoIP]
    original_rules: _containers.RepeatedCompositeFieldContainer[SimplifiedNameServer.OriginalRule]
    prioritized_domain: _containers.RepeatedCompositeFieldContainer[SimplifiedNameServer.PriorityDomain]
    query_strategy: QueryStrategy
    skipFallback: bool
    tag: str
    def __init__(self, address: _Optional[_Union[_destination_pb2.Endpoint, _Mapping]] = ..., client_ip: _Optional[str] = ..., tag: _Optional[str] = ..., prioritized_domain: _Optional[_Iterable[_Union[SimplifiedNameServer.PriorityDomain, _Mapping]]] = ..., geoip: _Optional[_Iterable[_Union[_common_pb2.GeoIP, _Mapping]]] = ..., original_rules: _Optional[_Iterable[_Union[SimplifiedNameServer.OriginalRule, _Mapping]]] = ..., fake_dns: _Optional[_Union[_fakedns_pb2.FakeDnsPoolMulti, _Mapping]] = ..., skipFallback: bool = ..., query_strategy: _Optional[_Union[QueryStrategy, str]] = ..., cache_strategy: _Optional[_Union[CacheStrategy, str]] = ..., fallback_strategy: _Optional[_Union[FallbackStrategy, str]] = ...) -> None: ...

class DomainMatchingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class QueryStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CacheStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FallbackStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
