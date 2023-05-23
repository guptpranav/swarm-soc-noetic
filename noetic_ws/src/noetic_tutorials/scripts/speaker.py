#!/usr/bin/env python3

import rospy
from std_msgs.msg import String     # import type of message to be published


def publisher():
    
    # initialize Publisher object from rospy that will publish 'std_msg.msg/String' type to topic '/audience' 
    pub = rospy.Publisher('/audience', String, queue_size=10)
    # initialize anonymous (uniquely named) publishing node
    rospy.init_node('speaker', anonymous=True)
    # defining rate of publishing in Hertz
    hz = 10
    rate = rospy.Rate(hz)
    
    # keep publishing as long as the core is running
    while not rospy.is_shutdown():
        data = "whatever you want to publish\ttime = %s" % rospy.get_time()

        # you could simultaneously display the data
        # on the terminal and to the log file
        rospy.loginfo(data)

        # publish the data to the topic using publish() method of publisher object
        pub.publish(data)

        # sleeps for time interval to maintain the publishing rate defined earlier
        rate.sleep()
  
  
if __name__ == '__main__':
    # it is good practice to maintain
    # a 'try'-'except' clause
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
