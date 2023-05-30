#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    

def user_trigger():
    rospy.wait_for_service('trigger')
    try:
        trigger = rospy.ServiceProxy('trigger', Empty)
        print("Please do something.")
        resp1 = trigger()
        num_1 = 5
        num_2 = 15
        sum_num = num_1 + num_2
        print("num_1 + num_2 = %s"%sum_num)
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        
if __name__ == "__main__":
    user_trigger()
    
    
