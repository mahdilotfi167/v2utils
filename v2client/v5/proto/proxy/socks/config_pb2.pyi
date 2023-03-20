from common.net import address_pb2 as _address_pb2
from common.net.packetaddr import config_pb2 as _config_pb2
from common.protocol import server_spec_pb2 as _server_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
NO_AUTH: AuthType
PASSWORD: AuthType
SOCKS4: Version
SOCKS4A: Version
SOCKS5: Version

class Account(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ClientConfig(_message.Message):
    __slots__ = ["server", "version"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    server: _containers.RepeatedCompositeFieldContainer[_server_spec_pb2.ServerEndpoint]
    version: Version
    def __init__(self, server: _Optional[_Iterable[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]]] = ..., version: _Optional[_Union[Version, str]] = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ["accounts", "address", "auth_type", "packet_encoding", "timeout", "udp_enabled", "user_level"]
    class AccountsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    PACKET_ENCODING_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    UDP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.ScalarMap[str, str]
    address: _address_pb2.IPOrDomain
    auth_type: AuthType
    packet_encoding: _config_pb2.PacketAddrType
    timeout: int
    udp_enabled: bool
    user_level: int
    def __init__(self, auth_type: _Optional[_Union[AuthType, str]] = ..., accounts: _Optional[_Mapping[str, str]] = ..., address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., udp_enabled: bool = ..., timeout: _Optional[int] = ..., user_level: _Optional[int] = ..., packet_encoding: _Optional[_Union[_config_pb2.PacketAddrType, str]] = ...) -> None: ...

class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
