import grpc
import concurrent
from concurrent import futures

import token_pb2
import token_pb2_grpc

class TokenServicer(token_pb2_grpc.TokensServicer):
  def lookupToken(self, request, context):
    print('we got something!!')
    response =  token_pb2.tokenResponse()
    response.message = f"here is your {request.token} token {request.ldap_name} ldap_name!"
    return response

def main():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  token_pb2_grpc.add_TokensServicer_to_server(TokenServicer(), server)
  print('Server Started. Listening on port 50051')
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

main()