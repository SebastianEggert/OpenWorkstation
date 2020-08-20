import opentrons
from openworkstation import robot2

# uncomment the following two line if PiCamera is used with a RaspberryPi
# from picamera import PiCamera
# from camera import camera

# uncomment used modules
# from moduleSensor import *
# liftings commands for a 96 well plate
from moduleLifter import lift_lid_from_plate96, lift_lid_from_holder_plate96
# placing commands for a 96 well plate
from moduleLifter import place_lid_onto_plate96, place_lid_onto_holder_plate96
from moduleTransportation import move_to_lidHolder, move_to_moduleLifter, \
    move_to_moduleSensor
# import measurement protocol scripted for a well palte format
from moduleTransportation import measure_96plate
from commands import connect, home_all

# reset robot
robot2.reset()

# if RPi is used, uncomment the next two lines
# camera.resolution = (750, 750)
# camera.rotation = 90

# define time for well measurement in moduleTransportation
# for example
# time_per_measurement = 120

# connect to USB ports
connect()
# home specified linear stages
home_all()


