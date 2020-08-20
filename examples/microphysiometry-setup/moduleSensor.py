from openworkstation import robot2

sensor_above_plate = 'G0 Z6'
sensor_into_plate = 'G0 Z12'


def lower_sensor_above_plate():
    # absolute positioning
    robot2._driver.send_command('G90')
    # lower suchtion cups
    robot2._driver.send_command(sensor_above_plate)


def lower_sensor_into_plate():
    # absolute positioning
    robot2._driver.send_command('G90')
    # lower suchtion cups
    robot2._driver.send_command(sensor_into_plate)
