from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["probe_interval", "probe_url", "subject_selector"]
    PROBE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PROBE_URL_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    probe_interval: int
    probe_url: str
    subject_selector: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, subject_selector: _Optional[_Iterable[str]] = ..., probe_url: _Optional[str] = ..., probe_interval: _Optional[int] = ...) -> None: ...

class HealthPingMeasurementResult(_message.Message):
    __slots__ = ["all", "average", "deviation", "fail", "max", "min"]
    ALL_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_FIELD_NUMBER: _ClassVar[int]
    DEVIATION_FIELD_NUMBER: _ClassVar[int]
    FAIL_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    all: int
    average: int
    deviation: int
    fail: int
    max: int
    min: int
    def __init__(self, all: _Optional[int] = ..., fail: _Optional[int] = ..., deviation: _Optional[int] = ..., average: _Optional[int] = ..., max: _Optional[int] = ..., min: _Optional[int] = ...) -> None: ...

class Intensity(_message.Message):
    __slots__ = ["probe_interval"]
    PROBE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    probe_interval: int
    def __init__(self, probe_interval: _Optional[int] = ...) -> None: ...

class ObservationResult(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[OutboundStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[OutboundStatus, _Mapping]]] = ...) -> None: ...

class OutboundStatus(_message.Message):
    __slots__ = ["alive", "delay", "health_ping", "last_error_reason", "last_seen_time", "last_try_time", "outbound_tag"]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    HEALTH_PING_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TRY_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_TAG_FIELD_NUMBER: _ClassVar[int]
    alive: bool
    delay: int
    health_ping: HealthPingMeasurementResult
    last_error_reason: str
    last_seen_time: int
    last_try_time: int
    outbound_tag: str
    def __init__(self, alive: bool = ..., delay: _Optional[int] = ..., last_error_reason: _Optional[str] = ..., outbound_tag: _Optional[str] = ..., last_seen_time: _Optional[int] = ..., last_try_time: _Optional[int] = ..., health_ping: _Optional[_Union[HealthPingMeasurementResult, _Mapping]] = ...) -> None: ...

class ProbeResult(_message.Message):
    __slots__ = ["alive", "delay", "last_error_reason"]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    alive: bool
    delay: int
    last_error_reason: str
    def __init__(self, alive: bool = ..., delay: _Optional[int] = ..., last_error_reason: _Optional[str] = ...) -> None: ...
