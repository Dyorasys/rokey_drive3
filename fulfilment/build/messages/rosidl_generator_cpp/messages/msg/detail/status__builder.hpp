// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from messages:msg/Status.idl
// generated code does not contain a copyright notice

#ifndef MESSAGES__MSG__DETAIL__STATUS__BUILDER_HPP_
#define MESSAGES__MSG__DETAIL__STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "messages/msg/detail/status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace messages
{

namespace msg
{

namespace builder
{

class Init_Status_status
{
public:
  Init_Status_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::messages::msg::Status status(::messages::msg::Status::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::messages::msg::Status msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::messages::msg::Status>()
{
  return messages::msg::builder::Init_Status_status();
}

}  // namespace messages

#endif  // MESSAGES__MSG__DETAIL__STATUS__BUILDER_HPP_
