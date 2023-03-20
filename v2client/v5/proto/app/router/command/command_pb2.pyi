from common.protoext import extensions_pb2 as _extensions_pb2
from common.net import network_pb2 as _network_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BalancerMsg(_message.Message):
    __slots__ = ["override", "principle_target"]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    PRINCIPLE_TARGET_FIELD_NUMBER: _ClassVar[int]
    override: OverrideInfo
    principle_target: PrincipleTargetInfo
    def __init__(self, override: _Optional[_Union[OverrideInfo, _Mapping]] = ..., principle_target: _Optional[_Union[PrincipleTargetInfo, _Mapping]] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetBalancerInfoRequest(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class GetBalancerInfoResponse(_message.Message):
    __slots__ = ["balancer"]
    BALANCER_FIELD_NUMBER: _ClassVar[int]
    balancer: BalancerMsg
    def __init__(self, balancer: _Optional[_Union[BalancerMsg, _Mapping]] = ...) -> None: ...

class OverrideBalancerTargetRequest(_message.Message):
    __slots__ = ["balancerTag", "target"]
    BALANCERTAG_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    balancerTag: str
    target: str
    def __init__(self, balancerTag: _Optional[str] = ..., target: _Optional[str] = ...) -> None: ...

class OverrideBalancerTargetResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OverrideInfo(_message.Message):
    __slots__ = ["target"]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: str
    def __init__(self, target: _Optional[str] = ...) -> None: ...

class PrincipleTargetInfo(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tag: _Optional[_Iterable[str]] = ...) -> None: ...

class RoutingContext(_message.Message):
    __slots__ = ["Attributes", "InboundTag", "Network", "OutboundGroupTags", "OutboundTag", "Protocol", "SourceIPs", "SourcePort", "TargetDomain", "TargetIPs", "TargetPort", "User"]
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    Attributes: _containers.ScalarMap[str, str]
    INBOUNDTAG_FIELD_NUMBER: _ClassVar[int]
    InboundTag: str
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    Network: _network_pb2.Network
    OUTBOUNDGROUPTAGS_FIELD_NUMBER: _ClassVar[int]
    OUTBOUNDTAG_FIELD_NUMBER: _ClassVar[int]
    OutboundGroupTags: _containers.RepeatedScalarFieldContainer[str]
    OutboundTag: str
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    Protocol: str
    SOURCEIPS_FIELD_NUMBER: _ClassVar[int]
    SOURCEPORT_FIELD_NUMBER: _ClassVar[int]
    SourceIPs: _containers.RepeatedScalarFieldContainer[bytes]
    SourcePort: int
    TARGETDOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGETIPS_FIELD_NUMBER: _ClassVar[int]
    TARGETPORT_FIELD_NUMBER: _ClassVar[int]
    TargetDomain: str
    TargetIPs: _containers.RepeatedScalarFieldContainer[bytes]
    TargetPort: int
    USER_FIELD_NUMBER: _ClassVar[int]
    User: str
    def __init__(self, InboundTag: _Optional[str] = ..., Network: _Optional[_Union[_network_pb2.Network, str]] = ..., SourceIPs: _Optional[_Iterable[bytes]] = ..., TargetIPs: _Optional[_Iterable[bytes]] = ..., SourcePort: _Optional[int] = ..., TargetPort: _Optional[int] = ..., TargetDomain: _Optional[str] = ..., Protocol: _Optional[str] = ..., User: _Optional[str] = ..., Attributes: _Optional[_Mapping[str, str]] = ..., OutboundGroupTags: _Optional[_Iterable[str]] = ..., OutboundTag: _Optional[str] = ...) -> None: ...

class SubscribeRoutingStatsRequest(_message.Message):
    __slots__ = ["FieldSelectors"]
    FIELDSELECTORS_FIELD_NUMBER: _ClassVar[int]
    FieldSelectors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, FieldSelectors: _Optional[_Iterable[str]] = ...) -> None: ...

class TestRouteRequest(_message.Message):
    __slots__ = ["FieldSelectors", "PublishResult", "RoutingContext"]
    FIELDSELECTORS_FIELD_NUMBER: _ClassVar[int]
    FieldSelectors: _containers.RepeatedScalarFieldContainer[str]
    PUBLISHRESULT_FIELD_NUMBER: _ClassVar[int]
    PublishResult: bool
    ROUTINGCONTEXT_FIELD_NUMBER: _ClassVar[int]
    RoutingContext: RoutingContext
    def __init__(self, RoutingContext: _Optional[_Union[RoutingContext, _Mapping]] = ..., FieldSelectors: _Optional[_Iterable[str]] = ..., PublishResult: bool = ...) -> None: ...
