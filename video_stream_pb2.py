# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video_stream.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12video_stream.proto\"\x17\n\x08VideoUrl\x12\x0b\n\x03url\x18\x01 \x01(\t\"#\n\x13\x41nnotatedVideoChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x32H\n\x12VideoStreamService\x12\x32\n\x0bStreamVideo\x12\t.VideoUrl\x1a\x14.AnnotatedVideoChunk\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'video_stream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VIDEOURL']._serialized_start=22
  _globals['_VIDEOURL']._serialized_end=45
  _globals['_ANNOTATEDVIDEOCHUNK']._serialized_start=47
  _globals['_ANNOTATEDVIDEOCHUNK']._serialized_end=82
  _globals['_VIDEOSTREAMSERVICE']._serialized_start=84
  _globals['_VIDEOSTREAMSERVICE']._serialized_end=156
# @@protoc_insertion_point(module_scope)