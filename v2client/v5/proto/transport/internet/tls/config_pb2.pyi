from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Certificate(_message.Message):
    __slots__ = ["Certificate", "Key", "certificate_file", "key_file", "usage"]
    class Usage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHORITY_ISSUE: Certificate.Usage
    AUTHORITY_VERIFY: Certificate.Usage
    AUTHORITY_VERIFY_CLIENT: Certificate.Usage
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FILE_FIELD_NUMBER: _ClassVar[int]
    Certificate: bytes
    ENCIPHERMENT: Certificate.Usage
    KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_FILE_FIELD_NUMBER: _ClassVar[int]
    Key: bytes
    USAGE_FIELD_NUMBER: _ClassVar[int]
    certificate_file: str
    key_file: str
    usage: Certificate.Usage
    def __init__(self, Certificate: _Optional[bytes] = ..., Key: _Optional[bytes] = ..., usage: _Optional[_Union[Certificate.Usage, str]] = ..., certificate_file: _Optional[str] = ..., key_file: _Optional[str] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["allow_insecure", "certificate", "disable_system_root", "enable_session_resumption", "next_protocol", "pinned_peer_certificate_chain_sha256", "server_name", "verify_client_certificate"]
    ALLOW_INSECURE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SYSTEM_ROOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SESSION_RESUMPTION_FIELD_NUMBER: _ClassVar[int]
    NEXT_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PINNED_PEER_CERTIFICATE_CHAIN_SHA256_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    allow_insecure: bool
    certificate: _containers.RepeatedCompositeFieldContainer[Certificate]
    disable_system_root: bool
    enable_session_resumption: bool
    next_protocol: _containers.RepeatedScalarFieldContainer[str]
    pinned_peer_certificate_chain_sha256: _containers.RepeatedScalarFieldContainer[bytes]
    server_name: str
    verify_client_certificate: bool
    def __init__(self, allow_insecure: bool = ..., certificate: _Optional[_Iterable[_Union[Certificate, _Mapping]]] = ..., server_name: _Optional[str] = ..., next_protocol: _Optional[_Iterable[str]] = ..., enable_session_resumption: bool = ..., disable_system_root: bool = ..., pinned_peer_certificate_chain_sha256: _Optional[_Iterable[bytes]] = ..., verify_client_certificate: bool = ...) -> None: ...
