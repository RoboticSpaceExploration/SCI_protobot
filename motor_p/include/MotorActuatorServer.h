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

#ifndef SRC_PROTOBOT_HARDWARE_INCLUDE_LEDARRAYSERVER_H_
#define SRC_PROTOBOT_HARDWARE_INCLUDE_LEDARRAYSERVER_H_

#include <ros/ros.h>
#include "motor_p/motor_toggle.h"
#include "../include/MotorActuatorSettings.h"
#include "../include/MotorActuator.h"

class MotorActuatorServer {
 public:
  explicit MotorActuatorServer(MotorActuatorSettings* mas_ptr);
  void AdvertiseServerCheckCallback(MotorActuatorServer* MotorActuator_Server);
  MotorActuator Motor_Actuator;

 private:
  void GetYamlParams(MotorActuatorSettings* mas_ptr);
  void CheckMotorToggle(uint8_t cmd);
  bool MotorCommandStatusCallback(
      motor_p::motor_toggle::Request& req,
      motor_p::motor_toggle::Response& res);
  ros::ServiceServer service;
  ros::NodeHandle nh;
};

#endif  // SRC_PROTOBOT_HARDWARE_INCLUDE_LEDARRAYSERVER_H_

