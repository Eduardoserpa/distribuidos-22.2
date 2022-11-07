# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EnvMsg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='EnvMsg.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x45nvMsg.proto\"\x1c\n\x08ToSensor\x12\x10\n\x08variable\x18\x01 \x01(\x02\"r\n\nFromSensor\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.FromSensor.sensortype\x12\x12\n\nqueue_name\x18\x02 \x01(\t\"*\n\nsensortype\x12\x08\n\x04UMID\x10\x00\x12\x08\n\x04TEMP\x10\x01\x12\x08\n\x04LUMN\x10\x02\"\xa3\x01\n\x0c\x46romActuator\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.FromActuator.actuatortype\x12\x10\n\x08variable\x18\x02 \x01(\x02\x12\x14\n\x0cgrpc_address\x18\x03 \x01(\t\x12\x13\n\x0bobject_name\x18\x04 \x01(\t\",\n\x0c\x61\x63tuatortype\x12\x08\n\x04UMID\x10\x00\x12\x08\n\x04TEMP\x10\x01\x12\x08\n\x04LUMN\x10\x02\"\xa0\x01\n\x0eToHomeAssitent\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.ToHomeAssitent.objecttype\x12\x13\n\x0bobject_name\x18\x02 \x01(\t\x12\x12\n\nqueue_name\x18\x03 \x01(\t\x12\x14\n\x0cgrpc_address\x18\x04 \x01(\t\"%\n\nobjecttype\x12\n\n\x06SENSOR\x10\x00\x12\x0b\n\x07\x41TUATOR\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FROMSENSOR_SENSORTYPE = _descriptor.EnumDescriptor(
  name='sensortype',
  full_name='FromSensor.sensortype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UMID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LUMN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=118,
  serialized_end=160,
)
_sym_db.RegisterEnumDescriptor(_FROMSENSOR_SENSORTYPE)

_FROMACTUATOR_ACTUATORTYPE = _descriptor.EnumDescriptor(
  name='actuatortype',
  full_name='FromActuator.actuatortype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UMID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LUMN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=282,
  serialized_end=326,
)
_sym_db.RegisterEnumDescriptor(_FROMACTUATOR_ACTUATORTYPE)

_TOHOMEASSITENT_OBJECTTYPE = _descriptor.EnumDescriptor(
  name='objecttype',
  full_name='ToHomeAssitent.objecttype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SENSOR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATUATOR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=452,
  serialized_end=489,
)
_sym_db.RegisterEnumDescriptor(_TOHOMEASSITENT_OBJECTTYPE)


_TOSENSOR = _descriptor.Descriptor(
  name='ToSensor',
  full_name='ToSensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable', full_name='ToSensor.variable', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=44,
)


_FROMSENSOR = _descriptor.Descriptor(
  name='FromSensor',
  full_name='FromSensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='FromSensor.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queue_name', full_name='FromSensor.queue_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FROMSENSOR_SENSORTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=160,
)


_FROMACTUATOR = _descriptor.Descriptor(
  name='FromActuator',
  full_name='FromActuator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='FromActuator.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variable', full_name='FromActuator.variable', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grpc_address', full_name='FromActuator.grpc_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='FromActuator.object_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FROMACTUATOR_ACTUATORTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=326,
)


_TOHOMEASSITENT = _descriptor.Descriptor(
  name='ToHomeAssitent',
  full_name='ToHomeAssitent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ToHomeAssitent.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='ToHomeAssitent.object_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queue_name', full_name='ToHomeAssitent.queue_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grpc_address', full_name='ToHomeAssitent.grpc_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOHOMEASSITENT_OBJECTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=489,
)

_FROMSENSOR.fields_by_name['type'].enum_type = _FROMSENSOR_SENSORTYPE
_FROMSENSOR_SENSORTYPE.containing_type = _FROMSENSOR
_FROMACTUATOR.fields_by_name['type'].enum_type = _FROMACTUATOR_ACTUATORTYPE
_FROMACTUATOR_ACTUATORTYPE.containing_type = _FROMACTUATOR
_TOHOMEASSITENT.fields_by_name['type'].enum_type = _TOHOMEASSITENT_OBJECTTYPE
_TOHOMEASSITENT_OBJECTTYPE.containing_type = _TOHOMEASSITENT
DESCRIPTOR.message_types_by_name['ToSensor'] = _TOSENSOR
DESCRIPTOR.message_types_by_name['FromSensor'] = _FROMSENSOR
DESCRIPTOR.message_types_by_name['FromActuator'] = _FROMACTUATOR
DESCRIPTOR.message_types_by_name['ToHomeAssitent'] = _TOHOMEASSITENT

ToSensor = _reflection.GeneratedProtocolMessageType('ToSensor', (_message.Message,), dict(
  DESCRIPTOR = _TOSENSOR,
  __module__ = 'EnvMsg_pb2'
  # @@protoc_insertion_point(class_scope:ToSensor)
  ))
_sym_db.RegisterMessage(ToSensor)

FromSensor = _reflection.GeneratedProtocolMessageType('FromSensor', (_message.Message,), dict(
  DESCRIPTOR = _FROMSENSOR,
  __module__ = 'EnvMsg_pb2'
  # @@protoc_insertion_point(class_scope:FromSensor)
  ))
_sym_db.RegisterMessage(FromSensor)

FromActuator = _reflection.GeneratedProtocolMessageType('FromActuator', (_message.Message,), dict(
  DESCRIPTOR = _FROMACTUATOR,
  __module__ = 'EnvMsg_pb2'
  # @@protoc_insertion_point(class_scope:FromActuator)
  ))
_sym_db.RegisterMessage(FromActuator)

ToHomeAssitent = _reflection.GeneratedProtocolMessageType('ToHomeAssitent', (_message.Message,), dict(
  DESCRIPTOR = _TOHOMEASSITENT,
  __module__ = 'EnvMsg_pb2'
  # @@protoc_insertion_point(class_scope:ToHomeAssitent)
  ))
_sym_db.RegisterMessage(ToHomeAssitent)


# @@protoc_insertion_point(module_scope)
