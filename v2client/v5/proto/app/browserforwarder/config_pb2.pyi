from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["listen_addr", "listen_port"]
    LISTEN_ADDR_FIELD_NUMBER: _ClassVar[int]
    LISTEN_PORT_FIELD_NUMBER: _ClassVar[int]
    listen_addr: str
    listen_port: int
    def __init__(self, listen_addr: _Optional[str] = ..., listen_port: _Optional[int] = ...) -> None: ...
