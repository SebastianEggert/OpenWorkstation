from openworkstation import robot2
from time import sleep

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
from moduleSensor import *
from commands import connect, home_all

# reset robot
robot2.reset()

# if RPi is used, uncomment the next two lines
# camera.resolution = (750, 750)
# camera.rotation = 90

# define time for well measurement in moduleTransportation
# for example
# time_per_measurement = 120

plate96_G1 = 'G0 X64.6 Y3.7'
plate96_G12 = 'G0 X64.6 Y100.9'

plate96_A1 = 'G0 X118 Y3.7'
plate96_A2 = 'G0 X118 Y11.9'
plate96_A3 = 'G0 X118 Y20.8'
plate96_A4 = 'G0 X118 Y29.7'
plate96_A5 = 'G0 X118 Y38.6'
plate96_A6 = 'G0 X118 Y47.5'
plate96_A7 = 'G0 X118 Y56.4'
plate96_A8 = 'G0 X118 Y65.3'
plate96_A9 = 'G0 X118 Y74.2'
plate96_A10 = 'G0 X118 Y83.1'
plate96_A11 = 'G0 X118 Y92.0'
plate96_A12 = 'G0 X118 Y100.9'

plate96_B1 = 'G0 X109.1 Y3.7'
plate96_B2 = 'G0 X109.1 Y11.9'
plate96_B3 = 'G0 X109.1 Y20.8'
plate96_B4 = 'G0 X109.1 Y29.7'
plate96_B5 = 'G0 X109.1 Y38.6'
plate96_B6 = 'G0 X109.1 Y47.5'
plate96_B7 = 'G0 X109.1 Y56.4'
plate96_B8 = 'G0 X109.1 Y65.3'
plate96_B9 = 'G0 X109.1 Y74.2'
plate96_B10 = 'G0 X109.1 Y83.1'
plate96_B11 = 'G0 X109.1 Y92.0'
plate96_B12 = 'G0 X109.1 Y100.9'

plate96_C1 = 'G0 X100.2 Y3.7'
plate96_C2 = 'G0 X100.2 Y11.9'
plate96_C3 = 'G0 X100.2 Y20.8'
plate96_C4 = 'G0 X100.2 Y29.7'
plate96_C5 = 'G0 X100.2 Y38.6'
plate96_C6 = 'G0 X100.2 Y47.5'
plate96_C7 = 'G0 X100.2 Y56.4'
plate96_C8 = 'G0 X100.2 Y65.3'
plate96_C9 = 'G0 X100.2 Y74.2'
plate96_C10 = 'G0 X100.2 Y83.1'
plate96_C11 = 'G0 X100.2 Y92.0'
plate96_C12 = 'G0 X100.2 Y100.9'

plate96_D1 = 'G0 X91.3 Y3.7'
plate96_D2 = 'G0 X91.3 Y11.9'
plate96_D3 = 'G0 X91.3 Y20.8'
plate96_D4 = 'G0 X91.3 Y29.7'
plate96_D5 = 'G0 X91.3 Y38.6'
plate96_D6 = 'G0 X91.3 Y47.5'
plate96_D7 = 'G0 X91.3 Y56.4'
plate96_D8 = 'G0 X91.3 Y65.3'
plate96_D9 = 'G0 X91.3 Y74.2'
plate96_D10 = 'G0 X91.3 Y83.1'
plate96_D11 = 'G0 X91.3 Y92.0'
plate96_D12 = 'G0 X91.3 Y100.9'

plate96_E1 = 'G0 X82.4 Y3.7'
plate96_E2 = 'G0 X82.4 Y11.9'
plate96_E3 = 'G0 X82.4 Y20.8'
plate96_E4 = 'G0 X82.4 Y29.7'
plate96_E5 = 'G0 X82.4 Y38.6'
plate96_E6 = 'G0 X82.4 Y47.5'
plate96_E7 = 'G0 X82.4 Y56.4'
plate96_E8 = 'G0 X82.4 Y65.3'
plate96_E9 = 'G0 X82.4 Y74.2'
plate96_E10 = 'G0 X82.4 Y83.1'
plate96_E11 = 'G0 X82.4 Y92.0'
plate96_E12 = 'G0 X82.4 Y100.9'

# connect to USB ports
connect()
# home specified linear stages

home_all()

# start of specific protocol commands

move_to_moduleLifter()
lift_lid_from_plate96()
move_to_lidHolder()
place_lid_onto_holder_plate96()

move_to_moduleSensor()

lower_sensor_above_plate()

robot2._driver.send_command('G90')
robot2._driver.send_command('G0 F500')
robot2._driver.send_command(plate96_A1)

lower_sensor_into_plate()
sleep(8)
lower_sensor_above_plate()


move_to_lidHolder()
lift_lid_from_holder_plate96()
move_to_moduleLifter()
place_lid_onto_plate96()

# once protocol is finished, home again
home_all()
