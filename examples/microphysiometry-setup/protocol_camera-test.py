import opentrons
from openworkstation import robot2, robot2, containers, instruments
from moduleSensor import *
from moduleLifter import *
from moduleTransportation import *
from commands import *

from picamera import PiCamera
from time import sleep

from camera import camera

robot2.reset()


modulepositions=getModulepositions()


camera.resolution = (750, 750)
camera.rotation = 90

connect()
home_all()
