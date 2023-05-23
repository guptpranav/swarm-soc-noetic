#!/usr/bin/env python3

import rospy
from std_msgs.msg import String     # import type of message to be read


def callback(data):
    # print raw message passed to callback() by Subscriber as std_msgs.msg/String type 
    rospy.loginfo(rospy.get_caller_id() + " and here's what I heard: %s", data.data)
    # otherwise simply print a convenient message on the terminal
    print('Data from /topic_name received')

def subscriber():
    # initialize an anonymous (uniquely named) node by the name 'listener'
    rospy.init_node('listener', anonymous=True)
    # initialize Subscriber object from rospy that will subscribe 'std_msg.msg/String' type from topic '/audience' and send it to callback()
    rospy.Subscriber("audience", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
