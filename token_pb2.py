# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: token.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='token.proto',
  package='tokens',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0btoken.proto\x12\x06tokens\"N\n\x12lookuptokenRequest\x12\x11\n\tldap_name\x18\x01 \x01(\t\x12\x16\n\x0etoken_accessor\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"h\n\x12\x63reatetokenRequest\x12\x11\n\tldap_name\x18\x01 \x01(\t\x12\x0e\n\x06header\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\t\x12\x0b\n\x03ttl\x18\x04 \x01(\t\x12\x11\n\trenewable\x18\x05 \x01(\t\"B\n\x11renewtokenRequest\x12\x11\n\tldap_name\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\x0b\n\x03ttl\x18\x03 \x01(\t\"#\n\rtokenResponse\x12\x12\n\njsonstring\x18\x01 \x01(\t\"N\n\x12revoketokenRequest\x12\x11\n\tldap_name\x18\x01 \x01(\t\x12\x16\n\x0etoken_accessor\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"$\n\x0erevokeResponse\x12\x12\n\njsonstring\x18\x01 \x01(\t2\x97\x02\n\x06Tokens\x12\x42\n\x0blookupToken\x12\x1a.tokens.lookuptokenRequest\x1a\x15.tokens.tokenResponse\"\x00\x12\x42\n\x0b\x63reateToken\x12\x1a.tokens.createtokenRequest\x1a\x15.tokens.tokenResponse\"\x00\x12@\n\nrenewToken\x12\x19.tokens.renewtokenRequest\x1a\x15.tokens.tokenResponse\"\x00\x12\x43\n\x0brevokeToken\x12\x1a.tokens.revoketokenRequest\x1a\x16.tokens.revokeResponse\"\x00\x62\x06proto3'
)




_LOOKUPTOKENREQUEST = _descriptor.Descriptor(
  name='lookuptokenRequest',
  full_name='tokens.lookuptokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ldap_name', full_name='tokens.lookuptokenRequest.ldap_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_accessor', full_name='tokens.lookuptokenRequest.token_accessor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='tokens.lookuptokenRequest.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=101,
)


_CREATETOKENREQUEST = _descriptor.Descriptor(
  name='createtokenRequest',
  full_name='tokens.createtokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ldap_name', full_name='tokens.createtokenRequest.ldap_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='header', full_name='tokens.createtokenRequest.header', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='tokens.createtokenRequest.payload', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='tokens.createtokenRequest.ttl', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='renewable', full_name='tokens.createtokenRequest.renewable', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=207,
)


_RENEWTOKENREQUEST = _descriptor.Descriptor(
  name='renewtokenRequest',
  full_name='tokens.renewtokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ldap_name', full_name='tokens.renewtokenRequest.ldap_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='tokens.renewtokenRequest.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='tokens.renewtokenRequest.ttl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=275,
)


_TOKENRESPONSE = _descriptor.Descriptor(
  name='tokenResponse',
  full_name='tokens.tokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jsonstring', full_name='tokens.tokenResponse.jsonstring', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=312,
)


_REVOKETOKENREQUEST = _descriptor.Descriptor(
  name='revoketokenRequest',
  full_name='tokens.revoketokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ldap_name', full_name='tokens.revoketokenRequest.ldap_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_accessor', full_name='tokens.revoketokenRequest.token_accessor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='tokens.revoketokenRequest.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=392,
)


_REVOKERESPONSE = _descriptor.Descriptor(
  name='revokeResponse',
  full_name='tokens.revokeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jsonstring', full_name='tokens.revokeResponse.jsonstring', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=430,
)

DESCRIPTOR.message_types_by_name['lookuptokenRequest'] = _LOOKUPTOKENREQUEST
DESCRIPTOR.message_types_by_name['createtokenRequest'] = _CREATETOKENREQUEST
DESCRIPTOR.message_types_by_name['renewtokenRequest'] = _RENEWTOKENREQUEST
DESCRIPTOR.message_types_by_name['tokenResponse'] = _TOKENRESPONSE
DESCRIPTOR.message_types_by_name['revoketokenRequest'] = _REVOKETOKENREQUEST
DESCRIPTOR.message_types_by_name['revokeResponse'] = _REVOKERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

lookuptokenRequest = _reflection.GeneratedProtocolMessageType('lookuptokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPTOKENREQUEST,
  '__module__' : 'token_pb2'
  # @@protoc_insertion_point(class_scope:tokens.lookuptokenRequest)
  })
_sym_db.RegisterMessage(lookuptokenRequest)

createtokenRequest = _reflection.GeneratedProtocolMessageType('createtokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOKENREQUEST,
  '__module__' : 'token_pb2'
  # @@protoc_insertion_point(class_scope:tokens.createtokenRequest)
  })
_sym_db.RegisterMessage(createtokenRequest)

renewtokenRequest = _reflection.GeneratedProtocolMessageType('renewtokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _RENEWTOKENREQUEST,
  '__module__' : 'token_pb2'
  # @@protoc_insertion_point(class_scope:tokens.renewtokenRequest)
  })
_sym_db.RegisterMessage(renewtokenRequest)

tokenResponse = _reflection.GeneratedProtocolMessageType('tokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOKENRESPONSE,
  '__module__' : 'token_pb2'
  # @@protoc_insertion_point(class_scope:tokens.tokenResponse)
  })
_sym_db.RegisterMessage(tokenResponse)

revoketokenRequest = _reflection.GeneratedProtocolMessageType('revoketokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVOKETOKENREQUEST,
  '__module__' : 'token_pb2'
  # @@protoc_insertion_point(class_scope:tokens.revoketokenRequest)
  })
_sym_db.RegisterMessage(revoketokenRequest)

revokeResponse = _reflection.GeneratedProtocolMessageType('revokeResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVOKERESPONSE,
  '__module__' : 'token_pb2'
  # @@protoc_insertion_point(class_scope:tokens.revokeResponse)
  })
_sym_db.RegisterMessage(revokeResponse)



_TOKENS = _descriptor.ServiceDescriptor(
  name='Tokens',
  full_name='tokens.Tokens',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=433,
  serialized_end=712,
  methods=[
  _descriptor.MethodDescriptor(
    name='lookupToken',
    full_name='tokens.Tokens.lookupToken',
    index=0,
    containing_service=None,
    input_type=_LOOKUPTOKENREQUEST,
    output_type=_TOKENRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='createToken',
    full_name='tokens.Tokens.createToken',
    index=1,
    containing_service=None,
    input_type=_CREATETOKENREQUEST,
    output_type=_TOKENRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='renewToken',
    full_name='tokens.Tokens.renewToken',
    index=2,
    containing_service=None,
    input_type=_RENEWTOKENREQUEST,
    output_type=_TOKENRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='revokeToken',
    full_name='tokens.Tokens.revokeToken',
    index=3,
    containing_service=None,
    input_type=_REVOKETOKENREQUEST,
    output_type=_REVOKERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOKENS)

DESCRIPTOR.services_by_name['Tokens'] = _TOKENS

# @@protoc_insertion_point(module_scope)
