import grpc
from market_pb2 import Tick

import gateway_pb2_grpc

class GatewayService(gateway_pb2_grpc.GatewayServiceServicer):
    def SubscribeTick(self, request, context):
        for i in range(1,10):
            tick = Tick(symbol=request.symbol,openPrice=i)
            yield tick