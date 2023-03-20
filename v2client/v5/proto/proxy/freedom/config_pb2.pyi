from common.protocol import server_spec_pb2 as _server_spec_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["destination_override", "domain_strategy", "timeout", "user_level"]
    class DomainStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AS_IS: Config.DomainStrategy
    DESTINATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    USER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    USE_IP: Config.DomainStrategy
    USE_IP4: Config.DomainStrategy
    USE_IP6: Config.DomainStrategy
    destination_override: DestinationOverride
    domain_strategy: Config.DomainStrategy
    timeout: int
    user_level: int
    def __init__(self, domain_strategy: _Optional[_Union[Config.DomainStrategy, str]] = ..., timeout: _Optional[int] = ..., destination_override: _Optional[_Union[DestinationOverride, _Mapping]] = ..., user_level: _Optional[int] = ...) -> None: ...

class DestinationOverride(_message.Message):
    __slots__ = ["server"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: _server_spec_pb2.ServerEndpoint
    def __init__(self, server: _Optional[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]] = ...) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
