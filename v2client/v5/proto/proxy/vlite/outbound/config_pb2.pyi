from common.net import address_pb2 as _address_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UDPProtocolConfig(_message.Message):
    __slots__ = ["address", "enable_fec", "enable_renegotiation", "enable_stabilization", "handshake_masking_padding_size", "password", "port", "scramble_packet"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RENEGOTIATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STABILIZATION_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKE_MASKING_PADDING_SIZE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    SCRAMBLE_PACKET_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.IPOrDomain
    enable_fec: bool
    enable_renegotiation: bool
    enable_stabilization: bool
    handshake_masking_padding_size: int
    password: str
    port: int
    scramble_packet: bool
    def __init__(self, address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ..., password: _Optional[str] = ..., scramble_packet: bool = ..., enable_fec: bool = ..., enable_stabilization: bool = ..., enable_renegotiation: bool = ..., handshake_masking_padding_size: _Optional[int] = ...) -> None: ...
