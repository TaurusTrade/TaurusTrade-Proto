from concurrent import futures
import logging

import grpc
import gateway_pb2_grpc
from GatewayService import GatewayService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gateway_pb2_grpc.add_GatewayServiceServicer_to_server(GatewayService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()