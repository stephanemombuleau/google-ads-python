# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.services import keyword_plan_idea_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__idea__service__pb2


class KeywordPlanIdeaServiceStub(object):
    """Proto file describing the keyword plan idea service.

    Service to generate keyword ideas.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateKeywordIdeas = channel.unary_unary(
                '/google.ads.googleads.v5.services.KeywordPlanIdeaService/GenerateKeywordIdeas',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__idea__service__pb2.GenerateKeywordIdeasRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__idea__service__pb2.GenerateKeywordIdeaResponse.FromString,
                )


class KeywordPlanIdeaServiceServicer(object):
    """Proto file describing the keyword plan idea service.

    Service to generate keyword ideas.
    """

    def GenerateKeywordIdeas(self, request, context):
        """Returns a list of keyword ideas.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeywordPlanIdeaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateKeywordIdeas': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateKeywordIdeas,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__idea__service__pb2.GenerateKeywordIdeasRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__idea__service__pb2.GenerateKeywordIdeaResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.KeywordPlanIdeaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeywordPlanIdeaService(object):
    """Proto file describing the keyword plan idea service.

    Service to generate keyword ideas.
    """

    @staticmethod
    def GenerateKeywordIdeas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.KeywordPlanIdeaService/GenerateKeywordIdeas',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__idea__service__pb2.GenerateKeywordIdeasRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_keyword__plan__idea__service__pb2.GenerateKeywordIdeaResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
