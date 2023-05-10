#! /usr/bin/python3
import rospy
import tf
import math
from geometry_msgs.msg import Twist
import turtlesim.srv
if __name__=='__main__':
 rospy.init_node('turtle_listener')
 listener=tf.TransformListener()
 rospy.wait_for_service('spawn')
spawner=rospy.ServiceProxy('spawn',turtlesim.srv.Spawn)
 spawner(4,2,0,'turtle2')
pub=rospy.Publisher('turtle2/cmd_vel',Twist,queue_size=10)

 rate=rospy.Rate(10.0)
 while not rospy.is_shutdown():
  try:
(trans,rot)=listener.lookupTransform('/turtle2','/turtle1',rospy.Time(0))
  except 
  (tf.LookupException,tf.ConnectivityException,tf.ExtrapolationException):
   continue
  linear=0.5*math.sqrt(trans[0] ** 2 + trans[1] ** 2)
  angular=4*math.atan2(trans[1],trans[0])
  cmd=Twist()
  cmd.linear.x=linear
  cmd.angular.z=angular
  pub.publish(cmd)
 
  rate.sleep()
