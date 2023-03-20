from transport.internet.headers.http import config_pb2 as _config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["header", "host", "method", "path"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    header: _containers.RepeatedCompositeFieldContainer[_config_pb2.Header]
    host: _containers.RepeatedScalarFieldContainer[str]
    method: str
    path: str
    def __init__(self, host: _Optional[_Iterable[str]] = ..., path: _Optional[str] = ..., method: _Optional[str] = ..., header: _Optional[_Iterable[_Union[_config_pb2.Header, _Mapping]]] = ...) -> None: ...
