// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from messages:msg/Control.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "messages/msg/detail/control__rosidl_typesupport_introspection_c.h"
#include "messages/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "messages/msg/detail/control__functions.h"
#include "messages/msg/detail/control__struct.h"


// Include directives for member types
// Member `control`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void messages__msg__Control__rosidl_typesupport_introspection_c__Control_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  messages__msg__Control__init(message_memory);
}

void messages__msg__Control__rosidl_typesupport_introspection_c__Control_fini_function(void * message_memory)
{
  messages__msg__Control__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember messages__msg__Control__rosidl_typesupport_introspection_c__Control_message_member_array[2] = {
  {
    "control",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(messages__msg__Control, control),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "distance",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(messages__msg__Control, distance),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers messages__msg__Control__rosidl_typesupport_introspection_c__Control_message_members = {
  "messages__msg",  // message namespace
  "Control",  // message name
  2,  // number of fields
  sizeof(messages__msg__Control),
  messages__msg__Control__rosidl_typesupport_introspection_c__Control_message_member_array,  // message members
  messages__msg__Control__rosidl_typesupport_introspection_c__Control_init_function,  // function to initialize message memory (memory has to be allocated)
  messages__msg__Control__rosidl_typesupport_introspection_c__Control_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t messages__msg__Control__rosidl_typesupport_introspection_c__Control_message_type_support_handle = {
  0,
  &messages__msg__Control__rosidl_typesupport_introspection_c__Control_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, messages, msg, Control)() {
  if (!messages__msg__Control__rosidl_typesupport_introspection_c__Control_message_type_support_handle.typesupport_identifier) {
    messages__msg__Control__rosidl_typesupport_introspection_c__Control_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &messages__msg__Control__rosidl_typesupport_introspection_c__Control_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
