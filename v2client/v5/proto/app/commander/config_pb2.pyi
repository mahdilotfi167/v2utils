from google.protobuf import any_pb2 as _any_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["service", "tag"]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    service: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    tag: str
    def __init__(self, tag: _Optional[str] = ..., service: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class ReflectionConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = ["name", "tag"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    name: _containers.RepeatedScalarFieldContainer[str]
    tag: str
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[_Iterable[str]] = ...) -> None: ...
