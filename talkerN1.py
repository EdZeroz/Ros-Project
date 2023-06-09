#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('pub1', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Sawasdeekarb I am Mick from pub1"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
