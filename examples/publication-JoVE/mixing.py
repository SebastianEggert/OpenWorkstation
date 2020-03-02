from opentrons import robot, containers, instruments
#Dominik Schneidereit 2.10.2019



#pipetting up and down a certain volume while also moving the pipette up and down
#stroke of 1 is pipettes the full pipette volume up and down, e.g. 0.5 would do half
#dH specifies the height of movement while pipetting (in mm)
#pipette is the pipette equipment object from which the calibration values are taken (! using this to mix on the secondary pipette is not yet implemented !)
#iterations specifies how often to repeat the command
#speed specifies the speed of pipetting and movement
#stroke, iterations and speed are optional parameters and can be omitted when calling the function, defaulting to the values specified below
# e.g. "smoothMix(myPipette, 10)" would be a valid call of the function
def smoothMix(pipette, dH, stroke=1, iterations = 1 ,speed = 5000):
    for i in range(iterations):
            
        strokeLength = pipette.positions['bottom'] - pipette.positions['top']
        
        speedCommandString = "G1 F%d" % speed
        
        # relative movement
        robot._driver.send_command('G91')
        robot._driver.send_command(speedCommandString)
        
        partialStroke = stroke*strokeLength
        moveCommandString = "G1 Z%2.f B%2.f" % (dH, -partialStroke)
        moveCommandString2 = "G1 Z%2.f B%2.f" % (-dH, partialStroke)
        # mix 1
        robot._driver.send_command(moveCommandString)
        robot._driver.send_command(moveCommandString2)
        
        # absolute movement
        robot._driver.send_command('G90')


#same as "smoothMix" function but moving in a spiraling motion up and down
#DOES NOT WORK AS INTENDED! :-/        
def swirlMix(container, pipette, dH, stroke=1, iterations=1 ,speed = 5000, swirls = 5):
    for i in range(iterations):
        strokeLength = pipette.positions['bottom'] - pipette.positions['top']
        speedCommandString = "G1 F%d" % speed
        speedCommandString2 = "G2 F%d" % speed
        partialStroke = stroke*strokeLength
        wellDiameter = container.well('A1').properties['diameter']
        swirlRadius = wellDiameter/4
        
        #prepare for movement
        robot._driver.send_command('G91')
        robot._driver.send_command(speedCommandString)
        moveCommandString = "G1 X0" % (swirlRadius)
        
        #decenter pipette
        robot._driver.send_command(moveCommandString)
        
        #prepare for swirling motion
        robot._driver.send_command(speedCommandString2)
        
        #swirl down
        for j in range(swirls):
           moveCommandString = "G2 X0 Y0 I%2.f Z%2.f B%2.f" % (-swirlRadius, dH/swirls, -(partialStroke/swirls))
           robot._driver.send_command(moveCommandString)
        
        #swirl back up
        for j in range(swirls):
           moveCommandString = "G2 X0 Y0 I%2.f Z%2.f B%2.f" % (-swirlRadius, dH/swirls, -(partialStroke/swirls))
           robot._driver.send_command(moveCommandString)
        
        #recenter pipette
        robot._driver.send_command(speedCommandString)
        moveCommandString = "G1 X0" % (-swirlRadius)
        robot._driver.send_command(moveCommandString)
        
        # absolute movement
        robot._driver.send_command('G90')