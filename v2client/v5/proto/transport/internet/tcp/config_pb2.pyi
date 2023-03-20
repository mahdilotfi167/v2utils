from google.protobuf import any_pb2 as _any_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["accept_proxy_protocol", "header_settings"]
    ACCEPT_PROXY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    HEADER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    accept_proxy_protocol: bool
    header_settings: _any_pb2.Any
    def __init__(self, header_settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., accept_proxy_protocol: bool = ...) -> None: ...
