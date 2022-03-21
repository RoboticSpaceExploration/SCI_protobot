# SCI_protobot

Important commands 
* rosnode list
* rostopic list
* rostopic info [package_name]
* rostopic echo [package_name]
* rosmsg show [message_type]


Run the following commands to start nodes
* roscore
* rosrun [package_name] [nodename] 
* rosrun rqt_graph rqt_graph : this shows the ROS nodes currently running as well as the topics that connect to them, running this is optional 

INSTALLING A ROS PACKAGE Example 
$ cd ~/catkin_ws/src
$ git clone -b kinetic-devel https://github.com/ros/urdf.git
$ git clone https://github.com/ROBOTIS-GIT/turtlebot3
$ cd ~/catkin_ws
$ catkin_make