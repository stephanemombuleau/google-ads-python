# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import keyword_plan_ad_group_keyword_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2
from google.ads.google_ads.v5.proto.services import keyword_plan_ad_group_keyword_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2


class KeywordPlanAdGroupKeywordServiceStub(object):
    """Proto file describing the keyword plan ad group keyword service.

    Service to manage Keyword Plan ad group keywords. KeywordPlanAdGroup is
    required to add ad group keywords. Positive and negative keywords are
    supported. A maximum of 10,000 positive keywords are allowed per keyword
    plan. A maximum of 1,000 negative keywords are allower per keyword plan. This
    includes campaign negative keywords and ad group negative keywords.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetKeywordPlanAdGroupKeyword = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanAdGroupKeywordService/GetKeywordPlanAdGroupKeyword',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.GetKeywordPlanAdGroupKeywordRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2.KeywordPlanAdGroupKeyword.FromString,
                )
        self.MutateKeywordPlanAdGroupKeywords = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanAdGroupKeywordService/MutateKeywordPlanAdGroupKeywords',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.MutateKeywordPlanAdGroupKeywordsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.MutateKeywordPlanAdGroupKeywordsResponse.FromString,
                )


class KeywordPlanAdGroupKeywordServiceServicer(object):
    """Proto file describing the keyword plan ad group keyword service.

    Service to manage Keyword Plan ad group keywords. KeywordPlanAdGroup is
    required to add ad group keywords. Positive and negative keywords are
    supported. A maximum of 10,000 positive keywords are allowed per keyword
    plan. A maximum of 1,000 negative keywords are allower per keyword plan. This
    includes campaign negative keywords and ad group negative keywords.
    """

    def GetKeywordPlanAdGroupKeyword(self, request, context):
        """Returns the requested Keyword Plan ad group keyword in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateKeywordPlanAdGroupKeywords(self, request, context):
        """Creates, updates, or removes Keyword Plan ad group keywords. Operation
        statuses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeywordPlanAdGroupKeywordServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetKeywordPlanAdGroupKeyword': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKeywordPlanAdGroupKeyword,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.GetKeywordPlanAdGroupKeywordRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2.KeywordPlanAdGroupKeyword.SerializeToString,
            ),
            'MutateKeywordPlanAdGroupKeywords': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateKeywordPlanAdGroupKeywords,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.MutateKeywordPlanAdGroupKeywordsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.MutateKeywordPlanAdGroupKeywordsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.KeywordPlanAdGroupKeywordService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeywordPlanAdGroupKeywordService(object):
    """Proto file describing the keyword plan ad group keyword service.

    Service to manage Keyword Plan ad group keywords. KeywordPlanAdGroup is
    required to add ad group keywords. Positive and negative keywords are
    supported. A maximum of 10,000 positive keywords are allowed per keyword
    plan. A maximum of 1,000 negative keywords are allower per keyword plan. This
    includes campaign negative keywords and ad group negative keywords.
    """

    @staticmethod
    def GetKeywordPlanAdGroupKeyword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanAdGroupKeywordService/GetKeywordPlanAdGroupKeyword',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.GetKeywordPlanAdGroupKeywordRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2.KeywordPlanAdGroupKeyword.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateKeywordPlanAdGroupKeywords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanAdGroupKeywordService/MutateKeywordPlanAdGroupKeywords',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.MutateKeywordPlanAdGroupKeywordsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__ad__group__keyword__service__pb2.MutateKeywordPlanAdGroupKeywordsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
