# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/errors/quota_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/errors/quota_error.proto',
  package='google.ads.googleads.v5.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v5.errorsB\017QuotaErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V5.Errors\312\002\036Google\\Ads\\GoogleAds\\V5\\Errors\352\002\"Google::Ads::GoogleAds::V5::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/ads/googleads_v5/proto/errors/quota_error.proto\x12\x1egoogle.ads.googleads.v5.errors\x1a\x1cgoogle/api/annotations.proto\"\x8f\x01\n\x0eQuotaErrorEnum\"}\n\nQuotaError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x02\x12\x15\n\x11\x41\x43\x43\x45SS_PROHIBITED\x10\x03\x12\"\n\x1eRESOURCE_TEMPORARILY_EXHAUSTED\x10\x04\x42\xea\x01\n\"com.google.ads.googleads.v5.errorsB\x0fQuotaErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V5.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V5\\Errors\xea\x02\"Google::Ads::GoogleAds::V5::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_QUOTAERRORENUM_QUOTAERROR = _descriptor.EnumDescriptor(
  name='QuotaError',
  full_name='google.ads.googleads.v5.errors.QuotaErrorEnum.QuotaError',
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
      name='RESOURCE_EXHAUSTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_PROHIBITED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_TEMPORARILY_EXHAUSTED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=139,
  serialized_end=264,
)
_sym_db.RegisterEnumDescriptor(_QUOTAERRORENUM_QUOTAERROR)


_QUOTAERRORENUM = _descriptor.Descriptor(
  name='QuotaErrorEnum',
  full_name='google.ads.googleads.v5.errors.QuotaErrorEnum',
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
    _QUOTAERRORENUM_QUOTAERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=264,
)

_QUOTAERRORENUM_QUOTAERROR.containing_type = _QUOTAERRORENUM
DESCRIPTOR.message_types_by_name['QuotaErrorEnum'] = _QUOTAERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuotaErrorEnum = _reflection.GeneratedProtocolMessageType('QuotaErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _QUOTAERRORENUM,
  '__module__' : 'google.ads.googleads_v5.proto.errors.quota_error_pb2'
  ,
  '__doc__': """Container for enum describing possible quota errors.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.errors.QuotaErrorEnum)
  })
_sym_db.RegisterMessage(QuotaErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
