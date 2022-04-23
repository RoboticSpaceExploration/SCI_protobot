/* MIT License

Copyright (c) [2022] [VIP Team RoSE]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. */

#include <stdint.h>
#include "ros/ros.h"
#include "motor_p/motor_toggle.h"

int main(int argc, char** argv) {
  ros::init(argc, argv, "motor_actuator_client_node");
  if (argc != 2) {
    ROS_INFO("USAGE: [cmd] between 0-3\n"
             "[1] : Flashing Success\n"
             "[2] : Autonomous Mode\n"
             "[3] : Teleop Mode\n"
             "[4] : Off");
    return 1;
  }

  ros::NodeHandle nh;
  ros::ServiceClient client = nh.serviceClient<motor_p::motor_toggle>
      ("motor_actuator_server");

  motor_p::motor_toggle srv;

  srv.request.motor_toggle = static_cast<uint8_t> (atoi(argv[1]));

  if (client.call(srv)) {
    ROS_INFO("Command sent to motor_actuator_server: [%d]", srv.request.motor_toggle);
    ROS_INFO("Reply: [%d]", srv.response.reply);
  } else {
    ROS_ERROR("[%d] is not a valid command ",
              srv.request.motor_toggle);
    ROS_ERROR("Reply: [%d]", srv.response.reply);
    return 1;
  }

  return 0;
}


