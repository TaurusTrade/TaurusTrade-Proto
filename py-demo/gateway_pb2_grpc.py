# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gateway_pb2 as gateway__pb2
import market_pb2 as market__pb2


class GatewayServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeTick = channel.unary_stream(
                '/taurustrade.framework.GatewayService/SubscribeTick',
                request_serializer=gateway__pb2.SymbolRequest.SerializeToString,
                response_deserializer=market__pb2.Tick.FromString,
                )


class GatewayServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubscribeTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GatewayServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeTick': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeTick,
                    request_deserializer=gateway__pb2.SymbolRequest.FromString,
                    response_serializer=market__pb2.Tick.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'taurustrade.framework.GatewayService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GatewayService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubscribeTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/taurustrade.framework.GatewayService/SubscribeTick',
            gateway__pb2.SymbolRequest.SerializeToString,
            market__pb2.Tick.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
