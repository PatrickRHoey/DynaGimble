#!/usr/bin/env python
import rospy
from time import sleep
from sensor_msgs.msg import Joy

class Joystick:
    def __init__(self):
        self.sub = rospy.Subscriber("/joy", Joy, self.joyCallback)
        self.joystick_message = []
        self.pan_joint = -0.3
        self.tilt_joint = 0.0

    def joyCallback(self, msg):
        self.joystick_message = msg
        #print(self.joystick_message)

    def getJoyStatus(self):


if __name__ == "__main__":
    rospy.init_node("joy_subscriber", anonymous=True)
    myJoyClass = Joystick()

    print(str(myJoyClass.getJoyStatus()))

    rospy.spin()


