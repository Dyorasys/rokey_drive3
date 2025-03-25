// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from messages:msg/Control.idl
// generated code does not contain a copyright notice

#ifndef MESSAGES__MSG__DETAIL__CONTROL__TRAITS_HPP_
#define MESSAGES__MSG__DETAIL__CONTROL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "messages/msg/detail/control__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace messages
{

namespace msg
{

inline void to_flow_style_yaml(
  const Control & msg,
  std::ostream & out)
{
  out << "{";
  // member: control
  {
    out << "control: ";
    rosidl_generator_traits::value_to_yaml(msg.control, out);
    out << ", ";
  }

  // member: distance
  {
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Control & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: control
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "control: ";
    rosidl_generator_traits::value_to_yaml(msg.control, out);
    out << "\n";
  }

  // member: distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance: ";
    rosidl_generator_traits::value_to_yaml(msg.distance, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Control & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace messages

namespace rosidl_generator_traits
{

[[deprecated("use messages::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const messages::msg::Control & msg,
  std::ostream & out, size_t indentation = 0)
{
  messages::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use messages::msg::to_yaml() instead")]]
inline std::string to_yaml(const messages::msg::Control & msg)
{
  return messages::msg::to_yaml(msg);
}

template<>
inline const char * data_type<messages::msg::Control>()
{
  return "messages::msg::Control";
}

template<>
inline const char * name<messages::msg::Control>()
{
  return "messages/msg/Control";
}

template<>
struct has_fixed_size<messages::msg::Control>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<messages::msg::Control>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<messages::msg::Control>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MESSAGES__MSG__DETAIL__CONTROL__TRAITS_HPP_
