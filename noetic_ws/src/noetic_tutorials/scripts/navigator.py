#!/usr/bin/env python3

import rospy
from noetic_tutorials.srv import Fibonacci, FibonacciResponse


def fibonacci_server(request):
    # sleeping for 5.0s as per assignment requirements
    rospy.sleep(5.0)

    # calculating fibonacci number given the index
    index = request.n
    a = 0
    b = 1
    N = 1
    for _ in range(index):
        N = a+b
        a = b
        b = N
    
    # returning fibonacci number as a FibonacciResponse() object
    return FibonacciResponse(a)

def fibonacci():
    # initializing 'autopose' server node
    rospy.init_node('autopose', anonymous=False)
    # initializing 'fibonaccifier' service that reads Fibonacci() type request and passes it to fibonacci_server() method
    service = rospy.Service('fibonaccifier', Fibonacci, fibonacci_server)
    rospy.spin()

if __name__ == "__main__":
    try:
        fibonacci()
    except rospy.ROSInterruptException:
        pass
