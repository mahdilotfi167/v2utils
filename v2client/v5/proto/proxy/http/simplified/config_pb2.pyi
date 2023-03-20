from common.protoext import extensions_pb2 as _extensions_pb2
from common.net import address_pb2 as _address_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientConfig(_message.Message):
    __slots__ = ["address", "port"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.IPOrDomain
    port: int
    def __init__(self, address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
