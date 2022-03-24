# SCI_protobot

This ros package implements control for motors. A keyboard is used to teleoperate the motor in Gazebo. 

## Controlling the motors:

1. Load the robot in the Gazebo environment.

	```
	$ roslaunch motor_p gazebo.launch
	```

2. Move the robot around. In another terminal type:

	 ```
	 $ rosrun motor_p keyboard_teleop.py 
	 ```

## Demo

![Screencast from 03-24-2022 03_35_56 AM](https://user-images.githubusercontent.com/70739998/159930850-f058981f-73fe-4b8a-8366-e06f385fa847.gif)

