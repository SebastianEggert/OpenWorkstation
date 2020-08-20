from time import sleep
from openworkstation import robot2
from moduleTransportation import getModuleposition


moduleposition = getModuleposition()

lifterON = 'M41'
lifterOFF = 'M40'

lifter_rest = 'G0 A30'

closed_plate24 = 'G0 A55'
closed_plate24_above = 'G0 A50'

closed_plate96 = 'G0 A64'
closed_plate96_above = 'G0 A59'

open_lidHolder_plate24 = 'G0 A58'
open_lidHolder_plate24_above = 'G0 A51'

open_lidHolder_plate96 = 'G0 A62'
open_lidHolder_plate96_above = 'G0 A55'

transportation_plate_base_above = 'G0 X21.3 Y5 Z5 B15'
transportation_holder_base = 'G0 X21.3 Y5 Z5 B15'
transportation_holder_base_above = 'G0 X21.3 Y5 Z5 B15'
lifter_rest = 'G0 A30'


def lift_lid_from_plate24():
    robot2._driver.send_command('G0 F2000')
    # absolute positioning
    robot2._driver.send_command('G90')
    # move plate to lifter module
    robot2._driver.send_command(moduleposition['moduleLifter'])
    # lower suchtion cups
    robot2._driver.send_command(closed_plate24_above)
    # decrease speed
    robot2._driver.send_command('G0 F500')
    # lower suchtion cups
    robot2._driver.send_command(closed_plate24)
    # wait 2 seconds
    sleep(2)
    # switch lifter on
    robot2._driver.send_command(lifterON)
    # wait 3 seconds
    sleep(3)
    # lift suction cups to rest positiong
    robot2._driver.send_command(closed_plate24_above)
    # decrease speed
    robot2._driver.send_command('G0 F2000')
    # lift suction cups to rest positiong
    robot2._driver.send_command(lifter_rest)


def lift_lid_from_plate96():
    robot2._driver.send_command('G0 F2000')
    # absolute positioning
    robot2._driver.send_command('G90')
    # move plate to lifter module
    robot2._driver.send_command(moduleposition['moduleLifter'])
    # lower suchtion cups
    robot2._driver.send_command(closed_plate96_above)
    # decrease speed
    robot2._driver.send_command('G0 F500')
    # lower suchtion cups
    robot2._driver.send_command(closed_plate96)
    # wait 2 seconds
    sleep(2)
    # switch lifter on
    robot2._driver.send_command(lifterON)
    # wait 3 seconds
    sleep(3)
    # lift suction cups to rest positiong
    robot2._driver.send_command(closed_plate96_above)
    # decrease speed
    robot2._driver.send_command('G0 F2000')
    # lift suction cups to rest positiong
    robot2._driver.send_command(lifter_rest)


def lift_lid_from_holder_plate24():
    robot2._driver.send_command('G0 F2000')
    # absolute positioning
    robot2._driver.send_command('G90')
    # move plate to lifter module
    robot2._driver.send_command(moduleposition['lidHolder'])
    # position above
    robot2._driver.send_command(open_lidHolder_plate24_above)
    # decrease speed
    robot2._driver.send_command('G0 F500')
    # lower suchtion cups
    robot2._driver.send_command(open_lidHolder_plate24)
    # wait 2 seconds
    sleep(2)
    # switch lifter on
    robot2._driver.send_command(lifterON)
    # wait 3 seconds
    sleep(3)
    # position above
    robot2._driver.send_command(open_lidHolder_plate24_above)
    robot2._driver.send_command('G0 F2000')
    # lift suction cups to rest positiong
    robot2._driver.send_command(lifter_rest)


def lift_lid_from_holder_plate96():
    robot2._driver.send_command('G0 F2000')
    # absolute positioning
    robot2._driver.send_command('G90')
    # move plate to lifter module
    robot2._driver.send_command(moduleposition['lidHolder'])
    # position above
    robot2._driver.send_command(open_lidHolder_plate96_above)
    # decrease speed
    robot2._driver.send_command('G0 F500')
    # lower suchtion cups
    robot2._driver.send_command(open_lidHolder_plate96)
    # wait 2 seconds
    sleep(2)
    # switch lifter on
    robot2._driver.send_command(lifterON)
    # wait 3 seconds
    sleep(3)
    # position above
    robot2._driver.send_command(open_lidHolder_plate96_above)
    robot2._driver.send_command('G0 F2000')
    # lift suction cups to rest positiong
    robot2._driver.send_command(lifter_rest)


def place_lid_onto_plate24():
    robot2._driver.send_command('G0 F2000')
    # absolute positioning
    robot2._driver.send_command('G90')
    # move plate to lifter module
    robot2._driver.send_command(moduleposition['moduleLifter'])
    # lower suchtion cups
    robot2._driver.send_command(closed_plate24_above)
    # decrease speed
    robot2._driver.send_command('G0 F500')
    # lower suchtion cups
    robot2._driver.send_command(closed_plate24)
    # wait 2 seconds
    sleep(2)
    # switch lifter on
    robot2._driver.send_command(lifterOFF)
    # wait 3 seconds
    sleep(3)
    # lift suction cups to rest positiong
    robot2._driver.send_command(closed_plate24_above)
    # decrease speed
    robot2._driver.send_command('G0 F2000')
    # lift suction cups to rest positiong
    robot2._driver.send_command(lifter_rest)


def place_lid_onto_plate96():
    robot2._driver.send_command('G0 F2000')
    # absolute positioning
    robot2._driver.send_command('G90')
    # move plate to lifter module
    robot2._driver.send_command(moduleposition['moduleLifter'])
    # lower suchtion cups
    robot2._driver.send_command(closed_plate96_above)
    # decrease speed
    robot2._driver.send_command('G0 F500')
    # lower suchtion cups
    robot2._driver.send_command(closed_plate96)
    # wait 2 seconds
    sleep(2)
    # switch lifter on
    robot2._driver.send_command(lifterOFF)
    # wait 3 seconds
    sleep(3)
    # lift suction cups to rest positiong
    robot2._driver.send_command(closed_plate96_above)
    # decrease speed
    robot2._driver.send_command('G0 F2000')
    # lift suction cups to rest positiong
    robot2._driver.send_command(lifter_rest)


def place_lid_onto_holder_plate24():
    robot2._driver.send_command('G0 F2000')
    # absolute positioning
    robot2._driver.send_command('G90')
    # move plate to lifter module
    robot2._driver.send_command(moduleposition['lidHolder'])
    # position above
    robot2._driver.send_command(open_lidHolder_plate24_above)
    # decrease speed
    robot2._driver.send_command('G0 F500')
    # lower suchtion cups
    robot2._driver.send_command(open_lidHolder_plate24)
    # wait 3 seconds
    sleep(3)
    # switch lifter on
    robot2._driver.send_command(lifterOFF)
    # position above
    robot2._driver.send_command(open_lidHolder_plate24_above)
    robot2._driver.send_command('G0 F2000')
    # lift suction cups to rest positiong
    robot2._driver.send_command(lifter_rest)


def place_lid_onto_holder_plate96():
    robot2._driver.send_command('G0 F2000')
    # absolute positioning
    robot2._driver.send_command('G90')
    # move plate to lifter module
    robot2._driver.send_command(moduleposition['lidHolder'])
    # position above
    robot2._driver.send_command(open_lidHolder_plate96_above)
    # decrease speed
    robot2._driver.send_command('G0 F500')
    # lower suchtion cups
    robot2._driver.send_command(open_lidHolder_plate96)
    # wait 2 seconds
    sleep(2)
    # switch lifter on
    robot2._driver.send_command('M40')
    # position above
    robot2._driver.send_command(open_lidHolder_plate96_above)
    robot2._driver.send_command('G0 F2000')
    # lift suction cups to rest positiong
    robot2._driver.send_command(lifter_rest)
