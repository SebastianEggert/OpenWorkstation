from time import sleep
from openworkstation import robot2

# the following commands operate the transportation module to the defined
# well position of a 96-well plate


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

plate96_F1 = 'G0 X73.5 Y3.7'
plate96_F2 = 'G0 X73.5 Y11.9'
plate96_F3 = 'G0 X73.5 Y20.8'
plate96_F4 = 'G0 X73.5 Y29.7'
plate96_F5 = 'G0 X73.5 Y38.6'
plate96_F6 = 'G0 X73.5 Y47.5'
plate96_F7 = 'G0 X73.5 Y56.4'
plate96_F8 = 'G0 X73.5 Y65.3'
plate96_F9 = 'G0 X73.5 Y74.2'
plate96_F10 = 'G0 X73.5 Y83.1'
plate96_F11 = 'G0 X73.5 Y92.0'
plate96_F12 = 'G0 X73.5 Y100.9'

plate96_G1 = 'G0 X64.6 Y3.7'
plate96_G2 = 'G0 X64.6 Y11.9'
plate96_G3 = 'G0 X64.6 Y20.8'
plate96_G4 = 'G0 X64.6 Y29.7'
plate96_G5 = 'G0 X64.6 Y38.6'
plate96_G6 = 'G0 X64.6 Y47.5'
plate96_G7 = 'G0 X64.6 Y56.4'
plate96_G8 = 'G0 X64.6 Y65.3'
plate96_G9 = 'G0 X64.6 Y74.2'
plate96_G10 = 'G0 X64.6 Y83.1'
plate96_G11 = 'G0 X64.6 Y92.0'
plate96_G12 = 'G0 X64.6 Y100.9'

plate96_H1 = 'G0 X55.7 Y3.7'
plate96_H2 = 'G0 X55.7 Y11.9'
plate96_H3 = 'G0 X55.7 Y20.8'
plate96_H4 = 'G0 X55.7 Y29.7'
plate96_H5 = 'G0 X55.7 Y38.6'
plate96_H6 = 'G0 X55.7 Y47.5'
plate96_H7 = 'G0 X55.7 Y56.4'
plate96_H8 = 'G0 X55.7 Y65.3'
plate96_H9 = 'G0 X55.7 Y74.2'
plate96_H10 = 'G0 X55.7 Y83.1'
plate96_H11 = 'G0 X55.7 Y92.0'
plate96_H12 = 'G0 X55.7 Y100.9'

def move_to_plate96_A1():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A1)
    sleep(0.1)


def move_to_plate96_A2():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A2)
    sleep(0.1)


def move_to_plate96_A3():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A3)
    sleep(0.1)


def move_to_plate96_A4():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A4)
    sleep(0.1)


def move_to_plate96_A5():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A5)
    sleep(0.1)


def move_to_plate96_A6():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A6)
    sleep(0.1)


def move_to_plate96_A7():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A7)
    sleep(0.1)


def move_to_plate96_A8():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A8)
    sleep(0.1)


def move_to_plate96_A9():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A9)
    sleep(0.1)


def move_to_plate96_A10():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A10)
    sleep(0.1)


def move_to_plate96_A11():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A11)
    sleep(0.1)


def move_to_plate96_A12():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_A12)
    sleep(0.1)


def move_to_plate96_B12():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B12)
    sleep(0.1)


def move_to_plate96_B11():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B11)
    sleep(0.1)


def move_to_plate96_B10():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B10)
    sleep(0.1)


def move_to_plate96_B9():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B9)
    sleep(0.1)


def move_to_plate96_B8():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B8)
    sleep(0.1)


def move_to_plate96_B7():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B7)
    sleep(0.1)


def move_to_plate96_B6():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B6)
    sleep(0.1)


def move_to_plate96_B5():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B5)
    sleep(0.1)


def move_to_plate96_B4():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B4)
    sleep(0.1)


def move_to_plate96_B3():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B3)
    sleep(0.1)


def move_to_plate96_B2():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B2)
    sleep(0.1)


def move_to_plate96_B1():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_B1)
    sleep(0.1)


def move_to_plate96_C1():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C1)
    sleep(0.1)


def move_to_plate96_C2():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C2)
    sleep(0.1)


def move_to_plate96_C3():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C3)
    sleep(0.1)


def move_to_plate96_C4():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C4)
    sleep(0.1)


def move_to_plate96_C5():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C5)
    sleep(0.1)


def move_to_plate96_C6():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C6)
    sleep(0.1)


def move_to_plate96_C7():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C7)
    sleep(0.1)


def move_to_plate96_C8():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C8)
    sleep(0.1)


def move_to_plate96_C9():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C9)
    sleep(0.1)


def move_to_plate96_C10():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C10)
    sleep(0.1)


def move_to_plate96_C11():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C11)
    sleep(0.1)


def move_to_plate96_C12():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_C12)
    sleep(0.1)


def move_to_plate96_D12():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D12)
    sleep(0.1)


def move_to_plate96_D11():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D11)
    sleep(0.1)


def move_to_plate96_D10():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D10)
    sleep(0.1)


def move_to_plate96_D9():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D9)
    sleep(0.1)


def move_to_plate96_D8():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D8)
    sleep(0.1)


def move_to_plate96_D7():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D7)
    sleep(0.1)


def move_to_plate96_D6():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D6)
    sleep(0.1)


def move_to_plate96_D5():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D5)
    sleep(0.1)


def move_to_plate96_D4():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D4)
    sleep(0.1)


def move_to_plate96_D3():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D3)
    sleep(0.1)


def move_to_plate96_D2():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D2)
    sleep(0.1)


def move_to_plate96_D1():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_D1)
    sleep(0.1)


def move_to_plate96_E1():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E1)
    sleep(0.1)


def move_to_plate96_E2():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E2)
    sleep(0.1)


def move_to_plate96_E3():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E3)
    sleep(0.1)


def move_to_plate96_E4():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E4)
    sleep(0.1)


def move_to_plate96_E5():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E5)
    sleep(0.1)


def move_to_plate96_E6():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E6)
    sleep(0.1)


def move_to_plate96_E7():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E7)
    sleep(0.1)


def move_to_plate96_E8():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E8)
    sleep(0.1)


def move_to_plate96_E9():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E9)
    sleep(0.1)


def move_to_plate96_E10():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E10)
    sleep(0.1)


def move_to_plate96_E11():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E11)
    sleep(0.1)


def move_to_plate96_E12():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_E12)
    sleep(0.1)


def move_to_plate96_F12():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F12)
    sleep(0.1)


def move_to_plate96_F11():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F11)
    sleep(0.1)


def move_to_plate96_F10():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F10)
    sleep(0.1)


def move_to_plate96_F9():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F9)
    sleep(0.1)


def move_to_plate96_F8():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F8)
    sleep(0.1)


def move_to_plate96_F7():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F7)
    sleep(0.1)


def move_to_plate96_F6():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F6)
    sleep(0.1)


def move_to_plate96_F5():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F5)
    sleep(0.1)


def move_to_plate96_F4():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F4)
    sleep(0.1)


def move_to_plate96_F3():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F3)
    sleep(0.1)


def move_to_plate96_F2():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F2)
    sleep(0.1)


def move_to_plate96_F1():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_F1)
    sleep(0.1)

def move_to_plate96_G1():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G1)
    sleep(0.1)


def move_to_plate96_G2():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G2)
    sleep(0.1)


def move_to_plate96_G3():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G3)
    sleep(0.1)


def move_to_plate96_G4():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G4)
    sleep(0.1)


def move_to_plate96_G5():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G5)
    sleep(0.1)


def move_to_plate96_G6():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G6)
    sleep(0.1)


def move_to_plate96_G7():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G7)
    sleep(0.1)


def move_to_plate96_G8():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G8)
    sleep(0.1)


def move_to_plate96_G9():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G9)
    sleep(0.1)


def move_to_plate96_G10():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G10)
    sleep(0.1)


def move_to_plate96_G11():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G11)
    sleep(0.1)


def move_to_plate96_G12():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_G12)
    sleep(0.1)


def move_to_plate96_H12():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H12)
    sleep(0.1)


def move_to_plate96_H11():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H11)
    sleep(0.1)


def move_to_plate96_H10():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H10)
    sleep(0.1)


def move_to_plate96_H9():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H9)
    sleep(0.1)


def move_to_plate96_H8():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H8)
    sleep(0.1)


def move_to_plate96_H7():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H7)
    sleep(0.1)


def move_to_plate96_H6():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H6)
    sleep(0.1)


def move_to_plate96_H5():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H5)
    sleep(0.1)


def move_to_plate96_H4():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H4)
    sleep(0.1)


def move_to_plate96_H3():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H3)
    sleep(0.1)


def move_to_plate96_H2():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H2)
    sleep(0.1)


def move_to_plate96_H1():
    robot2._driver.send_command('G90')
    robot2._driver.send_command('G0 F500')
    robot2._driver.send_command(plate96_H1)
    sleep(0.1)
