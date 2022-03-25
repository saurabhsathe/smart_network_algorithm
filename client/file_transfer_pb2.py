# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_transfer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x66ile_transfer.proto\"%\n\x08Response\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\x08\"<\n\x07Request\x12\x0e\n\x06\x63hukid\x18\x01 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x10\n\x08\x63lientip\x18\x03 \x01(\t\")\n\x13ServerSpeedResponse\x12\x12\n\nserver_mtu\x18\x01 \x01(\x03\"7\n\x12ServerSpeedRequest\x12\x10\n\x08\x63lientip\x18\x01 \x01(\t\x12\x0f\n\x07request\x18\x02 \x01(\x03\"7\n\x11\x46ileTransferStart\x12\x10\n\x08\x63lientip\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"5\n\x0f\x46ileTransferEnd\x12\x10\n\x08\x63lientip\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"6\n\x10NetworkTestStart\x12\x10\n\x08\x63lientip\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"4\n\x0eNetworkTestEnd\x12\x10\n\x08\x63lientip\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"3\n\x0eGeneralMessage\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x10\n\x08\x63lientip\x18\x02 \x01(\t2\x88\x03\n\x13\x46ileTransferService\x12&\n\rfile_transfer\x12\x08.Request\x1a\t.Response\"\x00\x12=\n\x0eServerResponse\x12\x13.ServerSpeedRequest\x1a\x14.ServerSpeedResponse\"\x00\x12:\n\x11TransferFileStart\x12\x12.FileTransferStart\x1a\x0f.GeneralMessage\"\x00\x12\x36\n\x0fTransferFileEnd\x12\x10.FileTransferEnd\x1a\x0f.GeneralMessage\"\x00\x12\x33\n\rOptimizeStart\x12\x0f.GeneralMessage\x1a\x0f.GeneralMessage\"\x00\x12\x31\n\x0bOptimizeEnd\x12\x0f.GeneralMessage\x1a\x0f.GeneralMessage\"\x00\x12.\n\x15OptimizerFileTransfer\x12\x08.Request\x1a\t.Response\"\x00\x62\x06proto3')



_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_SERVERSPEEDRESPONSE = DESCRIPTOR.message_types_by_name['ServerSpeedResponse']
_SERVERSPEEDREQUEST = DESCRIPTOR.message_types_by_name['ServerSpeedRequest']
_FILETRANSFERSTART = DESCRIPTOR.message_types_by_name['FileTransferStart']
_FILETRANSFEREND = DESCRIPTOR.message_types_by_name['FileTransferEnd']
_NETWORKTESTSTART = DESCRIPTOR.message_types_by_name['NetworkTestStart']
_NETWORKTESTEND = DESCRIPTOR.message_types_by_name['NetworkTestEnd']
_GENERALMESSAGE = DESCRIPTOR.message_types_by_name['GeneralMessage']
Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

ServerSpeedResponse = _reflection.GeneratedProtocolMessageType('ServerSpeedResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSPEEDRESPONSE,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:ServerSpeedResponse)
  })
_sym_db.RegisterMessage(ServerSpeedResponse)

ServerSpeedRequest = _reflection.GeneratedProtocolMessageType('ServerSpeedRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERSPEEDREQUEST,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:ServerSpeedRequest)
  })
_sym_db.RegisterMessage(ServerSpeedRequest)

FileTransferStart = _reflection.GeneratedProtocolMessageType('FileTransferStart', (_message.Message,), {
  'DESCRIPTOR' : _FILETRANSFERSTART,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:FileTransferStart)
  })
_sym_db.RegisterMessage(FileTransferStart)

FileTransferEnd = _reflection.GeneratedProtocolMessageType('FileTransferEnd', (_message.Message,), {
  'DESCRIPTOR' : _FILETRANSFEREND,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:FileTransferEnd)
  })
_sym_db.RegisterMessage(FileTransferEnd)

NetworkTestStart = _reflection.GeneratedProtocolMessageType('NetworkTestStart', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKTESTSTART,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:NetworkTestStart)
  })
_sym_db.RegisterMessage(NetworkTestStart)

NetworkTestEnd = _reflection.GeneratedProtocolMessageType('NetworkTestEnd', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKTESTEND,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:NetworkTestEnd)
  })
_sym_db.RegisterMessage(NetworkTestEnd)

GeneralMessage = _reflection.GeneratedProtocolMessageType('GeneralMessage', (_message.Message,), {
  'DESCRIPTOR' : _GENERALMESSAGE,
  '__module__' : 'file_transfer_pb2'
  # @@protoc_insertion_point(class_scope:GeneralMessage)
  })
_sym_db.RegisterMessage(GeneralMessage)

_FILETRANSFERSERVICE = DESCRIPTOR.services_by_name['FileTransferService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESPONSE._serialized_start=23
  _RESPONSE._serialized_end=60
  _REQUEST._serialized_start=62
  _REQUEST._serialized_end=122
  _SERVERSPEEDRESPONSE._serialized_start=124
  _SERVERSPEEDRESPONSE._serialized_end=165
  _SERVERSPEEDREQUEST._serialized_start=167
  _SERVERSPEEDREQUEST._serialized_end=222
  _FILETRANSFERSTART._serialized_start=224
  _FILETRANSFERSTART._serialized_end=279
  _FILETRANSFEREND._serialized_start=281
  _FILETRANSFEREND._serialized_end=334
  _NETWORKTESTSTART._serialized_start=336
  _NETWORKTESTSTART._serialized_end=390
  _NETWORKTESTEND._serialized_start=392
  _NETWORKTESTEND._serialized_end=444
  _GENERALMESSAGE._serialized_start=446
  _GENERALMESSAGE._serialized_end=497
  _FILETRANSFERSERVICE._serialized_start=500
  _FILETRANSFERSERVICE._serialized_end=892
# @@protoc_insertion_point(module_scope)