from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
RawTCP: Network
TCP: Network
UDP: Network
UNIX: Network
Unknown: Network

class NetworkList(_message.Message):
    __slots__ = ["network"]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    network: _containers.RepeatedScalarFieldContainer[Network]
    def __init__(self, network: _Optional[_Iterable[_Union[Network, str]]] = ...) -> None: ...

class Network(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
