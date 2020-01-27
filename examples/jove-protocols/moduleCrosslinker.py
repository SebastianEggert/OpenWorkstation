from opentrons import robot, robot2, containers, instruments
from moduleTransportation import getTransportposition
from time import sleep

transportposition=getTransportposition()

# examples for range
intensity_P1  = 'G0 Z130'
intensity_P2 = 'G0 Z50'

lightON  = 'M106'
lightOFF  = 'M107'


def crosslinking1min():
    #absolute positioning
    robot2._driver.send_command('G90')
    # move plate in crosslinker module
    # specifiy intensity
    robot2._driver.send_command(intensity_P1)
    # LEDs on
    robot2._driver.send_command(lightON)
    # in seconds
    sleep(360)
    # LEDs off
    robot2._driver.send_command(lightOFF)

def crosslinking2min():
    #absolute positioning
    robot2._driver.send_command('G90')
    # move plate in crosslinker module
    # specifiy intensity
    robot2._driver.send_command(intensity_P1)
    # LEDs on
    robot2._driver.send_command(lightON)
    # in seconds
    sleep(120)
    # LEDs off
    robot2._driver.send_command(lightOFF)

def crosslinking4min():
    #absolute positioning
    robot2._driver.send_command('G90')
    # move plate in crosslinker module
    # specifiy intensity
    robot2._driver.send_command(intensity_P1)
    # LEDs on
    robot2._driver.send_command(lightON)
    # in seconds
    sleep(240)
    # LEDs off
    robot2._driver.send_command(lightOFF)

def crosslinking6min():
    #absolute positioning
    robot2._driver.send_command('G90')
    # move plate in crosslinker module
    # specifiy intensity
    robot2._driver.send_command(intensity_P1)
    # LEDs on
    robot2._driver.send_command(lightON)
    # in seconds
    sleep(360)
    # LEDs off
    robot2._driver.send_command(lightOFF)

def crosslinking8min():
    #absolute positioning
    robot2._driver.send_command('G90')
    # move plate in crosslinker module
    # specifiy intensity
    robot2._driver.send_command(intensity_P1)
    # LEDs on
    robot2._driver.send_command(lightON)
    # in seconds
    sleep(480)
    # LEDs off
    robot2._driver.send_command(lightOFF)
