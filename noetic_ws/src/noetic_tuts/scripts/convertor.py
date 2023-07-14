#!/usr/bin/env python3

import math
import rospy
from noetic_tuts.msg import Euler, Quaternion

def convert(quat):
    w = quat.q0
    x = quat.q1
    y = quat.q2
    z = quat.q3

    eul = Euler()

    eul.phi =    math.atan2(2*(w*x + y*z), 1-2*(x*x + y*y))
    eul.theta = -math.pi/2 + 2*math.atan2((1+2*(w*y - x*z))**0.5, (1-2*(w*y - x*z))**0.5)
    eul.psi =    math.atan2(2*(w*z + x*y), 1-2*(y*y + z*z))
    
    publish(eul)


def publish(eul):
    pub = rospy.Publisher('/output', Euler, queue_size=10)
    rospy.loginfo(eul)
    pub.publish(eul)


def main():
    # initialize node with subscriber constantly listening to '/input', sending 'Quaternion' data to convert() 
    rospy.init_node('convertor', anonymous=False)
    sub = rospy.Subscriber('/input', Quaternion, convert)
    rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
