// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from messages:msg/Control.idl
// generated code does not contain a copyright notice

#ifndef MESSAGES__MSG__DETAIL__CONTROL__STRUCT_H_
#define MESSAGES__MSG__DETAIL__CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'control'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Control in the package messages.
typedef struct messages__msg__Control
{
  /// 입력 명령 {"control":"go", "distacne.mm":"200} /
  rosidl_runtime_c__String control;
  /// {"control":"stop"}, 튜플형식으로 해야 하나???
  float distance;
} messages__msg__Control;

// Struct for a sequence of messages__msg__Control.
typedef struct messages__msg__Control__Sequence
{
  messages__msg__Control * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} messages__msg__Control__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MESSAGES__MSG__DETAIL__CONTROL__STRUCT_H_
