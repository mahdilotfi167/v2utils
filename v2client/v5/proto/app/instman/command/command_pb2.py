# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/instman/command/command.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!app/instman/command/command.proto\x12\x1ev2ray.core.app.instman.command\x1a common/protoext/extensions.proto\"\x11\n\x0fListInstanceReq\" \n\x10ListInstanceResp\x12\x0c\n\x04name\x18\x01 \x03(\t\"L\n\x0e\x41\x64\x64InstanceReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nconfigType\x18\x02 \x01(\t\x12\x18\n\x10\x63onfigContentB64\x18\x03 \x01(\t\"\x11\n\x0f\x41\x64\x64InstanceResp\" \n\x10StartInstanceReq\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x13\n\x11StartInstanceResp\"(\n\x06\x43onfig:\x1e\x82\xb5\x18\r\n\x0bgrpcservice\x82\xb5\x18\t\x12\x07instman2\xf4\x02\n\x19InstanceManagementService\x12q\n\x0cListInstance\x12/.v2ray.core.app.instman.command.ListInstanceReq\x1a\x30.v2ray.core.app.instman.command.ListInstanceResp\x12n\n\x0b\x41\x64\x64Instance\x12..v2ray.core.app.instman.command.AddInstanceReq\x1a/.v2ray.core.app.instman.command.AddInstanceResp\x12t\n\rStartInstance\x12\x30.v2ray.core.app.instman.command.StartInstanceReq\x1a\x31.v2ray.core.app.instman.command.StartInstanceRespB\x7f\n&com.v2ray.core.app.observatory.instmanP\x01Z2github.com/v2fly/v2ray-core/v5/app/instman/command\xaa\x02\x1eV2Ray.Core.App.Instman.Commandb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.instman.command.command_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.v2ray.core.app.observatory.instmanP\001Z2github.com/v2fly/v2ray-core/v5/app/instman/command\252\002\036V2Ray.Core.App.Instman.Command'
  _CONFIG._options = None
  _CONFIG._serialized_options = b'\202\265\030\r\n\013grpcservice\202\265\030\t\022\007instman'
  _LISTINSTANCEREQ._serialized_start=103
  _LISTINSTANCEREQ._serialized_end=120
  _LISTINSTANCERESP._serialized_start=122
  _LISTINSTANCERESP._serialized_end=154
  _ADDINSTANCEREQ._serialized_start=156
  _ADDINSTANCEREQ._serialized_end=232
  _ADDINSTANCERESP._serialized_start=234
  _ADDINSTANCERESP._serialized_end=251
  _STARTINSTANCEREQ._serialized_start=253
  _STARTINSTANCEREQ._serialized_end=285
  _STARTINSTANCERESP._serialized_start=287
  _STARTINSTANCERESP._serialized_end=306
  _CONFIG._serialized_start=308
  _CONFIG._serialized_end=348
  _INSTANCEMANAGEMENTSERVICE._serialized_start=351
  _INSTANCEMANAGEMENTSERVICE._serialized_end=723
# @@protoc_insertion_point(module_scope)
