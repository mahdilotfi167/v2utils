from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["abstract", "padding", "path"]
    ABSTRACT_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    abstract: bool
    padding: bool
    path: str
    def __init__(self, path: _Optional[str] = ..., abstract: bool = ..., padding: bool = ...) -> None: ...
