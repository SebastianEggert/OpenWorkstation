import opentrons
from openworkstation import robot2, robot2, containers, instruments
from moduleSensor import *
from moduleSensor import *
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


#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.01.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.02.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.03.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.04.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.05.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.06.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.07.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.08.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.09.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.10.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.11.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.12.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.13.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.14.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.15.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.16.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.17.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.18.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.19.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.20.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.21.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.22.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.23.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.24.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.25.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.26.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.27.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.28.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.29.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.30.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.31.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.32.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.33.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.34.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.35.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.36.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.37.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.38.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.39.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.40.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.41.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.42.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.43.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.44.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.45.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.46.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.47.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.48.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.49.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.50.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.51.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.52.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.53.jpg')
sleep(5)

#home
robot2._driver.send_command('G28.2 X')

#move to position moduleSensor 
move_to_moduleSensor()

sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.54.jpg')
sleep(5)


#for axis registration
robot2._driver.send_command('G0 X107')
sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.55.jpg')
sleep(5)

robot2._driver.send_command('G0 X106')
sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.56.jpg')
sleep(5)

robot2._driver.send_command('G0 X105')
sleep(5)
camera.capture('/home/pi/Documents/protocols/experiments/1_performance_MMP/code/image0.57.jpg')
sleep(5)


