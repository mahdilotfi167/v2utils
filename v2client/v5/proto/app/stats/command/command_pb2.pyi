from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetStatsRequest(_message.Message):
    __slots__ = ["name", "reset"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    name: str
    reset: bool
    def __init__(self, name: _Optional[str] = ..., reset: bool = ...) -> None: ...

class GetStatsResponse(_message.Message):
    __slots__ = ["stat"]
    STAT_FIELD_NUMBER: _ClassVar[int]
    stat: Stat
    def __init__(self, stat: _Optional[_Union[Stat, _Mapping]] = ...) -> None: ...

class QueryStatsRequest(_message.Message):
    __slots__ = ["pattern", "patterns", "regexp", "reset"]
    PATTERNS_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    REGEXP_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    patterns: _containers.RepeatedScalarFieldContainer[str]
    regexp: bool
    reset: bool
    def __init__(self, pattern: _Optional[str] = ..., reset: bool = ..., patterns: _Optional[_Iterable[str]] = ..., regexp: bool = ...) -> None: ...

class QueryStatsResponse(_message.Message):
    __slots__ = ["stat"]
    STAT_FIELD_NUMBER: _ClassVar[int]
    stat: _containers.RepeatedCompositeFieldContainer[Stat]
    def __init__(self, stat: _Optional[_Iterable[_Union[Stat, _Mapping]]] = ...) -> None: ...

class Stat(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: int
    def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...

class SysStatsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SysStatsResponse(_message.Message):
    __slots__ = ["Alloc", "Frees", "LiveObjects", "Mallocs", "NumGC", "NumGoroutine", "PauseTotalNs", "Sys", "TotalAlloc", "Uptime"]
    ALLOC_FIELD_NUMBER: _ClassVar[int]
    Alloc: int
    FREES_FIELD_NUMBER: _ClassVar[int]
    Frees: int
    LIVEOBJECTS_FIELD_NUMBER: _ClassVar[int]
    LiveObjects: int
    MALLOCS_FIELD_NUMBER: _ClassVar[int]
    Mallocs: int
    NUMGC_FIELD_NUMBER: _ClassVar[int]
    NUMGOROUTINE_FIELD_NUMBER: _ClassVar[int]
    NumGC: int
    NumGoroutine: int
    PAUSETOTALNS_FIELD_NUMBER: _ClassVar[int]
    PauseTotalNs: int
    SYS_FIELD_NUMBER: _ClassVar[int]
    Sys: int
    TOTALALLOC_FIELD_NUMBER: _ClassVar[int]
    TotalAlloc: int
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    Uptime: int
    def __init__(self, NumGoroutine: _Optional[int] = ..., NumGC: _Optional[int] = ..., Alloc: _Optional[int] = ..., TotalAlloc: _Optional[int] = ..., Sys: _Optional[int] = ..., Mallocs: _Optional[int] = ..., Frees: _Optional[int] = ..., LiveObjects: _Optional[int] = ..., PauseTotalNs: _Optional[int] = ..., Uptime: _Optional[int] = ...) -> None: ...
