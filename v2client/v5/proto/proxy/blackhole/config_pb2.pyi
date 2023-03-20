from google.protobuf import any_pb2 as _any_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _any_pb2.Any
    def __init__(self, response: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class HTTPResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NoneResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
