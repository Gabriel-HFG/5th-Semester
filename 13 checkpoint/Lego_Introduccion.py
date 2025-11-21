#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

robot.settings(
    straight_speed=100000,     # mm/s
    straight_acceleration=500000,  # mm/s²
)

left_motor.run(20000)
right_motor.run(20000)

# Go forward and backwards for one meter.
robot.straight(5900)
ev3.speaker.beep()

robot.turn(110)
robot.straight(4690)
ev3.speaker.beep()

robot.turn(110)
robot.straight(8500)
ev3.speaker.beep()

ev3.speaker.say("Hello, I am EV3")
ev3.speaker.say("He he he ha")