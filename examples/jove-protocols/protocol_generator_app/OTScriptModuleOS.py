import tkinter
from tkinter import *
from math import *
import os
import sys
from numpy import*

# NOTES:
# ALL HASHTAGS WITH LETTER + STAR eg: "# a*" HAVE NOTES LISTED HERE - USUALLY THEY ARE UNRELATED TO NUMBERED SECTION
# BUT SHARE THE LOOP

# a*  : Not related to 'Equipment' function, uses this loop to create lists of ingredient specific wells for mixing
# b*  : Stores tiprack to matching pipette in Pipette list

bottom = 2
def depth(Well,Volume,Pip_Volume,disp_height):
    Final_Volume = Volume-Pip_Volume
    if Well=='Tube1point5mL':
        d = 9
        a = (pi*d**2)/4
        angle = radians(12.11)
        if Final_Volume<500:
            if Final_Volume>=400:
                end_height=12
            elif Final_Volume>=300:
                end_height=10
            else:
                end_height=bottom
        else:
            end_height=Volume/a
    elif Well=='heating-block-4x5':
        d=10.7
        a = (pi*d**2)/4
        if Final_Volume<500:
            if Final_Volume<=100:
                end_height=bottom
            elif Final_Volume<=200:
                end_height=5
            elif Final_Volume<=300:
                end_height=9
            elif Final_Volume<=400:
                end_height=11
            else:
                end_height=13.5
        else:
            end_height=16+(Final_Volume-500)/a
    elif Well=='tube-rack-2ml' or Well=='tube-rack-2ml-9x9':
        pass
    elif Well=='tube-rack-5ml-96':
        d = 14
        a = (pi*d**2)/4
        if Final_Volume<=100:
            end_height=bottom
        else:
            end_height=10+(Final_Volume-100)/a
    elif Well=='tube-rack-15_50ml':
        d = 26.5
        a = (pi*d**2)/4
        if Final_Volume<=5000:
            end_height=bottom
        else:
            end_height=16+(Final_Volume-5000)/a
    elif Well=='6-well-plate':
        d=34.8
        a=(pi*d**2)/4
        end_height=Final_Volume/a
    elif Well=='12-well-plate':
        d=22.1
        a=(pi*d**2)/4
        end_height=Final_Volume/a
    elif Well=='24-well-plate':
        d=15.6
        a=(pi*d**2)/4
        end_height=Final_Volume/a
    elif Well=='48-well-plate':
        d=11
        a=(pi*d**2)/4
        end_height=Final_Volume/a
    elif Well=='96-deep-well' or Well=='96-flat' or Well=='96-PCR-flat' or Well=='96-PCR-tall' or Well=='96-well-plate-20mm'\
          or Well=='e-gelgol' or Well=='hampton-1ml-deep-block' or Well=='PCR-strip-tall':
        d=6.94
        a=(pi*d**2)/4
        end_height=Final_Volume/a
    elif Well=='384-plate' or Well=='MALDI-plate':
        d=3.7
        a=(pi*d**2)/4
        end_height=Final_Volume/a
    elif Well=='5ml-3x4' or Well=='heating-block-3x4':
        d=14
        a=(pi*d**2)/4
        if Final_Volume<=500:
            end_height=bottom
        else:
            end_height=3.5+(Final_Volume-500)/a
    else:
        end_height=bottom
    if Pip_Volume<0:
        end_height+=disp_height
    else:
        if end_height<(bottom):
            end_height =bottom
        else:
            pass
    position = round(end_height,1)
    return position

def Mixing_Function(i,tray,j,Vol,In_Cells,In_Wells,Wells_In,In_Type,disp_height,Pipette_Type,t):

    ### NEW MIXING TO REPLACE ABOVE

    # DEPTH CALCULATIONS
    # Template
    """depth(In_Wells[i][tray][j],Vol,wellmax,disp_height)"""

    # Coding
    top = depth(Wells_In[i][tray][0],Vol,0,disp_height)+1
    mix_3 = depth(Wells_In[i][tray][0],Vol,wellmax,disp_height)
    mix_1 = depth(Wells_In[i][tray][0],Vol,Vol+wellmax,disp_height)
    mix_2 = round((mix_3-mix_1)/2,0)

    handling_volume = wellmax
    stroke_length = 1
    if mix_2<=2.0:
        mix_2=2
    else:
        pass
    if wellmax>Vol-Vol/20:
        Vol*=3/4
        stroke_length = round(3/4,3)
        handling_volume=Vol
    else:
        pass
    smooth=top-bottom
    if smooth<2:
        smooth=2
    else:
        pass
    #stroke_length = Vol


    # 1. POSITION 2mm INTO LIQUID TO START SEQUENCE:

    # Template
    """equipment['pd1000'].move_to(equipment['MixingD1'].wells('A2').bottom(17), strategy='direct')"""


    # Coding
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].move_to(equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(top)+"), strategy='direct')\n")


    # 2. SUCKS UP FULL PIPETTE WHILE MOVING DOWN INTO LIQUID AND DISPENSES WHEN COMING BACK UP (SMOOTH-MIX)

    # Template
    """smoothMix(equipment['pd1000'], 15, stroke=1 ,iterations=10)"""
    # Coding
    t.write("smoothMix(equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'], "+str(smooth)+", stroke="+str(stroke_length)+", iterations=10)\n")


    # (REPEATED) 1.

    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].move_to(equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(top)+"), strategy='direct')\n\n")


    # 3. REMOVE THE TOP 1000uL OF LIQUID AND DISPENSE AT THE BOTTOM

    # Template
    """equipment['pd1000'].aspirate(1000,equipment['MixingD1'].wells('A2').bottom(9))"""
    """equipment['pd1000'].dispense(1000,equipment['MixingD1'].wells('A2').bottom(2))"""

    # Coding
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].aspirate("+str(handling_volume)+",equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(mix_3)+"))\n")
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].dispense("+str(handling_volume)+",equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(mix_1)+"))\n\n")


    # 4. USE THE REGULAR 'MIX' FEATURE (SUCKS AND DISPENSES AT SAME HEIGHT) AT 3 HEIGHTS (3RDS WITH FULL PIPETTE)

    # Template
    """equipment['pd1000'].mix(2, 1000, equipment['MixingD1'].wells('A2').bottom(2))
    # middle
    equipment['pd1000'].mix(2, 1000, equipment['MixingD1'].wells('A2').bottom(5))
    # high
    equipment['pd1000'].mix(2, 1000, equipment['MixingD1'].wells('A2').bottom(9))"""

    # Coding
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].mix("+str(bottom)+", "+str(handling_volume)+", equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(mix_1)+"))\n")
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].mix("+str(bottom)+", "+str(handling_volume)+", equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(mix_2)+"))\n")
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].mix("+str(bottom)+", "+str(handling_volume)+", equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(mix_3)+"))\n\n")

    # (REPEAT) 3.

    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].aspirate("+str(handling_volume)+",equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(mix_3)+"))\n")
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].dispense("+str(handling_volume)+",equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(mix_1)+"))\n\n")

    # (REPEAT - LINE 1) 4.
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].mix("+str(bottom)+", "+str(handling_volume)+", equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(bottom)+"))\n\n")

    # (REPEAT) 1.
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].move_to(equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(top)+"), strategy='direct')\n")

    # (REPEAT) 2.
    t.write("smoothMix(equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'], "+str(smooth)+", stroke="+str(stroke_length)+", iterations=10)\n")

    # (REPEAT) 1.

    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].move_to(equipment['"+In_Type+str(In_Cells[i][tray][0])+\
            "'].wells('"+In_Wells[i][tray][j]+\
            "').bottom("+str(top)+"), strategy='direct')\n\n")


    # 5. HOVER OVER WELL TO ALLOW EXCESS TO DRIP

    # Template
    """equipment['pd1000'].delay(seconds=5)"""

    # Coding
    t.write("equipment['"+Pipette_Type[axis_max_number]+str(wellmax)+\
            "'].delay(seconds=5)\n")


def OTscript(filename,Cells,Cell_Use,Models,Tray_Pos,Well_Ingrs,Define_Wells,Well_Names,\
             Well_Vols,Well_Solvent1_Concs,Well_Solvent2_Concs,Well_SS_Concs,SS_Type,\
             Pipette_Type, Pipette_Gen_Vols, Pipette_Aspirate, Pipette_Dispense,disp_height,\
             input_number,mixer_number,output_number,tips_number,trash_number,In_Margin,Mix_Margin,\
             Customs_Create):
    global Solvent1_Well_Numbers, Solvent2_Well_Numbers,wellmax,axis_max_number

    ##### CODE HOUSE KEEPING (INITIAL PROTOCOLS #####
    t = open(''+str(filename)+'.py','w')

    f = open('modulePipetting.py','w')
    # Import all folders
    t.write("from time import sleep\n")
    t.write("import opentrons\n")
    t.write("from opentrons import robot, containers, instruments\n")
    t.write("import openworkstation\n")
    t.write("from openworkstation import robot2\n\n")
    t.write("from commands import *\n")
    t.write("from modulePipetting import *\n")
    t.write("from moduleCrosslinker import *\n")
    t.write("from moduleStorage import *\n")
    t.write("from moduleTransportation import *\n\n")
    t.write("# robot and robot 2 is being reset\n")
    t.write("robot.reset()\n")
    t.write("robot2.reset()\n\n\n")
    t.write("connect()\n")
    t.write("home_all\n\n\n")
    ##### 1. DEFINE CONTAINERS - Create 'Equipment' function #####
    f.write("import opentrons\n")
    f.write("from opentrons import robot, containers, instruments\n\n")
    f.write("# 1. DEFINE CONTAINERS - Create 'Equipment' function\n")
    f.write("def getEquipment():\n")
    f.write("      equipment={}\n")
    for i in range(0,len(Cells)):
        for j in Customs_Create:
            f.write(j+"\n")
        if Cell_Use[i][0]=='Tips':
            if Models[i][0]=='tiprack-250ul':
                f.write("      equipment['"+str(Well_Vols[i][0])+"Tiprack"+str(Cells[i][0])+\
                            "'] = containers.load('tiprack-1000ul', '"+str(Cells[i][0])+"')\n")
            else:
                f.write("      equipment['"+str(Well_Vols[i][0])+"Tiprack"+str(Cells[i][0])+\
                            "'] = containers.load('"+str(Models[i][0])+"', '"+str(Cells[i][0])+"')\n")
        elif Cell_Use[i][0]=='Trash':
            f.write("      equipment['Trash"+str(Cells[i][0])+"'] = containers.load('trash-box','"+str(Cells[i][0])+"')\n")
        elif Cell_Use[i][0]=='Ingredients':
            f.write("      equipment['Inputs"+str(Cells[i][0])+\
                            "'] = containers.load('"+str(Models[i][0])+"','"+str(Cells[i][0])+"')\n")
        elif Cell_Use[i][0]=='Mixing':
            f.write("      equipment['Mixing"+str(Cells[i][0])+"'] = containers.load('"+str(Models[i][0])+"','"+str(Cells[i][0])+"')\n")
        elif Cell_Use[i][0]=='Output':
            f.write("      equipment['Output"+str(Cells[i][0])+"'] = containers.load('"+str(Models[i][0])+"','"+str(Cells[i][0])+"')\n")
        else:
            pass



    # DEFINE PIPETTES
    Axis = [[],[]]
    Pip_Tiprack = [[],[]]
    Pip_Sizes = [[],[]]
    number_of_pipettes = trash_number - tips_number
    axis_min_number = 0
    axis_max_number = 0

    wellmin_number = tips_number
    wellmax_number = tips_number
    if number_of_pipettes>1:
        if int(Pipette_Gen_Vols[0])<int(Pipette_Gen_Vols[1]):
            wellmin=int(Pipette_Gen_Vols[0])
            wellmin_number=tips_number
            axis_min_number=0
            wellmax=int(Pipette_Gen_Vols[1])
            wellmax_number=tips_number+1
            axis_max_number=1
        else:
            wellmin=int(Pipette_Gen_Vols[1])
            wellmin_number=tips_number+1
            axis_min_number=1
            wellmax=int(Pipette_Gen_Vols[0])
            wellmax_number=tips_number
            axis_max_number=0
    else:
        wellmin=int(Pipette_Gen_Vols[0])
        wellmin_number=tips_number
        axis_min_number=0
        wellmax=int(Pipette_Gen_Vols[0])
        wellmax_number=tips_number+1
        axis_max_number=1
    Pip_Tiprack[axis_min_number]=(str(wellmin)+"Tiprack"+(Cells[wellmin_number][0])+"")
    Pip_Tiprack[axis_max_number]=(str(wellmax)+"Tiprack"+(Cells[wellmax_number][0])+"")
    Pip_Sizes[axis_min_number] = [wellmin]
    Pip_Sizes[axis_max_number] = [wellmax]

    if number_of_pipettes==1:
        if wellmax==10:
            Axis[0]='a'
            Axis[1]='a'
        else:
            Axis[0]='b'
            Axis[1]='b'
    else:
        Axis[axis_min_number]='a'
        Axis[axis_max_number]='b'
    for i in range(0,number_of_pipettes):
        f.write("      equipment['"+Pipette_Type[i]+Pipette_Gen_Vols[i]+"'] = instruments.Pipette(\n")
        f.write("         name='"+Pipette_Type[i]+Pipette_Gen_Vols[i]+"',\n")
        f.write("         axis='"+Axis[i][0]+"',\n")
        f.write("         max_volume="+(Pipette_Gen_Vols[i])+",\n")
        if int(Pipette_Gen_Vols[i])== 250:
            f.write("         min_volume="+str(int(int(Pipette_Gen_Vols[i])/5))+",\n")
        else:
            f.write("         min_volume="+str(int(int(Pipette_Gen_Vols[i])/10))+",\n")
        f.write("         channels=1,\n")
        f.write("         aspirate_speed="+(Pipette_Aspirate[i])+",\n")
        f.write("         dispense_speed="+(Pipette_Dispense[i])+",\n")
        f.write("         tip_racks=[equipment['"+str(Pipette_Gen_Vols[i])+"Tiprack"+str(Cells[tips_number+i][0])+"']],\n")
        f.write("         trash_container=equipment['Trash"+(Cells[trash_number][0])+"'])\n")
    New_Pip_Sizes=[]
    New_Axis=[]
    New_Pip_Tiprack=[]
    New_Pipette_Type = []
    New_Pipette_Gen_Vols = []
    for i in range(0,1):
        if Pip_Sizes[i][0]>Pip_Sizes[i+1][0]:
            New_Pip_Sizes.append([Pip_Sizes[i+1][0]])
            New_Pip_Sizes.append([Pip_Sizes[i][0]])
            New_Axis.append(Axis[i+1])
            New_Axis.append(Axis[i])
            New_Pip_Tiprack.append(Pip_Tiprack[i+1])
            New_Pip_Tiprack.append(Pip_Tiprack[i])
            New_Pipette_Type.append(Pipette_Type[i+1])
            New_Pipette_Type.append(Pipette_Type[i])
            New_Pipette_Gen_Vols.append(Pipette_Gen_Vols[i+1])
            New_Pipette_Gen_Vols.append(Pipette_Gen_Vols[i])
            new_wellmax_number = copy(wellmin_number)
            new_wellmin_number = copy(wellmax_number)
            new_axis_min_number = copy(axis_max_number)
            new_axis_max_number = copy(axis_min_number)
            Pip_Sizes = New_Pip_Sizes
            Axis = New_Axis
            Pip_Tiprack = New_Pip_Tiprack
            Pip_Sizes = New_Pip_Sizes
            Pipette_Type = New_Pipette_Type
            Pipette_Gen_Vols = New_Pipette_Gen_Vols
            wellmax_number = new_wellmax_number
            wellmin_number = new_wellmin_number
            axis_max_number = new_axis_max_number
            axis_min_number = new_axis_min_number
        else:
            pass


    f.write("      return(equipment)\n\n")
    f.close()

    ##### 2. PICK UP TIP - Creates functions to pick up tips #####
    Pipette_GetTip = [[],[]]
    for i in range(0,number_of_pipettes):
        if Pipette_Type[i]=='pd':
            Pipette_GetTip[i].append("pickup_")
            Pipette_GetTip[i].append("tip(")
        else:
            Pipette_GetTip[i].append("equipment['")
            Pipette_GetTip[i].append("'].pick_up_tip(")
    t.write("equipment=getEquipment()\n")
    # Check available ingredients - Solvent1, Solvent2, PhotoInitiator1, PhotoInitiator2, PBS, Water
    Input_Ingrs = [[],[],[],[],[],[],[]]
    Input_Cell_Locations = [[],[],[],[],[],[],[]]
    Input_Well_Locations = [[],[],[],[],[],[],[]]
    Input_Well_Concentrations = [[],[],[],[],[],[],[]]
    Input_Well_Vols  = [[],[],[],[],[],[],[]]
    Input_Cell_Counters = [[],[],[],[],[],[],[]]
    Input_Well_Type = [[],[],[],[],[],[],[]]
    for i in range(input_number,mixer_number):
        for j in range(0,len(Input_Ingrs)):
            Input_Ingrs[j].append([])
            Input_Cell_Locations[j].append([])
            Input_Well_Locations[j].append([])
            Input_Well_Concentrations[j].append([])
            Input_Well_Vols[j].append([])
            Input_Well_Type[j].append([])
            Input_Cell_Counters[j].append([])

        for j in range(0,len(Well_Ingrs[i])):
            if Well_Ingrs[i][j] == 'Main Solvent 1':
                if 'Main Solvent 1' in Input_Ingrs[0][i]:
                    pass
                else:
                    Input_Ingrs[0].append('Main Solvent 1')
                if Cells[i][0] in Input_Cell_Locations[0][i]:
                    pass
                else:
                    Input_Cell_Locations[0][i].append(Cells[i][0])
                    Input_Well_Type[0][i].append(Models[i][0])
                Input_Well_Locations[0][i].append(Well_Names[i][j])
                Input_Well_Concentrations[0][i].append(round(float(Well_Solvent1_Concs[i][j]),2))
                Input_Well_Vols[0][i].append(round(float(Well_Vols[i][j]),2))

            elif Well_Ingrs[i][j] == 'Main Solvent 2':
                if 'Main Solvent 2' in Input_Ingrs[1][i]:
                    pass
                else:
                    Input_Ingrs[1][i].append('Main Solvent 2')
                if Cells[i][0] in Input_Cell_Locations[1][i]:
                    pass
                else:
                    Input_Cell_Locations[1][i].append(Cells[i][0])
                    Input_Well_Type[1][i].append(Models[i][0])

                Input_Well_Locations[1][i].append(Well_Names[i][j])
                Input_Well_Concentrations[1][i].append(round(float(Well_Solvent2_Concs[i][j]),2))
                Input_Well_Vols[1][i].append(round(float(Well_Vols[i][j]),2))

            elif Well_Ingrs[i][j] == 'Secondary Solvent 1':
                if 'Secondary Solvent 1' in Input_Ingrs[2][i]:
                    pass
                else:
                    Input_Ingrs[2][i].append('Secondary Solvent 1')
                if Cells[i][0] in Input_Cell_Locations[2][i]:
                    pass
                else:
                    Input_Cell_Locations[2][i].append(Cells[i][0])
                    Input_Well_Type[2][i].append(Models[i][0])
                Input_Well_Locations[2][i].append(Well_Names[i][j])
                Input_Well_Concentrations[2][i].append(round(float(Well_SS_Concs[i][j]),2))
                Input_Well_Vols[2][i].append(round(float(Well_Vols[i][j]),2))

            elif Well_Ingrs[i][j] == 'Secondary Solvent 2':
                if 'Secondary Solvent 2' in Input_Ingrs[3][i]:
                    pass
                else:
                    Input_Ingrs[3][i].append('Secondary Solvent 2')
                if Cells[i][0] in Input_Cell_Locations[3][i]:
                    pass
                else:
                    Input_Cell_Locations[3][i].append(Cells[i][0])
                    Input_Well_Type[3][i].append(Models[i][0])
                Input_Well_Locations[3][i].append(Well_Names[i][j])
                Input_Well_Concentrations[3][i].append(round(float(Well_SS_Concs[i][j]),2))
                Input_Well_Vols[3][i].append(round(float(Well_Vols[i][j]),2))

            elif Well_Ingrs[i][j] == 'Diluent 1':
                if 'Diluent 1' in Input_Ingrs[4][i]:
                    pass
                else:
                    Input_Ingrs[4][i].append('Diluent 1')
                if Cells[i][0] in Input_Cell_Locations[4][i]:
                    pass
                else:
                    Input_Cell_Locations[4][i].append(Cells[i][0])
                    Input_Well_Type[4][i].append(Models[i][0])
                Input_Well_Locations[4][i].append(Well_Names[i][j])
                Input_Well_Vols[4][i].append(round(float(Well_Vols[i][j]),2))

            elif Well_Ingrs[i][j] == 'Diluent 2':
                if 'Diluent 2' in Input_Ingrs[5][i]:
                    pass
                else:
                    Input_Ingrs[5][i].append('Diluent 2')
                if Cells[i][0] in Input_Cell_Locations[5][i]:
                    pass
                else:
                    Input_Cell_Locations[5][i].append(Cells[i][0])
                    Input_Well_Type[5][i].append(Models[i][0])
                Input_Well_Locations[5][i].append(Well_Names[i][j])
                Input_Well_Vols[5][i].append(round(float(Well_Vols[i][j]),2))

    # Adjust to keep In_Margin ie % of liquid to remain in ingredient wells
    In_Margin = (100-In_Margin)/100
    """for i in range(0,len(Input_Well_Vols)):
        for tray in range(0,len(Input_Well_Vols[i])):
            for j in range(0,len(Input_Well_Vols[i][tray])):
                Input_Well_Vols[i][tray][j]*=In_Margin"""
    print("Filename = '"+filename+"'")
    print("Input_Cell_Locations = ",Input_Cell_Locations)
    print("Input_Well_Locations = ",Input_Well_Locations)
    print("Input_Well_Vols = ",Input_Well_Vols)
    print("")
    ##### Calculate Mixing Run #####
    # 1 = Uniform
    # 2 = Columns
    # 3 = Rows
    # 4 = Wells

    Out_Well_Vols = [[],[],[],[],[],[],[]]
    Out_Well_Vols_2 = [[],[],[],[],[],[],[]]
    Out_Well_Vol = 0
    Out_Cell_Locations = [[],[],[],[],[],[],[]]
    Out_Well_Locations = [[],[],[],[],[],[],[]]
    Out_Well_Type = [[],[],[],[],[],[],[]]
    Out_Cell_Counts = [[],[],[],[],[],[],[]]
    Out_Well_Type = [[],[],[],[],[],[],[]]
    Match_Out_Cell_Locations = [[],[],[],[],[],[],[]]
    Match_Out_Well_Locations = [[],[],[],[],[],[],[]]
    Match_Out_Mix_Well_Vols = [[],[],[],[],[],[],[]]
    Mixture_Vols = [[],[],[],[],[],[],[]]
    Mixture_Percents = [[],[],[],[],[],[],[]]
    tray = 0
    cell_prev = []
    for i in range(output_number,tips_number):
        tray = i-output_number
        for j in range(0,len(Input_Ingrs)):
            Out_Well_Vols[j].append([])
            Out_Cell_Locations[j].append([])
            Out_Well_Locations[j].append([])
            Out_Well_Vols_2[j].append([0])
            Out_Well_Type[j].append([])
            Out_Cell_Counts[j].append([])
            Mixture_Vols[j].append([])
            Mixture_Percents[j].append([])
            Match_Out_Cell_Locations[j].append([])
            Match_Out_Well_Locations[j].append([])
            Match_Out_Mix_Well_Vols[j].append([])

        #UNIFORM:

        if Define_Wells[i][0]==1:
            Out_Cell_Locations[6][tray].append(Cells[i][0])
            Out_Well_Type[6][tray].append(Models[i][0])
            for j in range(0,len(Well_Names[i])):
                Out_Well_Locations[6][tray].append(Well_Names[i][j])
                Out_Well_Vols[6][tray].append(round(float(Well_Vols[i][j]),2))
                Out_Well_Vol+=round(float(Well_Vols[i][j]),8)
            Mixture_Vols[6][tray].append(round(float(Out_Well_Vol)))
            # Calculate Percent of Substance required for inputted concentration
            try:
                Percent_Solvent1 = round(float(Well_Solvent1_Concs[i][0])/Input_Well_Concentrations[0][0][0],8)
            except:
                Percent_Solvent1 = 0
            try:
                Percent_Solvent2 = round(float(Well_Solvent2_Concs[i][0])/Input_Well_Concentrations[1][0][0],8)
            except:
                Percent_Solvent2 = 0
            Mixture_Percents[0][tray].append(Percent_Solvent1)
            Mixture_Percents[1][tray].append(Percent_Solvent2)
            if SS_Type[i][j]=='Secondary Solvent 1':
                try:
                    Percent_PI = round(float(Well_SS_Concs[i][j])/Input_Well_Concentrations[2][0][0],8)
                except:
                    Percent_PI = 0
                Mixture_Percents[2][tray].append(Percent_PI)
                Mixture_Percents[3][tray].append(0)
            elif SS_Type[i][j]=='Secondary Solvent 2':
                try:
                    Percent_PI = round(float(Well_SS_Concs[i][j])/Input_Well_Concentrations[3][0][0],8)
                except:
                    Percent_PI = 0
                Mixture_Percents[3][tray].append(Percent_PI)
                Mixture_Percents[2][tray].append(0)
            else:
                print("ERROR - Selected Secondary Solvent not in Input Tray (this may be a user input error")
                input('Press ENTER to exit')
            if Well_Ingrs[i][j]=='Diluent 1':
                Mixture_Percents[4][tray].append(round(1-Mixture_Percents[0][tray][0]-Mixture_Percents[1][tray][0]-Mixture_Percents[2][tray][0]-Mixture_Percents[3][tray][0],2))
                Mixture_Percents[5][tray].append(0)
            elif Well_Ingrs[i][j]=='Diluent 2':
                Mixture_Percents[5][tray].append(round(1-Mixture_Percents[0][tray][0]-Mixture_Percents[1][tray][0]-Mixture_Percents[2][tray][0]-Mixture_Percents[3][tray][0],2))
                Mixture_Percents[4][tray].append(0)
            else:
                print("ERROR - Selected Diluent not in Input Tray (this may be a user input error")
                input('Press ENTER to exit')


        #COLUMNS
        elif Define_Wells[i][0]==2:
            column=-1
            Out_Cell_Locations[6][tray].append(Cells[i][0])
            Out_Well_Type[6][tray].append(Models[i][0])
            for j in range(0,len(Tray_Pos[i])):
                z = Tray_Pos[i][j]-(Tray_Pos[i][j]%24)
                x = round(float(Well_Vols[i][j]),8)
                for k in range(0,len(Tray_Pos[i])):
                    z_2 = Tray_Pos[i][k]-(Tray_Pos[i][k]%24)
                    if Well_Names[i][k] in Out_Well_Locations[6][tray] or x<=0 or z_2!=z:
                        pass
                    else:
                        Out_Well_Type[6][tray].append(Models[i][0])
                        Out_Well_Locations[6][tray].append(Well_Names[i][k])
                        Out_Well_Vols[6][tray].append(round(float(Well_Vols[i][k]),2))
                        if k==j:
                            Mixture_Vols[6][tray].append(round(float(Well_Vols[i][k]),2))
                            column+=1
                            try:
                                Percent_Solvent1 = round(float(Well_Solvent1_Concs[i][j])/Input_Well_Concentrations[0][0][0],8)
                            except:
                                Percent_Solvent1 = 0
                            try:
                                Percent_Solvent2 = round(float(Well_Solvent2_Concs[i][j])/Input_Well_Concentrations[1][0][0],8)
                            except:
                                Percent_Solvent2 = 0
                            Mixture_Percents[0][tray].append(Percent_Solvent1)
                            Mixture_Percents[1][tray].append(Percent_Solvent2)
                            if SS_Type[i][j]=='Secondary Solvent 1':
                                try:
                                    Percent_PI = round(float(Well_SS_Concs[i][j])/Input_Well_Concentrations[2][0][0],8)
                                except:
                                    Percent_PI = 0
                                Mixture_Percents[2][tray].append(Percent_PI)
                                Mixture_Percents[3][tray].append(0)
                            elif SS_Type[i][j]=='Secondary Solvent 2':
                                try:
                                    Percent_PI = round(float(Well_SS_Concs[i][j])/Input_Well_Concentrations[3][0][0],8)
                                except:
                                    Percent_PI = 0
                                Mixture_Percents[3][tray].append(Percent_PI)
                                Mixture_Percents[2][tray].append(0)
                            else:
                                print("ERROR - Selected Secondary Solvent not in Input Tray (this may be a user input error")
                                input('Press ENTER to exit')
                            if Well_Ingrs[i][j]=='Diluent 1':
                                Mixture_Percents[4][tray].append(round(1-Mixture_Percents[0][tray][column]-Mixture_Percents[1][tray][column]-Mixture_Percents[2][tray][column]-Mixture_Percents[3][tray][column],2))
                                Mixture_Percents[5][tray].append(0)
                            elif Well_Ingrs[i][j]=='Diluent 2':
                                Mixture_Percents[5][tray].append(round(1-Mixture_Percents[0][tray][column]-Mixture_Percents[1][tray][column]-Mixture_Percents[2][tray][column]-Mixture_Percents[3][tray][column],2))
                                Mixture_Percents[4][tray].append(0)
                            else:
                                print("ERROR - Selected Diluent not in Input Tray (this may be a user input error")
                                input('Press ENTER to exit')
                        else:
                            Mixture_Vols[6][tray][column]+=round(float(Well_Vols[i][k]),8)


        #ROWS
        elif Define_Wells[i][0]==3:
            row=-1
            Out_Cell_Locations[6][tray].append(Cells[i][0])
            Out_Well_Type[6][tray].append(Models[i][0])
            for j in range(0,len(Tray_Pos[i])):
                x = round(float(Well_Vols[i][j]),8)
                z = Tray_Pos[i][j] - int(round((Tray_Pos[i][j])/24,0)*24)
                for k in range(0,len(Tray_Pos[i])):
                    z_2 = Tray_Pos[i][k] - int(round((Tray_Pos[i][k])/24,0)*24)
                    if Well_Names[i][k] in Out_Well_Locations[6][tray] or x<=0 or z_2!=z:
                        pass
                    else:
                        Out_Well_Type[6][tray].append(Models[i][0])
                        Out_Well_Locations[6][tray].append(Well_Names[i][k])
                        Out_Well_Vols[6][tray].append(round(float(Well_Vols[i][k]),2))
                        if k==j:
                            Mixture_Vols[6][tray].append(round(float(Well_Vols[i][k]),2))
                            row+=1
                            try:
                                Percent_Solvent1 = round(float(Well_Solvent1_Concs[i][j])/Input_Well_Concentrations[0][0][0],8)
                            except:
                                Percent_Solvent1 = 0
                            try:
                                Percent_Solvent2 = round(float(Well_Solvent2_Concs[i][j])/Input_Well_Concentrations[1][0][0],8)
                            except:
                                Percent_Solvent2 = 0
                            Mixture_Percents[0][tray].append(Percent_Solvent1)
                            Mixture_Percents[1][tray].append(Percent_Solvent2)

                            if SS_Type[i][j]=='Secondary Solvent 1':
                                try:
                                    Percent_PI = round(float(Well_SS_Concs[i][j])/Input_Well_Concentrations[2][0][0],8)
                                except:
                                    Percent_PI = 0
                                Mixture_Percents[2][tray].append(Percent_PI)
                                Mixture_Percents[3][tray].append(0)
                            elif SS_Type[i][j]=='Secondary Solvent 2':
                                try:
                                    Percent_PI = round(float(Well_SS_Concs[i][j])/Input_Well_Concentrations[3][0][0],8)
                                except:
                                    Percent_PI = 0
                                Mixture_Percents[3][tray].append(Percent_PI)
                                Mixture_Percents[2][tray].append(0)
                            else:
                                print("ERROR - Selected Secondary Solvent not in Input Tray (this may be a user input error")
                                input('Press ENTER to exit')
                            if Well_Ingrs[i][j]=='Diluent 1':
                                Mixture_Percents[4][tray].append(round(1-Mixture_Percents[0][tray][row]-Mixture_Percents[1][tray][row]-Mixture_Percents[2][tray][row]-Mixture_Percents[3][tray][row],2))
                                Mixture_Percents[5][tray].append(0)
                            elif Well_Ingrs[i][j]=='Diluent 2':
                                Mixture_Percents[5][tray].append(round(1-Mixture_Percents[0][tray][row]-Mixture_Percents[1][tray][row]-Mixture_Percents[2][tray][row]-Mixture_Percents[3][tray][row],2))
                                Mixture_Percents[4][tray].append(0)
                            else:
                                print("ERROR - Selected Diluent not in Input Tray (this may be a user input error")
                                input('Press ENTER to exit')
                        else:
                            Mixture_Vols[6][tray][row]+=round(float(Well_Vols[i][k]),8)



        #INDIVIDUAL WELLS

        #INDIVIDUAL WELLS

        elif Define_Wells[i][0]==4:
            well = -1
            Out_Cell_Locations[6][tray].append(Cells[i][0])
            Out_Well_Type[6][tray].append(Models[i][0])
            for j in range(0,len(Tray_Pos[i])):
                x = round(float(Well_Vols[i][j]),8)
                Mixture_Vols[6][tray].append(x)
                if x>0:
                    well+=1
                    Out_Well_Locations[6][tray].append(Well_Names[i][j])
                    Out_Well_Vols[6][tray].append(x)
                    try:
                        Percent_Solvent1 = round(float(Well_Solvent1_Concs[i][j])/Input_Well_Concentrations[0][0][0],8)
                    except:
                        Percent_Solvent1 = 0
                    try:
                        Percent_Solvent2 = round(float(Well_Solvent2_Concs[i][j])/Input_Well_Concentrations[1][0][0],8)
                    except:
                        Percent_Solvent2 = 0
                    Mixture_Percents[0][tray].append(Percent_Solvent1)
                    Mixture_Percents[1][tray].append(Percent_Solvent2)
                    if SS_Type[i][j]=='Secondary Solvent 1':
                        try:
                            Percent_PI = round(float(Well_SS_Concs[i][j])/Input_Well_Concentrations[2][0][0],8)
                        except:
                            Percent_PI = 0
                        Mixture_Percents[2][tray].append(Percent_PI)
                        Mixture_Percents[3][tray].append(0)
                    elif SS_Type[i][j]=='Secondary Solvent 2':
                        try:
                            Percent_PI = round(float(Well_SS_Concs[i][j])/Input_Well_Concentrations[3][0][0],8)
                        except:
                            Percent_PI = 0
                        Mixture_Percents[3][tray].append(Percent_PI)
                        Mixture_Percents[2][tray].append(0)
                    else:
                        print("ERROR - Selected Secondary Solvent not in Input Tray (this may be a user input error")
                        input('Press ENTER to exit')
                    if Well_Ingrs[i][j]=='Diluent 1':
                        Mixture_Percents[4][tray].append(round(1-Mixture_Percents[0][tray][well]-Mixture_Percents[1][tray][well]-Mixture_Percents[2][tray][well]-Mixture_Percents[3][tray][well],2))
                        Mixture_Percents[5][tray].append(0)
                    elif Well_Ingrs[i][j]=='Diluent 2':
                        Mixture_Percents[5][tray].append(round(1-Mixture_Percents[0][tray][well]-Mixture_Percents[1][tray][well]-Mixture_Percents[2][tray][well]-Mixture_Percents[3][tray][well],2))
                        Mixture_Percents[4][tray].append(0)
                    else:
                        print("ERROR - Selected Diluent not in Input Tray (this may be a user input error")
                        input('Press ENTER to exit')
    print("Mixture_Percents = ", Mixture_Percents)
    for i in range(0,len(Mixture_Vols[6])):
        tray=i
        print(tray)
        for j in range(0,len(Mixture_Vols[6][tray])):
            Mixture_Vols[0][tray].append(round(Mixture_Vols[6][tray][j]*Mixture_Percents[0][tray][j],2))
            Mixture_Vols[1][tray].append(round(Mixture_Vols[6][tray][j]*Mixture_Percents[1][tray][j],2))
            Mixture_Vols[2][tray].append(round(Mixture_Vols[6][tray][j]*Mixture_Percents[2][tray][j],2))
            Mixture_Vols[3][tray].append(round(Mixture_Vols[6][tray][j]*Mixture_Percents[3][tray][j],2))
            Mixture_Vols[4][tray].append(round(Mixture_Vols[6][tray][j]*Mixture_Percents[4][tray][j],2))
            Mixture_Vols[5][tray].append(round(Mixture_Vols[6][tray][j]*Mixture_Percents[5][tray][j],2))
    print("Mixture_Vols = ",Mixture_Vols)
    print("")

    # MIXING RUN
    Input_Tray_Counter = 0
    Mixing_Tray_Counter = 0
    Output_Tray_Counter = 0
    Input_Well_Counter = -1
    Tip_Counters = [0,0]
    Input_Well_Vol = -1
    Mix_Well_Vol = -1
    Mix_Well_Counter=0
    # Assign Mixing Wells
    number_mixing_trays = output_number - mixer_number
    Mix_Well_Vols = [[[]],[[]],[[]],[[]],[[]],[[]],[[]]]
    Mix_Cell_Locations = [[[]],[[]],[[]],[[]],[[]],[[]],[[]]]
    Mix_Well_Locations = [[[]],[[]],[[]],[[]],[[]],[[]],[[]]]
    Mix_Well_Type = [[[]],[[]],[[]],[[]],[[]],[[]],[[]]]
    Mix_Cell_Counters = [[[]],[[]],[[]],[[]],[[]],[[]],[[]]]
    # Mix_Margin ie % to remain in mixing wells
    Mix_Margin = (100+Mix_Margin)/100
    for tray in range(0,len(Mixture_Vols[6])):
        if Mixing_Tray_Counter==number_mixing_trays:
            print("ERROR - Not enough mixing wells to produce required volume")
            input('Press ENTER to exit')
        else:
            pass

        for i in range(0,len(Mixture_Vols[6][tray])):
            if Mix_Well_Counter==len(Well_Vols[mixer_number+Mixing_Tray_Counter]):
                Mixing_Tray_Counter+=1
                for i in range(0,len(Mix_Well_Vols)):
                    Mix_Well_Vols[i].append([])
                    Mix_Cell_Locations[i].append([])
                    Mix_Well_Locations[i].append([])
                    Mix_Well_Type[i].append([])
                if Mixing_Tray_Counter==number_mixing_trays:
                    print("ERROR - Not enough mixing wells to produce required volume")
                    input('Press ENTER to exit')
                else:
                    pass
                Mix_Well_Counter=0
            else:
                pass
            # set variable as the volume of the current output well
            measure_vol = round(Mixture_Vols[6][tray][i]*Mix_Margin,8)
            if measure_vol ==0:
                pass
            elif measure_vol<0:
                print("ERROR - negative volume has been inputted")
                input('Press ENTER to exit')
            else:
                # set a variable as the current mixing well size
                space_vol = round(float(Well_Vols[mixer_number+Mixing_Tray_Counter][0]),8)
                # set a variable as the difference between the desired volume and the space available in each mixing well
                difference = round(space_vol-measure_vol,8)
                if Cells[mixer_number+Mixing_Tray_Counter][0] in Mix_Cell_Locations[6][Mixing_Tray_Counter]:
                    pass
                else:
                    Mix_Cell_Locations[6][Mixing_Tray_Counter].append(Cells[mixer_number+Mixing_Tray_Counter][0])
                    Mix_Well_Type[6][Mixing_Tray_Counter].append(Models[mixer_number+Mixing_Tray_Counter][0])

                if difference>=0:
                    Mix_Well_Vols[6][Mixing_Tray_Counter].append(round(measure_vol,2))
                    Mix_Well_Vols[0][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[0][tray][i],2))
                    Mix_Well_Vols[1][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[1][tray][i],2))
                    Mix_Well_Vols[2][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[2][tray][i],2))
                    Mix_Well_Vols[3][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[3][tray][i],2))
                    Mix_Well_Vols[4][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[4][tray][i],2))
                    Mix_Well_Vols[5][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[5][tray][i],2))
                    Mix_Well_Locations[0][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                    Mix_Well_Locations[1][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                    Mix_Well_Locations[2][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                    Mix_Well_Locations[3][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                    Mix_Well_Locations[4][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                    Mix_Well_Locations[5][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                    Mix_Well_Locations[6][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                    Mix_Well_Counter +=1
                    if Cells[mixer_number+Mixing_Tray_Counter][0] in Mix_Cell_Locations[6][Mixing_Tray_Counter]:
                        pass
                    else:
                        Mix_Cell_Locations[6][Mixing_Tray_Counter].append(Cells[mixer_number+Mixing_Tray_Counter][0])
                        Mix_Well_Type[6][Mixing_Tray_Counter].append(Models[mixer_number+Mixing_Tray_Counter][0])
                    difference = 0
                else:
                    while difference<0:
                        if Mix_Well_Counter==len(Well_Vols[mixer_number+Mixing_Tray_Counter]):
                            Mixing_Tray_Counter+=1
                            for i in range(0,len(Mix_Well_Vols)):
                                Mix_Well_Vols[i].append([])
                                Mix_Cell_Locations[i].append([])
                                Mix_Well_Locations[i].append([])
                                Mix_Well_Type[i].append([])
                            if Mixing_Tray_Counter==number_mixing_trays:
                                print("ERROR - Not enough mixing wells to produce required volume")
                                input('Press ENTER to exit')
                            else:
                                pass
                            Mix_Well_Counter=0
                        else:
                            pass
                        measure_vol-=space_vol
                        measure_vol=round(measure_vol,8)
                        Mix_Well_Vols[6][Mixing_Tray_Counter].append(round(space_vol,2))
                        Mix_Well_Vols[0][Mixing_Tray_Counter].append(round(space_vol*Mixture_Percents[0][tray][i],2))
                        Mix_Well_Vols[1][Mixing_Tray_Counter].append(round(space_vol*Mixture_Percents[1][tray][i],2))
                        Mix_Well_Vols[2][Mixing_Tray_Counter].append(round(space_vol*Mixture_Percents[2][tray][i],2))
                        Mix_Well_Vols[3][Mixing_Tray_Counter].append(round(space_vol*Mixture_Percents[3][tray][i],2))
                        Mix_Well_Vols[4][Mixing_Tray_Counter].append(round(space_vol*Mixture_Percents[4][tray][i],2))
                        Mix_Well_Vols[5][Mixing_Tray_Counter].append(round(space_vol*Mixture_Percents[5][tray][i],2))
                        Mix_Well_Locations[0][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[1][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[2][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[3][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[4][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[5][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[6][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Counter+=1
                        difference = round(space_vol-measure_vol,8)
                        if Cells[mixer_number+Mixing_Tray_Counter][0] in Mix_Cell_Locations[6][Mixing_Tray_Counter]:
                            pass
                        else:
                            Mix_Cell_Locations[6][Mixing_Tray_Counter].append(Cells[mixer_number+Mixing_Tray_Counter][0])
                            Mix_Well_Type[6][Mixing_Tray_Counter].append(Models[mixer_number+Mixing_Tray_Counter][0])
                    if difference==0:
                        pass
                    else:
                        Mix_Well_Vols[6][Mixing_Tray_Counter].append(round(measure_vol,2))
                        Mix_Well_Vols[0][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[0][tray][i],2))
                        Mix_Well_Vols[1][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[1][tray][i],2))
                        Mix_Well_Vols[2][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[2][tray][i],2))
                        Mix_Well_Vols[3][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[3][tray][i],2))
                        Mix_Well_Vols[4][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[4][tray][i],2))
                        Mix_Well_Vols[5][Mixing_Tray_Counter].append(round(measure_vol*Mixture_Percents[5][tray][i],2))
                        Mix_Well_Locations[0][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[1][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[2][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[3][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[4][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[5][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Locations[6][Mixing_Tray_Counter].append(Well_Names[mixer_number+Mixing_Tray_Counter][Mix_Well_Counter])
                        Mix_Well_Counter+=1
    for i in range(0,7):
            Mix_Cell_Locations[i]=Mix_Cell_Locations[6]
            Mix_Well_Type[i]=Mix_Well_Type[6]
    Mix_Well_Counter = -1
    Mixing_Tray_Counter = 0

    print("Mix_Cell_Locations = ",Mix_Cell_Locations)
    print("Mix_Well_Locations = ",Mix_Well_Locations)
    print("Mix_Well_Vols = ",Mix_Well_Vols)
    print("Mix_Well_Type = ",Mix_Well_Type)
    print("")
    print("Out_Cell_Locations = ",Out_Cell_Locations)
    print("Out_Well_Locations = ",Out_Well_Locations)
    print("Out_Well_Vols = ",Out_Well_Vols)
    print("")
    Mix_Cell_Locations_2 = [[],[],[],[],[],[],[]]
    Mix_Well_Locations_2 = [[],[],[],[],[],[],[]]
    Mix_Well_Vols_2 = [[],[],[],[],[],[],[]]
    for tray in range(0,len(Mix_Well_Vols[6])):
        Mix_Well_Vols_2[0].append([])
        Mix_Well_Vols_2[1].append([])
        Mix_Well_Vols_2[2].append([])
        Mix_Well_Vols_2[3].append([])
        Mix_Well_Vols_2[4].append([])
        Mix_Well_Vols_2[5].append([])
        Mix_Well_Vols_2[6].append([])
        Mix_Cell_Locations_2[6].append([])
        Mix_Well_Locations_2[6].append([])

    for tray in range(0,len(Mix_Well_Vols[6])):
        Mix_Cell_Locations_2[6][tray]=Mix_Cell_Locations[6][tray]
        for i in range(0,len(Mix_Well_Vols[6][tray])):
            Mix_Well_Vols_2[0][tray].append(0)
            Mix_Well_Vols_2[1][tray].append(0)
            Mix_Well_Vols_2[2][tray].append(0)
            Mix_Well_Vols_2[3][tray].append(0)
            Mix_Well_Vols_2[4][tray].append(0)
            Mix_Well_Vols_2[5][tray].append(0)
            Mix_Well_Vols_2[6][tray].append(Mix_Well_Vols[6][tray][i])
            Mix_Well_Locations_2[6][tray].append(Mix_Well_Locations[6][tray][i])
    print("Mix_Cell_Locations_2 = ",Mix_Cell_Locations_2)
    print("Mix_Well_Locations_2 = ",Mix_Well_Locations_2)
    print("Mix_Well_Vols_2 = ",Mix_Well_Vols_2)
    print("")

    # Create Lists of Well Vols that change as volumes are moved for each Cycle - used to calculate pipetting depths
    Input_Depths = [[],[],[],[],[],[],[]]
    Mix_Depths = [[],[],[],[],[],[],[]]
    Output_Depths = [[],[],[],[],[],[],[]]
    print("In_Margin = ",In_Margin)
    print("Mix_Margin = ",Mix_Margin)
    for i in range(0,len(Input_Well_Vols)):
        for tray in range(0,len(Input_Well_Vols[i])):
            Input_Depths[i].append([])
            for j in range(0,len(Input_Well_Vols[i][tray])):
                Input_Depths[i][tray].append(Input_Well_Vols[i][tray][j])
    for i in range(0,len(Mix_Well_Vols_2)):
        for tray in range(0,len(Mix_Well_Vols_2[i])):
            Mix_Depths[i].append([])
            for j in range(0,len(Mix_Well_Vols_2[i][tray])):
                Mix_Depths[i][tray].append(Mix_Well_Vols_2[0][tray][j])

    for i in range(0,len(Out_Well_Vols)):
        for tray in range(0,len(Out_Well_Vols[i])):
            Output_Depths[i].append([])
            for j in range(0,len(Out_Well_Vols[i][tray])):
                Output_Depths[i][tray].append(0)

    # Define Input Wells as having less volume so that margin is left remaining
    for i in range(0,len(Input_Well_Vols)):
        for tray in range(0,len(Input_Well_Vols[i])):
            for j in range(0,len(Input_Well_Vols[i][tray])):
                Input_Well_Vols[i][tray][j]*=In_Margin
    print("Input_Depths = ",Input_Depths)
    print("Output_Depths = ",Output_Depths)

    # Cycle though Mixing run and Output Run

    for p in range(0,2):
        In_Tray_Counter = 0
        In_Well_Counter = -1
        In_Vol = -1
        Out_Well_Counter = 0
        Prev_Tip = -2
        if p ==0:
            start=0
            In_Vols = Input_Well_Vols[:]
            In_Cells = Input_Cell_Locations[:]
            In_Wells = Input_Well_Locations[:]
            in_number = copy(input_number)
            In_Type = 'Inputs'
            Out_Vols = Mix_Well_Vols[:]
            Out_Cells = Mix_Cell_Locations[:]
            Out_Wells = Mix_Well_Locations[:]
            out_number = copy(mixer_number)
            Out_Type = 'Mixing'
            Cycle_Vols = Out_Vols
            Wells_In = Input_Well_Type[:]
            Wells_Out = Mix_Well_Type[:]
            Asp_Depths = Input_Depths
            Disp_Depths = Mix_Depths
            Margin = 1-In_Margin
            finish=6
            Cycles = [5,4,3,2,1,0]
        else:
            start=6
            In_Vols.clear()
            In_Cells.clear()
            In_Wells.clear()
            In_Vols = Mix_Well_Vols_2[:]
            In_Cells = Mix_Cell_Locations_2[:]
            In_Wells = Mix_Well_Locations_2[:]
            in_number = copy(mixer_number)
            In_Type = 'Mixing'
            Out_Vols.clear()
            Out_Cells.clear()
            Out_Wells.clear()
            Out_Vols = Out_Well_Vols[:]
            Out_Cells = Out_Cell_Locations[:]
            Out_Wells = Out_Well_Locations[:]
            out_number = copy(output_number)
            Out_Type = 'Output'
            Cycle_Vols = Out_Vols
            Wells_In = Mix_Well_Type[:]
            Wells_Out = Out_Well_Type[:]
            Asp_Depths = Mix_Depths
            Disp_Depths = Output_Depths
            Margin = Mix_Margin-1
            finish=7
            Cycles = [6]
        Safety_Margin = In_Vol-In_Vol*Margin
        t.write("#RUN = "+In_Type+"\n")
        print("Run = ",p)
        print("Invols = ",In_Vols)
        print("Outvols = ",Out_Vols)
        # Cycle through all substances ('i')
        # CHANGE '1' TO 'len(Out_Vols)' WHEN READY FOR ALL LOOPS
        for i in Cycles:
            first_well = 0
            if i ==5:
                if Cycle_Vols[i]!='0':
                    t.write(" # 1 = Dilent 2\n")
                    tip_tray_select = 1
                    current_tip = tip_tray_select
                else:
                    pass
            elif i ==0:
                if Cycle_Vols[i]!='0':
                    t.write(" # 5 = Main Solvent 1\n")
                else:
                    pass
            elif i ==1:
                if Cycle_Vols[i]!='0':
                    t.write(" # 2 = Main Solvent 2\n")
                else:
                    pass
            elif i ==2:
                if Cycle_Vols[i]!='0':
                    t.write(" # 6 = Secondary Solvent 1\n")
                else:
                    pass
            elif i ==3:
                if Cycle_Vols[i]!='0':
                    t.write(" # 4 = Secondary Solvent 2\n")
                else:
                    pass
            elif i ==4:
                if Cycle_Vols[i]!='0':
                    t.write(" # 2 = Dilent 1\n")
                else:
                    pass


            elif i ==6:
                if Cycle_Vols[i]!='0':
                    t.write(" # 7 = MIXTURE\n")
                    #Mixing Step
                    t.write("# TRASH TIP \n")
                    t.write("equipment['"+Pipette_Type[current_tip]+Pipette_Gen_Vols[current_tip]+\
                    "'].drop_tip()\n")
                    Tip_Counters[current_tip]+=1
                    Tip_Counter = Tip_Counters[current_tip]
                    for tray in range(0,len(In_Vols[i])):
                        for j in range(0,len(In_Vols[i][tray])):
                            t.write("# GET TIP \n")
                            t.write(Pipette_GetTip[1][0]+Pipette_Type[1]+Pipette_Gen_Vols[1]+Pipette_GetTip[1][1]+str(Tip_Counter)+")\n")
                            Mixing_Function(i,tray,j,Mix_Well_Vols[i][tray][j],In_Cells,In_Wells,Wells_In,In_Type,disp_height,Pipette_Type,t)
                            #set variable to avoid new tip trash at start of Out Well runs
                            # Trashes tip after each mixing run
                            if j != len(In_Vols[i][tray])-1:
                                t.write("# TRASH TIP \n")
                                t.write("equipment['"+Pipette_Type[1]+Pipette_Gen_Vols[1]+\
                                "'].drop_tip()\n")
                                Tip_Counters[1]+=1
                                Tip_Counter = Tip_Counters[1]
                    t.write("# TRASH TIP \n")
                    t.write("equipment['"+Pipette_Type[1]+Pipette_Gen_Vols[1]+\
                    "'].drop_tip()\n")
                    Tip_Counters[1]+=1
                    Tip_Counter = Tip_Counters[1]
                    tip_tray_select = 1
                    current_tip = 5

                else:
                    pass
            tip_margin=0
            for tray in range(0,len(Out_Vols[i])):
                for j in range(0,len(Out_Vols[i][tray])):
                    print(j)
                    # This is the volume we are tracking
                    Out_Vol = round(float(Out_Vols[i][tray][j]),8)

                    # Cycle through all volumes in substance
                    if Out_Vol>0:
                        while Out_Vol>0:
                            #t.write("# start of while loop\n")
                            # CHECK TIP: SELECT APPROPRIATE TIP SIZE
                            if number_of_pipettes>1:
                                if Out_Vol<wellmax/10:
                                    if wellmax==250 and Out_Vol>=50:
                                        tip_tray_select = 1
                                        Tip_Counter = Tip_Counters[1]
                                    else:
                                        if wellmin==250 and Out_Vol<50:
                                            print("ERROR (Pre-Check) - pipetting volume too small to handle: Vol:"+str(Out_Vol)+"uL, Pipette Min:50uL")
                                            input("Press ENTER to continue")
                                        elif Out_Vol<wellmin/10:
                                            print("ERROR (Pre-Check)- pipetting volume too small to handle: Vol:"+str(Out_Vol)+"uL, Pipette Min:"+str(wellmin/10)+"uL")
                                            input("Press ENTER to continue")
                                        tip_tray_select = 0
                                        Tip_Counter = Tip_Counters[0]
                                else:
                                    if wellmax==250 and Out_Vol<50:
                                        tip_tray_select = 0
                                        Tip_Counter = Tip_Counters[0]
                                    else:
                                        tip_tray_select = 1
                                        Tip_Counter = Tip_Counters[1]
                            else:
                                tip_tray_select = 1
                                Tip_Counter = Tip_Counters[tip_tray_select]
                            # CHECK TIP: COMPLETE

                            # SPECIAL CASE TIP CHECK: for 250ul tips
                            if Pipette_Gen_Vols[tip_tray_select]==250:
                                if Tip_Counter == 5 or Tip_Counter ==6 or Tip_Counter == 7:
                                    Tip_Counter = 8
                                    Tip_Counters[tip_tray_select] = 8
                                elif Tip_Counter == 13 or Tip_Counter == 14 or Tip_Counter == 15:
                                    Tip_Counter == 16
                                    Tip_Counters[tip_tray_select] = 16
                                elif Tip_Counter == 21 or Tip_Counter == 22 or Tip_Counter == 23:
                                    Tip_Counter = 24
                                    Tip_Counters[tip_tray_select] = 24
                                elif Tip_Counter == 29 or Tip_Counter == 30 or Tip_Counter == 31:
                                    Tip_Counter = 32
                                    Tip_Counters[tip_tray_select] = 32
                                elif Tip_Counter == 37 or Tip_Counter == 38 or Tip_Counter == 39:
                                    Tip_Counter = 40
                                    Tip_Counters[tip_tray_select] = 40
                                elif Tip_Counter == 45 or Tip_Counter == 46 or Tip_Counter == 47:
                                    Tip_Counter = 48
                                    Tip_Counters[tip_tray_select] = 48
                                elif Tip_Counter == 53 or Tip_Counter == 54 or Tip_Counter == 55:
                                    Tip_Counter = 56
                                    Tip_Counters[tip_tray_select] = 56
                                else:
                                    pass
                            else:
                                pass
                            # SPECIAL CASE TIP CHECK: COMPLETE

                            # Assign Tip volume and margin based off tip selection
                            Tip_Vol = round(float(Pipette_Gen_Vols[tip_tray_select])*0.9,2)
                            # CHECK 2: TO HALVE VOLUME SO THAT REMAINING AMOUNT IS NOT TOO SMALL (general and special cases)
                            if wellmin==250:
                                if 0<Out_Vol-Tip_Vol<wellmin/5:
                                    used = 0
                                    Out_Vol =round(Out_Vol/2,8)
                                    True_Out_Vol = copy(Out_Vol)
                                else:
                                    used = 1
                            # General case
                            else:
                                if 0<Out_Vol-Tip_Vol<wellmin/10:
                                    used = 0
                                    Out_Vol =round(Out_Vol/2,8)
                                    True_Out_Vol = copy(Out_Vol)
                                else:
                                    used = 1
                            # Special case: 250uL
                            if Out_Vol<Pip_Sizes[0][0]/10:
                                if Pip_Sizes[0][0]==250 and Out_Vol>=50:
                                    pass
                                else:
                                    print("ERROR (Pre-Check 2) - Pipetting volume too small for Pipettes available: Pipette Volume = ",Out_Vol," , Smallest Pipette = ",Pip_Sizes[0][0])
                                    input('Press ENTER to exit')
                            else:
                                pass
                            # CHECK 2: COMPLETE

                            # CHECK 1: IF START OF A NEW INGREDIENT GET NEW PIPETTE
                            if p==0 and first_well==0:
                                if i!=5:
                                    t.write("# TRASH TIP \n")
                                    t.write("equipment['"+Pipette_Type[current_tip]+Pipette_Gen_Vols[current_tip]+\
                                    "'].drop_tip()\n")
                                    Tip_Counters[current_tip]+=1
                                    Tip_Counter = Tip_Counters[tip_tray_select]
                                else:
                                    pass
                                first_well+=1
                                t.write("# GET TIP \n")
                                t.write(Pipette_GetTip[tip_tray_select][0]+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+Pipette_GetTip[tip_tray_select][1]+str(Tip_Counter)+")\n")
                                current_tip = copy(tip_tray_select)
                                tip_margin = round(Tip_Vol/0.9*0.1,8)
                                In_Tray_Counter = 0
                                In_Well_Counter = -1
                                In_Vol = -1

                            # CHECK 1: COMPLETE

                            # IN_VOL CHECK - Check volume of Ingredient well, change well if empty
                            if In_Vol-Safety_Margin<=0:
                                In_Well_Counter += 1
                                if In_Well_Counter==len(In_Vols[i][In_Tray_Counter]):
                                    In_Tray_Counter +=1
                                    In_Well_Counter = 0
                                else:
                                    pass
                                # NEW IN WELL TIP CHANGE - Change tip if inwell changes for second cycle as new in well ofter = new concentration
                                if p==1:
                                    if first_well!=0:
                                        t.write("# TRASH TIP \n")
                                        t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[current_tip]+\
                                        "'].drop_tip()\n")
                                        Tip_Counters[current_tip]+=1
                                        Tip_Counter = Tip_Counters[current_tip]
                                    first_well=1
                                    t.write("# GET TIP \n")
                                    t.write(Pipette_GetTip[tip_tray_select][0]+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+Pipette_GetTip[tip_tray_select][1]+str(Tip_Counter)+")\n")
                                    Tip_Vol = round(float(Pipette_Gen_Vols[tip_tray_select])*0.9,2)
                                    Prev_Tip=In_Well_Counter
                                    tip_margin = round(Tip_Vol/0.9*0.1,8)
                                    current_tip = copy(tip_tray_select)
                                else:
                                    if current_tip != tip_tray_select:
                                        t.write("# TRASH TIP \n")
                                        t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[current_tip]+\
                                        "'].drop_tip()\n")
                                        Tip_Counters[current_tip]+=1
                                        Tip_Counter = Tip_Counters[current_tip]
                                        t.write("# GET TIP \n")
                                        t.write(Pipette_GetTip[tip_tray_select][0]+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+Pipette_GetTip[tip_tray_select][1]+str(Tip_Counter)+")\n")
                                        Tip_Vol = round(float(Pipette_Gen_Vols[tip_tray_select])*0.9,2)
                                        Prev_Tip=In_Well_Counter
                                        tip_margin = round(Tip_Vol/0.9*0.1,8)
                                        current_tip = copy(tip_tray_select)
                                    else:
                                        pass
                                try:
                                    In_Vol = round(float(In_Vols[i][In_Tray_Counter][In_Well_Counter]),0)
                                    Safety_Margin = round(Margin*In_Vol/(1+Margin),8)
                                except:
                                    if p==0:
                                        print("ERROR - Out of source volume: There is no more of this Ingredient - please increase Ingredient Volumes then redefine your setup with these changes")
                                        input("press ENTER to exit")
                                        exit()
                                    else:
                                        print("ERROR - Out of source volume: There is no more of this Mixture concentration - most likely due to excessive tip changes where tip margin volume is not pre-calculated")
                                        input("press ENTER to exit")
                                        exit()
                                # IN_VOL CHECK: COMPLETE
                            else:
                                # FIRST OUTWELLS TIP CHECK - Get new tip to start final Out_Wells
                                try:
                                    if current_tip != tip_tray_select:
                                        t.write("# TRASH TIP \n")
                                        t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[current_tip]+\
                                        "'].drop_tip()\n")
                                        Tip_Counters[current_tip]+=1
                                        Tip_Counter = Tip_Counters[current_tip]
                                        t.write("# GET TIP \n")
                                        t.write(Pipette_GetTip[tip_tray_select][0]+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+Pipette_GetTip[tip_tray_select][1]+str(Tip_Counter)+")\n")
                                        Tip_Vol = round(float(Pipette_Gen_Vols[tip_tray_select])*0.9,2)
                                        Prev_Tip=In_Well_Counter
                                        tip_margin = round(Tip_Vol/0.9*0.1,8)
                                        current_tip = copy(tip_tray_select)
                                    else:
                                        pass
                                except:
                                    pass
                            # FIND APPROPRIATE LOOP AND RUN
                                ######
                        # 1
                            if Out_Vol+tip_margin<=In_Vol+tip_margin<=Tip_Vol+tip_margin or Out_Vol+tip_margin<=Tip_Vol+tip_margin<=In_Vol+tip_margin:
                                print("   # Loop 1. \n")
                                asp_depth = depth(Wells_In[i][In_Tray_Counter][0],Asp_Depths[i][In_Tray_Counter][In_Well_Counter],Out_Vol+tip_margin,disp_height)
                                disp_depth = depth(Wells_Out[i][tray][0],Disp_Depths[6][tray][j],-Out_Vol,disp_height)
                                t.write("   # Loop 1. \n")
                                t.write("   # Aspirate/Dispense Volume = "+str(Out_Vol+tip_margin)+" \n")
                                t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
                                        "'].aspirate("+str(Out_Vol+tip_margin)+", equipment['"+In_Type+str(In_Cells[i][In_Tray_Counter][0])+\
                                        "'].wells('"+In_Wells[i][In_Tray_Counter][In_Well_Counter]+\
                                        "').bottom("+str(asp_depth)+"))\n")
                                # CHANGE IN INPUT WELL - decrease in amount
                                In_Vol -= Out_Vol
                                Asp_Depths[i][In_Tray_Counter][In_Well_Counter]-= (Out_Vol+tip_margin)
                                tip_margin=0
                                t.write("   # Dispense entire Out_Well_Vol into 1 Mixing Well \n")
                                t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
                                        "'].dispense("+str(Out_Vol)+", equipment['"+Out_Type+str(Out_Cells[i][tray][0])+\
                                        "'].wells('"+Out_Wells[i][tray][j]+\
                                        "').bottom("+str(disp_depth)+"))\n")
                                Disp_Depths[6][tray][j]+=Out_Vol
                                # CHANGE IN OUTPUT WELL - enough to fill
                                Out_Vol -= Out_Vol
                                In_Vol = round(In_Vol,8)


                        # 2
                            elif In_Vol+tip_margin<=Out_Vol+tip_margin<=Tip_Vol+tip_margin or In_Vol+tip_margin<=Tip_Vol+tip_margin<=Out_Vol+tip_margin:
                                print("   # Loop 2. \n")
                                asp_depth = depth(Wells_In[i][In_Tray_Counter][0],Asp_Depths[i][In_Tray_Counter][In_Well_Counter],In_Vol+tip_margin,disp_height)
                                disp_depth = depth(Wells_Out[i][tray][0],Disp_Depths[6][tray][j],-In_Vol,disp_height)
                                t.write("   # Loop 2. \n")
                                t.write("   # Aspirate/Dispense Volume = "+str(In_Vol+tip_margin)+" \n")
                                t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
                                        "'].aspirate("+str(In_Vol+tip_margin)+", equipment['"+In_Type+str(In_Cells[i][In_Tray_Counter][0])+\
                                        "'].wells('"+In_Wells[i][In_Tray_Counter][In_Well_Counter]+\
                                        "').bottom("+str(asp_depth)+"))\n")
                                Asp_Depths[i][In_Tray_Counter][In_Well_Counter]-=(In_Vol+tip_margin)
                                tip_margin=0
                                t.write("   # Dispense entire Out_Well_Vol into 1 Mixing Well \n")
                                t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
                                        "'].dispense("+str(In_Vol)+", equipment['"+Out_Type+str(Out_Cells[i][tray][0])+\
                                        "'].wells('"+Out_Wells[i][tray][j]+\
                                        "').bottom("+str(disp_depth)+"))\n")
                                Disp_Depths[6][tray][j]+=In_Vol
                                # CHANGE IN OUTWELL VOLUME - empty
                                Out_Vol -= In_Vol
                                In_Vol -= In_Vol
                                In_Vol = round(In_Vol,8)
                                print(Out_Vol)
                                Out_Vol = round(Out_Vol,8)

                        # 3
                            elif Tip_Vol+tip_margin<=Out_Vol+tip_margin<=In_Vol+tip_margin:
                                print("   # Loop 3. \n")
                                asp_depth = depth(Wells_In[i][In_Tray_Counter][0],Asp_Depths[i][In_Tray_Counter][In_Well_Counter],Tip_Vol+tip_margin,disp_height)
                                disp_depth = depth(Wells_Out[i][tray][0],Disp_Depths[6][tray][j],-Tip_Vol,disp_height)
                                t.write("   # Loop 3. \n")
                                #print(asp_depth)
                                t.write("   # Aspirate/Dispense Volume = "+str(Tip_Vol+tip_margin)+" \n")
                                t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
                                        "'].aspirate("+str(Tip_Vol+tip_margin)+", equipment['"+In_Type+str(In_Cells[i][In_Tray_Counter][0])+\
                                        "'].wells('"+In_Wells[i][In_Tray_Counter][In_Well_Counter]+\
                                        "').bottom("+str(asp_depth)+"))\n")
                                # CHANGE IN TIP_VOL - decrease by out vol
                                Asp_Depths[i][In_Tray_Counter][In_Well_Counter]-=(Tip_Vol+tip_margin)
                                # CHANGE IN INPUT WELL
                                In_Vol -= (Tip_Vol)
                                tip_margin=0
                                t.write("   # Dispense entire Out_Well_Vol into 1 Mixing Well \n")
                                t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
                                        "'].dispense("+str(Tip_Vol)+", equipment['"+Out_Type+str(Out_Cells[i][tray][0])+\
                                        "'].wells('"+Out_Wells[i][tray][j]+\
                                        "').bottom("+str(disp_depth)+"))\n")
                                Disp_Depths[6][tray][j]+=Tip_Vol
                                Out_Vol -= Tip_Vol
                                In_Vol = round(In_Vol,8)
                                Out_Vol = round(Out_Vol,8)

                        # 4
                            elif Tip_Vol+tip_margin<=In_Vol+tip_margin<=Out_Vol+tip_margin:
                                #print("   # Loop 4. \n")
                                asp_depth = depth(Wells_In[i][In_Tray_Counter][0],Asp_Depths[i][In_Tray_Counter][In_Well_Counter],Tip_Vol+tip_margin,disp_height)
                                disp_depth = depth(Wells_Out[i][tray][0],Disp_Depths[6][tray][j],-Tip_Vol,disp_height)
                                t.write("   # Loop 4. \n")
                                t.write("   # Aspirate/Dispense Volume = "+str(Tip_Vol+tip_margin)+" \n")
                                t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
                                        "'].aspirate("+str(Tip_Vol+tip_margin)+", equipment['"+In_Type+str(In_Cells[i][In_Tray_Counter][0])+\
                                        "'].wells('"+In_Wells[i][In_Tray_Counter][In_Well_Counter]+\
                                        "').bottom("+str(asp_depth)+"))\n")
                                # CHANGE IN INPUT WELL
                                In_Vol -= Tip_Vol
                                Asp_Depths[i][In_Tray_Counter][In_Well_Counter]-=(Tip_Vol+tip_margin)
                                tip_margin=0
                                t.write("   # Dispense entire Out_Well_Vol into 1 Mixing Well \n")
                                t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
                                        "'].dispense("+str(Tip_Vol)+", equipment['"+Out_Type+str(Out_Cells[i][tray][0])+\
                                        "'].wells('"+Out_Wells[i][tray][j]+\
                                        "').bottom("+str(disp_depth)+"))\n")
                                Disp_Depths[6][tray][j]+=Tip_Vol
                                # CHANGE IN OUTPUT WELL VOL
                                Out_Vol -= Tip_Vol
                                In_Vol = round(In_Vol,8)
                                Out_Vol = round(Out_Vol,8)
                            if used == 0:
                                Out_Vol=True_Out_Vol
                            else:
                                pass
                            current_tip = copy(tip_tray_select)
                    else:
                        pass
    t.write("# TRASH TIP \n")
    t.write("equipment['"+Pipette_Type[tip_tray_select]+Pipette_Gen_Vols[tip_tray_select]+\
    "'].drop_tip()\n")
    t.close()
    print("filename = '"+filename+"'")
    return input('Press ENTER to exit')
