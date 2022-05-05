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

#include "../include/MotorActuatorServer.h"
#include "../include/MotorActuatorSettings.h"

int main(int argc, char** argv) {
  ros::init(argc, argv, "motor_actuator_server_node");
  ROS_INFO("Initializing motor_actuator_server_node");

  MotorActuatorSettings* mas_ptr = new MotorActuatorSettings;

  MotorActuatorServer MotorActuator_Server(mas_ptr);
  MotorActuator_Server.Motor_Actuator.MotorActuatorInit(mas_ptr);

  MotorActuator_Server.AdvertiseServerCheckCallback(&MotorActuator_Server);

  ros::spin();

  MotorActuator_Server.Motor_Actuator.MotorActuatorQuit();
  delete mas_ptr;

  return 0;
}

MotorActuatorServer::MotorActuatorServer(MotorActuatorSettings* mas_ptr) {
  GetYamlParams(mas_ptr);
}

bool MotorActuatorServer::MotorCommandStatusCallback(
    motor_p::motor_toggle::Request& req,
    motor_p::motor_toggle::Response& res) {

  for (uint8_t i = 1; i <= 10; i++) {
    if (req.motor_toggle == i) {
      ROS_INFO("Received valid command from motor_actuator_client: "
               "Command: [%d]", req.motor_toggle);

      CheckMotorToggle(req.motor_toggle);

      ROS_INFO("Toggling motors");

      Motor_Actuator.ToggleMotorActuators(req.motor_toggle);

      res.reply = true;
      return true;
    }
  }

  if (req.motor_toggle == 93) {
    ROS_INFO("Received valid command from motor_actuator_client: "
             "Command: [%d]", req.motor_toggle);

    CheckMotorToggle(req.motor_toggle);

    ROS_INFO("Toggling motors");

    Motor_Actuator.ToggleMotorActuators(req.motor_toggle);

    res.reply = true;
    return true;
  }

  ROS_ERROR("Invalid command: [%d]", req.motor_toggle);
  return false;
}

void MotorActuatorServer::AdvertiseServerCheckCallback(
    MotorActuatorServer* MotorActuator_Server) {
  ROS_INFO("Advertising as motor_actuator_server");
  service = nh.advertiseService(
      "motor_actuator_server", &MotorActuatorServer::MotorCommandStatusCallback,
      MotorActuator_Server);
}

void MotorActuatorServer::GetYamlParams(MotorActuatorSettings* mas_ptr) {
  nh.getParam("/motor_settings/serial_port", mas_ptr->serialPortAddr);
  std::cout << mas_ptr->serialPortAddr << std::endl;
  nh.getParam("/motor_settings/baud_rate", mas_ptr->baudRate);
}

void MotorActuatorServer::CheckMotorToggle(uint8_t cmd) {
  switch (cmd) {
    case 0:
      ROS_INFO("Flashing Green Success");
      break;
    case 1:
      ROS_INFO("Autonomous Mode");
      break;
    case 2:
      ROS_INFO("Teleop Mode");
      break;
    case 3:
      ROS_INFO("LED Matrix Off");
      break;
    default:
      break;
  }
}

