from google.protobuf import any_pb2 as _any_pb2
from transport import config_pb2 as _config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["app", "extension", "inbound", "outbound", "transport"]
    APP_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    app: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    extension: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    inbound: _containers.RepeatedCompositeFieldContainer[InboundHandlerConfig]
    outbound: _containers.RepeatedCompositeFieldContainer[OutboundHandlerConfig]
    transport: _config_pb2.Config
    def __init__(self, inbound: _Optional[_Iterable[_Union[InboundHandlerConfig, _Mapping]]] = ..., outbound: _Optional[_Iterable[_Union[OutboundHandlerConfig, _Mapping]]] = ..., app: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., transport: _Optional[_Union[_config_pb2.Config, _Mapping]] = ..., extension: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class InboundHandlerConfig(_message.Message):
    __slots__ = ["proxy_settings", "receiver_settings", "tag"]
    PROXY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    proxy_settings: _any_pb2.Any
    receiver_settings: _any_pb2.Any
    tag: str
    def __init__(self, tag: _Optional[str] = ..., receiver_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., proxy_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class OutboundHandlerConfig(_message.Message):
    __slots__ = ["comment", "expire", "proxy_settings", "sender_settings", "tag"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    PROXY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SENDER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    comment: str
    expire: int
    proxy_settings: _any_pb2.Any
    sender_settings: _any_pb2.Any
    tag: str
    def __init__(self, tag: _Optional[str] = ..., sender_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., proxy_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., expire: _Optional[int] = ..., comment: _Optional[str] = ...) -> None: ...
