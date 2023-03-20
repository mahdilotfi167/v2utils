from google.protobuf import any_pb2 as _any_pb2
from common.net import port_pb2 as _port_pb2
from common.net import network_pb2 as _network_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from app.router.routercommon import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AsIs: DomainStrategy
DESCRIPTOR: _descriptor.FileDescriptor
IpIfNonMatch: DomainStrategy
IpOnDemand: DomainStrategy
UseIp: DomainStrategy

class BalancingRule(_message.Message):
    __slots__ = ["fallback_tag", "outbound_selector", "strategy", "strategy_settings", "tag"]
    FALLBACK_TAG_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    fallback_tag: str
    outbound_selector: _containers.RepeatedScalarFieldContainer[str]
    strategy: str
    strategy_settings: _any_pb2.Any
    tag: str
    def __init__(self, tag: _Optional[str] = ..., outbound_selector: _Optional[_Iterable[str]] = ..., strategy: _Optional[str] = ..., strategy_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., fallback_tag: _Optional[str] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["balancing_rule", "domain_strategy", "rule"]
    BALANCING_RULE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    balancing_rule: _containers.RepeatedCompositeFieldContainer[BalancingRule]
    domain_strategy: DomainStrategy
    rule: _containers.RepeatedCompositeFieldContainer[RoutingRule]
    def __init__(self, domain_strategy: _Optional[_Union[DomainStrategy, str]] = ..., rule: _Optional[_Iterable[_Union[RoutingRule, _Mapping]]] = ..., balancing_rule: _Optional[_Iterable[_Union[BalancingRule, _Mapping]]] = ...) -> None: ...

class RoutingRule(_message.Message):
    __slots__ = ["attributes", "balancing_tag", "cidr", "domain", "domain_matcher", "geo_domain", "geoip", "inbound_tag", "network_list", "networks", "port_list", "port_range", "protocol", "source_cidr", "source_geoip", "source_port_list", "tag", "user_email"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    BALANCING_TAG_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MATCHER_FIELD_NUMBER: _ClassVar[int]
    GEOIP_FIELD_NUMBER: _ClassVar[int]
    GEO_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    INBOUND_TAG_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_LIST_FIELD_NUMBER: _ClassVar[int]
    PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    PORT_RANGE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CIDR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GEOIP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    attributes: str
    balancing_tag: str
    cidr: _containers.RepeatedCompositeFieldContainer[_common_pb2.CIDR]
    domain: _containers.RepeatedCompositeFieldContainer[_common_pb2.Domain]
    domain_matcher: str
    geo_domain: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoSite]
    geoip: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoIP]
    inbound_tag: _containers.RepeatedScalarFieldContainer[str]
    network_list: _network_pb2.NetworkList
    networks: _containers.RepeatedScalarFieldContainer[_network_pb2.Network]
    port_list: _port_pb2.PortList
    port_range: _port_pb2.PortRange
    protocol: _containers.RepeatedScalarFieldContainer[str]
    source_cidr: _containers.RepeatedCompositeFieldContainer[_common_pb2.CIDR]
    source_geoip: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoIP]
    source_port_list: _port_pb2.PortList
    tag: str
    user_email: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tag: _Optional[str] = ..., balancing_tag: _Optional[str] = ..., domain: _Optional[_Iterable[_Union[_common_pb2.Domain, _Mapping]]] = ..., cidr: _Optional[_Iterable[_Union[_common_pb2.CIDR, _Mapping]]] = ..., geoip: _Optional[_Iterable[_Union[_common_pb2.GeoIP, _Mapping]]] = ..., port_range: _Optional[_Union[_port_pb2.PortRange, _Mapping]] = ..., port_list: _Optional[_Union[_port_pb2.PortList, _Mapping]] = ..., network_list: _Optional[_Union[_network_pb2.NetworkList, _Mapping]] = ..., networks: _Optional[_Iterable[_Union[_network_pb2.Network, str]]] = ..., source_cidr: _Optional[_Iterable[_Union[_common_pb2.CIDR, _Mapping]]] = ..., source_geoip: _Optional[_Iterable[_Union[_common_pb2.GeoIP, _Mapping]]] = ..., source_port_list: _Optional[_Union[_port_pb2.PortList, _Mapping]] = ..., user_email: _Optional[_Iterable[str]] = ..., inbound_tag: _Optional[_Iterable[str]] = ..., protocol: _Optional[_Iterable[str]] = ..., attributes: _Optional[str] = ..., domain_matcher: _Optional[str] = ..., geo_domain: _Optional[_Iterable[_Union[_common_pb2.GeoSite, _Mapping]]] = ...) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = ["balancing_rule", "domain_strategy", "rule"]
    BALANCING_RULE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    balancing_rule: _containers.RepeatedCompositeFieldContainer[BalancingRule]
    domain_strategy: DomainStrategy
    rule: _containers.RepeatedCompositeFieldContainer[SimplifiedRoutingRule]
    def __init__(self, domain_strategy: _Optional[_Union[DomainStrategy, str]] = ..., rule: _Optional[_Iterable[_Union[SimplifiedRoutingRule, _Mapping]]] = ..., balancing_rule: _Optional[_Iterable[_Union[BalancingRule, _Mapping]]] = ...) -> None: ...

class SimplifiedRoutingRule(_message.Message):
    __slots__ = ["attributes", "balancing_tag", "domain", "domain_matcher", "geo_domain", "geoip", "inbound_tag", "networks", "port_list", "protocol", "source_geoip", "source_port_list", "tag", "user_email"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    BALANCING_TAG_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MATCHER_FIELD_NUMBER: _ClassVar[int]
    GEOIP_FIELD_NUMBER: _ClassVar[int]
    GEO_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    INBOUND_TAG_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GEOIP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    attributes: str
    balancing_tag: str
    domain: _containers.RepeatedCompositeFieldContainer[_common_pb2.Domain]
    domain_matcher: str
    geo_domain: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoSite]
    geoip: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoIP]
    inbound_tag: _containers.RepeatedScalarFieldContainer[str]
    networks: _network_pb2.NetworkList
    port_list: str
    protocol: _containers.RepeatedScalarFieldContainer[str]
    source_geoip: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoIP]
    source_port_list: str
    tag: str
    user_email: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tag: _Optional[str] = ..., balancing_tag: _Optional[str] = ..., domain: _Optional[_Iterable[_Union[_common_pb2.Domain, _Mapping]]] = ..., geoip: _Optional[_Iterable[_Union[_common_pb2.GeoIP, _Mapping]]] = ..., port_list: _Optional[str] = ..., networks: _Optional[_Union[_network_pb2.NetworkList, _Mapping]] = ..., source_geoip: _Optional[_Iterable[_Union[_common_pb2.GeoIP, _Mapping]]] = ..., source_port_list: _Optional[str] = ..., user_email: _Optional[_Iterable[str]] = ..., inbound_tag: _Optional[_Iterable[str]] = ..., protocol: _Optional[_Iterable[str]] = ..., attributes: _Optional[str] = ..., domain_matcher: _Optional[str] = ..., geo_domain: _Optional[_Iterable[_Union[_common_pb2.GeoSite, _Mapping]]] = ...) -> None: ...

class StrategyLeastLoadConfig(_message.Message):
    __slots__ = ["baselines", "costs", "expected", "maxRTT", "observer_tag", "tolerance"]
    BASELINES_FIELD_NUMBER: _ClassVar[int]
    COSTS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    MAXRTT_FIELD_NUMBER: _ClassVar[int]
    OBSERVER_TAG_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    baselines: _containers.RepeatedScalarFieldContainer[int]
    costs: _containers.RepeatedCompositeFieldContainer[StrategyWeight]
    expected: int
    maxRTT: int
    observer_tag: str
    tolerance: float
    def __init__(self, costs: _Optional[_Iterable[_Union[StrategyWeight, _Mapping]]] = ..., baselines: _Optional[_Iterable[int]] = ..., expected: _Optional[int] = ..., maxRTT: _Optional[int] = ..., tolerance: _Optional[float] = ..., observer_tag: _Optional[str] = ...) -> None: ...

class StrategyLeastPingConfig(_message.Message):
    __slots__ = ["observer_tag"]
    OBSERVER_TAG_FIELD_NUMBER: _ClassVar[int]
    observer_tag: str
    def __init__(self, observer_tag: _Optional[str] = ...) -> None: ...

class StrategyRandomConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StrategyWeight(_message.Message):
    __slots__ = ["match", "regexp", "value"]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    REGEXP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    match: str
    regexp: bool
    value: float
    def __init__(self, regexp: bool = ..., match: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class DomainStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
