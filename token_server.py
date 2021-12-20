import grpc
import concurrent
from concurrent import futures
import hvac
import os

import token_pb2
import token_pb2_grpc

class TokenServicer(token_pb2_grpc.TokensServicer):
  def ldapLogin(self, request, context):
    print('Got ldap login request')
    file1 = open('./ldap.txt', 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
      count += 1
      if count == 1:
          _username = line.strip()
      else:
          _password = line.strip()

    client = hvac.Client(url='https://10.192.63.129:8200',verify = False)

    login_response = client.auth.ldap.login(
       username=_username,
       password=_password,
    )
    print('LDAP Authentication:')
    print(client.is_authenticated())

    current_token = client.auth.token.lookup_self()
    print("Token ties to LDAP:")
    print(current_token)

    print("Token generated:")
    token = client.auth.token.create(policies=['pd_software'], ttl='1h', renewable=True)
    print(token)

    #print("Token Renewed")
    #token = client.auth.token.renew('current token',wrap_ttl='240h')

    #print("Token Revoked")
    #token = client.auth.token.revoke('current token')
    # )

    response =  token_pb2.Response()
    response.jsonstring = f"here is your {request.ldap_name} token {request.password} ldap_name!"
    response.jsonstring = str(client.is_authenticated())
    return response


  def certLogin(self, request, context):
    print('Got certificate login request')
    client_cert_path = './certificate.crt'
    client_key_path = './privatekey.key'
    #server_cert_path = 'CA_cert.crt'

    client = hvac.Client(
        url='https://10.192.63.129:8200',
        cert=(client_cert_path, client_key_path),
        verify=False
    )
    res = client.is_authenticated()
    print("res:",res)	
    response =  token_pb2.Response()
    response.jsonstring = str(client.is_authenticated())
    return response

    #create_response = client.secrets.kv.v1.create_or_update_secret('s_pd_software/test', secret=dict(smu='true'))
    #read_response = client.secrets.kv.v1.read_secret('s_pd_software/test')
    #print('Value under path "s_pd_software/test" / key "smu": {val}'.format(val=read_response['data']['smu'],))

  def lookupToken(self, request, context):
    print('Got lookupToken request')
    file1 = open('./ldap.txt', 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
      count += 1
      if count == 1:
          _username = line.strip()
      else:
          _password = line.strip()

    client = hvac.Client(url='https://10.192.63.129:8200',verify = False)

    login_response = client.auth.ldap.login(
       username=_username,
       password=_password,
    )
    print('LDAP Authentication:')
    print(client.is_authenticated())

    response =  token_pb2.tokenResponse()
    response.jsonstring = f"here is your {request.token} token {request.ldap_name} ldap_name!"
    response.jsonstring = str(client.is_authenticated())
    return response

def main():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  token_pb2_grpc.add_TokensServicer_to_server(TokenServicer(), server)
  print('Server Started. Listening on port 50051')
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

main()