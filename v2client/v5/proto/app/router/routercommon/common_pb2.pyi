from common.protoext import extensions_pb2 as _extensions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CIDR(_message.Message):
    __slots__ = ["ip", "ip_addr", "prefix"]
    IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    ip: bytes
    ip_addr: str
    prefix: int
    def __init__(self, ip: _Optional[bytes] = ..., prefix: _Optional[int] = ..., ip_addr: _Optional[str] = ...) -> None: ...

class Domain(_message.Message):
    __slots__ = ["attribute", "type", "value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Attribute(_message.Message):
        __slots__ = ["bool_value", "int_value", "key"]
        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
        INT_VALUE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        bool_value: bool
        int_value: int
        key: str
        def __init__(self, key: _Optional[str] = ..., bool_value: bool = ..., int_value: _Optional[int] = ...) -> None: ...
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    Full: Domain.Type
    Plain: Domain.Type
    Regex: Domain.Type
    RootDomain: Domain.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    attribute: _containers.RepeatedCompositeFieldContainer[Domain.Attribute]
    type: Domain.Type
    value: str
    def __init__(self, type: _Optional[_Union[Domain.Type, str]] = ..., value: _Optional[str] = ..., attribute: _Optional[_Iterable[_Union[Domain.Attribute, _Mapping]]] = ...) -> None: ...

class GeoIP(_message.Message):
    __slots__ = ["cidr", "code", "country_code", "file_path", "inverse_match", "resource_hash"]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    INVERSE_MATCH_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
    cidr: _containers.RepeatedCompositeFieldContainer[CIDR]
    code: str
    country_code: str
    file_path: str
    inverse_match: bool
    resource_hash: bytes
    def __init__(self, country_code: _Optional[str] = ..., cidr: _Optional[_Iterable[_Union[CIDR, _Mapping]]] = ..., inverse_match: bool = ..., resource_hash: _Optional[bytes] = ..., code: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class GeoIPList(_message.Message):
    __slots__ = ["entry"]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.RepeatedCompositeFieldContainer[GeoIP]
    def __init__(self, entry: _Optional[_Iterable[_Union[GeoIP, _Mapping]]] = ...) -> None: ...

class GeoSite(_message.Message):
    __slots__ = ["code", "country_code", "domain", "file_path", "resource_hash"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
    code: str
    country_code: str
    domain: _containers.RepeatedCompositeFieldContainer[Domain]
    file_path: str
    resource_hash: bytes
    def __init__(self, country_code: _Optional[str] = ..., domain: _Optional[_Iterable[_Union[Domain, _Mapping]]] = ..., resource_hash: _Optional[bytes] = ..., code: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class GeoSiteList(_message.Message):
    __slots__ = ["entry"]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.RepeatedCompositeFieldContainer[GeoSite]
    def __init__(self, entry: _Optional[_Iterable[_Union[GeoSite, _Mapping]]] = ...) -> None: ...
