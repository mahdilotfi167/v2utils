from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["host", "service_name"]
    HOST_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    host: str
    service_name: str
    def __init__(self, host: _Optional[str] = ..., service_name: _Optional[str] = ...) -> None: ...
