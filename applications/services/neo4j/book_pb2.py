# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
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
  name='book.proto',
  package='rpc',
  syntax='proto3',
  serialized_options=b'Z\004/rpc\252\002\006Protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbook.proto\x12\x03rpc\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x16\n\x05Title\x12\r\n\x05title\x18\x01 \x01(\t\"c\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x03\x12\x0c\n\x04year\x18\x06 \x01(\x03\"D\n\nBookSimple\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0c\n\x04year\x18\x04 \x01(\x03\"$\n\x08\x42ookList\x12\x18\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\t.rpc.Book\"0\n\x0e\x42ookSimpleList\x12\x1e\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x0f.rpc.BookSimple2\xed\x02\n\x0b\x42ookService\x12\x31\n\x07GetBook\x12\x1b.google.protobuf.Int64Value\x1a\t.rpc.Book\x12\'\n\x0eGetBookByTitle\x12\n.rpc.Title\x1a\t.rpc.Book\x12\x33\n\x14GetBookSimpleByTitle\x12\n.rpc.Title\x1a\x0f.rpc.BookSimple\x12-\n\x10GetBooksBySearch\x12\n.rpc.Title\x1a\r.rpc.BookList\x12\x34\n\x0bGetAllBooks\x12\x16.google.protobuf.Empty\x1a\r.rpc.BookList\x12\x34\n\x11GetBookRecsAuthor\x12\n.rpc.Title\x1a\x13.rpc.BookSimpleList\x12\x32\n\x0fGetBookRecsYear\x12\n.rpc.Title\x1a\x13.rpc.BookSimpleListB\x0fZ\x04/rpc\xaa\x02\x06Protosb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_TITLE = _descriptor.Descriptor(
  name='Title',
  full_name='rpc.Title',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='rpc.Title.title', index=0,
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
  serialized_start=80,
  serialized_end=102,
)


_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='rpc.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rpc.Book.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.Book.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='rpc.Book.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='rpc.Book.author', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='rpc.Book.amount', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='rpc.Book.year', index=5,
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
  serialized_start=104,
  serialized_end=203,
)


_BOOKSIMPLE = _descriptor.Descriptor(
  name='BookSimple',
  full_name='rpc.BookSimple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rpc.BookSimple.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.BookSimple.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='rpc.BookSimple.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='rpc.BookSimple.year', index=3,
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
  serialized_start=205,
  serialized_end=273,
)


_BOOKLIST = _descriptor.Descriptor(
  name='BookList',
  full_name='rpc.BookList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='rpc.BookList.books', index=0,
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
  serialized_start=275,
  serialized_end=311,
)


_BOOKSIMPLELIST = _descriptor.Descriptor(
  name='BookSimpleList',
  full_name='rpc.BookSimpleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='rpc.BookSimpleList.books', index=0,
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
  serialized_start=313,
  serialized_end=361,
)

_BOOKLIST.fields_by_name['books'].message_type = _BOOK
_BOOKSIMPLELIST.fields_by_name['books'].message_type = _BOOKSIMPLE
DESCRIPTOR.message_types_by_name['Title'] = _TITLE
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['BookSimple'] = _BOOKSIMPLE
DESCRIPTOR.message_types_by_name['BookList'] = _BOOKLIST
DESCRIPTOR.message_types_by_name['BookSimpleList'] = _BOOKSIMPLELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Title = _reflection.GeneratedProtocolMessageType('Title', (_message.Message,), {
  'DESCRIPTOR' : _TITLE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Title)
  })
_sym_db.RegisterMessage(Title)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:rpc.Book)
  })
_sym_db.RegisterMessage(Book)

BookSimple = _reflection.GeneratedProtocolMessageType('BookSimple', (_message.Message,), {
  'DESCRIPTOR' : _BOOKSIMPLE,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:rpc.BookSimple)
  })
_sym_db.RegisterMessage(BookSimple)

BookList = _reflection.GeneratedProtocolMessageType('BookList', (_message.Message,), {
  'DESCRIPTOR' : _BOOKLIST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:rpc.BookList)
  })
_sym_db.RegisterMessage(BookList)

BookSimpleList = _reflection.GeneratedProtocolMessageType('BookSimpleList', (_message.Message,), {
  'DESCRIPTOR' : _BOOKSIMPLELIST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:rpc.BookSimpleList)
  })
_sym_db.RegisterMessage(BookSimpleList)


DESCRIPTOR._options = None

_BOOKSERVICE = _descriptor.ServiceDescriptor(
  name='BookService',
  full_name='rpc.BookService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=364,
  serialized_end=729,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBook',
    full_name='rpc.BookService.GetBook',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_wrappers__pb2._INT64VALUE,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBookByTitle',
    full_name='rpc.BookService.GetBookByTitle',
    index=1,
    containing_service=None,
    input_type=_TITLE,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBookSimpleByTitle',
    full_name='rpc.BookService.GetBookSimpleByTitle',
    index=2,
    containing_service=None,
    input_type=_TITLE,
    output_type=_BOOKSIMPLE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBooksBySearch',
    full_name='rpc.BookService.GetBooksBySearch',
    index=3,
    containing_service=None,
    input_type=_TITLE,
    output_type=_BOOKLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllBooks',
    full_name='rpc.BookService.GetAllBooks',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_BOOKLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBookRecsAuthor',
    full_name='rpc.BookService.GetBookRecsAuthor',
    index=5,
    containing_service=None,
    input_type=_TITLE,
    output_type=_BOOKSIMPLELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBookRecsYear',
    full_name='rpc.BookService.GetBookRecsYear',
    index=6,
    containing_service=None,
    input_type=_TITLE,
    output_type=_BOOKSIMPLELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKSERVICE)

DESCRIPTOR.services_by_name['BookService'] = _BOOKSERVICE

# @@protoc_insertion_point(module_scope)