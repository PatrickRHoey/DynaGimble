<h1>Dynamixel Gimble Controller</h1>
This allows you to control dynamixel motors via any standard linux joystick utilizing ROS. Currently configured for a RX-28 and
RX-24F Servo, but can be easily altered to fit any system of dynamixels. Designed on ROS-Kinetic.

\
If you intend to add additional servos to create an arm/etc you need to edit the yaml and the launch files
include in order to serve your project
<h2>Launch Instructions</h2>

1. roslaunch DynaGimble controller_manager.launch
2. roslaunch DynaGimble start_meta_controller.launch
3. rosrun joy joy_node
4. rosrun DynaGimble joy_testing.py

***
* Ensure that the power supply is properly powering your servos and that both the servos and the joystick are properly connected when running the system

<h2>Requirements</h2>
* ros-kinetic
* ros-kinetic-dynamixel-controllers
