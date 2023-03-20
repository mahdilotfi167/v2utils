from google.protobuf import any_pb2 as _any_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["congestion", "downlink_capacity", "header_config", "mtu", "read_buffer", "seed", "tti", "uplink_capacity", "write_buffer"]
    CONGESTION_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    HEADER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    READ_BUFFER_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    TTI_FIELD_NUMBER: _ClassVar[int]
    UPLINK_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    WRITE_BUFFER_FIELD_NUMBER: _ClassVar[int]
    congestion: bool
    downlink_capacity: DownlinkCapacity
    header_config: _any_pb2.Any
    mtu: MTU
    read_buffer: ReadBuffer
    seed: EncryptionSeed
    tti: TTI
    uplink_capacity: UplinkCapacity
    write_buffer: WriteBuffer
    def __init__(self, mtu: _Optional[_Union[MTU, _Mapping]] = ..., tti: _Optional[_Union[TTI, _Mapping]] = ..., uplink_capacity: _Optional[_Union[UplinkCapacity, _Mapping]] = ..., downlink_capacity: _Optional[_Union[DownlinkCapacity, _Mapping]] = ..., congestion: bool = ..., write_buffer: _Optional[_Union[WriteBuffer, _Mapping]] = ..., read_buffer: _Optional[_Union[ReadBuffer, _Mapping]] = ..., header_config: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., seed: _Optional[_Union[EncryptionSeed, _Mapping]] = ...) -> None: ...

class ConnectionReuse(_message.Message):
    __slots__ = ["enable"]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    def __init__(self, enable: bool = ...) -> None: ...

class DownlinkCapacity(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class EncryptionSeed(_message.Message):
    __slots__ = ["seed"]
    SEED_FIELD_NUMBER: _ClassVar[int]
    seed: str
    def __init__(self, seed: _Optional[str] = ...) -> None: ...

class MTU(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class ReadBuffer(_message.Message):
    __slots__ = ["size"]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...

class TTI(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class UplinkCapacity(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class WriteBuffer(_message.Message):
    __slots__ = ["size"]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...
