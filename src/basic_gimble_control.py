#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Joy
import sys, termios, tty, os, time


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def joy_callback(data, x, y):
    x_value = data.axes[1]
    y_value = data.axes[2]

    #Pan Joint
    if (x_value < (-0.5)):
        pan_status -= 0.1
    elif (x_value > (-0.5)):
        pan_status += 0.1

    #Tilt Joint
    if (y_value < (-0.5)):
        tilt_status -= 0.1
    if (y_value > (-0.5)):
        tilt_status += 0.1

def pan_tilt_joint():

    #Initial States
    pan_status = -0.3
    tilt_status = 0.0


    #Pan Joint Pub
    pubPan = rospy.Publisher('joint1_controller/command', Float64, queue_size=10)

    #Tilt Joint Pub
    pubTilt = rospy.Publisher('joint2_controller/command', Float64, queue_size=10)

    #Node init and Rate Set
    rospy.init_node('gimble', anonymous=True)
    rate = rospy.Rate(50) # 50hz - update rate

    #Joystick Subscriber
    rospy.Subscriber("joy", "sensor_msgs/Joy", joy_callback(pan_status, tilt_status))

    while not rospy.is_shutdown():

        #Tilt Joint
        rospy.loginfo(tilt_status)
        pubTilt.publish(tilt_status)

        #Pan Joint
        rospy.loginfo(pan_status)
        pubPan.publish(pan_status)

        """
        #Keyboard Testing
        input = getch()

        if input == 'l':
            tilt_status -= 0.01

        if input == 'h':
            tilt_status += 0.01

        if input == 'j':
            pan_status += 0.01

        if input == 'k':
            pan_status -= 0.01

        if input == 'q':
            time.sleep(5)

        """

        rate.sleep()


def pan_tilt_joint_keyboard():

    #Initial States
    pan_status = -0.3
    tilt_status = 0.0


    #Pan Joint Pub
    pubPan = rospy.Publisher('joint1_controller/command', Float64, queue_size=10)

    #Tilt Joint Pub
    pubTilt = rospy.Publisher('joint2_controller/command', Float64, queue_size=10)

    #Node init and Rate Set
    rospy.init_node('gimble', anonymous=True)
    rate = rospy.Rate(30) # 100hz - update rate

    #Joystick Subscriber
    #rospy.Subscriber("joy", sensor_msgs/Joy, joy_callback)

    while not rospy.is_shutdown():

        #Tilt Joint
        rospy.loginfo(tilt_status)
        pubTilt.publish(tilt_status)

        #Pan Joint
        rospy.loginfo(pan_status)
        pubPan.publish(pan_status)


        #Keyboard Testing
        input = getch()

        if input == 'l':
            tilt_status -= 0.01

        if input == 'h':
            tilt_status += 0.01

        if input == 'j':
            pan_status += 0.01

        if input == 'k':
            pan_status -= 0.01

        if input == 'q':
            time.sleep(5)




        rate.sleep()



if __name__ == '__main__':
    try:

        pan_tilt_joint_keyboard()
    except rospy.ROSInterruptException:
        pass