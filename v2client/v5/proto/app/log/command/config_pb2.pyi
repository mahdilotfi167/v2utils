from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FollowLogRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FollowLogResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RestartLoggerRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RestartLoggerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
