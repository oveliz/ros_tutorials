#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('twist_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 2.0  # change this value to adjust linear speed
        twist.angular.z = 1.0  # change this value to adjust angular speed
        rospy.loginfo("Publishing twist command: linear x: %s angular z: %s", twist.linear.x, twist.angular.z)
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
