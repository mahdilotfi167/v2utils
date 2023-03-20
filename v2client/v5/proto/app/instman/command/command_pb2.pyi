from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddInstanceReq(_message.Message):
    __slots__ = ["configContentB64", "configType", "name"]
    CONFIGCONTENTB64_FIELD_NUMBER: _ClassVar[int]
    CONFIGTYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    configContentB64: str
    configType: str
    name: str
    def __init__(self, name: _Optional[str] = ..., configType: _Optional[str] = ..., configContentB64: _Optional[str] = ...) -> None: ...

class AddInstanceResp(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Config(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListInstanceReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListInstanceResp(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[_Iterable[str]] = ...) -> None: ...

class StartInstanceReq(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class StartInstanceResp(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
