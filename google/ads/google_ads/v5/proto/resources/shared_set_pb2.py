# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/resources/shared_set.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import shared_set_status_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_shared__set__status__pb2
from google.ads.google_ads.v5.proto.enums import shared_set_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_shared__set__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/resources/shared_set.proto',
  package='google.ads.googleads.v5.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v5.resourcesB\016SharedSetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V5.Resources\312\002!Google\\Ads\\GoogleAds\\V5\\Resources\352\002%Google::Ads::GoogleAds::V5::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/ads/googleads_v5/proto/resources/shared_set.proto\x12!google.ads.googleads.v5.resources\x1a;google/ads/googleads_v5/proto/enums/shared_set_status.proto\x1a\x39google/ads/googleads_v5/proto/enums/shared_set_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xf2\x03\n\tSharedSet\x12\x41\n\rresource_name\x18\x01 \x01(\tB*\xe0\x41\x05\xfa\x41$\n\"googleads.googleapis.com/SharedSet\x12\x14\n\x02id\x18\x08 \x01(\x03\x42\x03\xe0\x41\x03H\x00\x88\x01\x01\x12Q\n\x04type\x18\x03 \x01(\x0e\x32>.google.ads.googleads.v5.enums.SharedSetTypeEnum.SharedSetTypeB\x03\xe0\x41\x05\x12\x11\n\x04name\x18\t \x01(\tH\x01\x88\x01\x01\x12W\n\x06status\x18\x05 \x01(\x0e\x32\x42.google.ads.googleads.v5.enums.SharedSetStatusEnum.SharedSetStatusB\x03\xe0\x41\x03\x12\x1e\n\x0cmember_count\x18\n \x01(\x03\x42\x03\xe0\x41\x03H\x02\x88\x01\x01\x12!\n\x0freference_count\x18\x0b \x01(\x03\x42\x03\xe0\x41\x03H\x03\x88\x01\x01:U\xea\x41R\n\"googleads.googleapis.com/SharedSet\x12,customers/{customer}/sharedSets/{shared_set}B\x05\n\x03_idB\x07\n\x05_nameB\x0f\n\r_member_countB\x12\n\x10_reference_countB\xfb\x01\n%com.google.ads.googleads.v5.resourcesB\x0eSharedSetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V5.Resources\xca\x02!Google\\Ads\\GoogleAds\\V5\\Resources\xea\x02%Google::Ads::GoogleAds::V5::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_shared__set__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_shared__set__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SHAREDSET = _descriptor.Descriptor(
  name='SharedSet',
  full_name='google.ads.googleads.v5.resources.SharedSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.resources.SharedSet.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A$\n\"googleads.googleapis.com/SharedSet', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v5.resources.SharedSet.id', index=1,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v5.resources.SharedSet.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v5.resources.SharedSet.name', index=3,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v5.resources.SharedSet.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='member_count', full_name='google.ads.googleads.v5.resources.SharedSet.member_count', index=5,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reference_count', full_name='google.ads.googleads.v5.resources.SharedSet.reference_count', index=6,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352AR\n\"googleads.googleapis.com/SharedSet\022,customers/{customer}/sharedSets/{shared_set}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_id', full_name='google.ads.googleads.v5.resources.SharedSet._id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='google.ads.googleads.v5.resources.SharedSet._name',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_member_count', full_name='google.ads.googleads.v5.resources.SharedSet._member_count',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_reference_count', full_name='google.ads.googleads.v5.resources.SharedSet._reference_count',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=306,
  serialized_end=804,
)

_SHAREDSET.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_shared__set__type__pb2._SHAREDSETTYPEENUM_SHAREDSETTYPE
_SHAREDSET.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_shared__set__status__pb2._SHAREDSETSTATUSENUM_SHAREDSETSTATUS
_SHAREDSET.oneofs_by_name['_id'].fields.append(
  _SHAREDSET.fields_by_name['id'])
_SHAREDSET.fields_by_name['id'].containing_oneof = _SHAREDSET.oneofs_by_name['_id']
_SHAREDSET.oneofs_by_name['_name'].fields.append(
  _SHAREDSET.fields_by_name['name'])
_SHAREDSET.fields_by_name['name'].containing_oneof = _SHAREDSET.oneofs_by_name['_name']
_SHAREDSET.oneofs_by_name['_member_count'].fields.append(
  _SHAREDSET.fields_by_name['member_count'])
_SHAREDSET.fields_by_name['member_count'].containing_oneof = _SHAREDSET.oneofs_by_name['_member_count']
_SHAREDSET.oneofs_by_name['_reference_count'].fields.append(
  _SHAREDSET.fields_by_name['reference_count'])
_SHAREDSET.fields_by_name['reference_count'].containing_oneof = _SHAREDSET.oneofs_by_name['_reference_count']
DESCRIPTOR.message_types_by_name['SharedSet'] = _SHAREDSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SharedSet = _reflection.GeneratedProtocolMessageType('SharedSet', (_message.Message,), {
  'DESCRIPTOR' : _SHAREDSET,
  '__module__' : 'google.ads.googleads_v5.proto.resources.shared_set_pb2'
  ,
  '__doc__': """SharedSets are used for sharing criterion exclusions across multiple
  campaigns.
  
  Attributes:
      resource_name:
          Immutable. The resource name of the shared set. Shared set
          resource names have the form:
          ``customers/{customer_id}/sharedSets/{shared_set_id}``
      id:
          Output only. The ID of this shared set. Read only.
      type:
          Immutable. The type of this shared set: each shared set holds
          only a single kind of resource. Required. Immutable.
      name:
          The name of this shared set. Required. Shared Sets must have
          names that are unique among active shared sets of the same
          type. The length of this string should be between 1 and 255
          UTF-8 bytes, inclusive.
      status:
          Output only. The status of this shared set. Read only.
      member_count:
          Output only. The number of shared criteria within this shared
          set. Read only.
      reference_count:
          Output only. The number of campaigns associated with this
          shared set. Read only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.resources.SharedSet)
  })
_sym_db.RegisterMessage(SharedSet)


DESCRIPTOR._options = None
_SHAREDSET.fields_by_name['resource_name']._options = None
_SHAREDSET.fields_by_name['id']._options = None
_SHAREDSET.fields_by_name['type']._options = None
_SHAREDSET.fields_by_name['status']._options = None
_SHAREDSET.fields_by_name['member_count']._options = None
_SHAREDSET.fields_by_name['reference_count']._options = None
_SHAREDSET._options = None
# @@protoc_insertion_point(module_scope)
