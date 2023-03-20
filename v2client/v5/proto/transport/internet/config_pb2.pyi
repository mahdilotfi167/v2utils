from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
DomainSocket: TransportProtocol
HTTP: TransportProtocol
MKCP: TransportProtocol
TCP: TransportProtocol
UDP: TransportProtocol
WebSocket: TransportProtocol

class ProxyConfig(_message.Message):
    __slots__ = ["tag", "transportLayerProxy"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    TRANSPORTLAYERPROXY_FIELD_NUMBER: _ClassVar[int]
    tag: str
    transportLayerProxy: bool
    def __init__(self, tag: _Optional[str] = ..., transportLayerProxy: bool = ...) -> None: ...

class SocketConfig(_message.Message):
    __slots__ = ["accept_proxy_protocol", "bind_address", "bind_port", "bind_to_device", "force_buf_size", "mark", "receive_original_dest_address", "rx_buf_size", "tcp_keep_alive_idle", "tcp_keep_alive_interval", "tfo", "tfo_queue_length", "tproxy", "tx_buf_size"]
    class TCPFastOpenState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class TProxyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACCEPT_PROXY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    AsIs: SocketConfig.TCPFastOpenState
    BIND_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BIND_PORT_FIELD_NUMBER: _ClassVar[int]
    BIND_TO_DEVICE_FIELD_NUMBER: _ClassVar[int]
    Disable: SocketConfig.TCPFastOpenState
    Enable: SocketConfig.TCPFastOpenState
    FORCE_BUF_SIZE_FIELD_NUMBER: _ClassVar[int]
    MARK_FIELD_NUMBER: _ClassVar[int]
    Off: SocketConfig.TProxyMode
    RECEIVE_ORIGINAL_DEST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RX_BUF_SIZE_FIELD_NUMBER: _ClassVar[int]
    Redirect: SocketConfig.TProxyMode
    TCP_KEEP_ALIVE_IDLE_FIELD_NUMBER: _ClassVar[int]
    TCP_KEEP_ALIVE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TFO_FIELD_NUMBER: _ClassVar[int]
    TFO_QUEUE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TPROXY_FIELD_NUMBER: _ClassVar[int]
    TProxy: SocketConfig.TProxyMode
    TX_BUF_SIZE_FIELD_NUMBER: _ClassVar[int]
    accept_proxy_protocol: bool
    bind_address: bytes
    bind_port: int
    bind_to_device: str
    force_buf_size: bool
    mark: int
    receive_original_dest_address: bool
    rx_buf_size: int
    tcp_keep_alive_idle: int
    tcp_keep_alive_interval: int
    tfo: SocketConfig.TCPFastOpenState
    tfo_queue_length: int
    tproxy: SocketConfig.TProxyMode
    tx_buf_size: int
    def __init__(self, mark: _Optional[int] = ..., tfo: _Optional[_Union[SocketConfig.TCPFastOpenState, str]] = ..., tproxy: _Optional[_Union[SocketConfig.TProxyMode, str]] = ..., receive_original_dest_address: bool = ..., bind_address: _Optional[bytes] = ..., bind_port: _Optional[int] = ..., accept_proxy_protocol: bool = ..., tcp_keep_alive_interval: _Optional[int] = ..., tfo_queue_length: _Optional[int] = ..., tcp_keep_alive_idle: _Optional[int] = ..., bind_to_device: _Optional[str] = ..., rx_buf_size: _Optional[int] = ..., tx_buf_size: _Optional[int] = ..., force_buf_size: bool = ...) -> None: ...

class StreamConfig(_message.Message):
    __slots__ = ["protocol", "protocol_name", "security_settings", "security_type", "socket_settings", "transport_settings"]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_NAME_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOCKET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    protocol: TransportProtocol
    protocol_name: str
    security_settings: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    security_type: str
    socket_settings: SocketConfig
    transport_settings: _containers.RepeatedCompositeFieldContainer[TransportConfig]
    def __init__(self, protocol: _Optional[_Union[TransportProtocol, str]] = ..., protocol_name: _Optional[str] = ..., transport_settings: _Optional[_Iterable[_Union[TransportConfig, _Mapping]]] = ..., security_type: _Optional[str] = ..., security_settings: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., socket_settings: _Optional[_Union[SocketConfig, _Mapping]] = ...) -> None: ...

class TransportConfig(_message.Message):
    __slots__ = ["protocol", "protocol_name", "settings"]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_NAME_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    protocol: TransportProtocol
    protocol_name: str
    settings: _any_pb2.Any
    def __init__(self, protocol: _Optional[_Union[TransportProtocol, str]] = ..., protocol_name: _Optional[str] = ..., settings: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class TransportProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
