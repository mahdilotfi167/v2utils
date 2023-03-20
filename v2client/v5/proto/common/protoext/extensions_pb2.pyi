from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
FIELD_OPT_FIELD_NUMBER: _ClassVar[int]
MESSAGE_OPT_FIELD_NUMBER: _ClassVar[int]
field_opt: _descriptor.FieldDescriptor
message_opt: _descriptor.FieldDescriptor

class FieldOpt(_message.Message):
    __slots__ = ["allowed_value_types", "allowed_values", "any_wants", "convert_time_parse_ip", "convert_time_read_file_into", "convert_time_resource_loading", "forbidden"]
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VALUE_TYPES_FIELD_NUMBER: _ClassVar[int]
    ANY_WANTS_FIELD_NUMBER: _ClassVar[int]
    CONVERT_TIME_PARSE_IP_FIELD_NUMBER: _ClassVar[int]
    CONVERT_TIME_READ_FILE_INTO_FIELD_NUMBER: _ClassVar[int]
    CONVERT_TIME_RESOURCE_LOADING_FIELD_NUMBER: _ClassVar[int]
    FORBIDDEN_FIELD_NUMBER: _ClassVar[int]
    allowed_value_types: _containers.RepeatedScalarFieldContainer[str]
    allowed_values: _containers.RepeatedScalarFieldContainer[str]
    any_wants: _containers.RepeatedScalarFieldContainer[str]
    convert_time_parse_ip: str
    convert_time_read_file_into: str
    convert_time_resource_loading: str
    forbidden: bool
    def __init__(self, any_wants: _Optional[_Iterable[str]] = ..., allowed_values: _Optional[_Iterable[str]] = ..., allowed_value_types: _Optional[_Iterable[str]] = ..., convert_time_read_file_into: _Optional[str] = ..., forbidden: bool = ..., convert_time_resource_loading: _Optional[str] = ..., convert_time_parse_ip: _Optional[str] = ...) -> None: ...

class MessageOpt(_message.Message):
    __slots__ = ["short_name", "transport_original_name", "type"]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_ORIGINAL_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    short_name: _containers.RepeatedScalarFieldContainer[str]
    transport_original_name: str
    type: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Iterable[str]] = ..., short_name: _Optional[_Iterable[str]] = ..., transport_original_name: _Optional[str] = ...) -> None: ...
