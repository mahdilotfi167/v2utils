from common.protocol import user_pb2 as _user_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["clients", "decryption", "fallbacks"]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    DECRYPTION_FIELD_NUMBER: _ClassVar[int]
    FALLBACKS_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    decryption: str
    fallbacks: _containers.RepeatedCompositeFieldContainer[Fallback]
    def __init__(self, clients: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., decryption: _Optional[str] = ..., fallbacks: _Optional[_Iterable[_Union[Fallback, _Mapping]]] = ...) -> None: ...

class Fallback(_message.Message):
    __slots__ = ["alpn", "dest", "path", "type", "xver"]
    ALPN_FIELD_NUMBER: _ClassVar[int]
    DEST_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    XVER_FIELD_NUMBER: _ClassVar[int]
    alpn: str
    dest: str
    path: str
    type: str
    xver: int
    def __init__(self, alpn: _Optional[str] = ..., path: _Optional[str] = ..., type: _Optional[str] = ..., dest: _Optional[str] = ..., xver: _Optional[int] = ...) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, users: _Optional[_Iterable[str]] = ...) -> None: ...
