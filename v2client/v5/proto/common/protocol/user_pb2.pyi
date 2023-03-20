from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["account", "email", "level"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    account: _any_pb2.Any
    email: str
    level: int
    def __init__(self, level: _Optional[int] = ..., email: _Optional[str] = ..., account: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
