# Move to Plate to Pipetting Module

from time import sleep

import opentrons
from opentrons import robot, robot2, containers, instruments

from commands import *
from modulePipetting import *
from moduleCrosslinker import *
#from moduleStorage import *
from moduleTransportation import getTransportposition


robot.reset()
robot2.reset()

equipment=getEquipment()
wellposition=getWellposition()
transportposition=getTransportposition()

# home all axis beginning with pipetting module, transportation module, crosslinker module, then storage module
connect()

home_all()

move_to_modulePipetting()
