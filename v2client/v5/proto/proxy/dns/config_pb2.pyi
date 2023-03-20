from common.net import destination_pb2 as _destination_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["server", "user_level"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    USER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    server: _destination_pb2.Endpoint
    user_level: int
    def __init__(self, server: _Optional[_Union[_destination_pb2.Endpoint, _Mapping]] = ..., user_level: _Optional[int] = ...) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
