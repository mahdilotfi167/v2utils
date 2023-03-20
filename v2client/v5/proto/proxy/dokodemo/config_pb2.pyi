from common.net import address_pb2 as _address_pb2
from common.net import network_pb2 as _network_pb2
from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["address", "follow_redirect", "network_list", "networks", "port", "timeout", "user_level"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_REDIRECT_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_LIST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    USER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.IPOrDomain
    follow_redirect: bool
    network_list: _network_pb2.NetworkList
    networks: _containers.RepeatedScalarFieldContainer[_network_pb2.Network]
    port: int
    timeout: int
    user_level: int
    def __init__(self, address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ..., network_list: _Optional[_Union[_network_pb2.NetworkList, _Mapping]] = ..., networks: _Optional[_Iterable[_Union[_network_pb2.Network, str]]] = ..., timeout: _Optional[int] = ..., follow_redirect: bool = ..., user_level: _Optional[int] = ...) -> None: ...

class SimplifiedConfig(_message.Message):
    __slots__ = ["address", "follow_redirect", "networks", "port"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_REDIRECT_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.IPOrDomain
    follow_redirect: bool
    networks: _network_pb2.NetworkList
    port: int
    def __init__(self, address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ..., networks: _Optional[_Union[_network_pb2.NetworkList, _Mapping]] = ..., follow_redirect: bool = ...) -> None: ...
