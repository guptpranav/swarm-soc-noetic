#!/usr/bin/env python3

import rospy
from noetic_tuts.srv import Fibonacci, FibonacciResponse
from std_msgs.msg import Int64


def fibonacci_client(data):
    # waiting for 'fibonaccifier' service server to spawn in ROS master
    index = data.data
    rospy.wait_for_service('fibonaccifier')
    
    if index is not None:
        try:
            # initializing 'fibonaccifier' service server caller
            fibonaccify = rospy.ServiceProxy('fibonaccifier', Fibonacci)
            # calling service by passing index in Fibonacci form and storing and logging the response
            response = fibonaccify(index)
            rospy.loginfo(response.result)
        except rospy.ServiceException:
            print('service call failed')

def main():
    # initializing 'navigator' client node
    rospy.init_node('navigator', anonymous=False)
    rospy.Subscriber('fiboard', Int64, fibonacci_client)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
