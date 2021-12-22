# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vinyl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vinyl.proto',
  package='rpc',
  syntax='proto3',
  serialized_options=b'Z\004/rpc\252\002\006Protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bvinyl.proto\x12\x03rpc\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x1b\n\nVinylTitle\x12\r\n\x05title\x18\x01 \x01(\t\"d\n\x05Vinyl\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x03\x12\x0c\n\x04year\x18\x06 \x01(\x03\"E\n\x0bVinylSimple\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x03 \x01(\t\x12\x0c\n\x04year\x18\x04 \x01(\x03\"\'\n\tVinylList\x12\x1a\n\x06vinyls\x18\x01 \x03(\x0b\x32\n.rpc.Vinyl\"3\n\x0fVinylSimpleList\x12 \n\x06vinyls\x18\x01 \x03(\x0b\x32\x10.rpc.VinylSimple2\x95\x03\n\x0cVinylService\x12\x33\n\x08GetVinyl\x12\x1b.google.protobuf.Int64Value\x1a\n.rpc.Vinyl\x12.\n\x0fGetVinylByTitle\x12\x0f.rpc.VinylTitle\x1a\n.rpc.Vinyl\x12:\n\x15GetVinylSimpleByTitle\x12\x0f.rpc.VinylTitle\x1a\x10.rpc.VinylSimple\x12\x34\n\x11GetVinylsBySearch\x12\x0f.rpc.VinylTitle\x1a\x0e.rpc.VinylList\x12\x36\n\x0cGetAllVinyls\x12\x16.google.protobuf.Empty\x1a\x0e.rpc.VinylList\x12;\n\x12GetVinylRecsArtist\x12\x0f.rpc.VinylTitle\x1a\x14.rpc.VinylSimpleList\x12\x39\n\x10GetVinylRecsYear\x12\x0f.rpc.VinylTitle\x1a\x14.rpc.VinylSimpleListB\x0fZ\x04/rpc\xaa\x02\x06Protosb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_VINYLTITLE = _descriptor.Descriptor(
  name='VinylTitle',
  full_name='rpc.VinylTitle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='rpc.VinylTitle.title', index=0,
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
  serialized_start=81,
  serialized_end=108,
)


_VINYL = _descriptor.Descriptor(
  name='Vinyl',
  full_name='rpc.Vinyl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rpc.Vinyl.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.Vinyl.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='rpc.Vinyl.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='artist', full_name='rpc.Vinyl.artist', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='rpc.Vinyl.amount', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='rpc.Vinyl.year', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=110,
  serialized_end=210,
)


_VINYLSIMPLE = _descriptor.Descriptor(
  name='VinylSimple',
  full_name='rpc.VinylSimple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rpc.VinylSimple.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.VinylSimple.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='artist', full_name='rpc.VinylSimple.artist', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='rpc.VinylSimple.year', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=212,
  serialized_end=281,
)


_VINYLLIST = _descriptor.Descriptor(
  name='VinylList',
  full_name='rpc.VinylList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vinyls', full_name='rpc.VinylList.vinyls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=283,
  serialized_end=322,
)


_VINYLSIMPLELIST = _descriptor.Descriptor(
  name='VinylSimpleList',
  full_name='rpc.VinylSimpleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vinyls', full_name='rpc.VinylSimpleList.vinyls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=324,
  serialized_end=375,
)

_VINYLLIST.fields_by_name['vinyls'].message_type = _VINYL
_VINYLSIMPLELIST.fields_by_name['vinyls'].message_type = _VINYLSIMPLE
DESCRIPTOR.message_types_by_name['VinylTitle'] = _VINYLTITLE
DESCRIPTOR.message_types_by_name['Vinyl'] = _VINYL
DESCRIPTOR.message_types_by_name['VinylSimple'] = _VINYLSIMPLE
DESCRIPTOR.message_types_by_name['VinylList'] = _VINYLLIST
DESCRIPTOR.message_types_by_name['VinylSimpleList'] = _VINYLSIMPLELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VinylTitle = _reflection.GeneratedProtocolMessageType('VinylTitle', (_message.Message,), {
  'DESCRIPTOR' : _VINYLTITLE,
  '__module__' : 'vinyl_pb2'
  # @@protoc_insertion_point(class_scope:rpc.VinylTitle)
  })
_sym_db.RegisterMessage(VinylTitle)

Vinyl = _reflection.GeneratedProtocolMessageType('Vinyl', (_message.Message,), {
  'DESCRIPTOR' : _VINYL,
  '__module__' : 'vinyl_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Vinyl)
  })
_sym_db.RegisterMessage(Vinyl)

VinylSimple = _reflection.GeneratedProtocolMessageType('VinylSimple', (_message.Message,), {
  'DESCRIPTOR' : _VINYLSIMPLE,
  '__module__' : 'vinyl_pb2'
  # @@protoc_insertion_point(class_scope:rpc.VinylSimple)
  })
_sym_db.RegisterMessage(VinylSimple)

VinylList = _reflection.GeneratedProtocolMessageType('VinylList', (_message.Message,), {
  'DESCRIPTOR' : _VINYLLIST,
  '__module__' : 'vinyl_pb2'
  # @@protoc_insertion_point(class_scope:rpc.VinylList)
  })
_sym_db.RegisterMessage(VinylList)

VinylSimpleList = _reflection.GeneratedProtocolMessageType('VinylSimpleList', (_message.Message,), {
  'DESCRIPTOR' : _VINYLSIMPLELIST,
  '__module__' : 'vinyl_pb2'
  # @@protoc_insertion_point(class_scope:rpc.VinylSimpleList)
  })
_sym_db.RegisterMessage(VinylSimpleList)


DESCRIPTOR._options = None

_VINYLSERVICE = _descriptor.ServiceDescriptor(
  name='VinylService',
  full_name='rpc.VinylService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=378,
  serialized_end=783,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetVinyl',
    full_name='rpc.VinylService.GetVinyl',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._INT64VALUE,
    output_type=_VINYL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVinylByTitle',
    full_name='rpc.VinylService.GetVinylByTitle',
    index=1,
    containing_service=None,
    input_type=_VINYLTITLE,
    output_type=_VINYL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVinylSimpleByTitle',
    full_name='rpc.VinylService.GetVinylSimpleByTitle',
    index=2,
    containing_service=None,
    input_type=_VINYLTITLE,
    output_type=_VINYLSIMPLE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVinylsBySearch',
    full_name='rpc.VinylService.GetVinylsBySearch',
    index=3,
    containing_service=None,
    input_type=_VINYLTITLE,
    output_type=_VINYLLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllVinyls',
    full_name='rpc.VinylService.GetAllVinyls',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_VINYLLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVinylRecsArtist',
    full_name='rpc.VinylService.GetVinylRecsArtist',
    index=5,
    containing_service=None,
    input_type=_VINYLTITLE,
    output_type=_VINYLSIMPLELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVinylRecsYear',
    full_name='rpc.VinylService.GetVinylRecsYear',
    index=6,
    containing_service=None,
    input_type=_VINYLTITLE,
    output_type=_VINYLSIMPLELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VINYLSERVICE)

DESCRIPTOR.services_by_name['VinylService'] = _VINYLSERVICE

# @@protoc_insertion_point(module_scope)
