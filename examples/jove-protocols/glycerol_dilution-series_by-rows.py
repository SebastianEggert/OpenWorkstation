import opentrons
from opentrons import robot, robot2, containers, instruments

from time import sleep

from commands import *
from modulePipetting import *
from mixing import *
from moduleCrosslinker import *
#from moduleStorage import *
from moduleTransportation import getTransportposition


# robot is being reset
robot.reset()
robot2.reset()

equipment=getEquipment()
transportposition=getTransportposition()


connect()
#home_all()
#move_to_modulePipetting()

robot.home()
# 1. DEFINE CONTAINERS - Create 'Equipment' function


equipment=getEquipment()
#RUN = Inputs
 # 1 = Dilent 2
# GET TIP
pickup_pd1000tip(0)
   # Loop 3.
   # Aspirate/Dispense Volume = 1000.0
equipment['pd1000'].aspirate(1000.0, equipment['InputsC1'].wells('A3').bottom(26.2))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(900.0, equipment['MixingD1'].wells('A1').bottom(6.1))
   # Loop 1.
   # Aspirate/Dispense Volume = 108.0
equipment['pd1000'].aspirate(108.0, equipment['InputsC1'].wells('A3').bottom(25.5))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(108.0, equipment['MixingD1'].wells('A1').bottom(6.8))
   # Loop 1.
   # Aspirate/Dispense Volume = 453.6
equipment['pd1000'].aspirate(453.6, equipment['InputsC1'].wells('A3').bottom(22.6))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(453.6, equipment['MixingD1'].wells('A2').bottom(2.0))
   # Loop 1.
   # Aspirate/Dispense Volume = 453.6
equipment['pd1000'].aspirate(453.6, equipment['InputsC1'].wells('A3').bottom(19.6))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(453.6, equipment['MixingD1'].wells('A2').bottom(6.1))
   # Loop 1.
   # Aspirate/Dispense Volume = 806.4
equipment['pd1000'].aspirate(806.4, equipment['InputsC1'].wells('A3').bottom(14.4))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(806.4, equipment['MixingD1'].wells('A3').bottom(5.5))
   # Loop 1.
   # Aspirate/Dispense Volume = 604.8
equipment['pd1000'].aspirate(604.8, equipment['InputsC1'].wells('A3').bottom(10.5))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(604.8, equipment['MixingD1'].wells('A4').bottom(4.2))
   # Loop 1.
   # Aspirate/Dispense Volume = 504.0
equipment['pd1000'].aspirate(504.0, equipment['InputsC1'].wells('A3').bottom(7.2))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(504.0, equipment['MixingD1'].wells('B1').bottom(3.5))
   # Loop 1.
   # Aspirate/Dispense Volume = 403.2
equipment['pd1000'].aspirate(403.2, equipment['InputsC1'].wells('A3').bottom(4.6))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(403.2, equipment['MixingD1'].wells('B2').bottom(2.0))
   # Loop 1.
   # Aspirate/Dispense Volume = 302.4
equipment['pd1000'].aspirate(302.4, equipment['InputsC1'].wells('A4').bottom(30.8))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(302.4, equipment['MixingD1'].wells('B3').bottom(2.0))
   # Loop 1.
   # Aspirate/Dispense Volume = 201.6
equipment['pd1000'].aspirate(201.6, equipment['InputsC1'].wells('A4').bottom(29.5))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(201.6, equipment['MixingD1'].wells('B4').bottom(2.0))
 # 2 = Dilent 1
 # 4 = Secondary Solvent 2
 # 6 = Secondary Solvent 1
 # 2 = Main Solvent 2
 # 5 = Main Solvent 1
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(1)
   # Loop 1.
   # Aspirate/Dispense Volume = 200.8
equipment['pd1000'].aspirate(200.8, equipment['InputsC1'].wells('A1').bottom(31.4))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(100.8, equipment['MixingD1'].wells('A2').bottom(6.8))
   # Loop 1.
   # Aspirate/Dispense Volume = 201.6
equipment['pd1000'].aspirate(201.6, equipment['InputsC1'].wells('A1').bottom(30.1))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(201.6, equipment['MixingD1'].wells('A3').bottom(6.8))
   # Loop 1.
   # Aspirate/Dispense Volume = 403.2
equipment['pd1000'].aspirate(403.2, equipment['InputsC1'].wells('A1').bottom(27.5))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(403.2, equipment['MixingD1'].wells('A4').bottom(6.8))
   # Loop 1.
   # Aspirate/Dispense Volume = 504.0
equipment['pd1000'].aspirate(504.0, equipment['InputsC1'].wells('A1').bottom(24.2))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(504.0, equipment['MixingD1'].wells('B1').bottom(6.8))
   # Loop 1.
   # Aspirate/Dispense Volume = 604.8
equipment['pd1000'].aspirate(604.8, equipment['InputsC1'].wells('A1').bottom(20.3))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(604.8, equipment['MixingD1'].wells('B2').bottom(6.8))
   # Loop 1.
   # Aspirate/Dispense Volume = 705.6
equipment['pd1000'].aspirate(705.6, equipment['InputsC1'].wells('A1').bottom(15.7))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(705.6, equipment['MixingD1'].wells('B3').bottom(6.8))
   # Loop 1.
   # Aspirate/Dispense Volume = 806.4
equipment['pd1000'].aspirate(806.4, equipment['InputsC1'].wells('A1').bottom(10.5))
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd1000'].dispense(806.4, equipment['MixingD1'].wells('B4').bottom(6.8))
#RUN = Mixing
 # 7 = MIXTURE
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(2)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A1').bottom(7.8))
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A1').bottom(7.8), strategy='direct')

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('A1').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('A1').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A1').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A1').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A1').bottom(2))

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('A1').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('A1').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A1').bottom(2))

equipment['pd1000'].move_to(equipment['MixingD1'].wells('A1').bottom(7.8), strategy='direct')
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A1').bottom(7.8), strategy='direct')

equipment['pd1000'].delay(seconds=5)
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(3)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A2').bottom(7.8))
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A2').bottom(7.8), strategy='direct')

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('A2').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('A2').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A2').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A2').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A2').bottom(2))

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('A2').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('A2').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A2').bottom(2))

equipment['pd1000'].move_to(equipment['MixingD1'].wells('A2').bottom(7.8), strategy='direct')
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A2').bottom(7.8), strategy='direct')

equipment['pd1000'].delay(seconds=5)
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(4)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A3').bottom(7.8))
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A3').bottom(7.8), strategy='direct')

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('A3').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('A3').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A3').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A3').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A3').bottom(2))

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('A3').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('A3').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A3').bottom(2))

equipment['pd1000'].move_to(equipment['MixingD1'].wells('A3').bottom(7.8), strategy='direct')
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A3').bottom(7.8), strategy='direct')

equipment['pd1000'].delay(seconds=5)
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(5)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A4').bottom(7.8))
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A4').bottom(7.8), strategy='direct')

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('A4').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('A4').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A4').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A4').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A4').bottom(2))

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('A4').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('A4').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('A4').bottom(2))

equipment['pd1000'].move_to(equipment['MixingD1'].wells('A4').bottom(7.8), strategy='direct')
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('A4').bottom(7.8), strategy='direct')

equipment['pd1000'].delay(seconds=5)
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(6)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B1').bottom(7.8))
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B1').bottom(7.8), strategy='direct')

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('B1').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('B1').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B1').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B1').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B1').bottom(2))

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('B1').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('B1').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B1').bottom(2))

equipment['pd1000'].move_to(equipment['MixingD1'].wells('B1').bottom(7.8), strategy='direct')
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B1').bottom(7.8), strategy='direct')

equipment['pd1000'].delay(seconds=5)
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(7)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B2').bottom(7.8))
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B2').bottom(7.8), strategy='direct')

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('B2').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('B2').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B2').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B2').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B2').bottom(2))

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('B2').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('B2').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B2').bottom(2))

equipment['pd1000'].move_to(equipment['MixingD1'].wells('B2').bottom(7.8), strategy='direct')
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B2').bottom(7.8), strategy='direct')

equipment['pd1000'].delay(seconds=5)
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(8)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B3').bottom(7.8))
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B3').bottom(7.8), strategy='direct')

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('B3').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('B3').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B3').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B3').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B3').bottom(2))

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('B3').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('B3').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B3').bottom(2))

equipment['pd1000'].move_to(equipment['MixingD1'].wells('B3').bottom(7.8), strategy='direct')
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B3').bottom(7.8), strategy='direct')

equipment['pd1000'].delay(seconds=5)
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd1000tip(9)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B4').bottom(7.8))
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B4').bottom(7.8), strategy='direct')

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('B4').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('B4').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B4').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B4').bottom(2))
equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B4').bottom(2))

equipment['pd1000'].aspirate(756.0,equipment['MixingD1'].wells('B4').bottom(2))
equipment['pd1000'].dispense(756.0,equipment['MixingD1'].wells('B4').bottom(2))

equipment['pd1000'].mix(2, 756.0, equipment['MixingD1'].wells('B4').bottom(2))

equipment['pd1000'].move_to(equipment['MixingD1'].wells('B4').bottom(7.8), strategy='direct')
smoothMix(equipment['pd1000'], 5.8, stroke=0.75, iterations=10)
equipment['pd1000'].move_to(equipment['MixingD1'].wells('B4').bottom(7.8), strategy='direct')

equipment['pd1000'].delay(seconds=5)
# TRASH TIP
equipment['pd1000'].drop_tip()
# GET TIP
pickup_pd100tip(0)
   # Loop 1.
   # Aspirate/Dispense Volume = 70.0
equipment['pd100'].aspirate(70.0, equipment['MixingD1'].wells('A1').bottom(6.3))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A1').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A1').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(6.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A2').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A2').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(5.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A3').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A3').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(5.2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A4').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A4').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(4.8))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A5').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A5').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(4.4))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A6').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A6').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(4.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A7').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A7').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(3.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A8').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A8').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A9').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A9').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A10').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A10').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A11').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A11').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A1').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('A12').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('A12').bottom(1.6))
# TRASH TIP
equipment['pd100'].drop_tip()
# GET TIP
pickup_pd100tip(1)
   # Loop 1.
   # Aspirate/Dispense Volume = 70.0
equipment['pd100'].aspirate(70.0, equipment['MixingD1'].wells('A2').bottom(6.3))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B1').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B1').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(6.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B2').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B2').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(5.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B3').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B3').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(5.2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B4').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B4').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(4.8))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B5').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B5').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(4.4))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B6').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B6').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(4.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B7').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B7').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(3.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B8').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B8').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B9').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B9').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B10').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B10').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B11').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B11').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A2').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('B12').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('B12').bottom(1.6))
# TRASH TIP
equipment['pd100'].drop_tip()
# GET TIP
pickup_pd100tip(2)
   # Loop 1.
   # Aspirate/Dispense Volume = 70.0
equipment['pd100'].aspirate(70.0, equipment['MixingD1'].wells('A3').bottom(6.3))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C1').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C1').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(6.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C2').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C2').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(5.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C3').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C3').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(5.2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C4').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C4').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(4.8))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C5').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C5').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(4.4))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C6').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C6').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(4.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C7').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C7').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(3.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C8').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C8').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C9').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C9').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C10').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C10').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C11').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C11').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A3').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('C12').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('C12').bottom(1.6))
# TRASH TIP
equipment['pd100'].drop_tip()
# GET TIP
pickup_pd100tip(3)
   # Loop 1.
   # Aspirate/Dispense Volume = 70.0
equipment['pd100'].aspirate(70.0, equipment['MixingD1'].wells('A4').bottom(6.3))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D1').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D1').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(6.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D2').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D2').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(5.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D3').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D3').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(5.2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D4').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D4').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(4.8))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D5').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D5').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(4.4))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D6').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D6').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(4.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D7').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D7').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(3.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D8').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D8').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D9').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D9').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D10').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D10').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D11').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D11').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('A4').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('D12').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('D12').bottom(1.6))
# TRASH TIP
equipment['pd100'].drop_tip()
# GET TIP
pickup_pd100tip(4)
   # Loop 1.
   # Aspirate/Dispense Volume = 70.0
equipment['pd100'].aspirate(70.0, equipment['MixingD1'].wells('B1').bottom(6.3))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E1').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E1').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(6.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E2').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E2').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(5.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E3').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E3').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(5.2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E4').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E4').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(4.8))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E5').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E5').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(4.4))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E6').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E6').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(4.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E7').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E7').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(3.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E8').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E8').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E9').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E9').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E10').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E10').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E11').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E11').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B1').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('E12').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('E12').bottom(1.6))
# TRASH TIP
equipment['pd100'].drop_tip()
# GET TIP
pickup_pd100tip(8)
   # Loop 1.
   # Aspirate/Dispense Volume = 70.0
equipment['pd100'].aspirate(70.0, equipment['MixingD1'].wells('B2').bottom(6.3))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F1').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F1').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(6.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F2').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F2').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(5.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F3').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F3').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(5.2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F4').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F4').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(4.8))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F5').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F5').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(4.4))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F6').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F6').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(4.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F7').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F7').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(3.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F8').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F8').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F9').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F9').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F10').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F10').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F11').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F11').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B2').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('F12').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('F12').bottom(1.6))
# TRASH TIP
equipment['pd100'].drop_tip()
# GET TIP
pickup_pd100tip(9)
   # Loop 1.
   # Aspirate/Dispense Volume = 70.0
equipment['pd100'].aspirate(70.0, equipment['MixingD1'].wells('B3').bottom(6.3))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G1').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G1').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(6.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G2').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G2').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(5.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G3').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G3').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(5.2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G4').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G4').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(4.8))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G5').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G5').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(4.4))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G6').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G6').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(4.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G7').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G7').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(3.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G8').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G8').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G9').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G9').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G10').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G10').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G11').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G11').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B3').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('G12').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('G12').bottom(1.6))
# TRASH TIP
equipment['pd100'].drop_tip()
# GET TIP
pickup_pd100tip(10)
   # Loop 1.
   # Aspirate/Dispense Volume = 70.0
equipment['pd100'].aspirate(70.0, equipment['MixingD1'].wells('B4').bottom(6.3))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H1').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H1').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(6.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H2').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H2').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(5.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H3').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H3').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(5.2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H4').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H4').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(4.8))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H5').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H5').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(4.4))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H6').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H6').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(4.0))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H7').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H7').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(3.6))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H8').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H8').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H9').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H9').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H10').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H10').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H11').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H11').bottom(1.6))
   # Loop 1.
   # Aspirate/Dispense Volume = 60.0
equipment['pd100'].aspirate(60.0, equipment['MixingD1'].wells('B4').bottom(2))
equipment['pd100'].move_to(equipment['TouchC2'].wells('H12').bottom(0))
equipment['pd100'].delay(seconds=2)
   # Dispense entire Out_Well_Vol into 1 Mixing Well
equipment['pd100'].dispense(60.0, equipment['OutputD2'].wells('H12').bottom(1.6))
# TRASH TIP
equipment['pd100'].drop_tip()

robot.home()
