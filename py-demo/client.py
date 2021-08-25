# Copyright 2015 gRPC authors.
from __future__ import print_function

import logging

import grpc
import gateway_pb2
import gateway_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = gateway_pb2_grpc.GatewayServiceStub(channel)
  req = gateway_pb2.SymbolRequest(symbol='a')
  response = stub.SubscribeTick(req)

  for tick in response:
      print(f'onTick:{tick}')


if __name__ == '__main__':
    logging.basicConfig()
    run()