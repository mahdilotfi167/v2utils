from common.taggedfeatures import skeleton_pb2 as _skeleton_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["holders"]
    HOLDERS_FIELD_NUMBER: _ClassVar[int]
    holders: _skeleton_pb2.Config
    def __init__(self, holders: _Optional[_Union[_skeleton_pb2.Config, _Mapping]] = ...) -> None: ...
