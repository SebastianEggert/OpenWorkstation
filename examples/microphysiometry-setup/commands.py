from openworkstation import robot2
from moduleTransportation import getModuleposition


moduleposition = getModuleposition()

# define USB port
# for macOS, ls /dev/tty.usb* in terminal
# for windows, check device manager and then USB connections; for example 'COM5'
robotUSB = 'COM5'


def connect():
    #robot2.connect()
    robot2.connect(robotUSB)


def home_all():
    # home sensor stage
    robot2._driver.send_command('G28.2 Z')
    # home lifter stage
    robot2._driver.send_command('G28.2 A')
    # home XY positioning table
    robot2._driver.send_command('G28.2 X')
    robot2._driver.send_command('G28.2 Y')
    # robot2._driver.send_command('G90')


def disconnect():
    # robot2.connect()
    robot2.disconnect(robotUSB)
