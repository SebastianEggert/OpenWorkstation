import csv  # Needed for customers
import sys

from openworkstation.robot.robot import Robot
from openworkstation.robot2.robot2 import Robot2

robot = Robot()
robot2 = Robot2()

def reset():
    global robot
    robot = Robot()
    return robot

def reset2():
    global robot2
    robot2 = Robot2()
    return robot2

__all__ = [robot, robot2, reset, reset2]


