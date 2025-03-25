// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from messages:msg/Control.idl
// generated code does not contain a copyright notice

#ifndef MESSAGES__MSG__DETAIL__CONTROL__BUILDER_HPP_
#define MESSAGES__MSG__DETAIL__CONTROL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "messages/msg/detail/control__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace messages
{

namespace msg
{

namespace builder
{

class Init_Control_distance
{
public:
  explicit Init_Control_distance(::messages::msg::Control & msg)
  : msg_(msg)
  {}
  ::messages::msg::Control distance(::messages::msg::Control::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::messages::msg::Control msg_;
};

class Init_Control_control
{
public:
  Init_Control_control()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Control_distance control(::messages::msg::Control::_control_type arg)
  {
    msg_.control = std::move(arg);
    return Init_Control_distance(msg_);
  }

private:
  ::messages::msg::Control msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::messages::msg::Control>()
{
  return messages::msg::builder::Init_Control_control();
}

}  // namespace messages

#endif  // MESSAGES__MSG__DETAIL__CONTROL__BUILDER_HPP_
