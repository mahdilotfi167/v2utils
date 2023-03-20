from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
Debug: Severity
Error: Severity
Info: Severity
Unknown: Severity
Warning: Severity

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
