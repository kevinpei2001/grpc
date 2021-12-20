// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var token_pb = require('./token_pb.js');

function serialize_tokens_createtokenRequest(arg) {
  if (!(arg instanceof token_pb.createtokenRequest)) {
    throw new Error('Expected argument of type tokens.createtokenRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_tokens_createtokenRequest(buffer_arg) {
  return token_pb.createtokenRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_tokens_lookuptokenRequest(arg) {
  if (!(arg instanceof token_pb.lookuptokenRequest)) {
    throw new Error('Expected argument of type tokens.lookuptokenRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_tokens_lookuptokenRequest(buffer_arg) {
  return token_pb.lookuptokenRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_tokens_renewtokenRequest(arg) {
  if (!(arg instanceof token_pb.renewtokenRequest)) {
    throw new Error('Expected argument of type tokens.renewtokenRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_tokens_renewtokenRequest(buffer_arg) {
  return token_pb.renewtokenRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_tokens_revokeResponse(arg) {
  if (!(arg instanceof token_pb.revokeResponse)) {
    throw new Error('Expected argument of type tokens.revokeResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_tokens_revokeResponse(buffer_arg) {
  return token_pb.revokeResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_tokens_revoketokenRequest(arg) {
  if (!(arg instanceof token_pb.revoketokenRequest)) {
    throw new Error('Expected argument of type tokens.revoketokenRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_tokens_revoketokenRequest(buffer_arg) {
  return token_pb.revoketokenRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_tokens_tokenResponse(arg) {
  if (!(arg instanceof token_pb.tokenResponse)) {
    throw new Error('Expected argument of type tokens.tokenResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_tokens_tokenResponse(buffer_arg) {
  return token_pb.tokenResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var TokensService = exports.TokensService = {
  lookupToken: {
    path: '/tokens.Tokens/lookupToken',
    requestStream: false,
    responseStream: false,
    requestType: token_pb.lookuptokenRequest,
    responseType: token_pb.tokenResponse,
    requestSerialize: serialize_tokens_lookuptokenRequest,
    requestDeserialize: deserialize_tokens_lookuptokenRequest,
    responseSerialize: serialize_tokens_tokenResponse,
    responseDeserialize: deserialize_tokens_tokenResponse,
  },
  createToken: {
    path: '/tokens.Tokens/createToken',
    requestStream: false,
    responseStream: false,
    requestType: token_pb.createtokenRequest,
    responseType: token_pb.tokenResponse,
    requestSerialize: serialize_tokens_createtokenRequest,
    requestDeserialize: deserialize_tokens_createtokenRequest,
    responseSerialize: serialize_tokens_tokenResponse,
    responseDeserialize: deserialize_tokens_tokenResponse,
  },
  renewToken: {
    path: '/tokens.Tokens/renewToken',
    requestStream: false,
    responseStream: false,
    requestType: token_pb.renewtokenRequest,
    responseType: token_pb.tokenResponse,
    requestSerialize: serialize_tokens_renewtokenRequest,
    requestDeserialize: deserialize_tokens_renewtokenRequest,
    responseSerialize: serialize_tokens_tokenResponse,
    responseDeserialize: deserialize_tokens_tokenResponse,
  },
  revokeToken: {
    path: '/tokens.Tokens/revokeToken',
    requestStream: false,
    responseStream: false,
    requestType: token_pb.revoketokenRequest,
    responseType: token_pb.revokeResponse,
    requestSerialize: serialize_tokens_revoketokenRequest,
    requestDeserialize: deserialize_tokens_revoketokenRequest,
    responseSerialize: serialize_tokens_revokeResponse,
    responseDeserialize: deserialize_tokens_revokeResponse,
  },
};

exports.TokensClient = grpc.makeGenericClientConstructor(TokensService);
