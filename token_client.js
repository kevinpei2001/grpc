const grpc = require('@grpc/grpc-js');
const messages = require('./token_pb');
const services = require('./token_grpc_pb');

function main() {
  const client = new services.TokensClient(
    'localhost:50051', grpc.credentials.createInsecure()
  );

  const lookuptokenRequest = new messages.lookuptokenRequest();
  lookuptokenRequest.setToken('abc');
  lookuptokenRequest.setLdapName('Steve.Nolan');

  client.lookupToken(lookuptokenRequest, function (err,response){
    if (err){
      console.log('Error', err);
    }else {
      console.log('response:', response)
    }
  })
}

main();
