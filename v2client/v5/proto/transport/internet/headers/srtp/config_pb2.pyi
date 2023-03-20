from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["csrc_count", "extension", "marker", "padding", "payload_type", "version"]
    CSRC_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    MARKER_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    csrc_count: int
    extension: bool
    marker: bool
    padding: bool
    payload_type: int
    version: int
    def __init__(self, version: _Optional[int] = ..., padding: bool = ..., extension: bool = ..., csrc_count: _Optional[int] = ..., marker: bool = ..., payload_type: _Optional[int] = ...) -> None: ...
