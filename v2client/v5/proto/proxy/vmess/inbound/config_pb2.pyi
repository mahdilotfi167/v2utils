from common.protocol import user_pb2 as _user_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["default", "detour", "secure_encryption_only", "user"]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DETOUR_FIELD_NUMBER: _ClassVar[int]
    SECURE_ENCRYPTION_ONLY_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    default: DefaultConfig
    detour: DetourConfig
    secure_encryption_only: bool
    user: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    def __init__(self, user: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., default: _Optional[_Union[DefaultConfig, _Mapping]] = ..., detour: _Optional[_Union[DetourConfig, _Mapping]] = ..., secure_encryption_only: bool = ...) -> None: ...

class DefaultConfig(_message.Message):
    __slots__ = ["alter_id", "level"]
    ALTER_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    alter_id: int
    level: int
    def __init__(self, alter_id: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...

class DetourConfig(_message.Message):
    __slots__ = ["to"]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: str
    def __init__(self, to: _Optional[str] = ...) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, users: _Optional[_Iterable[str]] = ...) -> None: ...
