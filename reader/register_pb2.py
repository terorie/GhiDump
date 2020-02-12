# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='register.proto',
  package='protoclasses',
  syntax='proto3',
  serialized_options=b'B\rRegisterProto',
  serialized_pb=b'\n\x0eregister.proto\x12\x0cprotoclasses\"8\n\x0fRegisterMessage\x12\x10\n\x08register\x18\x01 \x01(\t\x12\x13\n\x0bregister_id\x18\x02 \x01(\x05\"A\n\rRegistersList\x12\x30\n\tregisters\x18\x01 \x03(\x0b\x32\x1d.protoclasses.RegisterMessageB\x0f\x42\rRegisterProtob\x06proto3'
)




_REGISTERMESSAGE = _descriptor.Descriptor(
  name='RegisterMessage',
  full_name='protoclasses.RegisterMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='register', full_name='protoclasses.RegisterMessage.register', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='register_id', full_name='protoclasses.RegisterMessage.register_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=32,
  serialized_end=88,
)


_REGISTERSLIST = _descriptor.Descriptor(
  name='RegistersList',
  full_name='protoclasses.RegistersList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registers', full_name='protoclasses.RegistersList.registers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=90,
  serialized_end=155,
)

_REGISTERSLIST.fields_by_name['registers'].message_type = _REGISTERMESSAGE
DESCRIPTOR.message_types_by_name['RegisterMessage'] = _REGISTERMESSAGE
DESCRIPTOR.message_types_by_name['RegistersList'] = _REGISTERSLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterMessage = _reflection.GeneratedProtocolMessageType('RegisterMessage', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERMESSAGE,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:protoclasses.RegisterMessage)
  })
_sym_db.RegisterMessage(RegisterMessage)

RegistersList = _reflection.GeneratedProtocolMessageType('RegistersList', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERSLIST,
  '__module__' : 'register_pb2'
  # @@protoc_insertion_point(class_scope:protoclasses.RegistersList)
  })
_sym_db.RegisterMessage(RegistersList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)