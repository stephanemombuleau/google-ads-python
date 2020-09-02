# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/services/label_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import response_content_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2
from google.ads.google_ads.v5.proto.resources import label_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_label__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/services/label_service.proto',
  package='google.ads.googleads.v5.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v5.servicesB\021LabelServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V5.Services\312\002 Google\\Ads\\GoogleAds\\V5\\Services\352\002$Google::Ads::GoogleAds::V5::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:google/ads/googleads_v5/proto/services/label_service.proto\x12 google.ads.googleads.v5.services\x1a?google/ads/googleads_v5/proto/enums/response_content_type.proto\x1a\x33google/ads/googleads_v5/proto/resources/label.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"P\n\x0fGetLabelRequest\x12=\n\rresource_name\x18\x01 \x01(\tB&\xe0\x41\x02\xfa\x41 \n\x1egoogleads.googleapis.com/Label\"\x95\x02\n\x13MutateLabelsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12I\n\noperations\x18\x02 \x03(\x0b\x32\x30.google.ads.googleads.v5.services.LabelOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12i\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v5.enums.ResponseContentTypeEnum.ResponseContentType\"\xd8\x01\n\x0eLabelOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12:\n\x06\x63reate\x18\x01 \x01(\x0b\x32(.google.ads.googleads.v5.resources.LabelH\x00\x12:\n\x06update\x18\x02 \x01(\x0b\x32(.google.ads.googleads.v5.resources.LabelH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x8f\x01\n\x14MutateLabelsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12\x44\n\x07results\x18\x02 \x03(\x0b\x32\x33.google.ads.googleads.v5.services.MutateLabelResult\"c\n\x11MutateLabelResult\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x37\n\x05label\x18\x02 \x01(\x0b\x32(.google.ads.googleads.v5.resources.Label2\xa8\x03\n\x0cLabelService\x12\xa9\x01\n\x08GetLabel\x12\x31.google.ads.googleads.v5.services.GetLabelRequest\x1a(.google.ads.googleads.v5.resources.Label\"@\x82\xd3\xe4\x93\x02*\x12(/v5/{resource_name=customers/*/labels/*}\xda\x41\rresource_name\x12\xce\x01\n\x0cMutateLabels\x12\x35.google.ads.googleads.v5.services.MutateLabelsRequest\x1a\x36.google.ads.googleads.v5.services.MutateLabelsResponse\"O\x82\xd3\xe4\x93\x02\x30\"+/v5/customers/{customer_id=*}/labels:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xf8\x01\n$com.google.ads.googleads.v5.servicesB\x11LabelServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V5.Services\xca\x02 Google\\Ads\\GoogleAds\\V5\\Services\xea\x02$Google::Ads::GoogleAds::V5::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_label__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETLABELREQUEST = _descriptor.Descriptor(
  name='GetLabelRequest',
  full_name='google.ads.googleads.v5.services.GetLabelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.services.GetLabelRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A \n\036googleads.googleapis.com/Label', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=388,
  serialized_end=468,
)


_MUTATELABELSREQUEST = _descriptor.Descriptor(
  name='MutateLabelsRequest',
  full_name='google.ads.googleads.v5.services.MutateLabelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v5.services.MutateLabelsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v5.services.MutateLabelsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v5.services.MutateLabelsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v5.services.MutateLabelsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_content_type', full_name='google.ads.googleads.v5.services.MutateLabelsRequest.response_content_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=471,
  serialized_end=748,
)


_LABELOPERATION = _descriptor.Descriptor(
  name='LabelOperation',
  full_name='google.ads.googleads.v5.services.LabelOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v5.services.LabelOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v5.services.LabelOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v5.services.LabelOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v5.services.LabelOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
      name='operation', full_name='google.ads.googleads.v5.services.LabelOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=751,
  serialized_end=967,
)


_MUTATELABELSRESPONSE = _descriptor.Descriptor(
  name='MutateLabelsResponse',
  full_name='google.ads.googleads.v5.services.MutateLabelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v5.services.MutateLabelsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v5.services.MutateLabelsResponse.results', index=1,
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
  serialized_start=970,
  serialized_end=1113,
)


_MUTATELABELRESULT = _descriptor.Descriptor(
  name='MutateLabelResult',
  full_name='google.ads.googleads.v5.services.MutateLabelResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.services.MutateLabelResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.ads.googleads.v5.services.MutateLabelResult.label', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1115,
  serialized_end=1214,
)

_MUTATELABELSREQUEST.fields_by_name['operations'].message_type = _LABELOPERATION
_MUTATELABELSREQUEST.fields_by_name['response_content_type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_response__content__type__pb2._RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE
_LABELOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LABELOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_label__pb2._LABEL
_LABELOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_label__pb2._LABEL
_LABELOPERATION.oneofs_by_name['operation'].fields.append(
  _LABELOPERATION.fields_by_name['create'])
_LABELOPERATION.fields_by_name['create'].containing_oneof = _LABELOPERATION.oneofs_by_name['operation']
_LABELOPERATION.oneofs_by_name['operation'].fields.append(
  _LABELOPERATION.fields_by_name['update'])
_LABELOPERATION.fields_by_name['update'].containing_oneof = _LABELOPERATION.oneofs_by_name['operation']
_LABELOPERATION.oneofs_by_name['operation'].fields.append(
  _LABELOPERATION.fields_by_name['remove'])
_LABELOPERATION.fields_by_name['remove'].containing_oneof = _LABELOPERATION.oneofs_by_name['operation']
_MUTATELABELSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATELABELSRESPONSE.fields_by_name['results'].message_type = _MUTATELABELRESULT
_MUTATELABELRESULT.fields_by_name['label'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_label__pb2._LABEL
DESCRIPTOR.message_types_by_name['GetLabelRequest'] = _GETLABELREQUEST
DESCRIPTOR.message_types_by_name['MutateLabelsRequest'] = _MUTATELABELSREQUEST
DESCRIPTOR.message_types_by_name['LabelOperation'] = _LABELOPERATION
DESCRIPTOR.message_types_by_name['MutateLabelsResponse'] = _MUTATELABELSRESPONSE
DESCRIPTOR.message_types_by_name['MutateLabelResult'] = _MUTATELABELRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetLabelRequest = _reflection.GeneratedProtocolMessageType('GetLabelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLABELREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.label_service_pb2'
  ,
  '__doc__': """Request message for [LabelService.GetLabel][google.ads.googleads.v5.se
  rvices.LabelService.GetLabel].
  
  Attributes:
      resource_name:
          Required. The resource name of the label to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.GetLabelRequest)
  })
_sym_db.RegisterMessage(GetLabelRequest)

MutateLabelsRequest = _reflection.GeneratedProtocolMessageType('MutateLabelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATELABELSREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.label_service_pb2'
  ,
  '__doc__': """Request message for [LabelService.MutateLabels][google.ads.googleads.v
  5.services.LabelService.MutateLabels].
  
  Attributes:
      customer_id:
          Required. ID of the customer whose labels are being modified.
      operations:
          Required. The list of operations to perform on labels.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
      response_content_type:
          The response content type setting. Determines whether the
          mutable resource or just the resource name should be returned
          post mutation.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateLabelsRequest)
  })
_sym_db.RegisterMessage(MutateLabelsRequest)

LabelOperation = _reflection.GeneratedProtocolMessageType('LabelOperation', (_message.Message,), {
  'DESCRIPTOR' : _LABELOPERATION,
  '__module__' : 'google.ads.googleads_v5.proto.services.label_service_pb2'
  ,
  '__doc__': """A single operation (create, remove, update) on a label.
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          label.
      update:
          Update operation: The label is expected to have a valid
          resource name.
      remove:
          Remove operation: A resource name for the label being removed,
          in this format:  ``customers/{customer_id}/labels/{label_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.LabelOperation)
  })
_sym_db.RegisterMessage(LabelOperation)

MutateLabelsResponse = _reflection.GeneratedProtocolMessageType('MutateLabelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATELABELSRESPONSE,
  '__module__' : 'google.ads.googleads_v5.proto.services.label_service_pb2'
  ,
  '__doc__': """Response message for a labels mutate.
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateLabelsResponse)
  })
_sym_db.RegisterMessage(MutateLabelsResponse)

MutateLabelResult = _reflection.GeneratedProtocolMessageType('MutateLabelResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATELABELRESULT,
  '__module__' : 'google.ads.googleads_v5.proto.services.label_service_pb2'
  ,
  '__doc__': """The result for a label mutate.
  
  Attributes:
      resource_name:
          Returned for successful operations.
      label:
          The mutated label with only mutable fields after mutate. The
          field will only be returned when response\_content\_type is
          set to "MUTABLE\_RESOURCE".
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.MutateLabelResult)
  })
_sym_db.RegisterMessage(MutateLabelResult)


DESCRIPTOR._options = None
_GETLABELREQUEST.fields_by_name['resource_name']._options = None
_MUTATELABELSREQUEST.fields_by_name['customer_id']._options = None
_MUTATELABELSREQUEST.fields_by_name['operations']._options = None

_LABELSERVICE = _descriptor.ServiceDescriptor(
  name='LabelService',
  full_name='google.ads.googleads.v5.services.LabelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1217,
  serialized_end=1641,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLabel',
    full_name='google.ads.googleads.v5.services.LabelService.GetLabel',
    index=0,
    containing_service=None,
    input_type=_GETLABELREQUEST,
    output_type=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_label__pb2._LABEL,
    serialized_options=b'\202\323\344\223\002*\022(/v5/{resource_name=customers/*/labels/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateLabels',
    full_name='google.ads.googleads.v5.services.LabelService.MutateLabels',
    index=1,
    containing_service=None,
    input_type=_MUTATELABELSREQUEST,
    output_type=_MUTATELABELSRESPONSE,
    serialized_options=b'\202\323\344\223\0020\"+/v5/customers/{customer_id=*}/labels:mutate:\001*\332A\026customer_id,operations',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LABELSERVICE)

DESCRIPTOR.services_by_name['LabelService'] = _LABELSERVICE

# @@protoc_insertion_point(module_scope)
