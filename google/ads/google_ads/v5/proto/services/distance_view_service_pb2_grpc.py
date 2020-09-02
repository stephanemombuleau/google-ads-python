# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import distance_view_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_distance__view__pb2
from google.ads.google_ads.v5.proto.services import distance_view_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_distance__view__service__pb2


class DistanceViewServiceStub(object):
    """Proto file describing the Distance View service.

    Service to fetch distance views.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDistanceView = channel.unary_unary(
                '/google.ads.googleads.v5.services.DistanceViewService/GetDistanceView',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_distance__view__service__pb2.GetDistanceViewRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_distance__view__pb2.DistanceView.FromString,
                )


class DistanceViewServiceServicer(object):
    """Proto file describing the Distance View service.

    Service to fetch distance views.
    """

    def GetDistanceView(self, request, context):
        """Returns the attributes of the requested distance view.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DistanceViewServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDistanceView': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDistanceView,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_distance__view__service__pb2.GetDistanceViewRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_distance__view__pb2.DistanceView.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.DistanceViewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DistanceViewService(object):
    """Proto file describing the Distance View service.

    Service to fetch distance views.
    """

    @staticmethod
    def GetDistanceView(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.DistanceViewService/GetDistanceView',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_distance__view__service__pb2.GetDistanceViewRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_distance__view__pb2.DistanceView.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
