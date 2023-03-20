from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["accept_proxy_protocol", "early_data_header_name", "header", "max_early_data", "path", "use_browser_forwarding"]
    ACCEPT_PROXY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    EARLY_DATA_HEADER_NAME_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MAX_EARLY_DATA_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    USE_BROWSER_FORWARDING_FIELD_NUMBER: _ClassVar[int]
    accept_proxy_protocol: bool
    early_data_header_name: str
    header: _containers.RepeatedCompositeFieldContainer[Header]
    max_early_data: int
    path: str
    use_browser_forwarding: bool
    def __init__(self, path: _Optional[str] = ..., header: _Optional[_Iterable[_Union[Header, _Mapping]]] = ..., accept_proxy_protocol: bool = ..., max_early_data: _Optional[int] = ..., use_browser_forwarding: bool = ..., early_data_header_name: _Optional[str] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
