# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/net/destination.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.net import network_pb2 as common_dot_net_dot_network__pb2
from common.net import address_pb2 as common_dot_net_dot_address__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63ommon/net/destination.proto\x12\x15v2ray.core.common.net\x1a\x18\x63ommon/net/network.proto\x1a\x18\x63ommon/net/address.proto\"}\n\x08\x45ndpoint\x12/\n\x07network\x18\x01 \x01(\x0e\x32\x1e.v2ray.core.common.net.Network\x12\x32\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x03 \x01(\rB`\n\x19\x63om.v2ray.core.common.netP\x01Z)github.com/v2fly/v2ray-core/v5/common/net\xaa\x02\x15V2Ray.Core.Common.Netb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.net.destination_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.v2ray.core.common.netP\001Z)github.com/v2fly/v2ray-core/v5/common/net\252\002\025V2Ray.Core.Common.Net'
  _ENDPOINT._serialized_start=107
  _ENDPOINT._serialized_end=232
# @@protoc_insertion_point(module_scope)