#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64


def callback(data):
    x_axis = (data.axes[1] + 0.4) * 3.6
    y_axis = (data.axes[2] + 0.5) * 5.2

    print("X axis:" + str(x_axis))
    print("Y axis:" + str(y_axis))

    pub_x_axis.publish(x_axis)
    pub_y_axis.publish(y_axis)

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub_x_axis
    pub_x_axis = rospy.Publisher('joint1_controller/command', Float64, queue_size=10)

    global pub_y_axis
    pub_y_axis = rospy.Publisher('joint2_controller/command', Float64, queue_size=10)

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joystick_testing')
    rospy.spin()

if __name__ == '__main__':
    start()