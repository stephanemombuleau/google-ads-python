# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/common/targeting_setting.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import targeting_dimension_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_targeting__dimension__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/common/targeting_setting.proto',
  package='google.ads.googleads.v5.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v5.commonB\025TargetingSettingProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V5.Common\312\002\036Google\\Ads\\GoogleAds\\V5\\Common\352\002\"Google::Ads::GoogleAds::V5::Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<google/ads/googleads_v5/proto/common/targeting_setting.proto\x12\x1egoogle.ads.googleads.v5.common\x1a=google/ads/googleads_v5/proto/enums/targeting_dimension.proto\x1a\x1cgoogle/api/annotations.proto\"\xc5\x01\n\x10TargetingSetting\x12N\n\x13target_restrictions\x18\x01 \x03(\x0b\x32\x31.google.ads.googleads.v5.common.TargetRestriction\x12\x61\n\x1dtarget_restriction_operations\x18\x02 \x03(\x0b\x32:.google.ads.googleads.v5.common.TargetRestrictionOperation\"\x9e\x01\n\x11TargetRestriction\x12\x65\n\x13targeting_dimension\x18\x01 \x01(\x0e\x32H.google.ads.googleads.v5.enums.TargetingDimensionEnum.TargetingDimension\x12\x15\n\x08\x62id_only\x18\x03 \x01(\x08H\x00\x88\x01\x01\x42\x0b\n\t_bid_only\"\xf4\x01\n\x1aTargetRestrictionOperation\x12U\n\x08operator\x18\x01 \x01(\x0e\x32\x43.google.ads.googleads.v5.common.TargetRestrictionOperation.Operator\x12@\n\x05value\x18\x02 \x01(\x0b\x32\x31.google.ads.googleads.v5.common.TargetRestriction\"=\n\x08Operator\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03\x41\x44\x44\x10\x02\x12\n\n\x06REMOVE\x10\x03\x42\xf0\x01\n\"com.google.ads.googleads.v5.commonB\x15TargetingSettingProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V5.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V5\\Common\xea\x02\"Google::Ads::GoogleAds::V5::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_targeting__dimension__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_TARGETRESTRICTIONOPERATION_OPERATOR = _descriptor.EnumDescriptor(
  name='Operator',
  full_name='google.ads.googleads.v5.common.TargetRestrictionOperation.Operator',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REMOVE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=734,
  serialized_end=795,
)
_sym_db.RegisterEnumDescriptor(_TARGETRESTRICTIONOPERATION_OPERATOR)


_TARGETINGSETTING = _descriptor.Descriptor(
  name='TargetingSetting',
  full_name='google.ads.googleads.v5.common.TargetingSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_restrictions', full_name='google.ads.googleads.v5.common.TargetingSetting.target_restrictions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_restriction_operations', full_name='google.ads.googleads.v5.common.TargetingSetting.target_restriction_operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=387,
)


_TARGETRESTRICTION = _descriptor.Descriptor(
  name='TargetRestriction',
  full_name='google.ads.googleads.v5.common.TargetRestriction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='targeting_dimension', full_name='google.ads.googleads.v5.common.TargetRestriction.targeting_dimension', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_only', full_name='google.ads.googleads.v5.common.TargetRestriction.bid_only', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_bid_only', full_name='google.ads.googleads.v5.common.TargetRestriction._bid_only',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=390,
  serialized_end=548,
)


_TARGETRESTRICTIONOPERATION = _descriptor.Descriptor(
  name='TargetRestrictionOperation',
  full_name='google.ads.googleads.v5.common.TargetRestrictionOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operator', full_name='google.ads.googleads.v5.common.TargetRestrictionOperation.operator', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.ads.googleads.v5.common.TargetRestrictionOperation.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TARGETRESTRICTIONOPERATION_OPERATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=795,
)

_TARGETINGSETTING.fields_by_name['target_restrictions'].message_type = _TARGETRESTRICTION
_TARGETINGSETTING.fields_by_name['target_restriction_operations'].message_type = _TARGETRESTRICTIONOPERATION
_TARGETRESTRICTION.fields_by_name['targeting_dimension'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_targeting__dimension__pb2._TARGETINGDIMENSIONENUM_TARGETINGDIMENSION
_TARGETRESTRICTION.oneofs_by_name['_bid_only'].fields.append(
  _TARGETRESTRICTION.fields_by_name['bid_only'])
_TARGETRESTRICTION.fields_by_name['bid_only'].containing_oneof = _TARGETRESTRICTION.oneofs_by_name['_bid_only']
_TARGETRESTRICTIONOPERATION.fields_by_name['operator'].enum_type = _TARGETRESTRICTIONOPERATION_OPERATOR
_TARGETRESTRICTIONOPERATION.fields_by_name['value'].message_type = _TARGETRESTRICTION
_TARGETRESTRICTIONOPERATION_OPERATOR.containing_type = _TARGETRESTRICTIONOPERATION
DESCRIPTOR.message_types_by_name['TargetingSetting'] = _TARGETINGSETTING
DESCRIPTOR.message_types_by_name['TargetRestriction'] = _TARGETRESTRICTION
DESCRIPTOR.message_types_by_name['TargetRestrictionOperation'] = _TARGETRESTRICTIONOPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetingSetting = _reflection.GeneratedProtocolMessageType('TargetingSetting', (_message.Message,), {
  'DESCRIPTOR' : _TARGETINGSETTING,
  '__module__' : 'google.ads.googleads_v5.proto.common.targeting_setting_pb2'
  ,
  '__doc__': """Settings for the targeting-related features, at the campaign and ad
  group levels. For more details about the targeting setting, visit
  https://support.google.com/google-ads/answer/7365594
  
  Attributes:
      target_restrictions:
          The per-targeting-dimension setting to restrict the reach of
          your campaign or ad group.
      target_restriction_operations:
          The list of operations changing the target restrictions.
          Adding a target restriction with a targeting dimension that
          already exists causes the existing target restriction to be
          replaced with the new value.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.TargetingSetting)
  })
_sym_db.RegisterMessage(TargetingSetting)

TargetRestriction = _reflection.GeneratedProtocolMessageType('TargetRestriction', (_message.Message,), {
  'DESCRIPTOR' : _TARGETRESTRICTION,
  '__module__' : 'google.ads.googleads_v5.proto.common.targeting_setting_pb2'
  ,
  '__doc__': """The list of per-targeting-dimension targeting settings.
  
  Attributes:
      targeting_dimension:
          The targeting dimension that these settings apply to.
      bid_only:
          Indicates whether to restrict your ads to show only for the
          criteria you have selected for this targeting\_dimension, or
          to target all values for this targeting\_dimension and show
          ads based on your targeting in other TargetingDimensions. A
          value of ``true`` means that these criteria will only apply
          bid modifiers, and not affect targeting. A value of ``false``
          means that these criteria will restrict targeting as well as
          applying bid modifiers.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.TargetRestriction)
  })
_sym_db.RegisterMessage(TargetRestriction)

TargetRestrictionOperation = _reflection.GeneratedProtocolMessageType('TargetRestrictionOperation', (_message.Message,), {
  'DESCRIPTOR' : _TARGETRESTRICTIONOPERATION,
  '__module__' : 'google.ads.googleads_v5.proto.common.targeting_setting_pb2'
  ,
  '__doc__': """Operation to be performed on a target restriction list in a mutate.
  
  Attributes:
      operator:
          Type of list operation to perform.
      value:
          The target restriction being added to or removed from the
          list.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.TargetRestrictionOperation)
  })
_sym_db.RegisterMessage(TargetRestrictionOperation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
