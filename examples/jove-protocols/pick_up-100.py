import sys
import opentrons
from opentrons import robot, robot2, containers, instruments

from time import sleep

from commands import *
from modulePipetting import *
from mixing import *
from moduleCrosslinker import *
#from moduleStorage import *
from moduleTransportation import getTransportposition
#from calculations import getValues


# robot is being reset
robot.reset()
robot2.reset()

equipment=getEquipment()
transportposition=getTransportposition()




connect()
#home_all()
#move_to_modulePipetting()

robot.home()


pickup_pd100tip(0)



equipment['pd100'].drop_tip()





robot.home()
