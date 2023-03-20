from common.protocol import server_spec_pb2 as _server_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ClientConfig(_message.Message):
    __slots__ = ["server"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: _containers.RepeatedCompositeFieldContainer[_server_spec_pb2.ServerEndpoint]
    def __init__(self, server: _Optional[_Iterable[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]]] = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ["accounts", "allow_transparent", "timeout", "user_level"]
    class AccountsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_TRANSPARENT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    USER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.ScalarMap[str, str]
    allow_transparent: bool
    timeout: int
    user_level: int
    def __init__(self, timeout: _Optional[int] = ..., accounts: _Optional[_Mapping[str, str]] = ..., allow_transparent: bool = ..., user_level: _Optional[int] = ...) -> None: ...
