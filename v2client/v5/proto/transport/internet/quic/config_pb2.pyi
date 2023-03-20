from google.protobuf import any_pb2 as _any_pb2
from common.protocol import headers_pb2 as _headers_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["header", "key", "security"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    header: _any_pb2.Any
    key: str
    security: _headers_pb2.SecurityConfig
    def __init__(self, key: _Optional[str] = ..., security: _Optional[_Union[_headers_pb2.SecurityConfig, _Mapping]] = ..., header: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
