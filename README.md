# SCI_protobot

This ros package implements control for motors. A keyboard is used to teleoperate the motor in Gazebo. This directory is currently using ROS 1 (Noetic) tentatively

## Package Dependencies

- Joint State publisher. http://wiki.ros.org/joint_state_publisher

## Setup
1. Build package from source: navigate to the source folder of your catkin workspace and build this package using:
	```
	$ git clone https://github.com/RoboticSpaceExploration/SCI_protobot.git
	$ cd ..
	$ catkin_make
	```

### Controlling the motors:

1. Load the robot in the Gazebo environment.

	```
	$ roslaunch motor_p gazebo.launch
	```

2. Move the motor around. In another terminal type:

	 ```
	 $ rosrun motor_p keyboard_teleop.py 
	 ```

## Demo

![Screencast from 03-24-2022 03_35_56 AM](https://user-images.githubusercontent.com/70739998/159930850-f058981f-73fe-4b8a-8366-e06f385fa847.gif)
