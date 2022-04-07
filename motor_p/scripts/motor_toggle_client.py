#!/usr/bin/python2

from __future__ import print_function

import sys
import rospy
from motor_p.srv import Motor_toggle

def motor_toggle_client(x):
    rospy.wait_for_service('toggle_motor')
    try:
        toggle_motor = rospy.ServiceProxy('toggle_motor', Motor_toggle)
        resp1 = toggle_motor(x)
        return resp1.reply
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s"%(x))
    print("%s Requested" %(motor_toggle_client(x)))
