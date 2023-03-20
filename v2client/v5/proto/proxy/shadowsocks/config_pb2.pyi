from common.net import network_pb2 as _network_pb2
from common.protocol import user_pb2 as _user_pb2
from common.protocol import server_spec_pb2 as _server_spec_pb2
from common.net.packetaddr import config_pb2 as _config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AES_128_GCM: CipherType
AES_256_GCM: CipherType
CHACHA20_POLY1305: CipherType
DESCRIPTOR: _descriptor.FileDescriptor
NONE: CipherType
UNKNOWN: CipherType

class Account(_message.Message):
    __slots__ = ["cipher_type", "experiment_reduced_iv_head_entropy", "iv_check", "password"]
    CIPHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_REDUCED_IV_HEAD_ENTROPY_FIELD_NUMBER: _ClassVar[int]
    IV_CHECK_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    cipher_type: CipherType
    experiment_reduced_iv_head_entropy: bool
    iv_check: bool
    password: str
    def __init__(self, password: _Optional[str] = ..., cipher_type: _Optional[_Union[CipherType, str]] = ..., iv_check: bool = ..., experiment_reduced_iv_head_entropy: bool = ...) -> None: ...

class ClientConfig(_message.Message):
    __slots__ = ["server"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: _containers.RepeatedCompositeFieldContainer[_server_spec_pb2.ServerEndpoint]
    def __init__(self, server: _Optional[_Iterable[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]]] = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ["network", "packet_encoding", "udp_enabled", "user"]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    PACKET_ENCODING_FIELD_NUMBER: _ClassVar[int]
    UDP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    network: _containers.RepeatedScalarFieldContainer[_network_pb2.Network]
    packet_encoding: _config_pb2.PacketAddrType
    udp_enabled: bool
    user: _user_pb2.User
    def __init__(self, udp_enabled: bool = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., network: _Optional[_Iterable[_Union[_network_pb2.Network, str]]] = ..., packet_encoding: _Optional[_Union[_config_pb2.PacketAddrType, str]] = ...) -> None: ...

class CipherType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
