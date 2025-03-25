// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from messages:msg/Control.idl
// generated code does not contain a copyright notice

#ifndef MESSAGES__MSG__DETAIL__CONTROL__STRUCT_HPP_
#define MESSAGES__MSG__DETAIL__CONTROL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__messages__msg__Control __attribute__((deprecated))
#else
# define DEPRECATED__messages__msg__Control __declspec(deprecated)
#endif

namespace messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Control_
{
  using Type = Control_<ContainerAllocator>;

  explicit Control_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->control = "";
      this->distance = 0.0f;
    }
  }

  explicit Control_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : control(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->control = "";
      this->distance = 0.0f;
    }
  }

  // field types and members
  using _control_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _control_type control;
  using _distance_type =
    float;
  _distance_type distance;

  // setters for named parameter idiom
  Type & set__control(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->control = _arg;
    return *this;
  }
  Type & set__distance(
    const float & _arg)
  {
    this->distance = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    messages::msg::Control_<ContainerAllocator> *;
  using ConstRawPtr =
    const messages::msg::Control_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<messages::msg::Control_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<messages::msg::Control_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      messages::msg::Control_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<messages::msg::Control_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      messages::msg::Control_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<messages::msg::Control_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<messages::msg::Control_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<messages::msg::Control_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__messages__msg__Control
    std::shared_ptr<messages::msg::Control_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__messages__msg__Control
    std::shared_ptr<messages::msg::Control_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Control_ & other) const
  {
    if (this->control != other.control) {
      return false;
    }
    if (this->distance != other.distance) {
      return false;
    }
    return true;
  }
  bool operator!=(const Control_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Control_

// alias to use template instance with default allocator
using Control =
  messages::msg::Control_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace messages

#endif  // MESSAGES__MSG__DETAIL__CONTROL__STRUCT_HPP_
