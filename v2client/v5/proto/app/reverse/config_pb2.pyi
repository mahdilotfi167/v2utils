from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BridgeConfig(_message.Message):
    __slots__ = ["domain", "tag"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    domain: str
    tag: str
    def __init__(self, tag: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["bridge_config", "portal_config"]
    BRIDGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PORTAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    bridge_config: _containers.RepeatedCompositeFieldContainer[BridgeConfig]
    portal_config: _containers.RepeatedCompositeFieldContainer[PortalConfig]
    def __init__(self, bridge_config: _Optional[_Iterable[_Union[BridgeConfig, _Mapping]]] = ..., portal_config: _Optional[_Iterable[_Union[PortalConfig, _Mapping]]] = ...) -> None: ...

class Control(_message.Message):
    __slots__ = ["random", "state"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Control.State
    DRAIN: Control.State
    RANDOM_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    random: bytes
    state: Control.State
    def __init__(self, state: _Optional[_Union[Control.State, str]] = ..., random: _Optional[bytes] = ...) -> None: ...

class PortalConfig(_message.Message):
    __slots__ = ["domain", "tag"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    domain: str
    tag: str
    def __init__(self, tag: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...
