from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["ping_config", "subject_selector"]
    PING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    ping_config: HealthPingConfig
    subject_selector: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subject_selector: _Optional[_Iterable[str]] = ..., ping_config: _Optional[_Union[HealthPingConfig, _Mapping]] = ...) -> None: ...

class HealthPingConfig(_message.Message):
    __slots__ = ["connectivity", "destination", "interval", "samplingCount", "timeout"]
    CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    SAMPLINGCOUNT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    connectivity: str
    destination: str
    interval: int
    samplingCount: int
    timeout: int
    def __init__(self, destination: _Optional[str] = ..., connectivity: _Optional[str] = ..., interval: _Optional[int] = ..., samplingCount: _Optional[int] = ..., timeout: _Optional[int] = ...) -> None: ...
