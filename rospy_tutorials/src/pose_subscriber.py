#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(pose):
    rospy.loginfo("Turtle Pose: x: {}, y: {}, theta: {}".format(pose.x, pose.y, pose.theta))

def listener():
    rospy.init_node('turtle_pose_subscriber', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
