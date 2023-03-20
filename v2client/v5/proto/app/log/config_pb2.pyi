from common.log import log_pb2 as _log_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

Console: LogType
DESCRIPTOR: _descriptor.FileDescriptor
Event: LogType
File: LogType
None: LogType

class Config(_message.Message):
    __slots__ = ["access", "error"]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    access: LogSpecification
    error: LogSpecification
    def __init__(self, error: _Optional[_Union[LogSpecification, _Mapping]] = ..., access: _Optional[_Union[LogSpecification, _Mapping]] = ...) -> None: ...

class LogSpecification(_message.Message):
    __slots__ = ["level", "path", "type"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    level: _log_pb2.Severity
    path: str
    type: LogType
    def __init__(self, type: _Optional[_Union[LogType, str]] = ..., level: _Optional[_Union[_log_pb2.Severity, str]] = ..., path: _Optional[str] = ...) -> None: ...

class LogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
