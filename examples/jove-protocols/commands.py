from opentrons import robot, robot2, containers, instruments
from modulePipetting import getEquipment
from moduleTransportation import getTransportposition
from time import sleep

equipment=getEquipment()
transportposition=getTransportposition()


# to find USB names for mac
# ls /dev/tty.usb*
robotUSB  = '/dev/ttyACM0'
robot2USB  = '/dev/ttyACM1'

def connect():
    #robot.connect()
    robot.connect(robotUSB)
    #robot2.connect()
    robot2.connect(robot2USB)

def home_all():
    robot.home()
    robot2._driver.send_command('G28.2 Y Z')
    robot2._driver.send_command('G28.2 A')
    robot2._driver.send_command('G28.2 B')
    robot2._driver.send_command('G28.2 X')
    robot2._driver.send_command('G90')

def move_to_modulePipetting():
    robot2._driver.send_command('G90')
    robot2._driver.send_command(transportposition['modulePipetting'])
    robot2._driver.send_command('G4 S1')


def move_to_moduleCrosslinker():
    robot2._driver.send_command('G90')
    robot2._driver.send_command(transportposition['moduleCrosslinker'])
    robot2._driver.send_command('G4 S1')


def move_to_moduleStorage():
    robot2._driver.send_command('G90')
    robot2._driver.send_command(transportposition['moduleStorage'])
    robot2._driver.send_command('G4 S1')

def pickup_pd1000tip(i):
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(20))
    equipment['pd1000'].blow_out()
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(7), strategy='direct')
    equipment['pd1000'].delay(seconds=0.5)
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(4), strategy='direct')
    equipment['pd1000'].delay(seconds=0.5)
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(2), strategy='direct')
    equipment['pd1000'].delay(seconds=0.5)
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(1), strategy='direct')
    equipment['pd1000'].delay(seconds=0.5)
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(0), strategy='direct')
    equipment['pd1000'].delay(seconds=0.5)
    equipment['pd1000'].pick_up_tip(equipment['1000tiprack'][i])
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(0), strategy='direct')
    equipment['pd1000'].delay(seconds=0.5)
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(-0.3), strategy='direct')
    equipment['pd1000'].delay(seconds=0.5)
    equipment['pd1000'].move_to(equipment['1000tiprack'][i].bottom(-0.6), strategy='direct')


def pickup_pd100tip(i):
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(20))
    equipment['pd100'].blow_out()
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(7), strategy='direct')
    equipment['pd100'].delay(seconds=0.5)
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(4), strategy='direct')
    equipment['pd100'].delay(seconds=0.5)
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(2), strategy='direct')
    equipment['pd100'].delay(seconds=0.5)
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(1), strategy='direct')
    equipment['pd100'].delay(seconds=0.5)
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(0), strategy='direct')
    equipment['pd100'].delay(seconds=0.5)
    equipment['pd100'].pick_up_tip(equipment['100TiprackB1'][i])
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(0), strategy='direct')
    equipment['pd100'].delay(seconds=0.5)
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(-0.3), strategy='direct')
    equipment['pd100'].delay(seconds=0.5)
    equipment['pd100'].move_to(equipment['100TiprackB1'][i].bottom(-0.6), strategy='direct')
    
def pickup_pd250tip(i):
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(20))
    equipment['pd250'].blow_out()
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(7), strategy='direct')
    equipment['pd250'].delay(seconds=0.5)
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(4), strategy='direct')
    equipment['pd250'].delay(seconds=0.5)
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(2), strategy='direct')
    equipment['pd250'].delay(seconds=0.5)
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(1), strategy='direct')
    equipment['pd250'].delay(seconds=0.5)
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(0), strategy='direct')
    equipment['pd250'].delay(seconds=0.5)
    equipment['pd250'].pick_up_tip(equipment['250TiprackB1'][i])
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(0), strategy='direct')
    equipment['pd250'].delay(seconds=0.5)
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(-0.3), strategy='direct')
    equipment['pd250'].delay(seconds=0.5)
    equipment['pd250'].move_to(equipment['250TiprackB1'][i].bottom(-0.6), strategy='direct')
