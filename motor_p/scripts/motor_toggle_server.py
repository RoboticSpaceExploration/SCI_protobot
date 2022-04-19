#!/usr/bin/python2

from __future__ import print_function
from motor_control import *
import signal

from motor_p.srv import Motor_toggle,Motor_toggleResponse
import rospy

def signal_handler(signum, frame):
    print("SIGINT called, closing serial connection")
    motors_quit()
    exit(1)

def handle_motor_toggle(req):
    if(req.motor_toggle > 0):
        rospy.loginfo("Received valid command from motor_toggle_client: "
        "Command [%s]"%(req.motor_toggle))
        toggle_motors(int(req.motor_toggle))

    return Motor_toggleResponse(req.motor_toggle)

def motor_toggle_server():
    signal.signal(signal.SIGINT, signal_handler)
    motors_init() # initialize hardware interface
    rospy.init_node('motor_toggle_server')
    rospy.loginfo("Initializing motor_toggle_server_node")
    s = rospy.Service('toggle_motor', Motor_toggle, handle_motor_toggle)
    print("Ready to recieve motor control requests.")
    rospy.spin()

if __name__ == "__main__":
    motor_toggle_server()
