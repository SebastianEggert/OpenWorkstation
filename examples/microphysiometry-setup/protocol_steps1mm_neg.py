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
robot2._driver.send_command('G0 A24')
sleep(2)
move_to_moduleSensor()
sleep(2)

robot2._driver.send_command('G91')

#move 1mm to position 0
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.00.jpg')
sleep(2)

#move 1mm to position 1
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.01.jpg')
sleep(2)

#move 1mm to position 2
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.02.jpg')
sleep(2)

#move 1mm to position 3
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.03.jpg')
sleep(2)

#move 1mm to position 4
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.04.jpg')
sleep(2)

#move 1mm to position 5
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.05.jpg')
sleep(2)

#move 1mm to position 6
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.06.jpg')
sleep(2)

#move 1mm to position 7
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.07.jpg')
sleep(2)

#move 1mm to position 8
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.08.jpg')
sleep(2)

#move 1mm to position 9
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.09.jpg')
sleep(2)

#move 1mm to position 10
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.10.jpg')
sleep(2)

#move 1mm to position 11
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.11.jpg')
sleep(2)

#move 1mm to position 12
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.12.jpg')
sleep(2)

#move 1mm to position 13
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.13.jpg')
sleep(2)

#move 1mm to position 14
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.14.jpg')
sleep(2)

#move 1mm to position 15
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.15.jpg')
sleep(2)

#move 1mm to position 16
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.16.jpg')
sleep(2)

#move 1mm to position 17
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.17.jpg')
sleep(2)

#move 1mm to position 18
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.18.jpg')
sleep(2)

#move 1mm to position 19
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.19.jpg')
sleep(2)

#move 1mm to position 20
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.20.jpg')
sleep(2)

#move 1mm to position 21
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.21.jpg')
sleep(2)

#move 1mm to position 22
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.22.jpg')
sleep(2)

#move 1mm to position 23
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.23.jpg')
sleep(2)

#move 1mm to position 24
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.24.jpg')
sleep(2)

#move 1mm to position 25
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.25.jpg')
sleep(2)

#move 1mm to position 26
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.26.jpg')
sleep(2)

#move 1mm to position 27
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.27.jpg')
sleep(2)

#move 1mm to position 28
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.28.jpg')
sleep(2)

#move 1mm to position 29
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.29.jpg')
sleep(2)

#move 1mm to position 30
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.30.jpg')
sleep(2)

#move 1mm to position 31
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.31.jpg')
sleep(2)

#move 1mm to position 32
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.32.jpg')
sleep(2)

#move 1mm to position 33
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.33.jpg')
sleep(2)

#move 1mm to position 34
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.34.jpg')
sleep(2)

#move 1mm to position 35
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.35.jpg')
sleep(2)

#move 1mm to position 36
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.36.jpg')
sleep(2)

#move 1mm to position 37
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.37.jpg')
sleep(2)

#move 1mm to position 38
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.38.jpg')
sleep(2)

#move 1mm to position 39
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.39.jpg')
sleep(2)

#move 1mm to position 40
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.40.jpg')
sleep(2)

#move 1mm to position 41
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.41.jpg')
sleep(2)

#move 1mm to position 42
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.42.jpg')
sleep(2)

#move 1mm to position 43
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.43.jpg')
sleep(2)

#move 1mm to position 44
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.44.jpg')
sleep(2)

#move 1mm to position 45
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.45.jpg')
sleep(2)

#move 1mm to position 46
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.46.jpg')
sleep(2)

#move 1mm to position 47
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.47.jpg')
sleep(2)

#move 1mm to position 48
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.48.jpg')
sleep(2)

#move 1mm to position 49
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.49.jpg')
sleep(2)

#move 1mm to position 50
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.50.jpg')
sleep(2)

#move 1mm to position 51
robot2._driver.send_command('G0 X-1')
sleep(2)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.51.jpg')
sleep(2)




