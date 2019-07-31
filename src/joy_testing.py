#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64

x_axis = -0.0
y_axis = -0.0

def callback(data):
    #These values are based of off servo turn radius and the total arc you want them to be able to rotate about
    global x_axis
    global y_axis

    x_axis += ((data.axes[1]) * 0.2)
    y_axis += ((data.axes[2]) * 0.2)

    if (x_axis > 1.6):
        x_axis = 1.6
    elif(x_axis < -2.2):
        x_axis = -2.2

    if(y_axis > 2.5):
        y_axis = 2.5
    elif(y_axis < -2.5):
        y_axis = -2.5

    #Debugging messages-feel free to comment out
    print("X axis:" + str(x_axis))
    print("Y axis:" + str(y_axis))

    pub_x_axis.publish(x_axis)
    pub_y_axis.publish(y_axis)


# Intializes everything
def start():
    # starts the node
    rospy.init_node('Joystick_testing')

    #Pan Joint Positioning
    global pub_x_axis
    pub_x_axis = rospy.Publisher('joint1_controller/command', Float64, queue_size=10)

    #Tilt Joint Positioning
    global pub_y_axis
    pub_y_axis = rospy.Publisher('joint2_controller/command', Float64, queue_size=10)

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)

    rospy.spin()

if __name__ == '__main__':
    start()
