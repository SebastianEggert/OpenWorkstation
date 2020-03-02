
from opentrons import robot, containers, instruments
import opentrons
import curses
import time

from curses import wrapper
from modulePipetting import getEquipment
movementamounts= {1:0.1, 2:0.5, 3:1, 4:5, 5:10,6:20,7:40,8:80}
equipment=getEquipment()

robot.connect('/dev/ttyACM0')

# robot.connect()



input("Robot will now home, press enter to continue.")
robot.home()

placeables = {}
pipettes = {}
for key, value in equipment.items():

     if hasattr(value, 'axis'):

          pipettes[key]=value
     else:
          placeables[key]=value

placeableNames=sorted(list(placeables.keys()))
pipetteNames=sorted(list(pipettes.keys()))
def main(stdscr):
    currentlyCalibrating=placeableNames[0]
    currentPipette=pipetteNames[0]
    movementAmount=1
    position=list(robot._driver.get_head_position()["current"])
    position[0]=0
    def chooseWhatToCalibrate():
           nonlocal currentlyCalibrating
           stdscr.clear()
           stdscr.addstr("What should we calibrate?\n")
           for i,value in enumerate(placeableNames):
               stdscr.addstr(str(i+1)+" - " + value+"\n")
           curses.echo()            # Enable echoing of characters
           s = stdscr.getstr(15,0, 15)
           stdscr.addstr(s)
           currentlyCalibrating=placeableNames[int(s)-1]
           curses.noecho()
    def chooseWhatPipetteToCalibrate():
           nonlocal currentPipette
           stdscr.clear()
           stdscr.addstr("What pipette should we calibrate?\n")
           for i,value in enumerate(pipetteNames):
               stdscr.addstr(str(i+1)+" - " + value+"\n")
           curses.echo()            # Enable echoing of characters
           s = stdscr.getstr(10,0, 15)
           stdscr.addstr(s)
           currentPipette=pipetteNames[int(s)-1]
           curses.noecho()

    def calibratePlunger():
           plungerPos=0
           plungerTarget="top"
           plungerInc=1
           while 1:


                stdscr.clear()
                stdscr.addstr("CALIBRATION - PLUNGER MODE\n\n")
                stdscr.addstr("Keyboard shortcuts:\n\n")
                stdscr.addstr("T - start calibrating the 'top' position\n")
                stdscr.addstr("B - start calibrating the 'bottom' position\n")
                stdscr.addstr("O - start calibrating the 'get-new-tip' position\n")
                stdscr.addstr("E - start calibrating the 'drop_tip' (eject) position\n\n")
                stdscr.addstr("Numbers 1-8 - choose how far to move\n")
                stdscr.addstr("Arrow keys - move plunger up/down\n")
                stdscr.addstr("S - save this position\n")
                stdscr.addstr("M - move to this position\n")
                stdscr.addstr("\n\n")
                stdscr.addstr("V - switch back to container mode\n\n")
                stdscr.addstr("Currently calibrating plunger position: ")
                stdscr.addstr( str(plungerTarget)+"\n",curses.A_STANDOUT)
                stdscr.addstr("with pipette: ")
                stdscr.addstr(str(currentPipette)+"\n",curses.A_STANDOUT)
                stdscr.addstr("Movement increment: ")
                stdscr.addstr(str(plungerInc)+" mm\n",curses.A_STANDOUT)
                stdscr.addstr("Current position -  X: ")
                stdscr.addstr(str(plungerPos),curses.A_STANDOUT)

                key=stdscr.getkey()
                curses.flushinp()
                if key=="t":
                    plungerTarget="top"
                if key=="b":
                    plungerTarget="bottom"
                if key=="o":
                    plungerTarget="blow_out"
                if key=="e":
                    plungerTarget="drop_tip"
                if key=="s":
                    equipment[currentPipette].calibrate(plungerTarget)
                    stdscr.clear()
                    stdscr.addstr("plunger position saved")
                    stdscr.refresh()
                    time.sleep(1)


                if key=="m":
                    equipment[currentPipette].motor.move(equipment[currentPipette]._get_plunger_position(plungerTarget))
                    plungerPos=equipment[currentPipette]._get_plunger_position(plungerTarget)
                if key=="h":
                    equipment[currentPipette].home()
                    plungerPos=0
                if key=="v":
                    return()
                try:
                 if int(key) in movementamounts:
                    plungerInc=  movementamounts[int(key)]
                except ValueError:
                    pass

                if key == "KEY_UP":
                        plungerPos=plungerPos-plungerInc
                if key == "KEY_DOWN":
                        plungerPos=plungerPos+plungerInc
                #stdscr.addstr("Key"+key)

                equipment[currentPipette].motor.move(plungerPos)
                stdscr.refresh()
    while 1:
        stdscr.clear()
        stdscr.addstr("CALIBRATION MODE\n\n")
        stdscr.addstr("Keyboard shortcuts:\n")
        stdscr.addstr("P - choose what pipette to calibrate with\n")

        stdscr.addstr("C - choose what container to calibrate\n")
        stdscr.addstr("S - save this position\n")
        stdscr.addstr("H - home\n")
        stdscr.addstr("M - move to the currently saved position\n\n")
        stdscr.addstr("Numbers 1-8 - choose how far to move\n")
        stdscr.addstr("Arrow keys - move forwards/back/left/right\n")
        stdscr.addstr("Control + arrow keys - move up/down\n\n")
        stdscr.addstr("V - switch to calibrate this pipette's plunger/volume\n\n")
        stdscr.addstr("Currently pipette: ")

        stdscr.addstr(str(currentPipette)+"\n",curses.A_STANDOUT)
        stdscr.addstr("going to: ")
        stdscr.addstr(str(currentlyCalibrating)+"\n",curses.A_STANDOUT)

        stdscr.addstr("Movement increment: ")
        stdscr.addstr( str(movementAmount)+" mm\n",curses.A_STANDOUT)
        stdscr.addstr("Current position - ")
        stdscr.addstr("X:"+ str(position[0])+",Y:"+ str(position[1])+",Z:"+ str(position[2]),curses.A_STANDOUT)

        key=stdscr.getkey()
        curses.flushinp()
        if key=="c":
            chooseWhatToCalibrate()
        if key=="v":
            calibratePlunger()
        if key=="p":
            chooseWhatPipetteToCalibrate()
        if key=="s":
            well = equipment[currentlyCalibrating][0]
            pos = well.from_center(x=0, y=0, z=-1, reference=equipment[currentlyCalibrating])
            location = (equipment[currentlyCalibrating], pos)
            equipment[currentPipette].calibrate_position(location)
            stdscr.clear()
            stdscr.addstr("position saved")
            stdscr.refresh()
            time.sleep(1)


        if key=="m":
            well = equipment[currentlyCalibrating][0]
            pos = well.from_center(x=0, y=0, z=-1, reference=equipment[currentlyCalibrating])
            location = (equipment[currentlyCalibrating], pos)
            equipment[currentPipette].move_to(location)
            position=list(robot._driver.get_head_position()["current"])
        if key=="h":
            robot.home()
            position=list(robot._driver.get_head_position()["current"])
        try:
         if int(key) in movementamounts:
            movementAmount=  movementamounts[int(key)]
        except ValueError:
            pass
        if key == "q":
                position[2]=position[2]+movementAmount
        if key == "a":
                position[2]=position[2]-movementAmount
        if key == "KEY_LEFT":
                position[0]=position[0]-movementAmount
        if key == "KEY_RIGHT":
                position[0]=position[0]+movementAmount
        if key == "KEY_UP":
                position[1]=position[1]+movementAmount
        if key == "KEY_DOWN":
                position[1]=position[1]-movementAmount
        #stdscr.addstr("Key"+key)

        robot.move_head(x=position[0],y=position[1],z=position[2])
        stdscr.refresh()


wrapper(main)
