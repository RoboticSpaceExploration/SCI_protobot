# SCI_protobot

## Important commands 
- rosnode list
- rostopic list
- rostopic info *package_name*
- rostopic echo *package_name*
- rosmsg show *message_type*


## Run the following commands to start nodes
1. roscore
2. rosrun *package_name* *nodename* 
3. rosrun rqt_graph rqt_graph : this shows the ROS nodes currently running as well as the topics that connect to them, running this is optional 

## INSTALLING A ROS PACKAGE Example using git clone 
1. cd ~/catkin_ws/src
2. git clone -b kinetic-devel https://github.com/ros urdf.git
3. git clone https://github.com/ROBOTIS-GIT/turtlebot3
4. cd ~/catkin_ws
5. catkin_make

## INSTALLING A ROS PACKAGE Example form source code

- Whenever you see <mark>"Could not find a configuration file for package <package_name>"</mark> it means this package is missing and is needed for compiling your code.
- Possible solution: Use <mark>rosdep</mark> command, which will automatically try to find all the dependencies of your package and install them.



