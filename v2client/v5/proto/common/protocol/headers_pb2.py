# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/protocol/headers.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63ommon/protocol/headers.proto\x12\x1av2ray.core.common.protocol\"H\n\x0eSecurityConfig\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.v2ray.core.common.protocol.SecurityType*l\n\x0cSecurityType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06LEGACY\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\x12\x0e\n\nAES128_GCM\x10\x03\x12\x15\n\x11\x43HACHA20_POLY1305\x10\x04\x12\x08\n\x04NONE\x10\x05\x12\x08\n\x04ZERO\x10\x06\x42o\n\x1e\x63om.v2ray.core.common.protocolP\x01Z.github.com/v2fly/v2ray-core/v5/common/protocol\xaa\x02\x1aV2Ray.Core.Common.Protocolb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.protocol.headers_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.v2ray.core.common.protocolP\001Z.github.com/v2fly/v2ray-core/v5/common/protocol\252\002\032V2Ray.Core.Common.Protocol'
  _SECURITYTYPE._serialized_start=135
  _SECURITYTYPE._serialized_end=243
  _SECURITYCONFIG._serialized_start=61
  _SECURITYCONFIG._serialized_end=133
# @@protoc_insertion_point(module_scope)
