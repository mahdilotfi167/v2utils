from common.protoext import extensions_pb2 as _extensions_pb2
from transport.internet.tls import config_pb2 as _config_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
NO_ALPN: ForcedALPN
TRANSPORT_PREFERENCE_TAKE_PRIORITY: ForcedALPN
UTLS_PRESET: ForcedALPN

class Config(_message.Message):
    __slots__ = ["force_alpn", "imitate", "noSNI", "tls_config"]
    FORCE_ALPN_FIELD_NUMBER: _ClassVar[int]
    IMITATE_FIELD_NUMBER: _ClassVar[int]
    NOSNI_FIELD_NUMBER: _ClassVar[int]
    TLS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    force_alpn: ForcedALPN
    imitate: str
    noSNI: bool
    tls_config: _config_pb2.Config
    def __init__(self, tls_config: _Optional[_Union[_config_pb2.Config, _Mapping]] = ..., imitate: _Optional[str] = ..., noSNI: bool = ..., force_alpn: _Optional[_Union[ForcedALPN, str]] = ...) -> None: ...

class ForcedALPN(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
