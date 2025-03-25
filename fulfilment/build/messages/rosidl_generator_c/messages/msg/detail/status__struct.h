// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from messages:msg/Status.idl
// generated code does not contain a copyright notice

#ifndef MESSAGES__MSG__DETAIL__STATUS__STRUCT_H_
#define MESSAGES__MSG__DETAIL__STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'status'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Status in the package messages.
typedef struct messages__msg__Status
{
  /// 로봇 상태 INIT, READY, RUN, DISCONNECT
  rosidl_runtime_c__String status;
} messages__msg__Status;

// Struct for a sequence of messages__msg__Status.
typedef struct messages__msg__Status__Sequence
{
  messages__msg__Status * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} messages__msg__Status__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MESSAGES__MSG__DETAIL__STATUS__STRUCT_H_
