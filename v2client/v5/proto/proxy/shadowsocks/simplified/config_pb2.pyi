from common.protoext import extensions_pb2 as _extensions_pb2
from common.net import address_pb2 as _address_pb2
from common.net import network_pb2 as _network_pb2
from common.net.packetaddr import config_pb2 as _config_pb2
from proxy.shadowsocks import config_pb2 as _config_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientConfig(_message.Message):
    __slots__ = ["address", "experiment_reduced_iv_head_entropy", "method", "password", "port"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_REDUCED_IV_HEAD_ENTROPY_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.IPOrDomain
    experiment_reduced_iv_head_entropy: bool
    method: _config_pb2_1.CipherType
    password: str
    port: int
    def __init__(self, address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ..., method: _Optional[_Union[_config_pb2_1.CipherType, str]] = ..., password: _Optional[str] = ..., experiment_reduced_iv_head_entropy: bool = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ["method", "networks", "packet_encoding", "password"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    PACKET_ENCODING_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    method: _config_pb2_1.CipherType
    networks: _network_pb2.NetworkList
    packet_encoding: _config_pb2.PacketAddrType
    password: str
    def __init__(self, method: _Optional[_Union[_config_pb2_1.CipherType, str]] = ..., password: _Optional[str] = ..., networks: _Optional[_Union[_network_pb2.NetworkList, _Mapping]] = ..., packet_encoding: _Optional[_Union[_config_pb2.PacketAddrType, str]] = ...) -> None: ...
