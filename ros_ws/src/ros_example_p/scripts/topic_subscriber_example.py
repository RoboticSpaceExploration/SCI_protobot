#!/usr/bin/python3

# The above line will ensure the interpreter used is the first one on your environments path
# Every python file needs to start with this

import queue
import rospy                                                # import the rospy, which is a python library for ROS.
from std_msgs.msg import String                             # import the String message from the std_msgs package 

def callback(msg):                                          # Define a function called 'callback' that recieves a parameter named 'msg'

    print 
    msg.data                                            # Print the value 'data' inside the 'msg' parameter 

rospy.init_node('topic_subscriber')                     # Initiate a Node called 'topic_subscriber'
sub = rospy.Subscriber('/phrases', String, callback)    # Create a subscriber node object that will listen to the "phrases" topic and will call the 'callback'
                                                        # function each time it reads something from the topic

rospy.spin()                                            # Create a loop that will keep the program in execution


# sometimes a python file is created without execution permisions, so use the following command 
# to add execution permissions: chmod +x name_of_python_file.py

# HOW to run this file 
# rosrun ros_example_p topic_subscriber_example.py
# OR using the roslaunch 
# roslaunch ros_example_p topic_subscriber_example_launcher.launch


