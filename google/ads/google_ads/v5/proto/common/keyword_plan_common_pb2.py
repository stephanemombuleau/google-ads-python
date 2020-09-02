# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/common/keyword_plan_common.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import keyword_plan_competition_level_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__plan__competition__level__pb2
from google.ads.google_ads.v5.proto.enums import month_of_year_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_month__of__year__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/common/keyword_plan_common.proto',
  package='google.ads.googleads.v5.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v5.commonB\026KeywordPlanCommonProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V5.Common\312\002\036Google\\Ads\\GoogleAds\\V5\\Common\352\002\"Google::Ads::GoogleAds::V5::Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>google/ads/googleads_v5/proto/common/keyword_plan_common.proto\x12\x1egoogle.ads.googleads.v5.common\x1aHgoogle/ads/googleads_v5/proto/enums/keyword_plan_competition_level.proto\x1a\x37google/ads/googleads_v5/proto/enums/month_of_year.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xda\x03\n\x1cKeywordPlanHistoricalMetrics\x12\x39\n\x14\x61vg_monthly_searches\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12S\n\x16monthly_search_volumes\x18\x06 \x03(\x0b\x32\x33.google.ads.googleads.v5.common.MonthlySearchVolume\x12o\n\x0b\x63ompetition\x18\x02 \x01(\x0e\x32Z.google.ads.googleads.v5.enums.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel\x12\x36\n\x11\x63ompetition_index\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12?\n\x1alow_top_of_page_bid_micros\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bhigh_top_of_page_bid_micros\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"\xc2\x01\n\x13MonthlySearchVolume\x12)\n\x04year\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12I\n\x05month\x18\x02 \x01(\x0e\x32:.google.ads.googleads.v5.enums.MonthOfYearEnum.MonthOfYear\x12\x35\n\x10monthly_searches\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\xf1\x01\n\"com.google.ads.googleads.v5.commonB\x16KeywordPlanCommonProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V5.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V5\\Common\xea\x02\"Google::Ads::GoogleAds::V5::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__plan__competition__level__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_month__of__year__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_KEYWORDPLANHISTORICALMETRICS = _descriptor.Descriptor(
  name='KeywordPlanHistoricalMetrics',
  full_name='google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='avg_monthly_searches', full_name='google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics.avg_monthly_searches', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monthly_search_volumes', full_name='google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics.monthly_search_volumes', index=1,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='competition', full_name='google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics.competition', index=2,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='competition_index', full_name='google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics.competition_index', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low_top_of_page_bid_micros', full_name='google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics.low_top_of_page_bid_micros', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high_top_of_page_bid_micros', full_name='google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics.high_top_of_page_bid_micros', index=5,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=292,
  serialized_end=766,
)


_MONTHLYSEARCHVOLUME = _descriptor.Descriptor(
  name='MonthlySearchVolume',
  full_name='google.ads.googleads.v5.common.MonthlySearchVolume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='google.ads.googleads.v5.common.MonthlySearchVolume.year', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='month', full_name='google.ads.googleads.v5.common.MonthlySearchVolume.month', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monthly_searches', full_name='google.ads.googleads.v5.common.MonthlySearchVolume.monthly_searches', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=769,
  serialized_end=963,
)

_KEYWORDPLANHISTORICALMETRICS.fields_by_name['avg_monthly_searches'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANHISTORICALMETRICS.fields_by_name['monthly_search_volumes'].message_type = _MONTHLYSEARCHVOLUME
_KEYWORDPLANHISTORICALMETRICS.fields_by_name['competition'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_keyword__plan__competition__level__pb2._KEYWORDPLANCOMPETITIONLEVELENUM_KEYWORDPLANCOMPETITIONLEVEL
_KEYWORDPLANHISTORICALMETRICS.fields_by_name['competition_index'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANHISTORICALMETRICS.fields_by_name['low_top_of_page_bid_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANHISTORICALMETRICS.fields_by_name['high_top_of_page_bid_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MONTHLYSEARCHVOLUME.fields_by_name['year'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MONTHLYSEARCHVOLUME.fields_by_name['month'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_month__of__year__pb2._MONTHOFYEARENUM_MONTHOFYEAR
_MONTHLYSEARCHVOLUME.fields_by_name['monthly_searches'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['KeywordPlanHistoricalMetrics'] = _KEYWORDPLANHISTORICALMETRICS
DESCRIPTOR.message_types_by_name['MonthlySearchVolume'] = _MONTHLYSEARCHVOLUME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanHistoricalMetrics = _reflection.GeneratedProtocolMessageType('KeywordPlanHistoricalMetrics', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANHISTORICALMETRICS,
  '__module__' : 'google.ads.googleads_v5.proto.common.keyword_plan_common_pb2'
  ,
  '__doc__': """Historical metrics specific to the targeting options selected.
  Targeting options include geographies, network, etc. Refer to
  https://support.google.com/google-ads/answer/3022575 for more details.
  
  Attributes:
      avg_monthly_searches:
          Approximate number of monthly searches on this query averaged
          for the past 12 months.
      monthly_search_volumes:
          Approximate number of searches on this query for the past
          twelve months.
      competition:
          The competition level for the query.
      competition_index:
          The competition index for the query in the range [0, 100].
          Shows how competitive ad placement is for a keyword. The level
          of competition from 0-100 is determined by the number of ad
          slots filled divided by the total number of ad slots
          available. If not enough data is available, null is returned.
      low_top_of_page_bid_micros:
          Top of page bid low range (20th percentile) in micros for the
          keyword.
      high_top_of_page_bid_micros:
          Top of page bid high range (80th percentile) in micros for the
          keyword.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.KeywordPlanHistoricalMetrics)
  })
_sym_db.RegisterMessage(KeywordPlanHistoricalMetrics)

MonthlySearchVolume = _reflection.GeneratedProtocolMessageType('MonthlySearchVolume', (_message.Message,), {
  'DESCRIPTOR' : _MONTHLYSEARCHVOLUME,
  '__module__' : 'google.ads.googleads_v5.proto.common.keyword_plan_common_pb2'
  ,
  '__doc__': """Monthly search volume.
  
  Attributes:
      year:
          The year of the search volume (e.g. 2020).
      month:
          The month of the search volume.
      monthly_searches:
          Approximate number of searches for the month. A null value
          indicates the search volume is unavailable for that month.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.MonthlySearchVolume)
  })
_sym_db.RegisterMessage(MonthlySearchVolume)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
