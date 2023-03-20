from common.net import address_pb2 as _address_pb2
from common.net import port_pb2 as _port_pb2
from transport.internet import config_pb2 as _config_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
HTTP: KnownProtocols
TLS: KnownProtocols

class AllocationStrategy(_message.Message):
    __slots__ = ["concurrency", "refresh", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class AllocationStrategyConcurrency(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class AllocationStrategyRefresh(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    Always: AllocationStrategy.Type
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    External: AllocationStrategy.Type
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    Random: AllocationStrategy.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    concurrency: AllocationStrategy.AllocationStrategyConcurrency
    refresh: AllocationStrategy.AllocationStrategyRefresh
    type: AllocationStrategy.Type
    def __init__(self, type: _Optional[_Union[AllocationStrategy.Type, str]] = ..., concurrency: _Optional[_Union[AllocationStrategy.AllocationStrategyConcurrency, _Mapping]] = ..., refresh: _Optional[_Union[AllocationStrategy.AllocationStrategyRefresh, _Mapping]] = ...) -> None: ...

class InboundConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InboundHandlerConfig(_message.Message):
    __slots__ = ["proxy_settings", "receiver_settings", "tag"]
    PROXY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    proxy_settings: _any_pb2.Any
    receiver_settings: _any_pb2.Any
    tag: str
    def __init__(self, tag: _Optional[str] = ..., receiver_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., proxy_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class MultiplexingConfig(_message.Message):
    __slots__ = ["concurrency", "enabled"]
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    concurrency: int
    enabled: bool
    def __init__(self, enabled: bool = ..., concurrency: _Optional[int] = ...) -> None: ...

class OutboundConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReceiverConfig(_message.Message):
    __slots__ = ["allocation_strategy", "domain_override", "listen", "port_range", "receive_original_destination", "sniffing_settings", "stream_settings"]
    ALLOCATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    LISTEN_FIELD_NUMBER: _ClassVar[int]
    PORT_RANGE_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_ORIGINAL_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SNIFFING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    allocation_strategy: AllocationStrategy
    domain_override: _containers.RepeatedScalarFieldContainer[KnownProtocols]
    listen: _address_pb2.IPOrDomain
    port_range: _port_pb2.PortRange
    receive_original_destination: bool
    sniffing_settings: SniffingConfig
    stream_settings: _config_pb2.StreamConfig
    def __init__(self, port_range: _Optional[_Union[_port_pb2.PortRange, _Mapping]] = ..., listen: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., allocation_strategy: _Optional[_Union[AllocationStrategy, _Mapping]] = ..., stream_settings: _Optional[_Union[_config_pb2.StreamConfig, _Mapping]] = ..., receive_original_destination: bool = ..., domain_override: _Optional[_Iterable[_Union[KnownProtocols, str]]] = ..., sniffing_settings: _Optional[_Union[SniffingConfig, _Mapping]] = ...) -> None: ...

class SenderConfig(_message.Message):
    __slots__ = ["domain_strategy", "multiplex_settings", "proxy_settings", "stream_settings", "via"]
    class DomainStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AS_IS: SenderConfig.DomainStrategy
    DOMAIN_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MULTIPLEX_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROXY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    USE_IP: SenderConfig.DomainStrategy
    USE_IP4: SenderConfig.DomainStrategy
    USE_IP6: SenderConfig.DomainStrategy
    VIA_FIELD_NUMBER: _ClassVar[int]
    domain_strategy: SenderConfig.DomainStrategy
    multiplex_settings: MultiplexingConfig
    proxy_settings: _config_pb2.ProxyConfig
    stream_settings: _config_pb2.StreamConfig
    via: _address_pb2.IPOrDomain
    def __init__(self, via: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., stream_settings: _Optional[_Union[_config_pb2.StreamConfig, _Mapping]] = ..., proxy_settings: _Optional[_Union[_config_pb2.ProxyConfig, _Mapping]] = ..., multiplex_settings: _Optional[_Union[MultiplexingConfig, _Mapping]] = ..., domain_strategy: _Optional[_Union[SenderConfig.DomainStrategy, str]] = ...) -> None: ...

class SniffingConfig(_message.Message):
    __slots__ = ["destination_override", "enabled", "metadata_only"]
    DESTINATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    destination_override: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    metadata_only: bool
    def __init__(self, enabled: bool = ..., destination_override: _Optional[_Iterable[str]] = ..., metadata_only: bool = ...) -> None: ...

class KnownProtocols(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
