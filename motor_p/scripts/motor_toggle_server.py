#!/usr/bin/python3


from __future__ import print_function

from motor_p.srv import Motor_toggle,Motor_toggleResponse
import rospy

def handle_motor_toggle(req):
    rospy.loginfo("Received valid command from motor_toggle_client: "
    "Command [%s]"%(req.motor_toggle))
    return Motor_toggleResponse(req.motor_toggle)

def motor_toggle_server():
    rospy.init_node('motor_toggle_server')
    rospy.loginfo("Initializing motor_toggle_server_node")
    s = rospy.Service('toggle_motor', Motor_toggle, handle_motor_toggle)
    print("Ready to recieve motor control requests.")
    rospy.spin()

if __name__ == "__main__":
    motor_toggle_server()