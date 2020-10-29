#include <rclcpp/rclcpp.hpp>
#include <chrono>
#include <string>
#include <functional>

using namespace std::chrono_literals;

class MyNode : public rclcpp::Node
{
public:
  MyNode()
    : Node("my_node")
  {
    this->declare_parameter<std::string>("my_implicit_parameter", "hello");
    this->declare_parameter<std::string>("my_explicit_parameter", "world");
    timer_ = this->create_wall_timer(
    1000ms, std::bind(&MyNode::respond, this));
  }

  void respond()
  {
    this->get_parameter("my_implicit_parameter", implicit_parameter_string_);
    this->get_parameter("my_explicit_parameter", explicit_parameter_string_);
    RCLCPP_INFO(this->get_logger(), "[%s] [%s]", implicit_parameter_string_.c_str(), explicit_parameter_string_.c_str());
  }

private:
  std::string implicit_parameter_string_;
  std::string explicit_parameter_string_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MyNode>());
  rclcpp::shutdown();
  return 0;
}
