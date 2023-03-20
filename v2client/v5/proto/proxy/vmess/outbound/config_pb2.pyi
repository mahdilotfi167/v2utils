from common.protocol import server_spec_pb2 as _server_spec_pb2
from common.net import address_pb2 as _address_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["Receiver"]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    Receiver: _containers.RepeatedCompositeFieldContainer[_server_spec_pb2.ServerEndpoint]
    def __init__(self, Receiver: _Optional[_Iterable[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]]] = ...) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = ["address", "port", "uuid"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.IPOrDomain
    port: int
    uuid: str
    def __init__(self, address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ..., uuid: _Optional[str] = ...) -> None: ...
