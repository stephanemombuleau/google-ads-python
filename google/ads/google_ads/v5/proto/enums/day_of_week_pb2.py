# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/enums/day_of_week.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/enums/day_of_week.proto',
  package='google.ads.googleads.v5.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v5.enumsB\016DayOfWeekProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V5.Enums\312\002\035Google\\Ads\\GoogleAds\\V5\\Enums\352\002!Google::Ads::GoogleAds::V5::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5google/ads/googleads_v5/proto/enums/day_of_week.proto\x12\x1dgoogle.ads.googleads.v5.enums\x1a\x1cgoogle/api/annotations.proto\"\x97\x01\n\rDayOfWeekEnum\"\x85\x01\n\tDayOfWeek\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06MONDAY\x10\x02\x12\x0b\n\x07TUESDAY\x10\x03\x12\r\n\tWEDNESDAY\x10\x04\x12\x0c\n\x08THURSDAY\x10\x05\x12\n\n\x06\x46RIDAY\x10\x06\x12\x0c\n\x08SATURDAY\x10\x07\x12\n\n\x06SUNDAY\x10\x08\x42\xe3\x01\n!com.google.ads.googleads.v5.enumsB\x0e\x44\x61yOfWeekProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v5/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V5.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V5\\Enums\xea\x02!Google::Ads::GoogleAds::V5::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_DAYOFWEEKENUM_DAYOFWEEK = _descriptor.EnumDescriptor(
  name='DayOfWeek',
  full_name='google.ads.googleads.v5.enums.DayOfWeekEnum.DayOfWeek',
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
      name='MONDAY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TUESDAY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEDNESDAY', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THURSDAY', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRIDAY', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SATURDAY', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUNDAY', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=137,
  serialized_end=270,
)
_sym_db.RegisterEnumDescriptor(_DAYOFWEEKENUM_DAYOFWEEK)


_DAYOFWEEKENUM = _descriptor.Descriptor(
  name='DayOfWeekEnum',
  full_name='google.ads.googleads.v5.enums.DayOfWeekEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DAYOFWEEKENUM_DAYOFWEEK,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=270,
)

_DAYOFWEEKENUM_DAYOFWEEK.containing_type = _DAYOFWEEKENUM
DESCRIPTOR.message_types_by_name['DayOfWeekEnum'] = _DAYOFWEEKENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DayOfWeekEnum = _reflection.GeneratedProtocolMessageType('DayOfWeekEnum', (_message.Message,), {
  'DESCRIPTOR' : _DAYOFWEEKENUM,
  '__module__' : 'google.ads.googleads_v5.proto.enums.day_of_week_pb2'
  ,
  '__doc__': """Container for enumeration of days of the week, e.g., "Monday".""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.enums.DayOfWeekEnum)
  })
_sym_db.RegisterMessage(DayOfWeekEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
