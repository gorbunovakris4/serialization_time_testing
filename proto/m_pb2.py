# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: m.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='m.proto',
  package='test',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x07m.proto\x12\x04test\"g\n\x05Inner\x12\r\n\x05int_1\x18\x01 \x01(\x05\x12\x0f\n\x07\x66loat_1\x18\x02 \x01(\x02\x12\r\n\x05str_1\x18\x03 \x01(\t\x12\r\n\x05str_2\x18\x04 \x01(\t\x12\x0f\n\x07lst_int\x18\x05 \x03(\x05\x12\x0f\n\x07lst_str\x18\x06 \x03(\t\"!\n\x04Test\x12\x19\n\x04root\x18\x01 \x01(\x0b\x32\x0b.test.Inner')
)




_INNER = _descriptor.Descriptor(
  name='Inner',
  full_name='test.Inner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_1', full_name='test.Inner.int_1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_1', full_name='test.Inner.float_1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_1', full_name='test.Inner.str_1', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_2', full_name='test.Inner.str_2', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lst_int', full_name='test.Inner.lst_int', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lst_str', full_name='test.Inner.lst_str', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=120,
)


_TEST = _descriptor.Descriptor(
  name='Test',
  full_name='test.Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root', full_name='test.Test.root', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=155,
)

_TEST.fields_by_name['root'].message_type = _INNER
DESCRIPTOR.message_types_by_name['Inner'] = _INNER
DESCRIPTOR.message_types_by_name['Test'] = _TEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Inner = _reflection.GeneratedProtocolMessageType('Inner', (_message.Message,), dict(
  DESCRIPTOR = _INNER,
  __module__ = 'm_pb2'
  # @@protoc_insertion_point(class_scope:test.Inner)
  ))
_sym_db.RegisterMessage(Inner)

Test = _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), dict(
  DESCRIPTOR = _TEST,
  __module__ = 'm_pb2'
  # @@protoc_insertion_point(class_scope:test.Test)
  ))
_sym_db.RegisterMessage(Test)


# @@protoc_insertion_point(module_scope)
