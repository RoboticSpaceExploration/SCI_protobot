#!/usr/bin/python3

# The above line will ensure the interpreter used is the first one on your environments path
# Every python file needs to start with this

# The publisher node publishes topics that other nodes can subscribe to

import queue
import rospy                                                # import the rospy, which is a python library for ROS.
from std_msgs.msg import String                             # import the String message from the std_msgs package 

rospy.init_node('topic_publisher')                          # initiate a node called 'topic_publisher'
pub = rospy.Publisher('phrases', String, queue_size = 10)   # create a publisher object that will publish on the "phrases" topic
                                                            # messages of type string
rate = rospy.Rate(2)                                        # set a publish rate od 2 hz
msg_str = String()                                          # create a var of type string 
msg_str = "Hello world ros tutorial"                        # initialize 'msg_str' variable

while not rospy.is_shutdown():                              # create that will go until someone stops the program execution 

    pub.publish(msg_str)                                    # publish the msg_string 
    rate.sleep()                                            # make sure the publish rate maintains at 2 Hz


# sometimes a python file is created without execution permisions, so use the following command 
# to add execution permissions: chmod +x name_of_python_file.py

