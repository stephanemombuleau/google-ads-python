# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import campaign_asset_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__asset__pb2
from google.ads.google_ads.v5.proto.services import campaign_asset_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2


class CampaignAssetServiceStub(object):
    """Proto file describing the CampaignAsset service.

    Service to manage campaign assets.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCampaignAsset = channel.unary_unary(
                '/google.ads.googleads.v5.services.CampaignAssetService/GetCampaignAsset',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.GetCampaignAssetRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__asset__pb2.CampaignAsset.FromString,
                )
        self.MutateCampaignAssets = channel.unary_unary(
                '/google.ads.googleads.v5.services.CampaignAssetService/MutateCampaignAssets',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.MutateCampaignAssetsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.MutateCampaignAssetsResponse.FromString,
                )


class CampaignAssetServiceServicer(object):
    """Proto file describing the CampaignAsset service.

    Service to manage campaign assets.
    """

    def GetCampaignAsset(self, request, context):
        """Returns the requested campaign asset in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateCampaignAssets(self, request, context):
        """Creates or removes campaign assets. Operation statuses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CampaignAssetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCampaignAsset': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCampaignAsset,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.GetCampaignAssetRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__asset__pb2.CampaignAsset.SerializeToString,
            ),
            'MutateCampaignAssets': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateCampaignAssets,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.MutateCampaignAssetsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.MutateCampaignAssetsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.CampaignAssetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CampaignAssetService(object):
    """Proto file describing the CampaignAsset service.

    Service to manage campaign assets.
    """

    @staticmethod
    def GetCampaignAsset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.CampaignAssetService/GetCampaignAsset',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.GetCampaignAssetRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_campaign__asset__pb2.CampaignAsset.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateCampaignAssets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.CampaignAssetService/MutateCampaignAssets',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.MutateCampaignAssetsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_campaign__asset__service__pb2.MutateCampaignAssetsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
