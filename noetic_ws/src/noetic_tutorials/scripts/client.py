#!/usr/bin/env python3

import rospy
from noetic_tutorials.srv import Fibonacci, FibonacciResponse

def fibonacci_client(index):
    # initializing 'navigator' client node
    rospy.init_node('navigator', anonymous=False)
    # waiting for 'fibonaccifier' service server to spawn in ROS master
    rospy.wait_for_service('fibonaccifier')
    
    while not rospy.is_shutdown():
        try:
            # initializing 'fibonaccifier' service server caller
            fibonaccify = rospy.ServiceProxy('fibonaccifier', Fibonacci)
            # calling service by passing index in Fibonacci form and storing and logging the response
            response = fibonaccify(index)
            rospy.loginfo(response.result)
        except rospy.ServiceException:
            print('service call failed')

if __name__ == "__main__":
    try:
        fibonacci_client(12)
    except rospy.ROSInterruptException:
        pass
