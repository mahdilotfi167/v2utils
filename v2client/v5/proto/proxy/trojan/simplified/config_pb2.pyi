from common.protoext import extensions_pb2 as _extensions_pb2
from common.net import address_pb2 as _address_pb2
from common.net.packetaddr import config_pb2 as _config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientConfig(_message.Message):
    __slots__ = ["address", "password", "port"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.IPOrDomain
    password: str
    port: int
    def __init__(self, address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ..., password: _Optional[str] = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ["packet_encoding", "users"]
    PACKET_ENCODING_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    packet_encoding: _config_pb2.PacketAddrType
    users: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, users: _Optional[_Iterable[str]] = ..., packet_encoding: _Optional[_Union[_config_pb2.PacketAddrType, str]] = ...) -> None: ...
