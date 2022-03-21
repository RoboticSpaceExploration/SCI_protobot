#!/usr/bin/python3

# The above line will ensure the interpreter used is the first one on your environments path
# Every python file needs to start with this

import rospy # import the rospy, which is a python library for ROS.

rospy.init_node('printer_node') #initiate a node called printer_node
print 
"\n\nHello World - ROS tutorial\n\n" #simple python print 

# sometimes a python file is created without execution permisions, so use the following command 
# to add execution permissions: chmod +x name_of_python_file.py




