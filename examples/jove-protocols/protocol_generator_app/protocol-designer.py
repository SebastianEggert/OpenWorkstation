import tkinter
from tkinter import *
from math import *
import os
import sys
from numpy import*
from OTScriptModuleOS import OTscript
from Defaults import NewDefaults
from PIL import Image
from resizeimage import resizeimage

def Restart():
    ###### GLOBAL PARAMETER LISTS ###### ###### GLOBAL PARAMETER LISTS ###### ###### GLOBAL PARAMETER LISTS ######
    
    global Cells, Ingrs, Cell_Use, Models, Well_Names, Well_Ingrs, Well_Solvent1_Concs, Well_Solvent2_Concs, Well_SS_Concs,\
           Well_Vols, Tray_Pos, Define_Wells, SS_Type

    Cells = []
    Cell_Use = [['Ingredients'],['Mixing'],['Output'],['Tips'],['Trash']]
    Models = []
    Well_Names = []
    Well_Ingrs = []
    Well_Solvent1_Concs = []
    Well_Solvent2_Concs = []
    Well_SS_Concs = []
    Well_Vols = []
    Tray_Pos = []
    Define_Wells = []
    SS_Type = []
    global Pipette_Type, Pipette_Gen_Vols, Pipette_Aspirate, Pipette_Dispense
    Pipette_Type = []
    Pipette_Gen_Vols = []
    Pipette_Aspirate = []
    Pipette_Dispense =  []
    Pipette_Rack = []
    global Customs_Create
    Customs_Create = []
    ###### CONTAINER WELLS  ###### ###### CONTAINER WELLS  ###### ###### CONTAINER WELLS  ###### ###### CONTAINER WELLS  ###### 
    global point, T25flask, T75flask, trashbox, trough1row25ml,\
           W6wellplate,\
           W12wellplate, W5ml3x4, wheatonvialrack,\
           W24wellplate, W24vialplate, tuberack75ml, tuberack2ml, smallvialrack16x45,\
           W384plate, MALDIplate,\
           W48wellplate, W48vialplate, tuberack5ml96,\
           W96deepwell, W96flat, W96PCRflat, W96PCRtall, W96wellplate20mm, egelgol, hampton1mldeepblock, PCRstriptall,\
           tiprack10ul, tiprack100ul, tiprack200ul, tiprack250ul, tiprack1000ul,\
           alumblockpcrstrips,\
           rigaku,\
           tiprack1000ulchem,\
           tiprack10ulH,tiprack1000ulH,\
           trough12row, trough12rowshort,\
           tuberack1550ml,\
           tuberack2ml9x9,\
           tuberack80well,\
           heatingblock4x5, heatingblock3x4

    # TRAY WELL VOLUMES # equations are length*width*depth (length defined as longer side of tray, not longest well dimension
    #                     or  pi*(diameter/2)^2 *depth
    point_vol = 1
    T25flask_vol = 1
    T75flask_vol = 1
    trashbox_vol = 1

    trough1row25ml_vol = 7*70*40

    W6wellplate_vol = 1
    W12wellplate_vol = 1
    W5ml3x4_vol = 1
    wheatonvialrack_vol = 1
    W24wellplate_vol = 1
    W24vialplate_vol = 1

    tuberack75ml_vol = 750
    tuberack2ml_vol = 2000

    # pointy
    W384plate_vol =  zeros([24,16])
    W384plate_vol = [i+pi*((3.1/2)**2)*9.5 for i in W384plate_vol]

    MALDIplate_vol = 1
    W48wellplate_vol = 1
    W48vialplate_vol = 1
    tuberack5ml96_vol = 1

    W96deepwell_vol = zeros([8,12])
    W96deepwell_vol = [i+pi*((7.5/2)**2)*33.5 for i in W96deepwell_vol]

    W96flat_vol = 1

    W96PCRflat_vol = zeros([8,12])
    W96PCRflat_vol = [i+pi*((6.4/2)**2)*10.4 for i in W96PCRflat_vol]

    W96PCRtall_vol = zeros([8,12])
    W96PCRtall_vol = [i+pi*((6.4/2)**2)*15.4 for i in W96PCRtall_vol]

    W96wellplate20mm_vol = 1
    egelgol_vol = 1
    hampton1mldeepblock_vol = 1

    # pointy
    PCRstriptall_vol = zeros([8,12])
    PCRstriptall_vol = [i+pi*((6.4/2)**2)*19.5 for i in PCRstriptall_vol]

    tiprack10ul_vol = 10
    tiprack100ul_vol = 100
    tiprack200ul_vol = 200
    tiprack250ul_vol = 250
    tiprack1000ul_vol = 1000
    

    alumblockpcrstrips_vol = 1
    rigaku_vol = 1
    tiprack1000ulchem_vol = 1
    tiprack10ulH_vol = 1
    tiprack1000ulH_vol = 1
    trough12row_vol = 1

    tuberack1550ml_vol = [15000,15000,50000,50000,15000,15000,50000,50000,15000,15000]

    tuberack2ml9x9_vol = 1
    tuberack80well_vol = 1

    # WELL SLOT LISTS
    global Input_Vols, Input_Concs, Input_Ingrs, All_pos
    Input_Vols = ['blank']
    Input_Concs = ['blank']
    Input_Ingrs = ['blank']
    # All Positions
    All_pos = (['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12',\
                'A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24',\
                 'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12',\
                 'B13','B14','B15','B16','B17','B18','B19','B20','B21','B22','B23','B24',\
                 'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12',\
                 'C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24',\
                 'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12',\
                 'D13','D14','D15','D16','D17','D18','D19','D20','D21','D22','D23','D24',\
                 'E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12',\
                 'E13','E14','E15','E16','E17','E18','E19','E20','E21','E22','E23','E24',\
                 'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12',\
                 'F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24',\
                 'G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12',\
                 'G13','G14','G15','G16','G17','G18','G19','G20','G21','G22','G23','G24',\
                 'H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12',\
                 'H13','H14','H15','H16','H17','H18','H19','H20','H21','H22','H23','H24',\
                 'I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12',\
                 'I13','I14','I15','I16','I17','I18','I19','I20','I21','I22','I23','I24',\
                 'J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','J11','J12',\
                 'J13','J14','J15','J16','J17','J18','J19','J20','J21','J22','J23','J24',\
                 'K1','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12',\
                 'K13','K14','K15','K16','K17','K18','K19','K20','K21','K22','K23','K24',\
                 'L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12',\
                 'L13','L14','L15','L16','L17','L18','L19','L20','L21','L22','L23','L24',\
                 'M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12',\
                 'M13','M14','M15','M16','M17','M18','M19','M20','M21','M22','M23','M24',\
                 'N1','N2','N3','N4','N5','N6','N7','N8','N9','N10','N11','N12',\
                 'N13','N14','N15','N16','N17','N18','N19','N20','N21','N22','N23','N24',\
                 'O1','O2','O3','O4','O5','O6','O7','O8','O9','O10','O11','O12',\
                 'O13','O14','O15','O16','O17','O18','O19','O20','O21','O22','O23','O24',\
                 'P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12',\
                 'P13','P14','P15','P16','P17','P18','P19','P20','P21','P22','P23','P24'])

    # point, T25-flask, T75-flask, trash-box, trough-1row-25ml
    pos_1 = [0]
    point = pos_1
    T25flask = point
    T75flask = point
    trashbox = point
    trough1row25ml = point

    # well1 = '6-well-plate'
    pos_2 = [0,1,2,24,25,26]
    W6wellplate =  pos_2

    # 12-well-plate, 5ml-3x4, wheaton_vial_rack
    pos_3 = [0,1,2,3,24,25,26,27,48,49,50,51]
    W12wellplate = pos_3
    W5ml3x4 = W12wellplate
    wheatonvialrack = W12wellplate
    heatingblock3x4 = W12wellplate

    #smallvialrack16x45
    smallvialrack16x45 = [0,1,2,3,4,5,24,25,26,27,28,29,48,49,50,51,52,53]
    
    # 24-well-plate, 24-vial-plate, tube-rack-.75ml, tube-rack-2ml, small_vial_rack_16x45
    pos_4 = [0,1,2,3,4,5,24,25,26,27,28,29,48,49,50,51,52,53,72,73,74,75,76,77]
    W24wellplate = pos_4
    W24vialplate = W24wellplate
    tuberack75ml = W24wellplate
    tuberack2ml = W24wellplate
    
    global pos_5 #made global for use in custom tray setup
    pos_5 = list(range(0,384))
    W384plate =  pos_5
    MALDIplate = W384plate

    # 48-vial-plate, 48-well-plate, tube-rack-5ml-96
    pos_6 = [0,1,2,3,4,5,6,7,24,25,26,27,28,29,30,31,\
             48,49,50,51,52,53,54,55,72,73,74,75,76,77,78,79,\
             96,97,98,99,100,101,102,103,120,121,122,123,124,125,126,127]
    W48wellplate = pos_6
    W48vialplate = W48wellplate
    tuberack5ml96 = W48wellplate


    # 96-deep-well, 96-flat, 96-PCR-flat, 96-PCR-tall, 96-well-plate-20mm,
    # e-gelgol, hampton-1ml-deep-block, PCR-strip-tall, tiprack-1000ul,
    # tiprack-10ul, tiprack-200ul
    pos_7 = [0,1,2,3,4,5,6,7,8,9,10,11,24,25,26,27,28,29,30,31,32,33,34,35,\
             48,49,50,51,52,53,54,55,56,57,58,59,72,73,74,75,76,77,78,79,80,81,82,83,\
             96,97,98,99,100,101,102,103,104,105,106,107,120,121,122,123,124,125,126,127,128,129,130,131,\
             144,145,146,147,148,149,150,151,152,153,154,155,168,169,170,171,172,173,174,175,176,177,178,179]
    W96deepwell = pos_7
    W96flat = W96deepwell
    W96PCRflat = W96deepwell
    W96PCRtall = W96deepwell
    W96wellplate20mm = W96deepwell
    egelgol = W96deepwell
    hampton1mldeepblock = W96deepwell            
    PCRstriptall = W96deepwell
    tiprack10ul = W96deepwell
    tiprack100ul = W96deepwell
    tiprack200ul = W96deepwell
    tiprack250ul = W96deepwell
    tiprack1000ul = W96deepwell


    # alum-block-pcr-strips
    pos_8 = [0,1,24,25,48,49,72,73,96,97,120,121,144,145,168,169]
    alumblockpcrstrips = pos_8

    # rigaku-compact-crystallization-plate
    pos_9 = list(range(0,192))
    rigaku = pos_9

    # tiprack-1000ul-chem,
    pos_10 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,\
              24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,\
              48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,\
              72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,\
              96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115]
    tiprack1000ulchem = pos_10
        
    # tiprack-10ul-H
    pos_11 = [0,1,2,3,4,5,6,7,8,9,10,11,24,25,26,27,28,29,30,31,32,33,34,35,\
             48,49,50,51,52,53,54,55,56,57,58,59,72,73,74,75,76,77,78,79,80,81,82,83]
    tiprack10ulH = pos_11
    tiprack1000ulH = tiprack10ulH

    # trough_12row, trough-12row-short
    pos_12 = [0,1,2,3,4,5,6,7,8,9,10,11]
    trough12row = pos_12
    trough12rowshort = trough12row   
    # tube-rack-15_50ml
    pos_13 = [0,1,2,3,24,25,26,27,48,49]
    tuberack1550ml = pos_13

    # tube-rack-2ml-9x9
    pos_14 = [0,1,2,3,4,5,6,7,8,24,25,26,27,28,29,30,31,32,\
             48,49,50,51,52,53,54,55,56,72,73,74,75,76,77,78,79,80,\
             96,97,98,99,100,101,102,103,104,120,121,122,123,124,125,126,127,128,\
             144,145,146,147,148,149,150,151,152]
    tuberack2ml9x9 = pos_14

    # tube-rack-80well
    pos_15 = [0,1,2,3,4,5,6,7,8,9,24,25,26,27,28,29,30,31,32,33,\
             48,49,50,51,52,53,54,55,56,57,72,73,74,75,76,77,78,79,80,81,\
             96,97,98,99,100,101,102,103,104,105]
    tuberack80well = pos_15

    # heating-block-4x5
    pos_16 = [0,1,2,3,4,\
              24,25,26,27,28,\
              48,49,50,51,52,\
              72,73,74,75,76]
    heatingblock4x5 = pos_16

    ###### DROPDOWN INPUTS ###### ###### DROPDOWN INPUTS ###### ###### DROPDOWN INPUTS ###### ###### DROPDOWN INPUTS ###### 

    global Cell_Uses, Use_1,Use_2,Use_3,Use_4,Use_5,Use_NA,\
           Cell_Names,Cell_A1,Cell_B1,Cell_C1,Cell_D1,Cell_E1,Cell_A2,Cell_B2,Cell_C2,Cell_D2,Cell_E2,Cell_NA,\
           Trays,tray_NA,tray1,tray2,tray3,tray4,tray5,tray6,tray7,tray8,tray9,tray10,\
           tray11,tray12,tray13,tray14,tray15,tray16,tray19,tray20,\
           tray21,tray22,tray23,tray24,tray25,tray26,tray27,tray28,tray29,tray30,\
           tray31,tray32,tray33,tray34,tray35,tray36,tray37,tray38,tray39,tray40,\
           tray41,tray42,tray43,tray44



    Use_1 = 'Ingredients'
    Use_2 = 'Mixing'
    Use_3 = 'Output'
    Use_4 = 'Tips'
    Use_5 = 'Trash'
    Use_NA = 'N/A'
    Cell_Uses = [Use_1,Use_2,Use_3,Use_4,Use_5,Use_NA]

    # CELL DROPDOWN OPTIONS
    Cell_A1 = 'A1'
    Cell_B1 = 'B1'
    Cell_C1 = 'C1'
    Cell_D1 = 'D1'
    Cell_E1 = 'E1'
    Cell_A2 = 'A2'
    Cell_B2 = 'B2'
    Cell_C2 = 'C2'
    Cell_D2 = 'D2'
    Cell_E2 = 'E2'
    Cell_NA = 'N/A'
    Cell_Names = [Cell_A1,Cell_A2,Cell_B1,Cell_B2,Cell_C1,Cell_C2,Cell_D1,Cell_D2,Cell_E1,Cell_E2,Cell_NA]

    # TRAY DROPDOWN OPTIONS
    tray_NA = 'N/A'
    tray1 = '6-well-plate'
    tray2 = '12-well-plate'
    tray3 = '24-well-plate'
    tray4 = '24-vial-plate'
    tray5 = '48-well-plate'
    tray6 = '48-vial-plate'
    tray7 = '96-deep-well'
    tray8 = '96-flat'
    tray9 = '96-PCR-flat'
    tray10 = '96-PCR-tall'
    tray11 = '96-well-plate-20mm'
    tray12 = '384-plate'
    tray13 = '5ml-3x4'
    tray14 = 'alum-block-pcr-strips'
    tray15 = 'e-gelgol'
    tray16 = 'hampton-1ml-deep-block'
    tray17 = 'heating-block-3x4'
    tray18 = 'heating-block-4x5'
    tray19 = 'MALDI-plate'
    tray20 = 'PCR-strip-tall'
    tray21 = 'point'
    tray22 = 'rigaku-compact-crystallization-plate'
    tray23 = 'small_vial_rack_16x45'
    tray24 = 'tiprack-10ul'
    tray25 = 'tiprack-10ul-H'
    tray26 = 'tiprack-200ul'
    tray27 = 'tiprack-100ul'
    tray28 = 'tiprack-250ul'
    tray29 = 'tiprack-1000ul'
    tray30 = 'tiprack-1000ul-chem'
    tray31 = 'tiprack-1000ul-H'
    tray32 = 'trash-box'
    tray33 = 'trough-1row-25ml'
    tray34 = 'trough-12row'
    tray35 = 'trough-12row-short'
    tray36 = 'tube-rack-.75ml'
    tray37 = 'tube-rack-2ml'
    tray38 = 'tube-rack-2ml-9x9'
    tray39 = 'tube-rack-5ml-96'
    tray40 = 'tube-rack-15_50ml'
    tray41 = 'tube-rack-80well'
    tray42 = 'T25-flask'
    tray43 = 'T75-flask'
    tray44 = 'wheaton_vial_rack'
    tray45 = 'Custom'
    Trays = [tray_NA,tray1,tray2,tray3,tray4,tray5,tray6,tray7,tray8,tray9,tray10,\
            tray11,tray12,tray13,tray14,tray15,tray16,tray17,tray18,tray19,tray20,\
            tray21,tray22,tray23,tray24,tray25,tray26,tray27,tray28,tray29,tray30,\
            tray31,tray32,tray33,tray34,tray35,tray36,tray37,tray38,tray39,tray40,\
             tray41,tray42,tray43,tray44,tray45]

        # CATEGORY - CONCENTRATION, INGREDIENTS AND WELL ASSIGNMENT OPTIONS

    global Solvent_1, Solvent_2, Solvent_None, Gels, Diluent_1, Diluent_2, Diluent_NA, Diluents, SS_1, \
           SS_2, SSInitiator_None, SSInitiators, Tip1, Tip2, Tip3, Tip4, Tips, Wells1, Wells2,\
           Wells3, Wells, Ingrs, Tip_Setup
    

    Solvent_1 = 'Main Solvent 1'
    Solvent_2 = 'Main Solvent 2'
    Solvent_None = 'N/A'
    Gels = [Solvent_1, Solvent_2, Solvent_None]

    Diluent_1 = 'Diluent 1'
    Diluent_2 = 'Diluent 2'
    Diluents = [Diluent_1, Diluent_2]

    SS_1 = 'Secondary Solvent 1'
    SS_2 = 'Secondary Solvent 2'
    SSInitiators = [SS_1,SS_2]

    Tip4 = '10'
    Tip3 = '100'
    Tip2 = '250'
    Tip1 = '1000'
    Tips = [Tip1,Tip2,Tip3,Tip4]
    Tip_Setup = 0

    Wells1='Assign by Columns'
    Wells2='Assign Individual Wells'
    Wells3='Assign by Rows'
    Wells = [Wells1,Wells2,Wells3]

    Ingrs = [Solvent_None,Solvent_1,Solvent_2,SS_1,SS_2,Diluent_1,Diluent_2]

    ##### TRAY SETUP GEOMETRIES ##### ##### TRAY SETUP GEOMETRIES ##### ##### TRAY SETUP GEOMETRIES ##### 
    global Save_Row, Save_Column, Column_Label_Row,\
           Column_Ingr_Row, Column_Conc_Row, Column_SS_Conc_Row, Column_Vol_Row, Column_Letter_Row,Column_Label_Row2,\
           Column_Letter_Row2, Column_Ingr_Row2, Column_Conc_Row2, Column_SS_Conc_Row2, Column_Vol_Row2,\
           Row24, Row23, Row22, Row21, Row20, Row19, Row18, Row17, Row16, Row15, Row14 ,\
           Row13, Row12, Row11, Row10, Row9, Row8, Row7, Row6, Row5, Row4, Row3, Row2,\
           Row1, Row_Label_Column, Rows_Conc_Column, Rows_Ingr_Column, Rows_Vol_Column, Rows_SS_Column,\
           Col_A, Col_B, Col_C, Col_D, Col_E, Col_F, Col_G, Col_H, Col_I, Col_J, Col_K,\
           Col_L, Col_M, Col_N, Col_O, Col_P, Tray_Label_row, Tray_Label_column, Row_Label_Row

    
        # Rows
    Save_Row = 99
    
    gap = 6
    
    Row24 = 5
    Row23 = Row24+gap*1
    Row22 = Row24+gap*2
    Row21 = Row24+gap*3
    Row20 = Row24+gap*4
    Row19 = Row24+gap*5
    Row18 = Row24+gap*6
    Row17 = Row24+gap*7
    Row16 = Row24+gap*8
    Row15 = Row24+gap*9
    Row14 = Row24+gap*10
    Row13 = Row24+gap*11
    Row12 = Row24+gap*12
    Row11 = Row24+gap*13
    Row10 = Row24+gap*14
    Row9 = Row24+gap*15
    Row8 = Row24+gap*16
    Row7 = Row24+gap*17
    Row6 = Row24+gap*18
    Row5 = Row24+gap*19
    Row4 = Row24+gap*20
    Row3 = Row24+gap*21
    Row2 = Row24+gap*22
    Row1 = Row24+gap*23

    Row_Label_Row = Row24-3

    Column_Label_Row = Row24-3
    Column_Letter_Row = Row12-2
    Column_Ingr_Row = Row24+1
    Column_Conc_Row = Row24+2
    Column_SS_Conc_Row = Row24+3
    Column_Vol_Row = Row24+4

    Column_Label_Row2 = Row12-1
    Column_Letter_Row2 = Row1
    Column_Ingr_Row2 = Row12+1
    Column_Conc_Row2 = Row12+2
    Column_SS_Conc_Row2 = Row12+3
    Column_Vol_Row2 = Row12+4
    
        # Columns
    Save_Column = 4
    
    Col_A = 5
    Col_B = Col_A+1
    Col_C = Col_A+2
    Col_D = Col_A+3
    Col_E = Col_A+4
    Col_F = Col_A+5
    Col_G = Col_A+6
    Col_H = Col_A+7
    Col_I = Col_A
    Col_J = Col_A+1
    Col_K = Col_A+2
    Col_L = Col_A+3
    Col_M = Col_A+4
    Col_N = Col_A+5
    Col_O = Col_A+6
    Col_P = Col_A+7
    Row_Label_Column = Col_A-1
    Rows_Conc_Column = Row_Label_Column+2
    Rows_Conc_Column2 = Row_Label_Column+3
    
    Rows_Ingr_Column = Row_Label_Column+1
    Rows_Vol_Column = Row_Label_Column+5
    Rows_SS_Column = Row_Label_Column+4

    Tray_Label_row = 7
    Tray_Label_column = 3

    global wellcolour, Row_List, Column_List, Category_colour
    wellcolour = 'black'
    Category_colour = 'black'

    Row_List = [Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24,\
                    Row1,Row2,Row3,Row4,Row5,Row6,Row7,Row8,Row9,Row10,Row11,Row12,\
                    Row13,Row14,Row15,Row16,Row17,Row18,Row19,Row20,Row21,Row22,Row23,Row24]

    Column_List = Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,\
                  Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,Col_A,\
                  Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,\
                  Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,Col_B,\
                  Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,\
                  Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,Col_C,\
                  Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,\
                  Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,Col_D,\
                  Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,\
                  Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,Col_E,\
                  Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,\
                  Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,Col_F,\
                  Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,\
                  Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,Col_G,\
                  Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,\
                  Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,Col_H,\
                  Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,\
                  Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,Col_I,\
                  Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,\
                  Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,Col_J,\
                  Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,\
                  Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,Col_K,\
                  Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,\
                  Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,Col_L,\
                  Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,\
                  Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,Col_M,\
                  Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,\
                  Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,Col_N,\
                  Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,\
                  Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,Col_O,\
                  Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,\
                  Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,Col_P,\

    return StartUp()

# DESTROY BOTH OTS AND RESTART PROGRAM
def Destroy():
    try:
        OT.destroy()
    except:
        pass
    return Restart()

##### CELL RADIOBUTTON FUNCTIONS ##### ##### CELL RADIOBUTTON FUNCTIONS ##### ##### CELL RADIOBUTTON FUNCTIONS ##### 
def Add_No_Cell():
    try:
        Add_Use1_Menu.grid_remove()
        Add_Cell1_Menu.grid_remove()
        Add_Tray1_Menu.grid_remove()

        By_Uniform_Button1.grid_remove()
        By_Columns_Button1.grid_remove()
        By_Rows_Button1.grid_remove()
        By_Wells_Button1.grid_remove()
    except:
        pass

    try:
        Add_Use2_Menu.grid_remove()
        Add_Cell2_Menu.grid_remove()
        Add_Tray2_Menu.grid_remove()

        By_Uniform_Button2.grid_remove()
        By_Columns_Button2.grid_remove()
        By_Rows_Button2.grid_remove()
        By_Wells_Button2.grid_remove()

    except:
        pass
    
    try:
        Add_Use3_Menu.grid_remove()
        Add_Cell3_Menu.grid_remove()
        Add_Tray3_Menu.grid_remove()

        By_Uniform_Button3.grid_remove()
        By_Columns_Button3.grid_remove()
        By_Rows_Button3.grid_remove()
        By_Wells_Button3.grid_remove()
        
    except:
        pass
        
def Add_1_Cell():
    Add_No_Cell()
    Add_Use1_Menu.grid(row=Row19,column=Row_Label_Column,sticky=N+S+W+E)
    Add_Cell1_Menu.grid(row=Row19,column=Col_A,sticky=N+S+W+E)
    Add_Tray1_Menu.grid(row=Row19,column=Col_B,sticky=N+S+W+E)

    # ADDITIONAL ASSIGNMENT METHOD
    By_Uniform_Button1.grid(row = Row19, column = Col_C, sticky=N+S+E+W)
    By_Columns_Button1.grid(row = Row19, column = Col_D, sticky=N+S+E+W)
    By_Rows_Button1.grid(row = Row19, column = Col_E, sticky=N+S+E+W)
    By_Wells_Button1.grid(row = Row19, column = Col_F, sticky=N+S+E+W)
    
def Add_2_Cell():
    Add_1_Cell()
    Add_Use2_Menu.grid(row=Row18,column=Row_Label_Column,sticky=N+S+W+E)
    Add_Cell2_Menu.grid(row=Row18,column=Col_A,sticky=N+S+W+E)
    Add_Tray2_Menu.grid(row=Row18,column=Col_B,sticky=N+S+W+E)

    # ADDITIONAL ASSIGNMENT METHOD
    By_Uniform_Button2.grid(row = Row18, column = Col_C, sticky=N+S+E+W)
    By_Columns_Button2.grid(row = Row18, column = Col_D, sticky=N+S+E+W)
    By_Rows_Button2.grid(row = Row18, column = Col_E, sticky=N+S+E+W)
    By_Wells_Button2.grid(row = Row18, column = Col_F, sticky=N+S+E+W)
    
def Add_3_Cell():
    Add_2_Cell()
    Add_Use3_Menu.grid(row=Row17,column=Row_Label_Column,sticky=N+S+W+E)
    Add_Cell3_Menu.grid(row=Row17,column=Col_A,sticky=N+S+W+E)
    Add_Tray3_Menu.grid(row=Row17,column=Col_B,sticky=N+S+W+E)

    # ADDITIONAL ASSIGNMENT METHOD
    By_Uniform_Button3.grid(row = Row17, column = Col_C, sticky=N+S+E+W)
    By_Columns_Button3.grid(row = Row17, column = Col_D, sticky=N+S+E+W)
    By_Rows_Button3.grid(row = Row17, column = Col_E, sticky=N+S+E+W)
    By_Wells_Button3.grid(row = Row17, column = Col_F, sticky=N+S+E+W)

def StartUp():
    ###### INTERFACE GLOBAL DECLARATIONS ###### ###### INTERFACE GLOBAL DECLARATIONS ###### ###### INTERFACE GLOBAL DECLARATIONS ###### 
    global OT, background,w,h,heading,Opentron_Image, bgcolour, \
           Input_Menu, Mixing_Menu, Output_Menu, Tips_Menu, Trash_Menu, \
           Input_Tray, Mixing_Tray, Output_Tray, Tips_Tray, Trash_Tray, \
           Input_Menu2, Mixing_Menu2, Output_Menu2, Tips_Menu2, Trash_Menu2, \
           Input_Tray2, Mixing_Tray2, Output_Tray2, Tips_Tray2, Trash_Tray2, \
           Input_Vol2, Mixing_Vol2, Output_Vol2, Tips_Vol2, Trash_Vol2, \
           Input_Menu3, Mixing_Menu3, Output_Menu3, Tips_Menu3, Trash_Menu3, \
           Input_Tray3, Mixing_Tray3, Output_Tray3, Tips_Tray3, Trash_Tray3, \
           Input_Vol3, Mixing_Vol3, Output_Vol3, Tips_Vol3, Trash_Vol3, \
           Input_Menu4, Mixing_Menu4, Output_Menu4, Tips_Menu4, Trash_Menu4, \
           Input_Tray4, Mixing_Tray4, Output_Tray4, Tips_Tray4, Trash_Tray4, \
           Input_Vol4, Mixing_Vol4, Output_Vol4, Tips_Vol4, Trash_Vol4, \
           Label_Cell3, Label_Tray3, Label_Vol3, Label_Cell2, Label_Tray2,\
           Label_Vol2, Label_Cell3, Label_Tray3, Label_Vol3, Label_Stock_Conc

    ###### MAIN OTN CREATION ###### ###### MAIN OTN CREATION ###### ###### MAIN OTN CREATION ###### 
    OT = Tk()
    w,h = OT.winfo_screenwidth(), OT.winfo_screenheight()
    #w = 1920
    #h = 1080
    global screen_scaling
    screen_scaling1 = w/1920
    screen_scaling2 = h/1080
    if screen_scaling1<screen_scaling2:
        screen_scaling = screen_scaling1
        h = int(round((1080-200)*screen_scaling,0))
    else:
        screen_scaling = screen_scaling2
        h =int(round((1080-200)*screen_scaling,0))
        w = int(round(1920*screen_scaling,0))
    print("screen_scaling = ",screen_scaling)
    OT.geometry("%sx%s" % (w,h))
    bgcolour = 'white'
    OT.config(bg=bgcolour)

    ###### PROGRAM TITLE ######
    OT.title('OpenTrons Pipetting-Code Writer')
    
    ###### BACKGROUND IMAGE ###### ###### BACKGROUND IMAGE ###### ###### BACKGROUND IMAGE ######
    global Main_Pic, Rows_Pic
    with Image.open("OTMainBackground.png") as img:
        # Calculate the width and hight of an image
        pic_width, pic_height = img.size
    pic_width = int(round(pic_width*screen_scaling,0))
    pic_height = int(round(pic_height*screen_scaling,0))
    print("pic_width = ",pic_width)

    with open("OTMainBackground.png", 'r+b') as f:
        with Image.open(f) as image:
            image = image.resize((pic_width, pic_height), Image.ANTIALIAS) ## The (250, 250) is (height, width)
            image.save("OTMainBackground_use.png", image.format)
    with open("OTUniformBackground.png", 'r+b') as f:
        with Image.open(f) as image:
            image = image.resize((pic_width, pic_height), Image.ANTIALIAS) ## The (250, 250) is (height, width)
            image.save("OTUniformBackground_use.png", image.format)
    with open("OTColumnsBackground.png", 'r+b') as f:
        with Image.open(f) as image:
            image = image.resize((pic_width, pic_height), Image.ANTIALIAS) ## The (250, 250) is (height, width)
            image.save("OTColumnsBackground.png_use.png", image.format)
    with open("OTRowsBackground.png", 'r+b') as f:
        with Image.open(f) as image:
            image = image.resize((pic_width, pic_height), Image.ANTIALIAS) ## The (250, 250) is (height, width)
            image.save("OTRowsBackground_use.png", image.format)
    with open("OTIndBackground.png", 'r+b') as f:
        with Image.open(f) as image:
            image = image.resize((pic_width, pic_height), Image.ANTIALIAS) ## The (250, 250) is (height, width)
            image.save("OTIndBackground_use.png", image.format)
    with open("OTPipsBackground.png", 'r+b') as f:
        with Image.open(f) as image:
            image = image.resize((pic_width, pic_height), Image.ANTIALIAS) ## The (250, 250) is (height, width)
            image.save("OTPipsBackground_use.png", image.format)
            
    Opentron_Image = PhotoImage(file="OTMainBackground_use.png")
    
    Main_Pic=Label(OT, image=Opentron_Image)
    Main_Pic.place(x=0,y=0)
    
    ###### CONTINUE BUTTON DETAILS ###### ###### CONTINUE BUTTON DETAILS ###### ###### CONTINUE BUTTON DETAILS ######
    
    # CONTINUE BUTTON
    global Continue_x, Restart_x, Continue_y, Continue_bgcolour, Continue_fgcolour, Continue_w, Continue_h
    #w = 1920
    #h = 1080
    
    Continue_bgcolour = 'purple'
    Continue_fgcolour = 'white'
    Continue_w = int(round(200*screen_scaling,0))
    Continue_h = int(round(80*screen_scaling,0))
    Continue_x = int(round(w-Continue_w-50*screen_scaling,0))
    Continue_y = int(round(h-50*screen_scaling-Continue_h,0))
    Restart_x = int(round(110/1920*w*screen_scaling,0))

    ###### PLACEMENT GEOMETRIES ###### ###### PLACEMENT GEOMETRIES ###### ###### PLACEMENT GEOMETRIES ###### 
    global Radio_Cell1_row, Radio_Cell1_col, Radio_Cell2_row, Radio_Cell2_col, Radio_Cell3_row, Radio_Cell3_col,\
           Radio_Cell4_row, Radio_Cell4_col,\
           Cell_Column_Label_Row, By_Columns_Column, By_Rows_Column, Column_List,\
           Input_Cell_row, Mixing_Cell_row, Output_Cell_row, Tips_Cell_row, Trash_Cell_row, Add_Cell1_row, Add_Cell2_row,\
           Add_Cell3_row, Cell_Use_Labels_col, Cell_Selection_col, Tray_Selection_col, Label_Conc_col,\
           Label_Solvent1_col, Label_Solvent2_col, Label_Dil1_col, Label_Dil2_col, Stock_Gel_Label_row, Stock_Gel_Entry_row,\
           Stock_Solvent1_DD_row, Stock_Solvent2_DD_row, Stock_Gel_Label_col, Stock_Gel_Entry_col, Stock_Solvent1_DD_col, Stock_Solvent2_DD_col,\
           Dil1_DD_row, Dil2_DD_row, Dil1_DD_col, Dil2_DD_col, Output_Gel_Label_row, Output_Gel_Entry_row, Output_Gel_Label_col,\
           Output_Gel_Entry_col, Stock_SS_Label_row, Stock_SS_Entry_row, Stock_PI1_DD_row, Stock_PI2_DD_row, Stock_SS_Label_col,\
           Stock_SS_Entry_col, Stock_PI1_DD_col, Stock_PI2_DD_col, Output_SS_Label_row, Output_SS_Entry_row, Output_SS_Label_col,\
           Output_SS_Entry_col, label_font, heading_font, subheading_font, small_font, Heading_colour,\
           Cell_colour
    
    ###### FONT DETAILS ###### ###### FONT DETAILS ###### ###### FONT DETAILS ###### ###### FONT DETAILS ###### 
    global label_font, heading_font, subheading_font, small_font
    label_font = "Helvetica "+str(int(round(16*screen_scaling**2,0)))+" bold"
    heading_font = "Helvetica "+str(int(round(20*screen_scaling**2,0)))+" bold"
    subheading_font = "Helvetica "+str(int(round(14*screen_scaling**2,0)))+" bold"
    small_font = "Helvetica "+str(int(round(12*screen_scaling**2,0)))

    ###### LABELS ###### ###### LABELS ###### ###### LABELS ###### ###### LABELS ###### ###### LABELS ######

    
        # SECTION COLOUR
    Heading_colour = 'black'
        # CELLS COLOUR
    Cell_colour = 'purple'
        # ASSIGN METHOD COLOUR
    Assign_colour = 'purple'

    global Label_Cells, Label_Inputs, Label_Mixing, Label_Output, Label_Tips, Label_Trash,\
           Label_Cell1, Label_Tray, Label_Assign_By, Label_Uniform_Method, Label_Columns_Method, Label_Rows_Method,\
           Label_Rows_Method, Label_Wells_Method, Space_Protocol, Label_Protocol, Label_In_Margin, Label_Mix_Margin,\
           Label_Save,Label_py, Space_Protocol
    
        # CELL USE LABELS
    Label_Cells = Label(OT, text="Definition of Deck and Containers", font = heading_font, bg=bgcolour,fg=Heading_colour)
    Label_Cells.grid(row=Column_Label_Row-1,column=Row_Label_Column-1, columnspan=5, padx=(100*screen_scaling,0),pady=(50*screen_scaling,0), sticky=W+N)

    Label_Inputs = Label(OT, text = "Input Bay:", font = label_font, fg=Cell_colour, bg=bgcolour)
    Label_Inputs.grid(row=Row24,column=Row_Label_Column, sticky=N+S+W)

    Label_Mixing = Label(OT, text = "Mixing Bay:", font = label_font, fg=Cell_colour, bg=bgcolour)
    Label_Mixing.grid(row=Row23,column=Row_Label_Column, sticky=N+S+W)

    Label_Output = Label(OT, text = "Output Bay:", font = label_font, fg=Cell_colour, bg=bgcolour)
    Label_Output.grid(row=Row22,column=Row_Label_Column, sticky=N+S+W)

    Label_Tips = Label(OT, text = "Tips Bay:", font = label_font, fg=Cell_colour, bg=bgcolour)
    Label_Tips.grid(row=Row21,column=Row_Label_Column, sticky=N+S+W)

    Label_Trash = Label(OT, text = "Trash Bay:", font = label_font, fg=Cell_colour, bg=bgcolour)
    Label_Trash.grid(row=Row20,column=Row_Label_Column, sticky=N+S+W)

        # DROPDOWN COLUMN LABELS
    Label_Cell1 = Label(OT, text="Bay Location", font = subheading_font, fg=Cell_colour, bg=bgcolour)
    Label_Cell1.grid(row=Column_Label_Row,column=Col_A, sticky=N+S+E+W)

    Label_Tray = Label(OT, text="Tray Model", font = subheading_font, fg=Cell_colour, bg=bgcolour)
    Label_Tray.grid(row=Column_Label_Row,column=Col_B, sticky=N+S+E+W)

        # ASSIGN METHOD LABELS
    Label_Assign_By  = Label(OT, text="Define Wells", font = heading_font, fg=Heading_colour, bg=bgcolour)
    Label_Assign_By.grid(row=Column_Label_Row-1,column=Col_C, columnspan = 3, pady=(50*screen_scaling,0), sticky=W)

    Label_Uniform_Method = Label(OT, text="Uniformly     ", font = subheading_font, fg=Assign_colour, bg=bgcolour)
    Label_Uniform_Method.grid(row=Column_Label_Row,column=Col_C, sticky=N+S+E+W)
        
    Label_Columns_Method = Label(OT, text="By Columns     ", font = subheading_font, fg=Assign_colour, bg=bgcolour)
    Label_Columns_Method.grid(row=Column_Label_Row,column=Col_D, sticky=N+S+E+W)

    Label_Rows_Method = Label(OT, text="By Rows     ", font = subheading_font, fg=Assign_colour, bg=bgcolour)
    Label_Rows_Method.grid(row=Column_Label_Row,column=Col_E, sticky=N+S+E+W)
    
    Label_Wells_Method = Label(OT, text="Individually", font = subheading_font, fg=Assign_colour, bg=bgcolour)
    Label_Wells_Method.grid(row=Column_Label_Row,column=Col_F, sticky=N+S+E+W)

    Label_Protocol = Label(OT, text="Protocol Parameters", font = heading_font, fg=Heading_colour, bg=bgcolour)
    Label_Protocol .grid(row=Save_Row-5,column=Row_Label_Column-1, columnspan=3, padx=100*screen_scaling,pady=(175*screen_scaling,0), sticky=W)
    
    Label_In_Margin = Label(OT, text="Input Margin Volume (%)", font = subheading_font, fg=Assign_colour, bg=bgcolour)
    Label_In_Margin.grid(row=Save_Row-4,column=Row_Label_Column-1, columnspan = 2, padx=(150*screen_scaling,0), sticky=N+S+W)
    
    Label_Mix_Margin = Label(OT, text="Mixing Margin Volume (%)", font = subheading_font, fg=Assign_colour, bg=bgcolour)
    Label_Mix_Margin.grid(row=Save_Row-3,column=Row_Label_Column-1, columnspan = 2, padx=(150*screen_scaling,0), sticky=N+S+W)

    Label_Save = Label(OT, text= "Protocal Name", font = subheading_font, fg=Assign_colour, bg=bgcolour)
    Label_Save.grid(row=Save_Row,column=Row_Label_Column-1, padx=(150*screen_scaling,0), sticky=N+S+W)
    
    Label_py = Label(OT, text= ".py", font = small_font, bg=bgcolour)
    Label_py.grid(row=Save_Row,column=Row_Label_Column+2, sticky=N+S+W)

    ###### DROPDOWN MENU CREATION ###### ###### DROPDOWN MENU CREATION ###### ###### DROPDOWN MENU CREATION ###### 

    global Input_Cell1, Mixing_Cell1, Output_Cell1, Tips_Cell1, Trash_Cell1, Input_CellMenu1, Mixing_CellMenu1, Output_CellMenu1,\
           Tips_CellMenu1, Trash_CellMenu1, Input_Model1, Mixing_Model1, Output_Model1, Tips_Model1, Trash_Model1,\
           Input_TrayMenu1, Mixing_TrayMenu1, Output_TrayMenu1, Tips_TrayMenu1, Trash_TrayMenu1, Add_Use1, Add_Use1_Menu, Add_Cell1, Add_Cell1_Menu,\
           Add_Tray1, Add_Tray1_Menu, Add_Use2, Add_Use2_Menu, Add_Cell2, Add_Cell2_Menu, Add_Tray2, Add_Tray2_Menu,\
           Add_Use3, Add_Use3_Menu, Add_Cell3, Add_Cell3_Menu, Add_Tray3, Add_Tray3_Menu, Stock_Solvent1, Stock_Gel_Menu1,\
           Stock_Solvent2, Stock_Gel_Menu2, Stock_Dil1, Stock_Diluent_Menu1, Stock_Dil2, Stock_Diluent_Menu2, Stock_SS1,\
           Stock_SS_Menu1, Stock_SS2, Stock_SS_Menu2, Cell_Additions, Cell_Plus_0, Cell_Plus_1, Cell_Plus_2,\
           Cell_Plus_3,\
           Out_Assign_Var, Out_By_Columns_Button, Out_By_Rows_Button, Out_By_Wells_Button,\
           In_Assign_Var, In_By_Columns_Button, In_By_Rows_Button, In_By_Wells_Button,\
           Assign_Var1 , By_Columns_Button1, By_Rows_Button1, By_Wells_Button1,\
           Assign_Var2, By_Columns_Button2, By_Rows_Button2, By_Wells_Button2,\
           Assign_Var3, By_Columns_Button3, By_Rows_Button3, By_Wells_Button3,\
           By_Uniform_Button1, By_Uniform_Button2, By_Uniform_Button3

    # MAIN CELL SELECTION
    Input_Cell1 = StringVar(OT)
    Mixing_Cell1 = StringVar(OT)
    Output_Cell1 = StringVar(OT)
    Tips_Cell1 = StringVar(OT)
    Trash_Cell1 = StringVar(OT)
    # SET DEFAULT CELLS
    Input_Cell1.set(NewDefaults()[3])
    Mixing_Cell1.set(NewDefaults()[4])
    Output_Cell1.set(NewDefaults()[5])
    Tips_Cell1.set(NewDefaults()[6])
    Trash_Cell1.set(NewDefaults()[7])
    # CREATES MENUS
    Input_CellMenu1 = OptionMenu(OT,Input_Cell1,*Cell_Names)
    Input_CellMenu1.grid(row=Row24,column=Col_A,sticky=N+S+W+E)
    Mixing_CellMenu1 = OptionMenu(OT,Mixing_Cell1,*Cell_Names)
    Mixing_CellMenu1.grid(row=Row23,column=Col_A,sticky=N+S+W+E)
    Output_CellMenu1 = OptionMenu(OT,Output_Cell1,*Cell_Names)
    Output_CellMenu1.grid(row=Row22,column=Col_A,sticky=N+S+W+E)
    Tips_CellMenu1 = OptionMenu(OT,Tips_Cell1,*Cell_Names)
    Tips_CellMenu1.grid(row=Row21,column=Col_A,sticky=N+S+W+E)
    Trash_CellMenu1 = OptionMenu(OT,Trash_Cell1,*Cell_Names)
    Trash_CellMenu1.grid(row=Row20,column=Col_A,sticky=N+S+W+E)
    Input_CellMenu1.config(bg=bgcolour,font=small_font)
    Mixing_CellMenu1.config(bg=bgcolour,font=small_font)
    Output_CellMenu1.config(bg=bgcolour,font=small_font)
    Tips_CellMenu1.config(bg=bgcolour,font=small_font)
    Trash_CellMenu1.config(bg=bgcolour,font=small_font)

    # MAIN TRAY SELECTION
    Input_Model1 = StringVar(OT)
    Mixing_Model1 = StringVar(OT)
    Output_Model1 = StringVar(OT)
    Tips_Model1 = StringVar(OT)
    Trash_Model1 = StringVar(OT)

    #SET DEFAULT TRAYS
    Input_Model1.set(NewDefaults()[11])
    Mixing_Model1.set(NewDefaults()[12])
    Output_Model1.set(NewDefaults()[13])
    Tips_Model1.set(NewDefaults()[14])
    Trash_Model1.set(NewDefaults()[15])
    Input_TrayMenu1 = OptionMenu(OT,Input_Model1,*Trays)
    Input_TrayMenu1.grid(row=Row24,column=Col_B,sticky=N+S+W+E)
    Mixing_TrayMenu1 = OptionMenu(OT,Mixing_Model1,*Trays)
    Mixing_TrayMenu1.grid(row=Row23,column=Col_B,sticky=N+S+W+E)
    Output_TrayMenu1 = OptionMenu(OT,Output_Model1,*Trays)
    Output_TrayMenu1.grid(row=Row22,column=Col_B,sticky=N+S+W+E)
    Tips_TrayMenu1 = OptionMenu(OT,Tips_Model1,*Trays)
    Tips_TrayMenu1.grid(row=Row21,column=Col_B,sticky=N+S+W+E)
    Trash_TrayMenu1 = OptionMenu(OT,Trash_Model1,*Trays)
    Trash_TrayMenu1.grid(row=Row20,column=Col_B,sticky=N+S+W+E)
    Input_TrayMenu1.config(bg=bgcolour,font=small_font)
    Mixing_TrayMenu1.config(bg=bgcolour,font=small_font)
    Output_TrayMenu1.config(bg=bgcolour,font=small_font)
    Tips_TrayMenu1.config(bg=bgcolour,font=small_font)
    Trash_TrayMenu1.config(bg=bgcolour,font=small_font)


    default_Tray6 = NewDefaults()[16]
    default_Tray7 = NewDefaults()[17]
    default_Tray8 = NewDefaults()[18]
        # ADDITIONAL CELLS AND VARIABLE SETTINGS
        # ADD USE 1
    Add_Use1 = StringVar(OT)
    Add_Use1.set(NewDefaults()[0])
    Add_Use1_Menu = OptionMenu(OT,Add_Use1,*Cell_Uses)
    Add_Use1_Menu.config(fg=Cell_colour,bg=bgcolour,font=subheading_font)

        # ADD CELLS 1

    Add_Cell1 = StringVar(OT)
    Add_Cell1.set(NewDefaults()[8])
    Add_Cell1_Menu = OptionMenu(OT,Add_Cell1,*Cell_Names)
    Add_Cell1_Menu.config(bg=bgcolour,font=small_font)

        # ADD TRAYS 1
    Add_Tray1 = StringVar(OT)
    Add_Tray1.set(default_Tray6)
    Add_Tray1_Menu = OptionMenu(OT,Add_Tray1,*Trays)
    Add_Tray1_Menu.config(bg=bgcolour,font=small_font)

        # ADD USE 2
    Add_Use2 = StringVar(OT)
    Add_Use2.set(NewDefaults()[1])
    Add_Use2_Menu = OptionMenu(OT,Add_Use2,*Cell_Uses)
    Add_Use2_Menu.config(fg=Cell_colour,bg=bgcolour,font=subheading_font)

        # CELLS 2
    Add_Cell2 = StringVar(OT)
    Add_Cell2.set(NewDefaults()[9])
    Add_Cell2_Menu = OptionMenu(OT,Add_Cell2,*Cell_Names)
    Add_Cell2_Menu.config(bg=bgcolour,font=small_font)

        # ADD TRAYS 2
    Add_Tray2 = StringVar(OT)
    Add_Tray2.set(default_Tray7)
    Add_Tray2_Menu = OptionMenu(OT,Add_Tray2,*Trays)
    Add_Tray2_Menu.config(bg=bgcolour,font=small_font)

        # ADD USE 1
    Add_Use3 = StringVar(OT)
    Add_Use3.set(NewDefaults()[2])
    Add_Use3_Menu = OptionMenu(OT,Add_Use3,*Cell_Uses)
    Add_Use3_Menu.config(fg=Cell_colour,bg=bgcolour,font=subheading_font)

        # CELLS 3
    Add_Cell3 = StringVar(OT)
    Add_Cell3.set(NewDefaults()[10])
    Add_Cell3_Menu = OptionMenu(OT,Add_Cell3,*Cell_Names)
    Add_Cell3_Menu.config(bg=bgcolour,font=small_font)

        # ADD TRAYS 3
    Add_Tray3 = StringVar(OT)
    Add_Tray3.set(default_Tray8)
    Add_Tray3_Menu = OptionMenu(OT,Add_Tray3,*Trays)
    Add_Tray3_Menu.config(bg=bgcolour,font=small_font)

    ##### CELL RADIO BUTTON CREATION ##### ##### CELL RADIO BUTTON CREATION ##### ##### CELL RADIO BUTTON CREATION ##### 
    Cell_Additions = IntVar()
    Cell_Additions.set(NewDefaults()[19])
    Cell_Plus_0 = Radiobutton(OT, text="5 Bays", font=small_font, variable=Cell_Additions, value=1, command=lambda: Add_No_Cell(), bg=bgcolour)
    Cell_Plus_0.grid(row = Row20, column = Row_Label_Column-1, padx=(120*screen_scaling,0), sticky=N+S+W)
    Cell_Plus_1 = Radiobutton(OT, text="6 Bays", font=small_font, variable=Cell_Additions, value=2, command=lambda: Add_1_Cell(), bg=bgcolour)
    Cell_Plus_1.grid(row = Row19, column = Row_Label_Column-1, padx=(120*screen_scaling,0), pady=(9*screen_scaling,0), sticky=N+S+W)
    Cell_Plus_2 = Radiobutton(OT, text="7 Bays", font=small_font, variable=Cell_Additions, value=3, command=lambda: Add_2_Cell(), bg=bgcolour)
    Cell_Plus_2.grid(row = Row18, column = Row_Label_Column-1, padx=(120*screen_scaling,0), pady=(9*screen_scaling,0), sticky=N+S+W)
    Cell_Plus_3 = Radiobutton(OT, text="8 Bays", font=small_font, variable=Cell_Additions, value=4, command=lambda: Add_3_Cell(), bg=bgcolour)
    Cell_Plus_3.grid(row = Row17, column = Row_Label_Column-1, padx=(120*screen_scaling,0), pady=(9*screen_scaling,0), sticky=N+S+W)
    
    ##### INPUT/OUTPUT ASSIGNMENT METHOD RADIO BUTTONS ##### ##### INPUT/OUTPUT ASSIGNMENT METHOD RADIO BUTTONS #####
    Out_Assign_Var = IntVar()
    Out_Assign_Var.set(1)
    Out_By_Uniform_Button = Radiobutton(OT, variable=Out_Assign_Var, value=1, bg=bgcolour)
    Out_By_Uniform_Button.grid(row = Row22, column = Col_C, sticky=N+S+E+W)
    Out_By_Columns_Button = Radiobutton(OT, variable=Out_Assign_Var, value=2, bg=bgcolour)
    Out_By_Columns_Button.grid(row = Row22, column = Col_D, sticky=N+S+E+W)
    Out_By_Rows_Button = Radiobutton(OT, variable=Out_Assign_Var, value=3, bg=bgcolour)
    Out_By_Rows_Button.grid(row = Row22, column = Col_E, sticky=N+S+E+W)
    Out_By_Wells_Button = Radiobutton(OT, variable=Out_Assign_Var, value=4, bg=bgcolour)
    Out_By_Wells_Button.grid(row = Row22, column = Col_F, sticky=N+S+E+W)
    
    In_Assign_Var = IntVar()
    In_Assign_Var.set(2)
    In_By_Uniform_Button = Radiobutton(OT, variable=In_Assign_Var, value=1, bg=bgcolour)
    In_By_Uniform_Button.grid(row = Row24, column = Col_C, sticky=N+S+E+W)
    In_By_Columns_Button = Radiobutton(OT, variable=In_Assign_Var, value=2, bg=bgcolour)
    In_By_Columns_Button.grid(row = Row24, column = Col_D, sticky=N+S+E+W)
    In_By_Rows_Button = Radiobutton(OT, variable=In_Assign_Var, value=3, bg=bgcolour)
    In_By_Rows_Button.grid(row = Row24, column = Col_E, sticky=N+S+E+W)
    In_By_Wells_Button = Radiobutton(OT, variable=In_Assign_Var, value=4, bg=bgcolour)
    In_By_Wells_Button.grid(row = Row24, column = Col_F, sticky=N+S+E+W)

        # ADDITION CELL ASSIGNMENT METHOD RADIO BUTTONS

    Assign_Var1 = IntVar()
    Assign_Var1.set(1)
    By_Uniform_Button1 = Radiobutton(OT, variable=Assign_Var1, value=1, bg=bgcolour)
    By_Columns_Button1 = Radiobutton(OT, variable=Assign_Var1, value=2, bg=bgcolour)
    By_Rows_Button1 = Radiobutton(OT, variable=Assign_Var1, value=3, bg=bgcolour)
    By_Wells_Button1 = Radiobutton(OT, variable=Assign_Var1, value=4, bg=bgcolour)
    
    Assign_Var2 = IntVar()
    Assign_Var2.set(1)
    By_Uniform_Button2 = Radiobutton(OT, variable=Assign_Var2, value=1, bg=bgcolour)
    By_Columns_Button2 = Radiobutton(OT, variable=Assign_Var2, value=2, bg=bgcolour)
    By_Rows_Button2 = Radiobutton(OT, variable=Assign_Var2, value=3, bg=bgcolour)
    By_Wells_Button2 = Radiobutton(OT, variable=Assign_Var2, value=4, bg=bgcolour)

    Assign_Var3 = IntVar()
    Assign_Var3.set(1)
    By_Uniform_Button3 = Radiobutton(OT, variable=Assign_Var3, value=1, bg=bgcolour)
    By_Columns_Button3 = Radiobutton(OT, variable=Assign_Var3, value=2, bg=bgcolour)
    By_Rows_Button3 = Radiobutton(OT, variable=Assign_Var3, value=3, bg=bgcolour)
    By_Wells_Button3 = Radiobutton(OT, variable=Assign_Var3, value=4, bg=bgcolour)

    # SAVE AS BOX
    global File_Name, In_Margin_Entry,Mix_Margin_Entry
    File_Name = Entry()
    File_Name.insert(0,'Samples1')
    File_Name.grid(row=Save_Row,column=Row_Label_Column+1, sticky=N+S+E+W)
    In_Margin_Entry = Entry()
    In_Margin_Entry.insert(0,NewDefaults()[20])
    In_Margin_Entry.grid(row=Save_Row-4,column=Row_Label_Column+1, sticky=N+S+E+W)
    Mix_Margin_Entry = Entry()
    Mix_Margin_Entry.insert(0,NewDefaults()[21])
    Mix_Margin_Entry.grid(row=Save_Row-3,column=Row_Label_Column+1, sticky=N+S+E+W)

    
        
    # FIRST CONTINUE BUTTON
    global Defaults_Button, Restore_Defaults_Button
    default_x = int(Continue_x-250*screen_scaling)
    default_y = int(Continue_y+40*screen_scaling)
    defaults_width = int(round(250*screen_scaling,0))
    defaults_height = int(round(40*screen_scaling,0))
    Continue_Button = Button(OT,command = lambda: DefineWells(), text = 'Input Tray Setup', font =subheading_font,\
                            fg=Continue_fgcolour, bg = Continue_bgcolour)
    Continue_Button.place(x=Continue_x,y=Continue_y,width = Continue_w, height = Continue_h)

    Defaults_Button = Button(OT,command = lambda: SetDefaults(), text = 'Save as Default Setup', font =subheading_font,\
                            fg=Continue_fgcolour, bg = Continue_bgcolour)
    Defaults_Button.place(x=default_x,y=Continue_y,width = defaults_width, height = defaults_height)

    Restore_Defaults_Button = Button(OT,command = lambda: RestoreDefaults(), text = 'Restore Original Defaults', font =subheading_font,\
                            fg=Continue_fgcolour, bg = 'blue')
    Restore_Defaults_Button.place(x=default_x,y= default_y,width = defaults_width, height = defaults_height)

    Restart_Button = Button(OT, command = lambda: Destroy(), text = 'Restart', font =subheading_font,\
                            height = Continue_h, width = Continue_w, bg = 'red')
    try:
        Main_Pic.tagraise()
    except:
        pass
    global Main_List
    Main_List = [Main_Pic, Restart_Button, Continue_Button,\
                 Label_Cells, Label_Inputs, Label_Mixing, Label_Output, Label_Tips, Label_Trash,\
                 Label_Cell1, Label_Tray, Label_Assign_By, Label_Uniform_Method, Label_Columns_Method, Label_Rows_Method,\
                 Label_Rows_Method, Label_Wells_Method,\
                 Input_CellMenu1, Mixing_CellMenu1, Output_CellMenu1, Tips_CellMenu1, Trash_CellMenu1,\
                 Input_TrayMenu1, Mixing_TrayMenu1, Output_TrayMenu1, Tips_TrayMenu1, Trash_TrayMenu1,\
                 Add_Use1_Menu, Add_Cell1_Menu, Add_Tray1_Menu, Add_Use2_Menu, Add_Cell2_Menu, Add_Tray2_Menu,\
                 Add_Use3_Menu, Add_Cell3_Menu, Add_Tray3_Menu, Cell_Plus_0,\
                 Cell_Plus_1, Cell_Plus_2, Cell_Plus_3,\
                 Out_By_Uniform_Button,Out_By_Columns_Button, Out_By_Rows_Button, Out_By_Wells_Button,\
                 In_By_Uniform_Button, In_By_Columns_Button, In_By_Rows_Button, In_By_Wells_Button,\
                 By_Columns_Button1, By_Rows_Button1, By_Wells_Button1,\
                 By_Columns_Button2, By_Rows_Button2, By_Wells_Button2,\
                 By_Columns_Button3, By_Rows_Button3, By_Wells_Button3,\
                 By_Uniform_Button1, By_Uniform_Button2, By_Uniform_Button3,\
                 Label_Save,File_Name, Label_Protocol, Label_In_Margin,Label_Mix_Margin,In_Margin_Entry,Mix_Margin_Entry,\
                 Label_Save,Label_py]

    # EXECUTE DEFAULT CELL NUMBERS
    if NewDefaults()[19] == 1:
        Add_No_Cell
    elif NewDefaults()[19] == 2:
        Add_1_Cell()
    elif NewDefaults()[19] == 3:
        Add_2_Cell()
    else:
        Add_3_Cell
    
    return Restart_Button.place(x=Restart_x,y=Continue_y, width = Continue_w, height = Continue_h)



def writescript():
    if len(Pipette_Gen_Vols)==1:
        Pipette_Gen_Vols.append(Pipette_Gen_Vols[0])
    else:
        pass
    print('start')
    print("filename = '"+filename+"'")
    print("New_Cells =",New_Cells)
    print("New_Cell_Use =",New_Cell_Use)
    print("New_Models =",New_Models)
    print("New_Well_Ingrs =",New_Well_Ingrs)
    print("New_Define_Wells =",New_Define_Wells)
    print("New_Well_Names =",New_Well_Names)
    print("New_Well_Vols =",New_Well_Vols)
    print("New_Well_Solvent1_Concs =",New_Well_Solvent1_Concs)
    print("New_Well_Solvent2_Concs =",New_Well_Solvent2_Concs)
    print("New_Well_SS_Concs =",New_Well_SS_Concs)
    print("New_Tray_Pos =",New_Tray_Pos)
    print("New_SS_Type =",New_SS_Type)
    print("input_number = ",input_number)
    print("mixer_number = ",mixer_number)
    print("output_number = ",output_number)
    print("tips_number = ",tips_number)
    print("trash_number = ",trash_number)
    print("In_Margin = ",In_Margin)
    print("Mix_Margin = ",Mix_Margin)
    print("Pipette_Type = ",Pipette_Type)
    print("Pipette_Aspirate = ",Pipette_Aspirate)
    print("Pipette_Dispense = ",Pipette_Dispense)
    print("Pipette_Gen_Vols = ",Pipette_Gen_Vols)
    print("disp_height = ",disp_height)
    print("Customs_Create = ",Customs_Create)

    return OTscript(filename,New_Cells,New_Cell_Use,New_Models,New_Tray_Pos,New_Well_Ingrs,New_Define_Wells,New_Well_Names,\
             New_Well_Vols,New_Well_Solvent1_Concs,New_Well_Solvent2_Concs,New_Well_SS_Concs,New_SS_Type,\
             Pipette_Type, Pipette_Gen_Vols, Pipette_Aspirate, Pipette_Dispense, disp_height,\
             input_number,mixer_number,output_number,tips_number,trash_number,In_Margin,Mix_Margin,\
             Customs_Create)

def GetUniform(number,Tray):# GET INDIVIDUAL WELLS
    for i in New_Tray_Pos[number]:
        New_Well_Vols[number].append(Vol_List[0].get())
        if New_Cell_Use[number]==['Ingredients']:
            New_Well_Ingrs[number].append(Ingr_List[0].get())
            if New_Well_Ingrs[number][i]=='Main Solvent 1':
                New_Well_Solvent1_Concs[number].append(Solvent1_Conc_List[0].get())
                New_Well_Solvent2_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Main Solvent 2':
                New_Well_Solvent2_Concs[number].append(Solvent1_Conc_List[0].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Secondary Solvent 1':
                New_Well_SS_Concs[number].append(Solvent1_Conc_List[0].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Secondary Solvent 2':
                New_Well_SS_Concs[number].append(Solvent1_Conc_List[0].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
            else:
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
        elif New_Cell_Use[number]==['Output']:
            New_Well_Ingrs[number].append(Dilu_List[0].get())
            New_Well_Solvent1_Concs[number].append(Solvent1_Conc_List[0].get())
            New_Well_Solvent2_Concs[number].append(Solvent2_Conc_List[0].get())
            New_Well_SS_Concs[number].append(SS_Conc_List[0].get())
            New_SS_Type[number].append(SS_List[0].get())
    number+=1
    return Inputs(number)
    
def GetColumns(number,Tray): # GET COLUMNS
    for i in range(0,len(New_Tray_Pos[number])):
        z = New_Tray_Pos[number][i]-(New_Tray_Pos[number][i]%24)
        New_Well_Vols[number].append(Vol_List[z].get())
        if New_Cell_Use[number]==['Ingredients']:
            New_Well_Ingrs[number].append(Ingr_List[z].get())
            if New_Well_Ingrs[number][i]=='Main Solvent 1':
                New_Well_Solvent1_Concs[number].append(Solvent1_Conc_List[z].get())
                New_Well_Solvent2_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Main Solvent 2':
                New_Well_Solvent2_Concs[number].append(Solvent1_Conc_List[z].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Secondary Solvent 1':
                New_Well_SS_Concs[number].append(Solvent1_Conc_List[z].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Secondary Solvent 2':
                New_Well_SS_Concs[number].append(Solvent1_Conc_List[z].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
            else:
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
        elif New_Cell_Use[number]==['Output']:
            New_Well_Ingrs[number].append(Dilu_List[z].get())
            New_Well_Solvent1_Concs[number].append(Solvent1_Conc_List[z].get())
            New_Well_Solvent2_Concs[number].append(Solvent2_Conc_List[z].get())
            New_Well_SS_Concs[number].append(SS_Conc_List[z].get())
            New_SS_Type[number].append(SS_List[z].get())
        
    number+=1
    return Inputs(number)

def GetRows(number,Tray): # GET ROWS
    
    for i in range(0,len(New_Tray_Pos[number])):
        z = New_Tray_Pos[number][i] - int(round(New_Tray_Pos[number][i]/24,0)*24)
        New_Well_Vols[number].append(Vol_List[z].get())
        if New_Cell_Use[number]==['Ingredients']:
            New_Well_Ingrs[number].append(Ingr_List[z].get())
            if New_Well_Ingrs[number][i]=='Main Solvent 1':
                New_Well_Solvent1_Concs[number].append(Solvent1_Conc_List[z].get())
                New_Well_Solvent2_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Main Solvent 2':
                New_Well_Solvent2_Concs[number].append(Solvent1_Conc_List[z].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Secondary Solvent 1':
                New_Well_SS_Concs[number].append(Solvent1_Conc_List[z].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
            elif New_Well_Ingrs[number][i]=='Secondary Solvent 2':
                New_Well_SS_Concs[number].append(Solvent1_Conc_List[z].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
            else:
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
        elif New_Cell_Use[number]==['Output']:
            New_Well_Ingrs[number].append(Dilu_List[z].get())
            New_Well_Solvent1_Concs[number].append(Solvent1_Conc_List[z].get())
            New_Well_Solvent2_Concs[number].append(Solvent2_Conc_List[z].get())
            New_Well_SS_Concs[number].append(SS_Conc_List[z].get())
            New_SS_Type[number].append(SS_List[z].get())
        
    number+=1
    return Inputs(number)

def GetWells(number,Tray):# GET INDIVIDUAL WELLS
    for i in New_Tray_Pos[number]:
        New_Well_Vols[number].append(Vol_List[i].get())
        
        if New_Cell_Use[number]==['Ingredients']:
            New_Well_Ingrs[number].append(Ingr_List[i].get())
            if Ingr_List[i].get()=='Main Solvent 1':
                New_Well_Solvent1_Concs[number].append(Solvent1_Conc_List[i].get())
                New_Well_Solvent2_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
            elif Ingr_List[i].get()=='Main Solvent 2':
                New_Well_Solvent2_Concs[number].append(Solvent1_Conc_List[i].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
            elif Ingr_List[i].get()=='Secondary Solvent 1':
                New_Well_SS_Concs[number].append(Solvent1_Conc_List[i].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
            elif Ingr_List[i].get()=='Secondary Solvent 2':
                New_Well_SS_Concs[number].append(Solvent1_Conc_List[i].get())
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
            else:
                New_Well_Solvent1_Concs[number].append('0')
                New_Well_Solvent2_Concs[number].append('0')
                New_Well_SS_Concs[number].append('0')
        elif New_Cell_Use[number]==['Output']:
            New_Well_Ingrs[number].append(Dilu_List[i].get())
            New_Well_Solvent1_Concs[number].append(Solvent1_Conc_List[i].get())
            New_Well_Solvent2_Concs[number].append(Solvent2_Conc_List[i].get())
            New_Well_SS_Concs[number].append(SS_Conc_List[i].get())
            New_SS_Type[number].append(SS_List[i].get())
        
    number+=1
    return Inputs(number)

def Pipette_Parameters(number,Tray):
    global Tip_Setup, disp_height
    if Tip_Setup>=1:
        pass
    else:
        for i in Pipette_List:
            i.grid_remove()
        
        if Pipette1_Type.get()==1:
            Pipette_Type.append('pd')
        else:
            Pipette_Type.append('ad')
        if Pipette2_Type.get()==1:
            Pipette_Type.append('pd')
        else:
            Pipette_Type.append('ad')
        Pipette_Aspirate.append(Pippett1_Aspirate_Entry.get())
        Pipette_Aspirate.append(Pippett2_Aspirate_Entry.get())
        Pipette_Dispense.append(Pippett1_Dispense_Entry.get())
        Pipette_Dispense.append(Pippett2_Dispense_Entry.get())
    if Tray=='tiprack-10ul' or Tray=='tiprack-10ul-H':
        Pipette_Gen_Vols.append('10')
    elif Tray=='tiprack-100ul':
        Pipette_Gen_Vols.append('100')
    elif Tray=='tiprack-200ul':
        Pipette_Gen_Vols.append('200')
    elif Tray=='tiprack-250ul':
        Pipette_Gen_Vols.append('250')
    else:
        Pipette_Gen_Vols.append('1000')
    disp_height = round(float(Dispense_Height_Entry.get()),8)
    # Change variable 'Tip_Setup' so that this function is skipped for other tips trays detected
    Tip_Setup +=1
    # Increase variable 'number' so that next cell is run through the Inputs function
    number += 1
    return Inputs(number)

def ByUniform(number,Tray):
    try:
        for i in Inputs_List:
            try:
                i.grid_remove()
            except:
                pass
    except:
        pass
    Opentron_Image.config(file="OTUniformBackground.png")
    # LABELS
    In_Out_Tray_Label.grid(row=Row_Label_Row, column = Tray_Label_column,columnspan=1,padx=(100*screen_scaling,0),pady=(70*screen_scaling,0))
    In_Out_Tray_Label.config(text=New_Cells[number][0]+" "+New_Cell_Use[number][0]+" Inputs")
    
    z = 0
    # Row Number
    Row_Label_List[0].grid(row=Row_List[0],column=Row_Label_Column,sticky=N+S+E+W)
    Row_Label_List[0].config(text="All Wells")
    # Volume Column Heading and Input
    Vol_Label_List[0].grid(row=Row24-1,column=Column_List[0]+5,pady=(0,0),sticky=N+S+E+W)
    Vol_List[0].grid(row=Row_List[0],column=Column_List[0]+5,sticky=N+S+E+W)
    
    # Substance Column Heading and Input
    if New_Cell_Use[number][0]=='Ingredients':
        Solvent1_Conc_Label_List[0].config(text='Main Solvent 1 Concentation (%)')
        Solvent1_Conc_Label_List[0].grid(row=Row24-1,column=Column_List[0]+1,sticky=N+S+E+W)
        Solvent1_Conc_List[0].grid(row=Row_List[0],column=Column_List[0]+1,pady=(0,0),sticky=N+S+E+W)
        Ingr_Label_List[0].grid(row=Row24-1,column=Column_List[0],pady=(0,0),sticky=N+S+E+W)
        IngrMenu_List[0].grid(row=Row_List[0],column=Column_List[0],sticky=N+S+E+W)
    elif New_Cell_Use[number]==['Output']:
        Dilu_Label_List[0].grid(row=Row24-1,column=Column_List[0],pady=(0,0),sticky=N+S+E+W)
        DiluMenu_List[0].grid(row=Row_List[0],column=Column_List[0],sticky=N+S+E+W)
        for i in range(input_number,output_number):
            if 'Main Solvent 2' in New_Well_Ingrs[i]:
                Solvent2_Conc_Label_List[0].config(text='Main Solvent 2 Concentation (%)')
                Solvent2_Conc_Label_List[0].grid(row=Row24-1,column=Column_List[0]+2,pady=(0,0),sticky=N+S+E+W)
                Solvent2_Conc_List[0].grid(row=Row_List[0],column=Column_List[0]+2,sticky=N+S+E+W)
            else:
                pass
            if 'Main Solvent 1' in New_Well_Ingrs[i]:
                # Main Solvent 1 Column Heading and Input
                Solvent1_Conc_Label_List[0].config(text='Main Solvent 1 Concentation (%)')
                Solvent1_Conc_Label_List[0].grid(row=Row24-1,column=Column_List[0]+1,pady=(0,0),sticky=N+S+E+W)
                Solvent1_Conc_List[0].grid(row=Row_List[0],column=Column_List[0]+1,sticky=N+S+E+W)
            else:
                pass
            if 'Secondary Solvent 1' in New_Well_Ingrs[i] or 'Secondary Solvent 2' in New_Well_Ingrs[i]:
                SS_Conc_Label_List[0].grid(row=Row24-1,column=Column_List[0]+4,sticky=N+S+E+W)
                SS_Conc_List[0].grid(row=Row_List[0],column=Column_List[0]+4,pady=(0,0),sticky=N+S+E+W)
                SS_Label_List[0].grid(row=Row24-1,column=Column_List[0]+3,pady=(0,0),sticky=N+S+E+W)
                SSMenu_List[0].grid(row=Row_List[0],column=Column_List[0]+3,sticky=N+S+E+W)
            else:
                pass

    button_count = number+1
    button_text = "Pipette Setup"
    while button_count < len(New_Cells):
        if New_Cell_Use[button_count] == ['Ingredients']:
            button_text = "Input Setup"
            button_count = len(New_Cells)
        elif New_Cell_Use[button_count] == ['Output']:
            button_text = "Output Setup"
            button_count = len(New_Cells)
        else:
            button_count +=1
    Next_Button = Button(OT,command = lambda: GetUniform(number,New_Tray_Pos[number]), text = button_text, font =subheading_font,\
                            fg=Continue_fgcolour, bg = Continue_bgcolour)

    return Next_Button.place(x=Continue_x,y=Continue_y,width = Continue_w, height = Continue_h)

def ByColumns(number,Tray): # ASSIGN BY COLUMNS A-P
    
    try:
        for i in Inputs_List:
            try:
                i.grid_remove()
            except:
                pass
            try:
                i.config(padx=(0,0),pady=(0,0))
            except:
                pass
    except:
        pass
    Opentron_Image.config(file="OTColumnsBackground.png")
    # LABELS
    Row_Label_List[0].config(text='1')
    In_Out_Tray_Label.grid(row=Row_Label_Row, column = Tray_Label_column, padx=(50*screen_scaling,0), pady=(50*screen_scaling,20*screen_scaling))
    In_Out_Tray_Label.config(text=New_Cells[number][0]+" "+New_Cell_Use[number][0]+" Inputs")
    Column_Label.grid(row=Row_List[9]-6,column=Row_Label_Column-1, sticky=N+S+E)

    # Set if statement for all trays with columns up to 'H'
    
    for i in New_Tray_Pos[number]:
        if i<193:
            z = i-(i%24)
            Column_Label_List[z].grid(row=Row_List[9]-6,column=Column_List[z],sticky=N+S+E+W)
            # Volume Column Heading and Input
            Vol_Label_List[z].grid(row=Row_List[9]-4,column=Column_List[z]+Sub, pady=(0,0),sticky=N+S+E+W)
            Vol_List[z].grid(row=Row_List[9]-4,column=Column_List[z],sticky=N+S+E+W)

            if New_Cell_Use[number][0]=='Ingredients':
                Ingr_Label_List[z].grid(row=Row_List[9]-5,column=Column_List[z]+Sub,sticky=N+S+E+W)
                IngrMenu_List[z].grid(row=Row_List[9]-5,column=Column_List[z],sticky=N+S+E+W)
                # Main Solvent 1 Column Heading and Input
                Solvent1_Conc_Label_List[z].config(text='Concentation (%)')
                Solvent1_Conc_Label_List[z].grid(row=Row_List[9]-3,column=Column_List[z]+Sub, pady=(0,0),sticky=N+S+E+W)
                Solvent1_Conc_List[z].grid(row=Row_List[9]-3,column=Column_List[z],sticky=N+S+E+W)
            
            elif New_Cell_Use[number]==['Output']:
                Dilu_Label_List[z].grid(row=Row_List[9]-5,column=Column_List[z]+Sub,sticky=N+S+E+W)
                DiluMenu_List[z].grid(row=Row_List[9]-5,column=Column_List[z],sticky=N+S+E+W)
                for i in range(input_number,output_number):
                    if 'Main Solvent 2' in New_Well_Ingrs[i]:
                        Solvent2_Conc_Label_List[z].config(text='Main Solvent 2 Concentation (%)')
                        Solvent2_Conc_Label_List[z].grid(row=Row_List[9]-2,column=Column_List[z]+Sub, pady=(0,0),sticky=N+S+E+W)
                        Solvent2_Conc_List[z].grid(row=Row_List[9]-2,column=Column_List[z],sticky=N+S+E+W)
                    else:
                        pass
                    if 'Main Solvent 1' in New_Well_Ingrs[i]:
                        # Main Solvent 1 Column Heading and Input
                        Solvent1_Conc_Label_List[z].config(text='Main Solvent 1 Concentation (%)')
                        Solvent1_Conc_Label_List[z].grid(row=Row_List[9]-3,column=Column_List[z]+Sub, pady=(0,0),sticky=N+S+E+W)
                        Solvent1_Conc_List[z].grid(row=Row_List[9]-3,column=Column_List[z],sticky=N+S+E+W)
                    else:
                        pass
                    if 'Secondary Solvent 1' in New_Well_Ingrs[i] or 'Secondary Solvent 2' in New_Well_Ingrs[i]:
                        SS_Label_List[z].grid(row=Row_List[9]-1,column=Column_List[z]+Sub,sticky=N+S+E+W)
                        SSMenu_List[z].grid(row=Row_List[9]-1,column=Column_List[z],sticky=N+S+E+W)
                        SS_Conc_Label_List[z].grid(row=Row_List[9],column=Column_List[z]+Sub,sticky=N+S+E+W)
                        SS_Conc_List[z].grid(row=Row_List[9],column=Column_List[z],sticky=N+S+E+W)
                        
                    else:
                        pass
                
        else:
            z = i-(i%24)
            Column_Label2.grid(row=Row_List[0]-6,column=Row_Label_Column-1, sticky=N+S+E)
            Column_Label_List[z].grid(row=Row_List[0]-6,column=Column_List[z],sticky=N+S+E+W)
            # Volume Column Heading and Input
            Vol_Label_List[z+1].grid(row=Row_List[0]-4,column=Column_List[z]+Sub-7, pady=(0,0),sticky=N+S+E+W)
            Vol_List[z].grid(row=Row_List[0]-4,column=Column_List[z],sticky=N+S+E+W)

            if New_Cell_Use[number][0]=='Ingredients':
                Ingr_Label_List[z+1].grid(row=Row_List[0]-5,column=Column_List[z]+Sub-7,sticky=N+S+E+W)
                IngrMenu_List[z].grid(row=Row_List[0]-5,column=Column_List[z],sticky=N+S+E+W)
                # Main Solvent 1 Column Heading and Input
                Solvent1_Conc_Label_List[z+1].config(text='Main Solvent 1 Concentation (%)')
                Solvent1_Conc_Label_List[z+1].grid(row=Row_List[0]-3,column=Column_List[z]+Sub-7, pady=(0,0),sticky=N+S+E+W)
                Solvent1_Conc_List[z].grid(row=Row_List[0]-3,column=Column_List[z],sticky=N+S+E+W)
            elif New_Cell_Use[number]==['Output']:
                Dilu_Label_List[z+1].grid(row=Row_List[0]-5,column=Column_List[z]+Sub-7, pady=(0,0),sticky=N+S+E+W)
                DiluMenu_List[z].grid(row=Row_List[0]-5,column=Column_List[z],sticky=N+S+E+W)
                for i in range(input_number,output_number):
                    if 'Main Solvent 2' in New_Well_Ingrs[i]:
                        Solvent2_Conc_Label_List[z+1].config(text='Main Solvent 2 Concentation (%)')
                        Solvent2_Conc_Label_List[z+1].grid(row=Row_List[0]-2,column=Column_List[z]+Sub-7, pady=(0,0),sticky=N+S+E+W)
                        Solvent2_Conc_List[z].grid(row=Row_List[0]-2,column=Column_List[z],sticky=N+S+E+W)
                    else:
                        pass
                    if 'Main Solvent 1' in New_Well_Ingrs[i]:
                        # Main Solvent 1 Column Heading and Input
                        Solvent1_Conc_Label_List[z+1].config(text='Main Solvent 1 Concentation (%)')
                        Solvent1_Conc_Label_List[z+1].grid(row=Row_List[0]-3,column=Column_List[z]+Sub-7, pady=(0,0),sticky=N+S+E+W)
                        Solvent1_Conc_List[z].grid(row=Row_List[0]-3,column=Column_List[z],sticky=N+S+E+W)
                    else:
                        pass
                    if 'Secondary Solvent 1' in New_Well_Ingrs[i] or 'Secondary Solvent 2' in New_Well_Ingrs[i]:
                        SS_Label_List[z+1].grid(row=Row_List[0]-1,column=Column_List[z]+Sub-7, pady=(0,0),sticky=N+S+E+W)
                        SSMenu_List[z].grid(row=Row_List[0]-1,column=Column_List[z],sticky=N+S+E+W)
                        SS_Conc_Label_List[z+1].grid(row=Row_List[0],column=Column_List[z]+Sub-7, pady=(0,0),sticky=N+S+E+W)
                        SS_Conc_List[z].grid(row=Row_List[0],column=Column_List[z],sticky=N+S+E+W)
                        
                    else:
                        pass
   
    button_text = "Pipette Setup"
    button_count = number+1
    while button_count < len(New_Cells):
        if New_Cell_Use[button_count] == ['Ingredients']:
            button_text = "Next Input Setup"
            button_count = len(New_Cells)
        elif New_Cell_Use[button_count] == ['Output']:
            button_text = "Next Output Setup"
            button_count = len(New_Cells)
        else:
            button_count +=1
    
    Next_Button = Button(OT,command = lambda: GetColumns(number,New_Tray_Pos[number]), text = button_text, font =subheading_font,\
                            fg=Continue_fgcolour, bg = Continue_bgcolour)
    
    return Next_Button.place(x=Continue_x,y=Continue_y,width = Continue_w, height = Continue_h)




def ByRows(number,Tray): # ASSIGN BY ROWS 1-24
    try:
        for i in Inputs_List:
            try:
                i.grid_remove()
            except:
                pass
    except:
        pass
    Opentron_Image.config(file="OTRowsBackground.png")
    
    In_Out_Tray_Label.grid(row=Row24-1, column = Tray_Label_column, columnspan=1, padx=(100*screen_scaling,20*screen_scaling),pady=(40*screen_scaling,0))
    In_Out_Tray_Label.config(text=New_Cells[number][0]+" "+New_Cell_Use[number][0]+" Inputs")
    Row_Label_List[0].config(text='1')
    Row_Label.grid(row=Row24-1,column=Row_Label_Column, pady=(40*screen_scaling,0), padx=(0,0), sticky=N+S+E+W)

    for i in New_Tray_Pos[number]:
        z = i - int(round(i/24,0)*24)
        # Row Number
        Row_Label_List[z].grid(row=Row_List[z],column=Row_Label_Column, padx=(0,0),pady=(0,0) ,sticky=N+S+E+W)
        # Volume Column Heading and Input
        Vol_Label_List[z].grid(row=Row24-1,column=Column_List[0]+1, pady=(40*screen_scaling,0),sticky=N+S+E+W)
        Vol_List[z].grid(row=Row_List[z],column=Column_List[0]+1,sticky=N+S+E+W)
        
        # Substance Column Heading and Input
        if New_Cell_Use[number][0]=='Ingredients':
            Ingr_Label_List[z].grid(row=Row24-1,column=Column_List[0], pady=(40*screen_scaling,0),sticky=N+S+E+W)
            IngrMenu_List[z].grid(row=Row_List[z],column=Column_List[0],sticky=N+S+E+W)
            # Main Solvent 1 Column Heading and Input
            Solvent1_Conc_Label_List[z].config(text='Main Solvent 1 Concentation (%)')
            Solvent1_Conc_Label_List[z].grid(row=Row24-1,column=Column_List[0]+2, pady=(40*screen_scaling,0),sticky=N+S+E+W)
            Solvent1_Conc_List[z].grid(row=Row_List[z],column=Column_List[0]+2,sticky=N+S+E+W)
        elif New_Cell_Use[number]==['Output']:
            Dilu_Label_List[z].grid(row=Row24-1,column=Column_List[0], pady=(40*screen_scaling,0),sticky=N+S+E+W)
            DiluMenu_List[z].grid(row=Row_List[z],column=Column_List[0],sticky=N+S+E+W)
            for j in range(input_number,output_number):
                if 'Main Solvent 2' in New_Well_Ingrs[j]:
                    Solvent2_Conc_Label_List[z].config(text='Main Solvent 2 Concentation (%)')
                    Solvent2_Conc_Label_List[z].grid(row=Row24-1,column=Column_List[0]+3, pady=(40*screen_scaling,0),sticky=N+S+E+W)
                    Solvent2_Conc_List[z].grid(row=Row_List[z],column=Column_List[0]+3,sticky=N+S+E+W)
                else:
                    pass
                if 'Main Solvent 1' in New_Well_Ingrs[j]:
                    # Main Solvent 1 Column Heading and Input
                    Solvent1_Conc_Label_List[z].config(text='Main Solvent 1 Concentation (%)')
                    Solvent1_Conc_Label_List[z].grid(row=Row24-1,column=Column_List[0]+2, pady=(40*screen_scaling,0),sticky=N+S+E+W)
                    Solvent1_Conc_List[z].grid(row=Row_List[z],column=Column_List[0]+2,sticky=N+S+E+W)
                else:
                    pass
                if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                    SS_Label_List[z].grid(row=Row24-1,column=Column_List[0]+4, pady=(40*screen_scaling,0),sticky=N+S+E+W)
                    SSMenu_List[z].grid(row=Row_List[z],column=Column_List[0]+4,sticky=N+S+E+W)
                    SS_Conc_Label_List[z].grid(row=Row24-1,column=Column_List[0]+5, pady=(40*screen_scaling,0),sticky=N+S+E+W)
                    SS_Conc_List[z].grid(row=Row_List[z],column=Column_List[0]+5,sticky=N+S+E+W)
                else:
                    pass

    button_count = number+1
    button_text = "Pipette Setup"
    while button_count < len(New_Cells):
        if New_Cell_Use[button_count] == ['Ingredients']:
            button_text = "Input Setup"
            button_count = len(New_Cells)
        elif New_Cell_Use[button_count] == ['Output']:
            button_text = "Output Setup"
            button_count = len(New_Cells)
        else:
            button_count +=1

    Next_Button = Button(OT,command = lambda: GetRows(number,New_Tray_Pos[number]), text = button_text, font =subheading_font,\
                            fg=Continue_fgcolour, bg = Continue_bgcolour)

    return Next_Button.place(x=Continue_x,y=Continue_y,width = Continue_w, height = Continue_h)

    
def ByWells(number,Tray,Wells): #ASSIGN INDIVIDUAL WELLS
    try:
        for i in Inputs_List:
            try:
                i.grid_remove()
            except:
                pass
            try:
                i.config(padx=(0,0),pady=(0,0))
            except:
                pass
    except:
        pass            
    Opentron_Image.config(file="OTIndBackground.png")
    In_Out_Tray_Label.grid(row=Row_Label_Row, column = Row_Label_Column, columnspan = 3, padx=(45*screen_scaling,0),pady=(50*screen_scaling,0),sticky=N+S+W)
    In_Out_Tray_Label.config(text=New_Cells[number][0]+" "+New_Cell_Use[number][0]+" Inputs")
    Row_Label_List[0].config(text='1')
    Row_Label.grid(row=Row_Label_Row+1,column=Row_Label_Column, padx=(100*screen_scaling,0), pady=(0,0),sticky=N+S+E+W)
    Column_Label.grid(row=Row1+2,column=Row_Label_Column, padx=(100*screen_scaling,0), sticky=N+S+E+W)
    
    
    # PLACE ALL INPUTS RELEVANT TO SELECTED TRAY
        
    button_text = "Pipette Setup"
    button_count = number+1
    while button_count < len(New_Cells):
        if New_Cell_Use[button_count] == ['Ingredients']:
            button_text = "Next Input Setup"
            button_count = len(New_Cells)
        elif New_Cell_Use[button_count] == ['Output']:
            button_text = "Next Output Setup"
            button_count = len(New_Cells)
        else:
            button_count +=1

    # LARGE TRAYS - DIVERTED TO LARGETRAYS() 
    if Tray==['96-deep-well'] or Tray==['96-flat'] or Tray==['96-PCR-flat'] or Tray==['96-PCR-tall'] or Tray==['96-well-plate-20mm']\
           or Tray==['e-gelgol'] or Tray==['hampton-1ml-deep-block'] or Tray==['PCR-strip-tall']\
           or Tray==['rigaku-compact-crystallization-plate']\
           or Tray==['384-plate'] or Tray==['MALDI-plate']:
        for i in Wells:          
            if i <=174:
                if '7' in All_pos[i] or '8' in All_pos[i] or '9' in All_pos[i] or '10' in All_pos[i] or '11' in All_pos[i] or '12' in All_pos[i]\
                    or '13' in All_pos[i] or '14' in All_pos[i] or '15' in All_pos[i] or '16' in All_pos[i]\
                     or '17' in All_pos[i]or '18' in All_pos[i] or '19' in All_pos[i] or '20' in All_pos[i]\
                      or '21' in All_pos[i] or '22' in All_pos[i] or '23' in All_pos[i] or '24' in All_pos[i]:
                    pass
                else:
                    Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
                    Row_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
                    # Volume Label and Input
                    Vol_Label_List[i].grid(row=Row_List[i]-4,column=Row_Label_Column+Sub, pady=(0,0), padx=(0,0), sticky=N+S+E+W)
                    Vol_List[i].grid(row=Row_List[i]-4,column=Column_List[i],sticky=N+S+E+W)
                    
                    if New_Cell_Use[number][0]=='Ingredients':
                        Ingr_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        IngrMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                        # Main Solvent 1 Label and Input
                        Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                        Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub, pady=(0,0), padx=(0,0),sticky=N+S+E+W)
                        Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                    elif New_Cell_Use[number]==['Output']:
                        Dilu_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        DiluMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                        for j in range(input_number,output_number):
                            if 'Main Solvent 2' in New_Well_Ingrs[j]:
                                Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                                Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub, pady=(0,0), padx=(0,0),sticky=N+S+E+W)
                                Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                            else:
                                pass
                            if 'Main Solvent 1' in New_Well_Ingrs[j]:
                                # Main Solvent 1 Label and Input
                                Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub, pady=(0,0), padx=(0,0),sticky=N+S+E+W)
                                Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                            else:
                                pass
                            if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                                SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                                SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub, pady=(0,0), padx=(0,0),sticky=N+S+E+W)
                                SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                            else:
                                pass
                        
        if Tray==['384-plate'] or Tray==['MALDI-plate']:
            window_count = 1
        else:
            window_count = 2
        Next_Button = Button(OT,command = lambda: LargeTrays(number,Tray,Wells,window_count), text = "Next Wells", font =subheading_font,\
                            fg=Continue_fgcolour, bg = Continue_bgcolour)

    # SMALL TRAYS
    else:
        for i in Wells:
            Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
            Row_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
            # Volume Label and Input
            Vol_Label_List[i].grid(row=Row_List[i]-4,column=Row_Label_Column+Sub,sticky=N+S+E+W)
            Vol_List[i].grid(row=Row_List[i]-4,column=Column_List[i],sticky=N+S+E+W)
            
            if New_Cell_Use[number][0]=='Ingredients':
                Ingr_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                IngrMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                # Main Solvent 1 Label and Input
                Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
            elif New_Cell_Use[number]==['Output']:
                Dilu_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                DiluMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                for j in range(input_number,output_number):
                    if 'Main Solvent 2' in New_Well_Ingrs[j]:
                        Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                        Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                    else:
                        pass
                    if 'Main Solvent 1' in New_Well_Ingrs[j]:
                        # Main Solvent 1 Label and Input
                        Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                        Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                    else:
                        pass
                    if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                        SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                        SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                    else:
                        pass
        
        Next_Button = Button(OT,command = lambda: GetWells(number,New_Tray_Pos[number]), text = button_text, font =subheading_font,\
                                fg=Continue_fgcolour, bg = Continue_bgcolour)

    return Next_Button.place(x=Continue_x,y=Continue_y,width = Continue_w, height = Continue_h)
    


def LargeTrays(number,Tray,Wells,window_count):
    for i in Inputs_List:
        try:
            i.grid_remove()
        except:
            pass
    In_Out_Tray_Label.grid(row=Row_Label_Row, column = Row_Label_Column, columnspan = 3, padx=(45*screen_scaling,0),pady=(50*screen_scaling,0),sticky=N+S+W)
    In_Out_Tray_Label.config(text=New_Cells[number][0]+" "+New_Cell_Use[number][0]+" Inputs")
    Row_Label_List[0].config(text='1')
    Row_Label.grid(row=Row_Label_Row+1,column=Row_Label_Column, padx=(100*screen_scaling,0), pady=(0,0),sticky=N+S+E+W)
    Column_Label.grid(row=Row1+2,column=Row_Label_Column, padx=(100*screen_scaling,0), sticky=N+S+E+W)
    if window_count==1 or window_count==3 or window_count==5 or window_count==7:
        for i in Wells:
            if 'A' in All_pos[i] or 'B' in All_pos[i] or 'C' in All_pos[i] or 'D' in All_pos[i]\
             or 'E' in All_pos[i] or 'F' in All_pos[i] or 'G' in All_pos[i] or 'H' in All_pos[i]:
                pass
            else:
                if window_count==1:
                    if '7' in All_pos[i] or '8' in All_pos[i] or '9' in All_pos[i] or '10' in All_pos[i] or '11' in All_pos[i]\
                     or '12' in All_pos[i] or '13' in All_pos[i] or '14' in All_pos[i] or '15' in All_pos[i]\
                      or '16' in All_pos[i] or '17' in All_pos[i]or '18' in All_pos[i] or '19' in All_pos[i]\
                       or '20' in All_pos[i] or '21' in All_pos[i] or '22' in All_pos[i] or '23' in All_pos[i]\
                        or '24' in All_pos[i]:
                        pass
                    else:
                        Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
                        Row_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
                        # Volume Label and Input
                        Vol_Label_List[i].grid(row=Row_List[i]-4,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        Vol_List[i].grid(row=Row_List[i]-4,column=Column_List[i],sticky=N+S+E+W)
                        
                        if New_Cell_Use[number][0]=='Ingredients':
                            Ingr_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            IngrMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                            # Main Solvent 1 Label and Input
                            Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                            Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                        elif New_Cell_Use[number]==['Output']:
                            Dilu_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            DiluMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                            for j in range(input_number,output_number):
                                if 'Main Solvent 2' in New_Well_Ingrs[j]:
                                    Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                                    Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Main Solvent 1' in New_Well_Ingrs[j]:
                                    # Main Solvent 1 Label and Input
                                    Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                    Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                                    SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                                    SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                elif window_count==3:
                    if '7' in All_pos[i] or '8' in All_pos[i] or '9' in All_pos[i] or '10' in All_pos[i] or '11' in All_pos[i]\
                     or '12' in All_pos[i]:
                        if '17' in All_pos[i] or '18' in All_pos[i] or '19' in All_pos[i]:
                            pass
                        else:
                            Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
                            Row_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
                            # Volume Label and Input
                            Vol_Label_List[i].grid(row=Row_List[i]-4,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            Vol_List[i].grid(row=Row_List[i]-4,column=Column_List[i],sticky=N+S+E+W)
                            
                            if New_Cell_Use[number][0]=='Ingredients':
                                Ingr_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                IngrMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                                # Main Solvent 1 Label and Input
                                Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                            elif New_Cell_Use[number]==['Output']:
                                Dilu_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                DiluMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                                for j in range(input_number,output_number):
                                    if 'Main Solvent 2' in New_Well_Ingrs[j]:
                                        Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                                        Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                        Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                                    else:
                                        pass
                                    if 'Main Solvent 1' in New_Well_Ingrs[j]:
                                        # Main Solvent 1 Label and Input
                                        Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                        Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                        Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                                    else:
                                        pass
                                    if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                                        SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                        SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                                        SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                        SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                                    else:
                                        pass
                    else:
                        pass
                elif window_count==5:
                    if  '13' in All_pos[i] or '14' in All_pos[i] or '15' in All_pos[i] or '16' in All_pos[i] or '17' in All_pos[i]\
                       or '18' in All_pos[i]:
                        Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
                        Row_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
                        # Volume Label and Input
                        Vol_Label_List[i].grid(row=Row_List[i]-4,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        Vol_List[i].grid(row=Row_List[i]-4,column=Column_List[i],sticky=N+S+E+W)
                        
                        if New_Cell_Use[number][0]=='Ingredients':
                            Ingr_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            IngrMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                            # Main Solvent 1 Label and Input
                            Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                            Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                        elif New_Cell_Use[number]==['Output']:
                            Dilu_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            DiluMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                            for j in range(input_number,output_number):
                                if 'Main Solvent 2' in New_Well_Ingrs[j]:
                                    Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                                    Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Main Solvent 1' in New_Well_Ingrs[j]:
                                    # Main Solvent 1 Label and Input
                                    Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                    Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                                    SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                                    SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                    else:
                        pass
                else:
                    if '19' in All_pos[i] or '20' in All_pos[i] or '21' in All_pos[i] or '22' in All_pos[i] or '23' in All_pos[i] or '24' in All_pos[i]:
                        Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
                        Row_Label_List[i].grid(row=Row_List[i-5]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
                        # Volume Label and Input
                        Vol_Label_List[i].grid(row=Row_List[i-5]-4,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        Vol_List[i].grid(row=Row_List[i-5]-4,column=Column_List[i],sticky=N+S+E+W)
                        
                        if New_Cell_Use[number][0]=='Ingredients':
                            Ingr_Label_List[i].grid(row=Row_List[i-5]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            IngrMenu_List[i].grid(row=Row_List[i-5]-5,column=Column_List[i],sticky=N+S+E+W)
                            # Main Solvent 1 Label and Input
                            Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                            Solvent1_Conc_Label_List[i].grid(row=Row_List[i-5]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            Solvent1_Conc_List[i].grid(row=Row_List[i-5]-3,column=Column_List[i],sticky=N+S+E+W)
                        elif New_Cell_Use[number]==['Output']:
                            Dilu_Label_List[i].grid(row=Row_List[i-5]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            DiluMenu_List[i].grid(row=Row_List[i-5]-5,column=Column_List[i],sticky=N+S+E+W)
                            for j in range(input_number,output_number):
                                if 'Main Solvent 2' in New_Well_Ingrs[j]:
                                    Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                                    Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Main Solvent 1' in New_Well_Ingrs[j]:
                                    # Main Solvent 1 Label and Input
                                    Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                    Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                                    SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                                    SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass                             
        window_count += 1
        Next_Button = Button(OT,command = lambda: LargeTrays(number,Tray,Wells,window_count), text = "Next Wells", font =subheading_font,\
                    fg=Continue_fgcolour, bg = Continue_bgcolour)
        Next_Button.place(x=Continue_x,y=Continue_y,width = Continue_w, height = Continue_h)

    elif window_count == 2 or window_count==4 or window_count==6:
        for i in Wells:
            if 'A' in All_pos[i] or 'B' in All_pos[i] or 'C' in All_pos[i] or 'D' in All_pos[i]\
             or 'E' in All_pos[i] or 'F' in All_pos[i] or 'G' in All_pos[i] or 'H' in All_pos[i]:
                if window_count==2:
                    if '7' in All_pos[i] or '8' in All_pos[i] or '9' in All_pos[i] or '10' in All_pos[i] or '11' in All_pos[i]\
                     or '12' in All_pos[i]:
                        if '17' in All_pos[i] or '18' in All_pos[i] or '19' in All_pos[i]:
                            pass
                        else:
                            Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
                            Row_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
                            # Volume Label and Input
                            Vol_Label_List[i].grid(row=Row_List[i]-4,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            Vol_List[i].grid(row=Row_List[i]-4,column=Column_List[i],sticky=N+S+E+W)
                            
                            Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                            if New_Cell_Use[number][0]=='Ingredients':
                                Ingr_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                IngrMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                                # Main Solvent 1 Label and Input
                                Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            elif New_Cell_Use[number]==['Output']:
                                Dilu_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                DiluMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                                for j in range(input_number,output_number):
                                    if 'Main Solvent 2' in New_Well_Ingrs[j]:
                                        Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                                        Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                        Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                                    else:
                                        pass
                                    if 'Main Solvent 1' in New_Well_Ingrs[j]:
                                        # Main Solvent 1 Label and Input
                                        Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                        Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                        Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                                    else:
                                        pass
                                    if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                                        SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                        SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                                        SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                        SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                                    else:
                                        pass
                    else:
                        pass
                elif window_count==4:
                    if '13' in All_pos[i] or '14' in All_pos[i] or '15' in All_pos[i] or '16' in All_pos[i]\
                       or '17' in All_pos[i] or '18' in All_pos[i]:
                        Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
                        Row_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
                        # Volume Label and Input
                        Vol_Label_List[i].grid(row=Row_List[i]-4,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        Vol_List[i].grid(row=Row_List[i]-4,column=Column_List[i],sticky=N+S+E+W)
                        
                        if New_Cell_Use[number][0]=='Ingredients':
                            Ingr_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            IngrMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                            # Main Solvent 1 Label and Input
                            Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                            Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                        elif New_Cell_Use[number]==['Output']:
                            Dilu_Label_List[i].grid(row=Row_List[i]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            DiluMenu_List[i].grid(row=Row_List[i]-5,column=Column_List[i],sticky=N+S+E+W)
                            for j in range(input_number,output_number):
                                if 'Main Solvent 2' in New_Well_Ingrs[j]:
                                    Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                                    Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Main Solvent 1' in New_Well_Ingrs[j]:
                                    # Main Solvent 1 Label and Input
                                    Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                    Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                                    SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                                    SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                    else:
                        pass
                else:
                    if '19' in All_pos[i] or '20' in All_pos[i] or '21' in All_pos[i] or '22' in All_pos[i] or '23' in All_pos[i] or '24' in All_pos[i]:
                        Column_Label_List[i].grid(row=Row1+2,column=Column_List[i],sticky=N+S+E+W)
                        Row_Label_List[i].grid(row=Row_List[i-5]-5,column=Row_Label_Column, padx=(100*screen_scaling,0),sticky=N+S+E+W)
                        # Volume Label and Input
                        Vol_Label_List[i].grid(row=Row_List[i-5]-4,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                        Vol_List[i].grid(row=Row_List[i-5]-4,column=Column_List[i],sticky=N+S+E+W)
                        
                        if New_Cell_Use[number][0]=='Ingredients':
                            Ingr_Label_List[i].grid(row=Row_List[i-5]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            IngrMenu_List[i].grid(row=Row_List[i-5]-5,column=Column_List[i],sticky=N+S+E+W)
                            # Main Solvent 1 Label and Input
                            Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                            Solvent1_Conc_Label_List[i].grid(row=Row_List[i-5]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            Solvent1_Conc_List[i].grid(row=Row_List[i-5]-3,column=Column_List[i],sticky=N+S+E+W)
                        elif New_Cell_Use[number]==['Output']:
                            Dilu_Label_List[i].grid(row=Row_List[i-5]-5,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                            DiluMenu_List[i].grid(row=Row_List[i-5]-5,column=Column_List[i],sticky=N+S+E+W)
                            for j in range(input_number,output_number):
                                if 'Main Solvent 2' in New_Well_Ingrs[j]:
                                    Solvent2_Conc_Label_List[i].config(text='Main Solvent 2 Concentation (%)')
                                    Solvent2_Conc_Label_List[i].grid(row=Row_List[i]-2,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent2_Conc_List[i].grid(row=Row_List[i]-2,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Main Solvent 1' in New_Well_Ingrs[j]:
                                    # Main Solvent 1 Label and Input
                                    Solvent1_Conc_Label_List[i].config(text='Main Solvent 1 Concentation (%)')
                                    Solvent1_Conc_Label_List[i].grid(row=Row_List[i]-3,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    Solvent1_Conc_List[i].grid(row=Row_List[i]-3,column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                                if 'Secondary Solvent 1' in New_Well_Ingrs[j] or 'Secondary Solvent 2' in New_Well_Ingrs[j]:
                                    SS_Label_List[i].grid(row=Row_List[i]-1,column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SSMenu_List[i].grid(row=Row_List[i]-1,column=Column_List[i],sticky=N+S+E+W)
                                    SS_Conc_Label_List[i].grid(row=Row_List[i],column=Row_Label_Column+Sub,sticky=N+S+E+W)
                                    SS_Conc_List[i].grid(row=Row_List[i],column=Column_List[i],sticky=N+S+E+W)
                                else:
                                    pass
                    else:
                        pass
            else:
                pass
        if Tray==['384-plate'] or Tray==['MALDI-plate']:
            window_count += 1
        else:
            window_count += 2

        if Tray==['96-deep-well'] or Tray==['96-flat'] or Tray==['96-PCR-flat'] or Tray==['96-PCR-tall']\
           or Tray==['96-well-plate-20mm'] or Tray==['e-gelgol'] or Tray==['hampton-1ml-deep-block'] or Tray==['PCR-strip-tall']:
            window_count=10
        else:
            pass
        
        Next_Button = Button(OT,command=lambda: LargeTrays(number,Tray,Wells,window_count), text="Next Wells", font=subheading_font,\
                    fg=Continue_fgcolour, bg=Continue_bgcolour)
        Next_Button.place(x=Continue_x, y=Continue_y, width = Continue_w, height=Continue_h)
    else:
        GetWells(number,New_Tray_Pos[number])

def Pipette_Setup(number,Tray):
    global Tip_Setup
    for i in Inputs_List:
        try:
            i.grid_remove()
        except:
            pass
    global Pipette1_Type, Pipette2_Type, Axis_Heading, Type_Heading, Type1_Label, Type2_Label, Pipette1_Label,\
           Pipette1_Type1, Pipette1_Type2, Pipette2_Label, Pipette2_Type1, Pipette2_Type2, Speed_Heading, \
           Aspirate_Heading, Dispense_Heading, Pippett1_Aspirate_Entry,\
           Pippett1_Dispense_Entry, Pippett2_Aspirate_Entry, Pippett2_Dispense_Entry,\
           Parameters_Label, Dispense_Height_Label, Dispense_Height_Entry, Pipette_List
    Opentron_Image.config(file="OTPipsBackground.png")
    # Label the Cell being
    In_Out_Tray_Label.grid(row=Row_Label_Row, column = Tray_Label_column,columnspan=1, padx=(200*screen_scaling,0), pady=(70*screen_scaling,0))
    In_Out_Tray_Label.config(text="Pipetting Setup",font = heading_font)
    # Creates integer variable that determines Pipette type, 1 = positive displacement, 2 = air pressure.
    # Default set to positive displacement
    Pipette1_Type = IntVar()
    Pipette1_Type.set(1)
    Pipette2_Type = IntVar()
    Pipette2_Type.set(1)
    # Type Heading and Types Labels
    Axis_Heading = Label(OT, text="Axis:", font=heading_font, bg=bgcolour)
    Axis_Heading.grid(row=Row24-1, column=Row_Label_Column, sticky=N+S+E)
    Type_Heading = Label(OT, text="Type:", font=subheading_font, fg='purple',bg=bgcolour)
    Type_Heading.grid(row=Row24, column=Row_Label_Column, sticky=N+S+W)
    Type1_Label = Label(OT, text="    Positive Displacement", font=small_font, bg=bgcolour)
    Type2_Label = Label(OT, text="    Air-Driven Pipette", font=small_font, bg=bgcolour)
    Type1_Label.grid(row=Row23, column=Row_Label_Column, sticky=N+S+W)
    Type2_Label.grid(row=Row22, column=Row_Label_Column, sticky=N+S+W)

    # pipette 1 and 2 headings and Type selection buttons
    Pipette1_Label = Label(OT, text="A (Pipette #1)", font=subheading_font, fg='purple',bg=bgcolour)
    Pipette1_Label.grid(row=Row24-1, column=Col_A, padx=(20*screen_scaling,0), sticky=N+S+E+W)
    Pipette1_Type1 = Radiobutton(OT, variable=Pipette1_Type, value=1, bg=bgcolour)
    Pipette1_Type1.grid(row=Row23, column=Col_A, sticky=N+S+E+W)
    Pipette1_Type2 = Radiobutton(OT, variable=Pipette1_Type, value=2, bg=bgcolour)
    Pipette1_Type2.grid(row=Row22, column=Col_A, sticky=N+S+E+W)
    
    Pipette2_Label = Label(OT, text="B (Pipette #2)", font=subheading_font, fg='purple',bg=bgcolour)
    Pipette2_Label.grid(row=Row24-1, column=Col_B, padx=(20*screen_scaling,0), sticky=N+S+E+W)
    Pipette2_Type1 = Radiobutton(OT, variable=Pipette2_Type, value=1, bg=bgcolour)
    Pipette2_Type1.grid(row=Row23, column=Col_B)
    Pipette2_Type2 = Radiobutton(OT, variable=Pipette2_Type, value=2, bg=bgcolour)
    Pipette2_Type2.grid(row=Row22, column=Col_B)
    # Pipetting Speeds labels and entries
    Speed_Heading = Label(OT, text="Pipetting Speed:", font=subheading_font, fg='purple',bg=bgcolour)
    Aspirate_Heading = Label(OT, text="   Aspirate", font=small_font, bg=bgcolour)
    Dispense_Heading = Label(OT, text="   Dispense", font=small_font, bg=bgcolour)
    Speed_Heading.grid(row=Row18, column=Row_Label_Column,sticky=N+S+W)
    Aspirate_Heading.grid(row=Row17, column=Row_Label_Column,sticky=N+S+W)
    Dispense_Heading.grid(row=Row16, column=Row_Label_Column,sticky=N+S+W)
    Pippett1_Aspirate_Entry = Entry()
    Pippett1_Aspirate_Entry.insert(0,400)
    Pippett1_Dispense_Entry = Entry()
    Pippett1_Dispense_Entry.insert(0,800)
    Pippett2_Aspirate_Entry = Entry()
    Pippett2_Aspirate_Entry.insert(0,400)
    Pippett2_Dispense_Entry = Entry()
    Pippett2_Dispense_Entry.insert(0,800)
    Pippett1_Aspirate_Entry.grid(row=Row17, column=Col_A, sticky=N+S+E+W)
    Pippett1_Dispense_Entry.grid(row=Row16, column=Col_A, sticky=N+S+E+W)
    Pippett2_Aspirate_Entry.grid(row=Row17, column=Col_B, sticky=N+S+E+W)
    Pippett2_Dispense_Entry.grid(row=Row16, column=Col_B, sticky=N+S+E+W)
    Parameters_Label = Label(OT, text="Parameters:", font=subheading_font, fg='purple',bg=bgcolour)
    Parameters_Label.grid(row=Row15, column=Row_Label_Column, sticky=N+S+W)
    Dispense_Height_Label = Label(OT, text="Dispensing Height Above Calibration", font=small_font, bg=bgcolour)
    Dispense_Height_Label.grid(row=Row14, column=Row_Label_Column, sticky=N+S+W)
    Dispense_Height_Entry  = Entry()
    Dispense_Height_Entry.insert(0,3)
    Dispense_Height_Entry.grid(row=Row14, column=Col_A, sticky=N+S+E+W)
    # List of all new features for easy removal loop
    Pipette_List = [In_Out_Tray_Label, Axis_Heading, Type_Heading, Type1_Label, Type2_Label, Pipette1_Label,\
                   Pipette1_Type1, Pipette1_Type2, Pipette2_Label, Pipette2_Type1, Pipette2_Type2,\
                   Speed_Heading, Aspirate_Heading, Dispense_Heading, Pippett1_Aspirate_Entry,\
                   Pippett1_Dispense_Entry, Pippett2_Aspirate_Entry, Pippett2_Dispense_Entry,
                   Parameters_Label, Dispense_Height_Label,Dispense_Height_Entry]
    
    # Button to continue
    Next_Button = Button(OT, command=lambda: Pipette_Parameters(number,Tray), text="Finish", font=subheading_font,\
                fg=Continue_fgcolour, bg=Continue_bgcolour)
    
    return Next_Button.place(x=Continue_x, y=Continue_y, width=Continue_w, height=Continue_h)

def Custom_Store(Custom_Number):
    pos_Custom = []
    grid1 = CS_Grid1_Entry.get()
    grid2 = CS_Grid2_Entry.get()
    spacing1 = CS_Spacing1_Entry.get()
    spacing2 = CS_Spacing2_Entry.get()
    diameter = CS_Diameter_Entry.get()
    depth = CS_Depth_Entry.get()
    Customs_Create.append("containers.create('"+New_Models[Custom_Number][0]+"', grid=("+grid1+", "+grid1+"), spacing=("+spacing1+", "+spacing2+"), diameter="+diameter+", depth="+depth+")")
    for i in range(0,int(grid1)):
        for j in range(0,int(grid2)):
            position = str(i+i*23+j)
            position = int(position)
            pos_Custom.append(pos_5[position])
    Tray_Pos[Custom_Number]=pos_Custom
    New_Tray_Pos[Custom_Number]=pos_Custom
    for h in Tray_Pos[Custom_Number]:
        Well_Names[Custom_Number].append(All_pos[h])
    CS.destroy()
    return Inputs(Custom_Number)
    
def Custom_Setup(Custom_Number):
    global CS, CS_Setup_Label1, CS_Grid1_Entry, CS_Grid2_Entry, CS_Spacing1_Entry, CS_Spacing2_Entry, CS_Diameter_Entry, CS_Depth_Entry
    New_Models[Custom_Number][0]='Custom'+str(Custom_Number)
    CS = Tk()
    CSw = 1360
    CSh = 185
    CS.geometry("%sx%s" % (CSw,CSh))
    CS.config(bg=bgcolour)
    CS_Label = Label(CS, text = "Custom Tray Setup", font = heading_font, fg='black',bg=bgcolour)
    CS_Space1 = Label(CS, text = "     ", font = small_font, fg='black',bg=bgcolour)
    CS_Space2 = Label(CS, text = "      ", font = small_font, fg='black',bg=bgcolour)
    CS_Setup_Label1 = Label(CS, text = "containers.create('Custom"+str(Custom_Number)+"',", font = small_font, fg=Cell_colour,bg=bgcolour)
    CS_Setup_Label2 = Label(CS, text = "grid=(", font = small_font, fg=Cell_colour,bg=bgcolour)
    CS_Grid1_Entry = Entry(CS)
    CS_Setup_Label3 = Label(CS, text = ",", font = small_font, fg=Cell_colour,bg=bgcolour)
    CS_Grid2_Entry = Entry(CS)
    CS_Setup_Label4 = Label(CS, text = "), spacing=(", font = small_font, fg=Cell_colour,bg=bgcolour)
    CS_Spacing1_Entry = Entry(CS)
    CS_Setup_Label5 = Label(CS, text = ",", font = small_font, fg=Cell_colour,bg=bgcolour)
    CS_Spacing2_Entry = Entry(CS)
    CS_Setup_Label8 = Label(CS, text = "), diameter=", font = small_font, fg=Cell_colour,bg=bgcolour)
    CS_Diameter_Entry = Entry(CS)
    CS_Setup_Label9 = Label(CS, text = ", depth=", font = small_font, fg=Cell_colour,bg=bgcolour)
    CS_Depth_Entry = Entry(CS)
    CS_Setup_Label10 = Label(CS, text = ")", font = small_font, fg=Cell_colour,bg=bgcolour)

    CS_Label.grid(row=0,column=1, columnspan=3, sticky=N+S+W)
    CS_Space1.grid(row=1,column=0, sticky=N+S+W)
    CS_Setup_Label1.grid(row=2,column=1, sticky=N+S+W)
    CS_Setup_Label2.grid(row=2,column=2, sticky=N+S+W)
    CS_Grid1_Entry.grid(row=2,column=3, sticky=N+S+E+W)
    CS_Setup_Label3.grid(row=2,column=4, sticky=N+S+W)
    CS_Grid2_Entry.grid(row=2,column=5, sticky=N+S+E+W)
    CS_Setup_Label4.grid(row=2,column=6, sticky=N+S+W)
    CS_Spacing1_Entry.grid(row=2,column=7, sticky=N+S+E+W)
    CS_Setup_Label5.grid(row=2,column=8, sticky=N+S+W)
    CS_Spacing2_Entry.grid(row=2,column=9, sticky=N+S+E+W)
    CS_Setup_Label8.grid(row=2,column=10, sticky=N+S+W)
    CS_Diameter_Entry.grid(row=2,column=11, sticky=N+S+E+W)
    CS_Setup_Label9.grid(row=2,column=12, sticky=N+S+W)
    CS_Depth_Entry.grid(row=2,column=13, sticky=N+S+E+W)
    CS_Setup_Label10.grid(row=2,column=14, sticky=N+S+W)
    CS_Space2.grid(row=3,column=0, sticky=N+S+W)
    Next_Button = Button(CS,command=lambda: Custom_Store(Custom_Number), text="Store Tray", font=subheading_font,\
                fg=Continue_fgcolour, bg=Continue_bgcolour)
    Next_Button.grid(row=4, column = 13, sticky=N+S+E+W)

def DefineWells():
    
    global limit, filename, Mode, Tray_Pic, In_Margin, Mix_Margin
    Defaults_Button.destroy()
    Restore_Defaults_Button.destroy()
    filename = File_Name.get()
    In_Margin = int(In_Margin_Entry.get())
    Mix_Margin = int(Mix_Margin_Entry.get())
    
    # GET 1ST CELLS
    Cells.append([Input_Cell1.get()])
    Cells.append([Mixing_Cell1.get()])
    Cells.append([Output_Cell1.get()])
    Cells.append([Tips_Cell1.get()])
    Cells.append([Trash_Cell1.get()])

    # GET 1ST MODELS
    Models.append([Input_Model1.get()])
    Models.append([Mixing_Model1.get()])
    Models.append([Output_Model1.get()])
    Models.append([Tips_Model1.get()])
    Models.append([Trash_Model1.get()])
    
    # GET ADDITIONAL CELL 1
    Cell_Use.append([Add_Use1.get()])
    Cells.append([Add_Cell1.get()])
    Models.append([Add_Tray1.get()])
    # GET ADDITIONAL CELL 2
    Cell_Use.append([Add_Use2.get()])
    Cells.append([Add_Cell2.get()])
    Models.append([Add_Tray2.get()])
    # GET ADDITIONAL CELL 3
    Cell_Use.append([Add_Use3.get()])
    Cells.append([Add_Cell3.get()])
    Models.append([Add_Tray3.get()])
    for i in range(0,len(Cells)): # i selects the cell in question
        # CREATE BLANK ROWS IN EACH LIST
        Well_Solvent1_Concs.append([])
        Well_Solvent2_Concs.append([])
        Well_SS_Concs.append([])
        Well_Vols.append([])
        Well_Ingrs.append([])
        Well_Names.append([])
        Tray_Pos.append([])
        Define_Wells.append([])
        SS_Type.append([])
        # GET METHODS   
        if i ==0:
            Define_Wells[i].append(In_Assign_Var.get())
        elif i ==2:
            Define_Wells[i].append(Out_Assign_Var.get())
        elif Cells[i] != ['N/A']:
            if i == 5:
                Define_Wells[i].append(Assign_Var1.get())
            elif i == 6:
                Define_Wells[i].append(Assign_Var2.get())
            elif i == 7:
                Define_Wells[i].append(Assign_Var3.get())
            else:
                pass
        else:
            pass
    
        # CONVERT THE MODEL ROW FROM NAME TO LIST OF WELL POSITIONS
        if Models[i]==['6-well-plate']:
            Tray_Pos[i]=W6wellplate
        if Models[i]==['12-well-plate']:
            Tray_Pos[i]=W12wellplate
        if Models[i]==['24-well-plate']:
            Tray_Pos[i]=W24wellplate
        if Models[i]==['24-vial-plate']:
            Tray_Pos[i]=W24vialplate
        if Models[i]==['48-well-plate']:
            Tray_Pos[i]=W48wellplate
        if Models[i]==['48-vial-plate']:
            Tray_Pos[i]=W48vialplate
        if Models[i]==['96-deep-well']:
            Tray_Pos[i]=W96deepwell
        if Models[i]==['96-flat']:
            Tray_Pos[i]=W96flat
        if Models[i]==['96-PCR-flat']:
            Tray_Pos[i]=W96PCRflat
        if Models[i]==['96-PCR-tall']:
            Tray_Pos[i]=W96PCRtall
        if Models[i]==['96-well-plate-20mm']:
            Tray_Pos[i]=W96wellplate20mm
        if Models[i]==['384-plate']:
            Tray_Pos[i]=W384plate
        if Models[i]==['e-gelgol']:
            Tray_Pos[i]=egelgol
        if Models[i]==['hampton-1ml-deep-block']:
            Tray_Pos[i]=hampton1mldeepblock
        if Models[i]==['MALDI-plate']:
            Tray_Pos[i]=MALDIplate
        if Models[i]==['PCR-strip-tall']:
            Tray_Pos[i]=PCRstriptall
        if Models[i]==['point']:
            Tray_Pos[i]=point
        if Models[i]==['rigaku-compact-crystallization-plate']:
            Tray_Pos[i]=rigaku
        if Models[i]==['tiprack-10ul']:
            Tray_Pos[i]=tiprack10ul
        if Models[i]==['tiprack-10ul-H']:
            Tray_Pos[i]=tiprack10ulH
        if Models[i]==['tiprack-100ul']:
            Tray_Pos[i]=tiprack100ul
        if Models[i]==['tiprack-200ul']:
            Tray_Pos[i]=tiprack200ul
        if Models[i]==['tiprack-250ul']:
            Tray_Pos[i]=tiprack250ul
        if Models[i]==['tiprack-1000ul']:
            Tray_Pos[i]=tiprack1000ul
        if Models[i]==['tiprack-1000ul-chem']:
            Tray_Pos[i]=tiprack1000ulchem
        if Models[i]==['tiprack-1000ul-H']:
            Tray_Pos[i]=tiprack1000ulH
        if Models[i]==['trash-box']:
            Tray_Pos[i]=trashbox
        if Models[i]==['trough-1row-25ml']:
            Tray_Pos[i]=trough1row25ml
        if Models[i]==['trough-12row']:
            Tray_Pos[i]=trough12row
        if Models[i]==['trough-12row-short']:
            Tray_Pos[i]=trough12rowshort
        if Models[i]==['tube-rack-.75ml']:
            Tray_Pos[i]=tuberack75ml
        if Models[i]==['tube-rack-2ml']:
            Tray_Pos[i]=tuberack2ml
        if Models[i]==['tube-rack-2ml-9x9']:
            Tray_Pos[i]=tuberack2ml9x9
        if Models[i]==['tube-rack-5ml-96']:
            Tray_Pos[i]=tuberack5ml96
        if Models[i]==['tube-rack-15_50ml']:
            Tray_Pos[i]=tuberack1550ml
        if Models[i]==['tube-rack-80well']:
            Tray_Pos[i]=tuberack80well
        if Models[i]==['wheaton_vial_rack']:
            Tray_Pos[i]=wheatonvialrack
        if Models[i]==['5ml-3x4']:
            Tray_Pos[i]=W5ml3x4
        if Models[i]==['alum-block-pcr-strips']:
            Tray_Pos[i]=alumblockpcrstrips
        if Models[i]==['small_vial_rack_16x45']:
            Tray_Pos[i]=smallvialrack16x45
        if Models[i]==['T25-flask']:
            Tray_Pos[i]=T25flask
        if Models[i]==['T75-flask']:
            Tray_Pos[i]=T75flask
        if Models[i]==['heating-block-4x5']:
            Tray_Pos[i]=W5ml3x4
        if Models[i]==['heating-block-3x4']:
            Tray_Pos[i]=W5ml3x4
        
        # ADD WELL NAMES TO LIST BY SORTING THROUGH WELL POSITIONS
        for h in Tray_Pos[i]:
            if h != 'N/A':
                Well_Names[i].append(All_pos[h])
            else:
                pass
    
    limit = 0
    for i in Cells:
        if i==['N/A']:
            pass
        else:
            limit+=1
    # Check no incorrect trays selected
    for i in range(0,limit):
        if Cell_Use[i][0]=='Tips':
            if Models[i][0]=='tiprack-10ul' or Models[i][0]=='tiprack-10ul-H' or Models[i][0]=='tiprack-100ul'\
                or Models[i][0]=='tiprack-200ul' or Models[i][0]=='tiprack-250ul' or Models[i][0]=='tiprack-1000ul'\
                 or Models[i][0]=='tiprack-1000ul-chem' or Models[i][0]=='tiprack-1000ul-H':
                pass
            else:
                print("ERROR - Incorrect Model Setup. Model "+Models[i][0]+" selected for "+Cell_Use[i][0]+" use.")
                break
                Restart()
        elif Cell_Use[i][0]=='Ingredients' or Cell_Use[i][0]=='Output' or Cell_Use[i][0]=='Mixing':
            if Models[i][0]=='tiprack-10ul' or Models[i][0]=='tiprack-10ul-H' or Models[i][0]=='tiprack-100ul'\
                or Models[i][0]=='tiprack-200ul' or Models[i][0]=='tiprack-250ul' or Models[i][0]=='tiprack-1000ul'\
                 or Models[i][0]=='tiprack-1000ul-chem' or Models[i][0]=='tiprack-1000ul-H' or Models[i][0]=='Trash':
                print("ERROR - Incorrect Model Setup. Model "+Models[i][0]+" selected for "+Cell_Use[i][0]+" use.")
                break
                Restart()
            else:
                pass  
        elif Cell_Use[i][0]=='N/A':
            pass
        else:
            if Models[i][0]!='trash-box':
                print("ERROR - Incorrect Model Setup. Model "+Models[i][0]+" selected for "+Cell_Use[i][0]+" use.")
                break
                Restart()
            else:
                pass
    global New_Cells, New_Cell_Use, New_Models, New_Tray_Pos, New_Define_Wells, New_Well_Names, New_Well_Ingrs,\
           New_Well_Solvent1_Concs, New_Well_Solvent2_Concs, New_Well_SS_Concs, New_Well_Vols, New_SS_Type,\
           input_number, output_number, mixer_number, tips_number, trash_number
    
    New_Cells = [[],[],[],[],[],[],[],[]]
    New_Cell_Use = [[],[],[],[],[],[],[],[]]
    New_Models = [[],[],[],[],[],[],[],[]]
    New_Tray_Pos = [[],[],[],[],[],[],[],[]]
    New_Define_Wells = [[],[],[],[],[],[],[],[]]
    New_Well_Names = [[],[],[],[],[],[],[],[]]
    New_Well_Ingrs = [[],[],[],[],[],[],[],[]]
    New_Well_Solvent1_Concs = [[],[],[],[],[],[],[],[]]
    New_Well_Solvent2_Concs = [[],[],[],[],[],[],[],[]]
    New_Well_SS_Concs = [[],[],[],[],[],[],[],[]]
    New_Well_Vols = [[],[],[],[],[],[],[],[]]
    New_SS_Type = [[],[],[],[],[],[],[],[]]
    counter = 0
    # Rearrange to desired order of input-mixing-output-tips-trash
    for i in range(0,len(Cells)):
        if Cell_Use[i]==["Ingredients"]:
            New_Cells[counter] = Cells[i]
            New_Cell_Use[counter] = Cell_Use[i]
            New_Models[counter] = Models[i]
            New_Tray_Pos[counter] = Tray_Pos[i]
            New_Define_Wells[counter] = Define_Wells[i]
            New_Well_Names[counter] = Well_Names[i]
            New_Well_Ingrs[counter] = Well_Ingrs[i]
            New_Well_Solvent1_Concs[counter] = Well_Solvent1_Concs[i]
            New_Well_Solvent2_Concs[counter] = Well_Solvent2_Concs[i]
            New_Well_SS_Concs[counter] = Well_SS_Concs[i]
            New_Well_Vols[counter] = Well_Vols[i]
            New_SS_Type[counter] = SS_Type[i]
            counter +=1
        else:
            pass
    for i in range(0,len(Cells)):
        if Cell_Use[i]==["Mixing"]:
            New_Cells[counter] = Cells[i]
            New_Cell_Use[counter] = Cell_Use[i]
            New_Models[counter] = Models[i]
            New_Tray_Pos[counter] = Tray_Pos[i]
            New_Define_Wells[counter] = Define_Wells[i]
            New_Well_Names[counter] = Well_Names[i]
            New_Well_Ingrs[counter] = Well_Ingrs[i]
            New_Well_Solvent1_Concs[counter] = Well_Solvent1_Concs[i]
            New_Well_Solvent2_Concs[counter] = Well_Solvent2_Concs[i]
            New_Well_SS_Concs[counter] = Well_SS_Concs[i]
            New_Well_Vols[counter] = Well_Vols[i]
            New_SS_Type[counter] = SS_Type[i]
            counter +=1
        else:
            pass
    for i in range(0,len(Cells)):
        if Cell_Use[i]==["Output"]:
            New_Cells[counter] = Cells[i]
            New_Cell_Use[counter] = Cell_Use[i]
            New_Models[counter] = Models[i]
            New_Tray_Pos[counter] = Tray_Pos[i]
            New_Define_Wells[counter] = Define_Wells[i]
            New_Well_Names[counter] = Well_Names[i]
            New_Well_Ingrs[counter] = Well_Ingrs[i]
            New_Well_Solvent1_Concs[counter] = Well_Solvent1_Concs[i]
            New_Well_Solvent2_Concs[counter] = Well_Solvent2_Concs[i]
            New_Well_SS_Concs[counter] = Well_SS_Concs[i]
            New_Well_Vols[counter] = Well_Vols[i]
            New_SS_Type[counter] = SS_Type[i]
            counter +=1
        else:
            pass
    for i in range(0,len(Cells)):
        if Cell_Use[i]==["Tips"]:
            New_Cells[counter] = Cells[i]
            New_Cell_Use[counter] = Cell_Use[i]
            New_Models[counter] = Models[i]
            New_Tray_Pos[counter] = Tray_Pos[i]
            New_Define_Wells[counter] = Define_Wells[i]
            New_Well_Names[counter] = Well_Names[i]
            New_Well_Ingrs[counter] = Well_Ingrs[i]
            New_Well_Solvent1_Concs[counter] = Well_Solvent1_Concs[i]
            New_Well_Solvent2_Concs[counter] = Well_Solvent2_Concs[i]
            New_Well_SS_Concs[counter] = Well_SS_Concs[i]
            New_Well_Vols[counter] = Well_Vols[i]
            New_SS_Type[counter] = SS_Type[i]
            counter +=1
        else:
            pass
    for i in range(0,len(Cells)):
        if Cell_Use[i]==["Trash"]:
            New_Cells[counter] = Cells[i]
            New_Cell_Use[counter] = Cell_Use[i]
            New_Models[counter] = Models[i]
            New_Tray_Pos[counter] = Tray_Pos[i]
            New_Define_Wells[counter] = Define_Wells[i]
            New_Well_Names[counter] = Well_Names[i]
            New_Well_Ingrs[counter] = Well_Ingrs[i]
            New_Well_Solvent1_Concs[counter] = Well_Solvent1_Concs[i]
            New_Well_Solvent2_Concs[counter] = Well_Solvent2_Concs[i]
            New_Well_SS_Concs[counter] = Well_SS_Concs[i]
            New_Well_Vols[counter] = Well_Vols[i]
            New_SS_Type[counter] = SS_Type[i]
            counter +=1
        else:
            pass
    for i in range(0,len(Cells)):
        if Cells[i]==['N/A']:
            New_Cells[counter] = Cells[i]
            New_Cell_Use[counter] = Cell_Use[i]
            New_Models[counter] = Models[i]
            New_Tray_Pos[counter] = Tray_Pos[i]
            New_Define_Wells[counter] = Define_Wells[i]
            New_Well_Names[counter] = Well_Names[i]
            New_Well_Ingrs[counter] = Well_Ingrs[i]
            New_Well_Solvent1_Concs[counter] = Well_Solvent1_Concs[i]
            New_Well_Solvent2_Concs[counter] = Well_Solvent2_Concs[i]
            New_Well_SS_Concs[counter] = Well_SS_Concs[i]
            New_Well_Vols[counter] = Well_Vols[i]
            New_SS_Type[counter] = SS_Type[i]
            counter +=1
        else:
            pass
    input_number = 0
    for i in range(0,len(Cells)):
        if New_Cell_Use[i]==["Mixing"]:
            try:
                if mixer_number<i-input_number:
                    pass
                else:
                    pass
            except:
                mixer_number = i
        elif New_Cell_Use[i]==["Output"]:
            try:
                if output_number<i-input_number:
                    pass
                else:
                    pass
            except:
                output_number = i
        elif New_Cell_Use[i]==["Tips"]:
            try:
                if tips_number<i-input_number:
                    pass
                else:
                    pass
            except:
                tips_number = i
        elif New_Cell_Use[i]==["Trash"]:
            try:
                if trash_number<i-input_number:
                    pass
                else:
                    pass
            except:
                trash_number = i
    if trash_number-tips_number>2:
        print("ERROR - Too many tip sizes, code will auto-sort up to 2 tipracks for two-axis head only")
        input("Press ENTER to Restart")
        OT.destroy()
        Restart()
    else:
        pass
    return TraySetup()

def Inputs(count):
    #### INSERT ####
    #### INSERT ####
    #### INSERT ####
    if New_Models[count][0]=='Custom':
        Custom_Setup(count)
    else:
    #### INSERT ####
    #### INSERT ####
    #### INSERT ####
        if count == limit:
            print("Beginning Script-writing")
            OT.destroy()
            writescript()
            Restart()
        else:
            for i in range(0,len(Ingr_List)):
                # Sets Default selections
                if i%2==0:
                    Ingr_List[i].set(Solvent_1)
                else:
                    Ingr_List[i].set(Diluent_2)
            for i in range(0,len(Dilu_List)):
                # Sets Default selections
                Dilu_List[i].set(Diluent_2)
                SS_List[i].set(SS_1)

            # Defaulted to max 'working' volumes and max volume of min vial-size
            if New_Models[count][0]=='6-well-plate':
                insert_vol=2900 # Researched
            elif New_Models[count][0]=='12-well-plate':
                insert_vol=1140 # Researched
            elif New_Models[count][0]=='24-well-plate':
                insert_vol=570 # Researched
            elif New_Models[count][0]=='24-vial-plate':
                insert_vol=1500 # Researched
            elif New_Models[count][0]=='48-well-plate':
                insert_vol=285 # Researched
            elif New_Models[count][0]=='48-vial-plate':
                insert_vol=1500 # Researched
            elif New_Models[count][0]=='96-deep-well':
                insert_vol=1000 # Researched
            elif New_Models[count][0]=='96-flat':
                insert_vol=200 # Researched
            elif New_Models[count][0]=='96-PCR-flat' or New_Models[count][0]=='96-PCR-tall':
                insert_vol=200 # Researched
            elif New_Models[count][0]=='96-well-plate-20mm':
                insert_vol=200
            elif New_Models[count][0]=='hampton-1ml-deep-block':
                insert_vol=1000 # Researched
            elif New_Models[count][0]=='e-gelgol':
                insert_vol=100
            elif New_Models[count][0]=='PCR-strip-tall':
                insert_vol=100 # Researched
            elif New_Models[count][0]=='trough-12row':
                insert_vol=21000 # Researched
            elif New_Models[count][0]=='trough-12row-short':
                insert_vol=7000 # Researched
            elif New_Models[count][0]=='trough-1row-25ml':
                insert_vol=25000 # Researched
            elif New_Models[count][0]=='tube-rack-.75ml':
                insert_vol=750 # Researched
            elif New_Models[count][0]=='tube-rack-2ml':
                insert_vol=2000 # Researched
            elif New_Models[count][0]=='tube-rack-2ml-9x9':
                insert_vol=2000 # Researched
            elif New_Models[count][0]=='tube-rack-5ml-96':
                insert_vol=5000 # Researched
            elif New_Models[count][0]=='tube-rack-15_50ml':
                insert_vol=15000 # Researched - special case
            elif New_Models[count][0]=='tube-rack-80well':
                insert_vol=1500 # Researched
            elif New_Models[count][0]=='wheaton_vial_rack':
                insert_vol=100 # Unknown
            elif New_Models[count][0]=='5ml-3x4':
                insert_vol=5000 # Researched
            elif New_Models[count][0]=='heating-block-4x5':
                insert_vol=1500 # Researched
            elif New_Models[count][0]=='heating-block-3x4':
                insert_vol=5000 # Researched
            elif New_Models[count][0]=='alum-block-pcr-strips':
                insert_vol=200 # Researched
            elif New_Models[count][0]=='small_vial_rack_16x45':
                insert_vol=100  # Unknown
            elif New_Models[count][0]=='T25-flask':
                insert_vol=50000 # Researched
            elif New_Models[count][0]=='T75-flask':
                insert_vol=250000 # Researched
            elif New_Models[count][0]=='rigaku-compact-crystallization-plate':
                insert_vol=145 # Unknown
            elif New_Models[count][0]=='MALDI-plate':
                insert_vol=145 # Unknown
            elif New_Models[count][0]=='384-plate':
                insert_vol=145 # Researched
            else:
                insert_vol=145 # Smallest volume for any unknown plates

            
                
            if New_Cell_Use[count][0]=='Ingredients':
                for i in Solvent1_Conc_List:
                    i.delete(0,'end')
                    i.insert(0,20)

                for i in Solvent2_Conc_List:
                    i.delete(0,'end')
                    i.insert(0,0)

                for i in SS_Conc_List:
                    i.delete(0,'end')
                    i.insert(0,0)

                for i in Vol_List:
                    i.delete(0,'end')
                    i.insert(0,insert_vol)
            else:
                for i in Solvent1_Conc_List:
                    i.delete(0,'end')
                    i.insert(0,5)

                for i in Solvent2_Conc_List:
                    i.delete(0,'end')
                    i.insert(0,10)

                for i in SS_Conc_List:
                    i.delete(0,'end')
                    i.insert(0,0.15)

                for i in Vol_List:
                    i.delete(0,'end')
                    i.insert(0,50)

            try:
                for i in Inputs_List:
                    i.grid_remove()
            except:
                pass

            try:
                Next_Button.destroy()
            except:
                pass

            #Tray_Image = PhotoImage(file=Models[count]+".png")
            #Tray_Pic=Label(OT, image=Tray_Image)
            #Tray_Pic.place(x=900,y=0)
            # COUNT EXCEEDS LEN(CELLS) AFTER CALL HAVE BEEN DONE
            #if Cell_Use[count]==["Output"]:
                
            
            
                
            # IF INPUT BAY
            if New_Cell_Use[count]==["Ingredients"] or New_Cell_Use[count]==["Output"]:
                if New_Define_Wells[count]==[1]:
                    ByUniform(count,New_Models[count])
                elif New_Define_Wells[count]==[2]:
                    ByColumns(count,New_Models[count])
                elif New_Define_Wells[count]==[3]:
                    ByRows(count,New_Models[count])
                elif New_Define_Wells[count]==[4]:
                    ByWells(count,New_Models[count],New_Tray_Pos[count])
                else:
                    pass
                
            # SET VOLUMES OF MIXING AND TIPS
            elif New_Cell_Use[count]==['Tips']:
                if New_Models[count]==['tiprack-10ul'] or New_Models[count]==['tiprack-10ul-H']:
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append('10')
                elif New_Models[count]==['tiprack-100ul']:
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append('100')
                elif New_Models[count]==['tiprack-200ul']:
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append('200')
                elif New_Models[count]==['tiprack-250ul']:
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append('250')
                elif New_Models[count]==['tiprack-1000ul'] or New_Models[count]==['tiprack-1000ul-chem'] or New_Models[count]==['tiprack-1000ul-H']:
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append('1000')
                if Tip_Setup >=1:
                    Pipette_Parameters(count,New_Models[count][0])
                else:
                    Pipette_Setup(count,New_Models[count][0])
                
            # ALL MIXING WILL BE MINUS 10% TO AVOID SPILL
            elif New_Cell_Use[count]==['Mixing']:
                if New_Models[count][0]=='6-well-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(16800))
                        # working vol = 1.9-2.9mL
                elif New_Models[count][0]=='12-well-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(6900))
                        # Working vol = 0.76-1.14mL
                elif New_Models[count][0]=='24-well-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(3400))
                        # Working vol = 0.38-0.57mL
                elif New_Models[count][0]=='24-vial-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                        # Unknown 
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='48-well-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(1600))
                        # Working vol = 0.19-0.285mL
                elif New_Models[count][0]=='48-vial-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                        # Unknown 
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='96-deep-well':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(200))
                        # Working vol = SAME
                        # CHECK ME
                elif New_Models[count][0]=='96-flat':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(360))
                        # Working vol = 75-200uL
                        # CHECK ME        
                elif New_Models[count][0]=='96-PCR-flat' or New_Models[count][0]=='96-PCR-tall':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(200))
                        # Working vol = SAME
                        # CHECK ME
                elif New_Models[count][0]=='96-well-plate-20mm':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(323))
                        # Working vol = 280uL
                        # CHECK ME
                elif New_Models[count][0]=='hampton-1ml-deep-block':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(1000))
                        # Working vol = 1000uL
                        # CHECK ME
                elif New_Models[count][0]=='e-gelgol':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                        # Working vol = unknown
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='PCR-strip-tall':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                        # Working vol = unknown - all set to zero
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='trough-12row':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(290000))
                        # Working vol = 290mL
                        # CHECK ME
                elif New_Models[count][0]=='trough-12row-short':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(21000))
                        # Working vol = 7000uL
                        # CHECK ME
                elif New_Models[count][0]=='trough-1row-25ml':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(25000))
                        # Working vol = 25000uL
                        # CHECK ME
                elif New_Models[count][0]=='tube-rack-.75ml':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(750))
                        # Working vol = 750uL
                        # GUESS FROM NAME
                elif New_Models[count][0]=='tube-rack-2ml':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(2000))
                        # Working vol = 2000uL
                        # GUESS FROM NAME
                elif New_Models[count][0]=='tube-rack-2ml-9x9':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(2000))
                        # Working vol = 2000uL
                        # GUESS FROM NAME
                elif New_Models[count][0]=='tube-rack-5ml-96':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(5000))
                        # Working vol = 2000uL
                        # GUESS FROM NAME
                elif Models[count][0]=='tube-rack-15_50ml':
                    for i in Tray_Pos[count]:
                        Well_Vols[count].append(str(50000))
                        # Working vol = 50000uL
                        # GUESS FROM NAME
                elif New_Models[count][0]=='tube-rack-80well':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                        # Working vol = unknown - all set to zero
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='wheaton_vial_rack':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                        # Working vol = unknown - all set to zero
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='5ml-3x4':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(5000))
                        # Working vol = 5000uL
                        # GUESS FROM NAME
                elif New_Models[count][0]=='heating-block-3x4':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(5000))
                elif New_Models[count][0]=='heating-block-4x5':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(1500))
                elif New_Models[count][0]=='alum-block-pcr-strips':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                        # Working vol = unknown - all set to zero
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='small_vial_rack_16x45':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                        # Working vol = unknown - all set to zero
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='T25-flask':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(50000))
                        # Working vol = 5-7.5mL
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='T75-flask':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(250000))
                        # Working vol = 15-22.5mL
                        # UNKNOWN - SET TO ZERO
                elif New_Models[count][0]=='rigaku-compact-crystallization-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(152))
                        # Working vol = 145uL
                        # GUESS - CHECK ME                
                elif New_Models[count][0]=='MALDI-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(152))
                        # Working vol = 145uL
                        # GUESS - CHECK ME
                elif New_Models[count][0]=='384-plate':
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(152))
                        # Working vol = 145uL
                else:
                    for i in New_Tray_Pos[count]:
                        New_Well_Vols[count].append(str(0))
                count+=1
                Inputs(count)

            else:
                count+=1
                Inputs(count)


def SetDefaults():
    with open('Defaults.py','r') as f:
        line = f.readlines()
    line[6]= "    default_Use6 = '"+Add_Use1.get()+"'\n"
    line[7]= "    default_Use7 = '"+Add_Use2.get()+"'\n"
    line[8]= "    default_Use8 = '"+Add_Use3.get()+"'\n"

    line[10]= "    default_Cell1 = '"+Input_Cell1.get()+"'\n"
    line[11]= "    default_Cell2 = '"+Mixing_Cell1.get()+"'\n"
    line[12]= "    default_Cell3 = '"+Output_Cell1.get()+"'\n"
    line[13]= "    default_Cell4 = '"+Tips_Cell1.get()+"'\n"
    line[14]= "    default_Cell5 = '"+Trash_Cell1.get()+"'\n"
    line[15]= "    default_Cell6 = '"+Add_Cell1.get()+"'\n"
    line[16]= "    default_Cell7 = '"+Add_Cell2.get()+"'\n"
    line[17]= "    default_Cell8 = '"+Add_Cell3.get()+"'\n"
    
    line[19]= "    default_Tray1 = '"+Input_Model1.get()+"'\n"
    line[20]= "    default_Tray2 = '"+Mixing_Model1.get()+"'\n"
    line[21]= "    default_Tray3 = '"+Output_Model1.get()+"'\n"
    line[22]= "    default_Tray4 = '"+Tips_Model1.get()+"'\n"
    line[23]= "    default_Tray5 = '"+Trash_Model1.get()+"'\n"
    line[24]= "    default_Tray6 = '"+Add_Tray1.get()+"'\n"
    line[25]= "    default_Tray7 = '"+Add_Tray2.get()+"'\n"
    line[26]= "    default_Tray8 = '"+Add_Tray3.get()+"'\n"

    line[28]= "    default_Cell_Addition = "+str(Cell_Additions.get())+"\n"
    
    line[30]= "    default_In_Margin = "+In_Margin_Entry.get()+"\n"
    line[31]= "    default_Mix_Margin = "+Mix_Margin_Entry.get()+"\n"
                    
    with open('Defaults.py','w') as f:
        f.writelines(line)
    
def RestoreDefaults():
    with open('Defaults.py','r') as f:
        line = f.readlines()
    line[6]= line[41]
    line[7]= line[42]
    line[8]= line[43]

    line[10]= line[45]
    line[11]= line[46]
    line[12]= line[47]
    line[13]= line[48]
    line[14]= line[49]
    line[15]= line[50]
    line[16]= line[51]
    line[17]= line[52]
    
    line[19]= line[54]
    line[20]= line[55]
    line[21]= line[56]
    line[22]= line[57]
    line[23]= line[58]
    line[24]= line[59]
    line[25]= line[60]
    line[26]= line[61]

    line[28]= line[63]

    line[30]= line[65]
    line[31]= line[66]
    
    with open('Defaults.py','w') as f:
        f.writelines(line)
    
def TraySetup():

    global OT, ColumnA_Label, Column_Label2, ColumnB_Label, ColumnC_Label, ColumnD_Label, ColumnE_Label, ColumnF_Label,\
           ColumnG_Label, ColumnH_Label, ColumnI_Label, ColumnJ_Label, ColumnK_Label, ColumnL_Label, ColumnM_Label,\
           ColumnN_Label, ColumnO_Label, ColumnP_Label, Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label,\
           Row6_Label, Row7_Label, Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label,\
           Row14_Label, Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
           Row22_Label, Row23_Label, Row24_Label, Row_Label, Column_Label, In_Out_Tray_Label, \
           Column_Label_List, Row_Label_List, Inputs_List
    for i in Main_List:
        try:
            i.grid_remove()
        except:
            pass
    # MAIN OT
    
    ##### TRAY SETUP LABELS ##### ##### TRAY SETUP LABELS ##### ##### TRAY SETUP LABELS ##### ##### TRAY SETUP LABELS #####
    Heading_Label = Label(OT, text="Parameters:", font = subheading_font, fg=Category_colour,bg=bgcolour)
    In_Out_Tray_Label = Label(OT, text="blank", font = subheading_font, fg=Category_colour,bg=bgcolour) 
    
    
    Column_Label = Label(OT,text='Column:', font = small_font, bg=bgcolour)
    Column_Label2 = Label(OT,text='Column:', font = small_font, bg=bgcolour)
    ColumnA_Label = Label(OT,text='A', font = subheading_font, bg=bgcolour)
    ColumnB_Label = Label(OT,text='B', font = subheading_font, bg=bgcolour)
    ColumnC_Label = Label(OT,text='C', font = subheading_font, bg=bgcolour)
    ColumnD_Label = Label(OT,text='D', font = subheading_font, bg=bgcolour)
    ColumnE_Label = Label(OT,text='E', font = subheading_font, bg=bgcolour)
    ColumnF_Label = Label(OT,text='F', font = subheading_font, bg=bgcolour)
    ColumnG_Label = Label(OT,text='G', font = subheading_font, bg=bgcolour)
    ColumnH_Label = Label(OT,text='H', font = subheading_font, bg=bgcolour)
    ColumnI_Label = Label(OT,text='I', font = subheading_font, bg=bgcolour)
    ColumnJ_Label = Label(OT,text='J', font = subheading_font, bg=bgcolour)
    ColumnK_Label = Label(OT,text='K', font = subheading_font, bg=bgcolour)
    ColumnL_Label = Label(OT,text='L', font = subheading_font, bg=bgcolour)
    ColumnM_Label = Label(OT,text='M', font = subheading_font, bg=bgcolour)
    ColumnN_Label = Label(OT,text='N', font = subheading_font, bg=bgcolour)
    ColumnO_Label = Label(OT,text='O', font = subheading_font, bg=bgcolour)
    ColumnP_Label = Label(OT,text='P', font = subheading_font, bg=bgcolour)

    Row_Label = Label(OT,text='Row', font = small_font, bg=bgcolour)
    Row1_Label = Label(OT,text='1', font = subheading_font, bg=bgcolour)
    Row2_Label = Label(OT,text='2', font = subheading_font, bg=bgcolour)
    Row3_Label = Label(OT,text='3', font = subheading_font, bg=bgcolour)
    Row4_Label = Label(OT,text='4', font = subheading_font, bg=bgcolour)
    Row5_Label = Label(OT,text='5', font = subheading_font, bg=bgcolour)
    Row6_Label = Label(OT,text='6', font = subheading_font, bg=bgcolour)
    Row7_Label = Label(OT,text='7', font = subheading_font, bg=bgcolour)
    Row8_Label = Label(OT,text='8', font = subheading_font, bg=bgcolour)
    Row9_Label = Label(OT,text='9', font = subheading_font, bg=bgcolour)
    Row10_Label = Label(OT,text='10', font = subheading_font, bg=bgcolour)
    Row11_Label = Label(OT,text='11', font = subheading_font, bg=bgcolour)
    Row12_Label = Label(OT,text='12', font = subheading_font, bg=bgcolour)
    Row13_Label = Label(OT,text='13', font = subheading_font, bg=bgcolour)
    Row14_Label = Label(OT,text='14', font = subheading_font, bg=bgcolour)
    Row15_Label = Label(OT,text='15', font = subheading_font, bg=bgcolour)
    Row16_Label = Label(OT,text='16', font = subheading_font, bg=bgcolour)
    Row17_Label = Label(OT,text='17', font = subheading_font, bg=bgcolour)
    Row18_Label = Label(OT,text='18', font = subheading_font, bg=bgcolour)
    Row19_Label = Label(OT,text='19', font = subheading_font, bg=bgcolour)
    Row20_Label = Label(OT,text='20', font = subheading_font, bg=bgcolour)
    Row21_Label = Label(OT,text='21', font = subheading_font, bg=bgcolour)
    Row22_Label = Label(OT,text='22', font = subheading_font, bg=bgcolour)
    Row23_Label = Label(OT,text='23', font = subheading_font, bg=bgcolour)
    Row24_Label = Label(OT,text='24', font = subheading_font, bg=bgcolour)

    Column_Label_List = [ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,\
                          ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,\
                          ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,\
                          ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,ColumnA_Label,\
                          ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,\
                          ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,\
                          ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,\
                          ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,ColumnB_Label,\
                          ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,\
                          ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,\
                          ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,\
                          ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,ColumnC_Label,\
                          ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,\
                          ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,\
                          ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,\
                          ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,ColumnD_Label,\
                          ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,\
                          ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,\
                          ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,\
                          ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,ColumnE_Label,\
                          ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,\
                          ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,\
                          ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,\
                          ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,ColumnF_Label,\
                          ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,\
                          ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,\
                          ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,\
                          ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,ColumnG_Label,\
                          ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,\
                          ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,\
                          ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,\
                          ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,ColumnH_Label,\
                          ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,\
                          ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,\
                          ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,\
                          ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,ColumnI_Label,\
                          ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,\
                          ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,\
                          ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,\
                          ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,ColumnJ_Label,\
                          ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,\
                          ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,\
                          ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,\
                          ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,ColumnK_Label,\
                          ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,\
                          ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,\
                          ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,\
                          ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,ColumnL_Label,\
                          ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,\
                          ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,\
                          ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,\
                          ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,ColumnM_Label,\
                          ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,\
                          ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,\
                          ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,\
                          ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,ColumnN_Label,\
                          ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,\
                          ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,\
                          ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,\
                          ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,ColumnO_Label,\
                          ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,\
                          ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,\
                          ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,\
                          ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label,ColumnP_Label]

    Row_Label_List = [Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label,\
                       Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label,\
                       Row8_Label, Row9_Label, Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label,\
                       Row15_Label, Row16_Label, Row17_Label, Row18_Label, Row19_Label, Row20_Label, Row21_Label,\
                       Row22_Label, Row23_Label, Row24_Label]
    
    global Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
           Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
           Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
           Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
           Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
           Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
           Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
           Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
           Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
           Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
           WA1_Ingr, WA2_Ingr, WA3_Ingr, WA4_Ingr, WA5_Ingr, WA6_Ingr,\
           WA7_Ingr, WA8_Ingr, WA9_Ingr, WA10_Ingr, WA11_Ingr, WA12_Ingr,\
           WA13_Ingr, WA14_Ingr, WA15_Ingr, WA16_Ingr, WA17_Ingr, WA18_Ingr,\
           WA19_Ingr, WA20_Ingr, WA21_Ingr, WA22_Ingr, WA23_Ingr, WA24_Ingr,\
           WB1_Ingr, WB2_Ingr, WB3_Ingr, WB4_Ingr, WB5_Ingr, WB6_Ingr,\
           WB7_Ingr, WB8_Ingr, WB9_Ingr, WB10_Ingr, WB11_Ingr, WB12_Ingr,\
           WB13_Ingr, WB14_Ingr, WB15_Ingr, WB16_Ingr, WB17_Ingr, WB18_Ingr,\
           WB19_Ingr, WB20_Ingr, WB21_Ingr, WB22_Ingr, WB23_Ingr, WB24_Ingr,\
           WC1_Ingr, WC2_Ingr, WC3_Ingr, WC4_Ingr, WC5_Ingr, WC6_Ingr,\
           WC7_Ingr, WC8_Ingr, WC9_Ingr, WC10_Ingr, WC11_Ingr, WC12_Ingr,\
           WC13_Ingr, WC14_Ingr, WC15_Ingr, WC16_Ingr, WC17_Ingr, WC18_Ingr,\
           WC19_Ingr, WC20_Ingr, WC21_Ingr, WC22_Ingr, WC23_Ingr, WC24_Ingr,\
           WD1_Ingr, WD2_Ingr, WD3_Ingr, WD4_Ingr, WD5_Ingr, WD6_Ingr,\
           WD7_Ingr, WD8_Ingr, WD9_Ingr, WD10_Ingr, WD11_Ingr, WD12_Ingr,\
           WD13_Ingr, WD14_Ingr, WD15_Ingr, WD16_Ingr, WD17_Ingr, WD18_Ingr,\
           WD19_Ingr, WD20_Ingr, WD21_Ingr, WD22_Ingr, WD23_Ingr, WD24_Ingr,\
           WE1_Ingr, WE2_Ingr, WE3_Ingr, WE4_Ingr, WE5_Ingr, WE6_Ingr,\
           WE7_Ingr, WE8_Ingr, WE9_Ingr, WE10_Ingr, WE11_Ingr, WE12_Ingr,\
           WE13_Ingr, WE14_Ingr, WE15_Ingr, WE16_Ingr, WE17_Ingr, WE18_Ingr,\
           WE19_Ingr, WE20_Ingr, WE21_Ingr, WE22_Ingr, WE23_Ingr, WE24_Ingr,\
           WF1_Ingr, WF2_Ingr, WF3_Ingr, WF4_Ingr, WF5_Ingr, WF6_Ingr,\
           WF7_Ingr, WF8_Ingr, WF9_Ingr, WF10_Ingr, WF11_Ingr, WF12_Ingr,\
           WF13_Ingr, WF14_Ingr, WF15_Ingr, WF16_Ingr, WF17_Ingr, WF18_Ingr,\
           WF19_Ingr, WF20_Ingr, WF21_Ingr, WF22_Ingr, WF23_Ingr, WF24_Ingr,\
           WG1_Ingr, WG2_Ingr, WG3_Ingr, WG4_Ingr, WG5_Ingr, WG6_Ingr,\
           WG7_Ingr, WG8_Ingr, WG9_Ingr, WG10_Ingr, WG11_Ingr, WG12_Ingr,\
           WG13_Ingr, WG14_Ingr, WG15_Ingr, WG16_Ingr, WG17_Ingr, WG18_Ingr,\
           WG19_Ingr, WG20_Ingr, WG21_Ingr, WG22_Ingr, WG23_Ingr, WG24_Ingr,\
           WH1_Ingr, WH2_Ingr, WH3_Ingr, WH4_Ingr, WH5_Ingr, WH6_Ingr,\
           WH7_Ingr, WH8_Ingr, WH9_Ingr, WH10_Ingr, WH11_Ingr, WH12_Ingr,\
           WH13_Ingr, WH14_Ingr, WH15_Ingr, WH16_Ingr, WH17_Ingr, WH18_Ingr,\
           WH19_Ingr, WH20_Ingr, WH21_Ingr, WH22_Ingr, WH23_Ingr, WH24_Ingr,\
           WI1_Ingr, WI2_Ingr, WI3_Ingr, WI4_Ingr, WI5_Ingr, WI6_Ingr,\
           WI7_Ingr, WI8_Ingr, WI9_Ingr, WI10_Ingr, WI11_Ingr, WI12_Ingr,\
           WI13_Ingr, WI14_Ingr, WI15_Ingr, WI16_Ingr, WI17_Ingr, WI18_Ingr,\
           WI19_Ingr, WI20_Ingr, WI21_Ingr, WI22_Ingr, WI23_Ingr, WI24_Ingr,\
           WJ1_Ingr, WJ2_Ingr, WJ3_Ingr, WJ4_Ingr, WJ5_Ingr, WJ6_Ingr,\
           WJ7_Ingr, WJ8_Ingr, WJ9_Ingr, WJ10_Ingr, WJ11_Ingr, WJ12_Ingr,\
           WJ13_Ingr, WJ14_Ingr, WJ15_Ingr, WJ16_Ingr, WJ17_Ingr, WJ18_Ingr,\
           WJ19_Ingr, WJ20_Ingr, WJ21_Ingr, WJ22_Ingr, WJ23_Ingr, WJ24_Ingr,\
           WK1_Ingr, WK2_Ingr, WK3_Ingr, WK4_Ingr, WK5_Ingr, WK6_Ingr,\
           WK7_Ingr, WK8_Ingr, WK9_Ingr, WK10_Ingr, WK11_Ingr, WK12_Ingr,\
           WK13_Ingr, WK14_Ingr, WK15_Ingr, WK16_Ingr, WK17_Ingr, WK18_Ingr,\
           WK19_Ingr, WK20_Ingr, WK21_Ingr, WK22_Ingr, WK23_Ingr, WK24_Ingr,\
           WL1_Ingr, WL2_Ingr, WL3_Ingr, WL4_Ingr, WL5_Ingr, WL6_Ingr,\
           WL7_Ingr, WL8_Ingr, WL9_Ingr, WL10_Ingr, WL11_Ingr, WL12_Ingr,\
           WL13_Ingr, WL14_Ingr, WL15_Ingr, WL16_Ingr, WL17_Ingr, WL18_Ingr,\
           WL19_Ingr, WL20_Ingr, WL21_Ingr, WL22_Ingr, WL23_Ingr, WL24_Ingr,\
           WM1_Ingr, WM2_Ingr, WM3_Ingr, WM4_Ingr, WM5_Ingr, WM6_Ingr,\
           WM7_Ingr, WM8_Ingr, WM9_Ingr, WM10_Ingr, WM11_Ingr, WM12_Ingr,\
           WM13_Ingr, WM14_Ingr, WM15_Ingr, WM16_Ingr, WM17_Ingr, WM18_Ingr,\
           WM19_Ingr, WM20_Ingr, WM21_Ingr, WM22_Ingr, WM23_Ingr, WM24_Ingr,\
           WN1_Ingr, WN2_Ingr, WN3_Ingr, WN4_Ingr, WN5_Ingr, WN6_Ingr,\
           WN7_Ingr, WN8_Ingr, WN9_Ingr, WN10_Ingr, WN11_Ingr, WN12_Ingr,\
           WN13_Ingr, WN14_Ingr, WN15_Ingr, WN16_Ingr, WN17_Ingr, WN18_Ingr,\
           WN19_Ingr, WN20_Ingr, WN21_Ingr, WN22_Ingr, WN23_Ingr, WN24_Ingr,\
           WO1_Ingr, WO2_Ingr, WO3_Ingr, WO4_Ingr, WO5_Ingr, WO6_Ingr,\
           WO7_Ingr, WO8_Ingr, WO9_Ingr, WO10_Ingr, WO11_Ingr, WO12_Ingr,\
           WO13_Ingr, WO14_Ingr, WO15_Ingr, WO16_Ingr, WO17_Ingr, WO18_Ingr,\
           WO19_Ingr, WO20_Ingr, WO21_Ingr, WO22_Ingr, WO23_Ingr, WO24_Ingr,\
           WP1_Ingr, WP2_Ingr, WP3_Ingr, WP4_Ingr, WP5_Ingr, WP6_Ingr,\
           WP7_Ingr, WP8_Ingr, WP9_Ingr, WP10_Ingr, WP11_Ingr, WP12_Ingr,\
           WP13_Ingr, WP14_Ingr, WP15_Ingr, WP16_Ingr, WP17_Ingr, WP18_Ingr,\
           WP19_Ingr, WP20_Ingr, WP21_Ingr, WP22_Ingr, WP23_Ingr, WP24_Ingr,\
           WA1_Solvent1_Conc, WA2_Solvent1_Conc, WA3_Solvent1_Conc, WA4_Solvent1_Conc, WA5_Solvent1_Conc, WA6_Solvent1_Conc,\
           WA7_Solvent1_Conc, WA8_Solvent1_Conc, WA9_Solvent1_Conc, WA10_Solvent1_Conc, WA11_Solvent1_Conc, WA12_Solvent1_Conc,\
           WA13_Solvent1_Conc, WA14_Solvent1_Conc, WA15_Solvent1_Conc, WA16_Solvent1_Conc, WA17_Solvent1_Conc, WA18_Solvent1_Conc,\
           WA19_Solvent1_Conc, WA20_Solvent1_Conc, WA21_Solvent1_Conc, WA22_Solvent1_Conc, WA23_Solvent1_Conc, WA24_Solvent1_Conc,\
           WB1_Solvent1_Conc, WB2_Solvent1_Conc, WB3_Solvent1_Conc, WB4_Solvent1_Conc, WB5_Solvent1_Conc, WB6_Solvent1_Conc,\
           WB7_Solvent1_Conc, WB8_Solvent1_Conc, WB9_Solvent1_Conc, WB10_Solvent1_Conc, WB11_Solvent1_Conc, WB12_Solvent1_Conc,\
           WB13_Solvent1_Conc, WB14_Solvent1_Conc, WB15_Solvent1_Conc, WB16_Solvent1_Conc, WB17_Solvent1_Conc, WB18_Solvent1_Conc,\
           WB19_Solvent1_Conc, WB20_Solvent1_Conc, WB21_Solvent1_Conc, WB22_Solvent1_Conc, WB23_Solvent1_Conc, WB24_Solvent1_Conc,\
           WC1_Solvent1_Conc, WC2_Solvent1_Conc, WC3_Solvent1_Conc, WC4_Solvent1_Conc, WC5_Solvent1_Conc, WC6_Solvent1_Conc,\
           WC7_Solvent1_Conc, WC8_Solvent1_Conc, WC9_Solvent1_Conc, WC10_Solvent1_Conc, WC11_Solvent1_Conc, WC12_Solvent1_Conc,\
           WC13_Solvent1_Conc, WC14_Solvent1_Conc, WC15_Solvent1_Conc, WC16_Solvent1_Conc, WC17_Solvent1_Conc, WC18_Solvent1_Conc,\
           WC19_Solvent1_Conc, WC20_Solvent1_Conc, WC21_Solvent1_Conc, WC22_Solvent1_Conc, WC23_Solvent1_Conc, WC24_Solvent1_Conc,\
           WD1_Solvent1_Conc, WD2_Solvent1_Conc, WD3_Solvent1_Conc, WD4_Solvent1_Conc, WD5_Solvent1_Conc, WD6_Solvent1_Conc,\
           WD7_Solvent1_Conc, WD8_Solvent1_Conc, WD9_Solvent1_Conc, WD10_Solvent1_Conc, WD11_Solvent1_Conc, WD12_Solvent1_Conc,\
           WD13_Solvent1_Conc, WD14_Solvent1_Conc, WD15_Solvent1_Conc, WD16_Solvent1_Conc, WD17_Solvent1_Conc, WD18_Solvent1_Conc,\
           WD19_Solvent1_Conc, WD20_Solvent1_Conc, WD21_Solvent1_Conc, WD22_Solvent1_Conc, WD23_Solvent1_Conc, WD24_Solvent1_Conc,\
           WE1_Solvent1_Conc, WE2_Solvent1_Conc, WE3_Solvent1_Conc, WE4_Solvent1_Conc, WE5_Solvent1_Conc, WE6_Solvent1_Conc,\
           WE7_Solvent1_Conc, WE8_Solvent1_Conc, WE9_Solvent1_Conc, WE10_Solvent1_Conc, WE11_Solvent1_Conc, WE12_Solvent1_Conc,\
           WE13_Solvent1_Conc, WE14_Solvent1_Conc, WE15_Solvent1_Conc, WE16_Solvent1_Conc, WE17_Solvent1_Conc, WE18_Solvent1_Conc,\
           WE19_Solvent1_Conc, WE20_Solvent1_Conc, WE21_Solvent1_Conc, WE22_Solvent1_Conc, WE23_Solvent1_Conc, WE24_Solvent1_Conc,\
           WF1_Solvent1_Conc, WF2_Solvent1_Conc, WF3_Solvent1_Conc, WF4_Solvent1_Conc, WF5_Solvent1_Conc, WF6_Solvent1_Conc,\
           WF7_Solvent1_Conc, WF8_Solvent1_Conc, WF9_Solvent1_Conc, WF10_Solvent1_Conc, WF11_Solvent1_Conc, WF12_Solvent1_Conc,\
           WF13_Solvent1_Conc, WF14_Solvent1_Conc, WF15_Solvent1_Conc, WF16_Solvent1_Conc, WF17_Solvent1_Conc, WF18_Solvent1_Conc,\
           WF19_Solvent1_Conc, WF20_Solvent1_Conc, WF21_Solvent1_Conc, WF22_Solvent1_Conc, WF23_Solvent1_Conc, WF24_Solvent1_Conc,\
           WG1_Solvent1_Conc, WG2_Solvent1_Conc, WG3_Solvent1_Conc, WG4_Solvent1_Conc, WG5_Solvent1_Conc, WG6_Solvent1_Conc,\
           WG7_Solvent1_Conc, WG8_Solvent1_Conc, WG9_Solvent1_Conc, WG10_Solvent1_Conc, WG11_Solvent1_Conc, WG12_Solvent1_Conc,\
           WG13_Solvent1_Conc, WG14_Solvent1_Conc, WG15_Solvent1_Conc, WG16_Solvent1_Conc, WG17_Solvent1_Conc, WG18_Solvent1_Conc,\
           WG19_Solvent1_Conc, WG20_Solvent1_Conc, WG21_Solvent1_Conc, WG22_Solvent1_Conc, WG23_Solvent1_Conc, WG24_Solvent1_Conc,\
           WH1_Solvent1_Conc, WH2_Solvent1_Conc, WH3_Solvent1_Conc, WH4_Solvent1_Conc, WH5_Solvent1_Conc, WH6_Solvent1_Conc,\
           WH7_Solvent1_Conc, WH8_Solvent1_Conc, WH9_Solvent1_Conc, WH10_Solvent1_Conc, WH11_Solvent1_Conc, WH12_Solvent1_Conc,\
           WH13_Solvent1_Conc, WH14_Solvent1_Conc, WH15_Solvent1_Conc, WH16_Solvent1_Conc, WH17_Solvent1_Conc, WH18_Solvent1_Conc,\
           WH19_Solvent1_Conc, WH20_Solvent1_Conc, WH21_Solvent1_Conc, WH22_Solvent1_Conc, WH23_Solvent1_Conc, WH24_Solvent1_Conc,\
           WI1_Solvent1_Conc, WI2_Solvent1_Conc, WI3_Solvent1_Conc, WI4_Solvent1_Conc, WI5_Solvent1_Conc, WI6_Solvent1_Conc,\
           WI7_Solvent1_Conc, WI8_Solvent1_Conc, WI9_Solvent1_Conc, WI10_Solvent1_Conc, WI11_Solvent1_Conc, WI12_Solvent1_Conc,\
           WI13_Solvent1_Conc, WI14_Solvent1_Conc, WI15_Solvent1_Conc, WI16_Solvent1_Conc, WI17_Solvent1_Conc, WI18_Solvent1_Conc,\
           WI19_Solvent1_Conc, WI20_Solvent1_Conc, WI21_Solvent1_Conc, WI22_Solvent1_Conc, WI23_Solvent1_Conc, WI24_Solvent1_Conc,\
           WJ1_Solvent1_Conc, WJ2_Solvent1_Conc, WJ3_Solvent1_Conc, WJ4_Solvent1_Conc, WJ5_Solvent1_Conc, WJ6_Solvent1_Conc,\
           WJ7_Solvent1_Conc, WJ8_Solvent1_Conc, WJ9_Solvent1_Conc, WJ10_Solvent1_Conc, WJ11_Solvent1_Conc, WJ12_Solvent1_Conc,\
           WJ13_Solvent1_Conc, WJ14_Solvent1_Conc, WJ15_Solvent1_Conc, WJ16_Solvent1_Conc, WJ17_Solvent1_Conc, WJ18_Solvent1_Conc,\
           WJ19_Solvent1_Conc, WJ20_Solvent1_Conc, WJ21_Solvent1_Conc, WJ22_Solvent1_Conc, WJ23_Solvent1_Conc, WJ24_Solvent1_Conc,\
           WK1_Solvent1_Conc, WK2_Solvent1_Conc, WK3_Solvent1_Conc, WK4_Solvent1_Conc, WK5_Solvent1_Conc, WK6_Solvent1_Conc,\
           WK7_Solvent1_Conc, WK8_Solvent1_Conc, WK9_Solvent1_Conc, WK10_Solvent1_Conc, WK11_Solvent1_Conc, WK12_Solvent1_Conc,\
           WK13_Solvent1_Conc, WK14_Solvent1_Conc, WK15_Solvent1_Conc, WK16_Solvent1_Conc, WK17_Solvent1_Conc, WK18_Solvent1_Conc,\
           WK19_Solvent1_Conc, WK20_Solvent1_Conc, WK21_Solvent1_Conc, WK22_Solvent1_Conc, WK23_Solvent1_Conc, WK24_Solvent1_Conc,\
           WL1_Solvent1_Conc, WL2_Solvent1_Conc, WL3_Solvent1_Conc, WL4_Solvent1_Conc, WL5_Solvent1_Conc, WL6_Solvent1_Conc,\
           WL7_Solvent1_Conc, WL8_Solvent1_Conc, WL9_Solvent1_Conc, WL10_Solvent1_Conc, WL11_Solvent1_Conc, WL12_Solvent1_Conc,\
           WL13_Solvent1_Conc, WL14_Solvent1_Conc, WL15_Solvent1_Conc, WL16_Solvent1_Conc, WL17_Solvent1_Conc, WL18_Solvent1_Conc,\
           WL19_Solvent1_Conc, WL20_Solvent1_Conc, WL21_Solvent1_Conc, WL22_Solvent1_Conc, WL23_Solvent1_Conc, WL24_Solvent1_Conc,\
           WM1_Solvent1_Conc, WM2_Solvent1_Conc, WM3_Solvent1_Conc, WM4_Solvent1_Conc, WM5_Solvent1_Conc, WM6_Solvent1_Conc,\
           WM7_Solvent1_Conc, WM8_Solvent1_Conc, WM9_Solvent1_Conc, WM10_Solvent1_Conc, WM11_Solvent1_Conc, WM12_Solvent1_Conc,\
           WM13_Solvent1_Conc, WM14_Solvent1_Conc, WM15_Solvent1_Conc, WM16_Solvent1_Conc, WM17_Solvent1_Conc, WM18_Solvent1_Conc,\
           WM19_Solvent1_Conc, WM20_Solvent1_Conc, WM21_Solvent1_Conc, WM22_Solvent1_Conc, WM23_Solvent1_Conc, WM24_Solvent1_Conc,\
           WN1_Solvent1_Conc, WN2_Solvent1_Conc, WN3_Solvent1_Conc, WN4_Solvent1_Conc, WN5_Solvent1_Conc, WN6_Solvent1_Conc,\
           WN7_Solvent1_Conc, WN8_Solvent1_Conc, WN9_Solvent1_Conc, WN10_Solvent1_Conc, WN11_Solvent1_Conc, WN12_Solvent1_Conc,\
           WN13_Solvent1_Conc, WN14_Solvent1_Conc, WN15_Solvent1_Conc, WN16_Solvent1_Conc, WN17_Solvent1_Conc, WN18_Solvent1_Conc,\
           WN19_Solvent1_Conc, WN20_Solvent1_Conc, WN21_Solvent1_Conc, WN22_Solvent1_Conc, WN23_Solvent1_Conc, WN24_Solvent1_Conc,\
           WO1_Solvent1_Conc, WO2_Solvent1_Conc, WO3_Solvent1_Conc, WO4_Solvent1_Conc, WO5_Solvent1_Conc, WO6_Solvent1_Conc,\
           WO7_Solvent1_Conc, WO8_Solvent1_Conc, WO9_Solvent1_Conc, WO10_Solvent1_Conc, WO11_Solvent1_Conc, WO12_Solvent1_Conc,\
           WO13_Solvent1_Conc, WO14_Solvent1_Conc, WO15_Solvent1_Conc, WO16_Solvent1_Conc, WO17_Solvent1_Conc, WO18_Solvent1_Conc,\
           WO19_Solvent1_Conc, WO20_Solvent1_Conc, WO21_Solvent1_Conc, WO22_Solvent1_Conc, WO23_Solvent1_Conc, WO24_Solvent1_Conc,\
           WP1_Solvent1_Conc, WP2_Solvent1_Conc, WP3_Solvent1_Conc, WP4_Solvent1_Conc, WP5_Solvent1_Conc, WP6_Solvent1_Conc,\
           WP7_Solvent1_Conc, WP8_Solvent1_Conc, WP9_Solvent1_Conc, WP10_Solvent1_Conc, WP11_Solvent1_Conc, WP12_Solvent1_Conc,\
           WP13_Solvent1_Conc, WP14_Solvent1_Conc, WP15_Solvent1_Conc, WP16_Solvent1_Conc, WP17_Solvent1_Conc, WP18_Solvent1_Conc,\
           WP19_Solvent1_Conc, WP20_Solvent1_Conc, WP21_Solvent1_Conc, WP22_Solvent1_Conc, WP23_Solvent1_Conc, WP24_Solvent1_Conc,\
           WA1_Solvent2_Conc, WA2_Solvent2_Conc, WA3_Solvent2_Conc, WA4_Solvent2_Conc, WA5_Solvent2_Conc, WA6_Solvent2_Conc,\
           WA7_Solvent2_Conc, WA8_Solvent2_Conc, WA9_Solvent2_Conc, WA10_Solvent2_Conc, WA11_Solvent2_Conc, WA12_Solvent2_Conc,\
           WA13_Solvent2_Conc, WA14_Solvent2_Conc, WA15_Solvent2_Conc, WA16_Solvent2_Conc, WA17_Solvent2_Conc, WA18_Solvent2_Conc,\
           WA19_Solvent2_Conc, WA20_Solvent2_Conc, WA21_Solvent2_Conc, WA22_Solvent2_Conc, WA23_Solvent2_Conc, WA24_Solvent2_Conc,\
           WB1_Solvent2_Conc, WB2_Solvent2_Conc, WB3_Solvent2_Conc, WB4_Solvent2_Conc, WB5_Solvent2_Conc, WB6_Solvent2_Conc,\
           WB7_Solvent2_Conc, WB8_Solvent2_Conc, WB9_Solvent2_Conc, WB10_Solvent2_Conc, WB11_Solvent2_Conc, WB12_Solvent2_Conc,\
           WB13_Solvent2_Conc, WB14_Solvent2_Conc, WB15_Solvent2_Conc, WB16_Solvent2_Conc, WB17_Solvent2_Conc, WB18_Solvent2_Conc,\
           WB19_Solvent2_Conc, WB20_Solvent2_Conc, WB21_Solvent2_Conc, WB22_Solvent2_Conc, WB23_Solvent2_Conc, WB24_Solvent2_Conc,\
           WC1_Solvent2_Conc, WC2_Solvent2_Conc, WC3_Solvent2_Conc, WC4_Solvent2_Conc, WC5_Solvent2_Conc, WC6_Solvent2_Conc,\
           WC7_Solvent2_Conc, WC8_Solvent2_Conc, WC9_Solvent2_Conc, WC10_Solvent2_Conc, WC11_Solvent2_Conc, WC12_Solvent2_Conc,\
           WC13_Solvent2_Conc, WC14_Solvent2_Conc, WC15_Solvent2_Conc, WC16_Solvent2_Conc, WC17_Solvent2_Conc, WC18_Solvent2_Conc,\
           WC19_Solvent2_Conc, WC20_Solvent2_Conc, WC21_Solvent2_Conc, WC22_Solvent2_Conc, WC23_Solvent2_Conc, WC24_Solvent2_Conc,\
           WD1_Solvent2_Conc, WD2_Solvent2_Conc, WD3_Solvent2_Conc, WD4_Solvent2_Conc, WD5_Solvent2_Conc, WD6_Solvent2_Conc,\
           WD7_Solvent2_Conc, WD8_Solvent2_Conc, WD9_Solvent2_Conc, WD10_Solvent2_Conc, WD11_Solvent2_Conc, WD12_Solvent2_Conc,\
           WD13_Solvent2_Conc, WD14_Solvent2_Conc, WD15_Solvent2_Conc, WD16_Solvent2_Conc, WD17_Solvent2_Conc, WD18_Solvent2_Conc,\
           WD19_Solvent2_Conc, WD20_Solvent2_Conc, WD21_Solvent2_Conc, WD22_Solvent2_Conc, WD23_Solvent2_Conc, WD24_Solvent2_Conc,\
           WE1_Solvent2_Conc, WE2_Solvent2_Conc, WE3_Solvent2_Conc, WE4_Solvent2_Conc, WE5_Solvent2_Conc, WE6_Solvent2_Conc,\
           WE7_Solvent2_Conc, WE8_Solvent2_Conc, WE9_Solvent2_Conc, WE10_Solvent2_Conc, WE11_Solvent2_Conc, WE12_Solvent2_Conc,\
           WE13_Solvent2_Conc, WE14_Solvent2_Conc, WE15_Solvent2_Conc, WE16_Solvent2_Conc, WE17_Solvent2_Conc, WE18_Solvent2_Conc,\
           WE19_Solvent2_Conc, WE20_Solvent2_Conc, WE21_Solvent2_Conc, WE22_Solvent2_Conc, WE23_Solvent2_Conc, WE24_Solvent2_Conc,\
           WF1_Solvent2_Conc, WF2_Solvent2_Conc, WF3_Solvent2_Conc, WF4_Solvent2_Conc, WF5_Solvent2_Conc, WF6_Solvent2_Conc,\
           WF7_Solvent2_Conc, WF8_Solvent2_Conc, WF9_Solvent2_Conc, WF10_Solvent2_Conc, WF11_Solvent2_Conc, WF12_Solvent2_Conc,\
           WF13_Solvent2_Conc, WF14_Solvent2_Conc, WF15_Solvent2_Conc, WF16_Solvent2_Conc, WF17_Solvent2_Conc, WF18_Solvent2_Conc,\
           WF19_Solvent2_Conc, WF20_Solvent2_Conc, WF21_Solvent2_Conc, WF22_Solvent2_Conc, WF23_Solvent2_Conc, WF24_Solvent2_Conc,\
           WG1_Solvent2_Conc, WG2_Solvent2_Conc, WG3_Solvent2_Conc, WG4_Solvent2_Conc, WG5_Solvent2_Conc, WG6_Solvent2_Conc,\
           WG7_Solvent2_Conc, WG8_Solvent2_Conc, WG9_Solvent2_Conc, WG10_Solvent2_Conc, WG11_Solvent2_Conc, WG12_Solvent2_Conc,\
           WG13_Solvent2_Conc, WG14_Solvent2_Conc, WG15_Solvent2_Conc, WG16_Solvent2_Conc, WG17_Solvent2_Conc, WG18_Solvent2_Conc,\
           WG19_Solvent2_Conc, WG20_Solvent2_Conc, WG21_Solvent2_Conc, WG22_Solvent2_Conc, WG23_Solvent2_Conc, WG24_Solvent2_Conc,\
           WH1_Solvent2_Conc, WH2_Solvent2_Conc, WH3_Solvent2_Conc, WH4_Solvent2_Conc, WH5_Solvent2_Conc, WH6_Solvent2_Conc,\
           WH7_Solvent2_Conc, WH8_Solvent2_Conc, WH9_Solvent2_Conc, WH10_Solvent2_Conc, WH11_Solvent2_Conc, WH12_Solvent2_Conc,\
           WH13_Solvent2_Conc, WH14_Solvent2_Conc, WH15_Solvent2_Conc, WH16_Solvent2_Conc, WH17_Solvent2_Conc, WH18_Solvent2_Conc,\
           WH19_Solvent2_Conc, WH20_Solvent2_Conc, WH21_Solvent2_Conc, WH22_Solvent2_Conc, WH23_Solvent2_Conc, WH24_Solvent2_Conc,\
           WI1_Solvent2_Conc, WI2_Solvent2_Conc, WI3_Solvent2_Conc, WI4_Solvent2_Conc, WI5_Solvent2_Conc, WI6_Solvent2_Conc,\
           WI7_Solvent2_Conc, WI8_Solvent2_Conc, WI9_Solvent2_Conc, WI10_Solvent2_Conc, WI11_Solvent2_Conc, WI12_Solvent2_Conc,\
           WI13_Solvent2_Conc, WI14_Solvent2_Conc, WI15_Solvent2_Conc, WI16_Solvent2_Conc, WI17_Solvent2_Conc, WI18_Solvent2_Conc,\
           WI19_Solvent2_Conc, WI20_Solvent2_Conc, WI21_Solvent2_Conc, WI22_Solvent2_Conc, WI23_Solvent2_Conc, WI24_Solvent2_Conc,\
           WJ1_Solvent2_Conc, WJ2_Solvent2_Conc, WJ3_Solvent2_Conc, WJ4_Solvent2_Conc, WJ5_Solvent2_Conc, WJ6_Solvent2_Conc,\
           WJ7_Solvent2_Conc, WJ8_Solvent2_Conc, WJ9_Solvent2_Conc, WJ10_Solvent2_Conc, WJ11_Solvent2_Conc, WJ12_Solvent2_Conc,\
           WJ13_Solvent2_Conc, WJ14_Solvent2_Conc, WJ15_Solvent2_Conc, WJ16_Solvent2_Conc, WJ17_Solvent2_Conc, WJ18_Solvent2_Conc,\
           WJ19_Solvent2_Conc, WJ20_Solvent2_Conc, WJ21_Solvent2_Conc, WJ22_Solvent2_Conc, WJ23_Solvent2_Conc, WJ24_Solvent2_Conc,\
           WK1_Solvent2_Conc, WK2_Solvent2_Conc, WK3_Solvent2_Conc, WK4_Solvent2_Conc, WK5_Solvent2_Conc, WK6_Solvent2_Conc,\
           WK7_Solvent2_Conc, WK8_Solvent2_Conc, WK9_Solvent2_Conc, WK10_Solvent2_Conc, WK11_Solvent2_Conc, WK12_Solvent2_Conc,\
           WK13_Solvent2_Conc, WK14_Solvent2_Conc, WK15_Solvent2_Conc, WK16_Solvent2_Conc, WK17_Solvent2_Conc, WK18_Solvent2_Conc,\
           WK19_Solvent2_Conc, WK20_Solvent2_Conc, WK21_Solvent2_Conc, WK22_Solvent2_Conc, WK23_Solvent2_Conc, WK24_Solvent2_Conc,\
           WL1_Solvent2_Conc, WL2_Solvent2_Conc, WL3_Solvent2_Conc, WL4_Solvent2_Conc, WL5_Solvent2_Conc, WL6_Solvent2_Conc,\
           WL7_Solvent2_Conc, WL8_Solvent2_Conc, WL9_Solvent2_Conc, WL10_Solvent2_Conc, WL11_Solvent2_Conc, WL12_Solvent2_Conc,\
           WL13_Solvent2_Conc, WL14_Solvent2_Conc, WL15_Solvent2_Conc, WL16_Solvent2_Conc, WL17_Solvent2_Conc, WL18_Solvent2_Conc,\
           WL19_Solvent2_Conc, WL20_Solvent2_Conc, WL21_Solvent2_Conc, WL22_Solvent2_Conc, WL23_Solvent2_Conc, WL24_Solvent2_Conc,\
           WM1_Solvent2_Conc, WM2_Solvent2_Conc, WM3_Solvent2_Conc, WM4_Solvent2_Conc, WM5_Solvent2_Conc, WM6_Solvent2_Conc,\
           WM7_Solvent2_Conc, WM8_Solvent2_Conc, WM9_Solvent2_Conc, WM10_Solvent2_Conc, WM11_Solvent2_Conc, WM12_Solvent2_Conc,\
           WM13_Solvent2_Conc, WM14_Solvent2_Conc, WM15_Solvent2_Conc, WM16_Solvent2_Conc, WM17_Solvent2_Conc, WM18_Solvent2_Conc,\
           WM19_Solvent2_Conc, WM20_Solvent2_Conc, WM21_Solvent2_Conc, WM22_Solvent2_Conc, WM23_Solvent2_Conc, WM24_Solvent2_Conc,\
           WN1_Solvent2_Conc, WN2_Solvent2_Conc, WN3_Solvent2_Conc, WN4_Solvent2_Conc, WN5_Solvent2_Conc, WN6_Solvent2_Conc,\
           WN7_Solvent2_Conc, WN8_Solvent2_Conc, WN9_Solvent2_Conc, WN10_Solvent2_Conc, WN11_Solvent2_Conc, WN12_Solvent2_Conc,\
           WN13_Solvent2_Conc, WN14_Solvent2_Conc, WN15_Solvent2_Conc, WN16_Solvent2_Conc, WN17_Solvent2_Conc, WN18_Solvent2_Conc,\
           WN19_Solvent2_Conc, WN20_Solvent2_Conc, WN21_Solvent2_Conc, WN22_Solvent2_Conc, WN23_Solvent2_Conc, WN24_Solvent2_Conc,\
           WO1_Solvent2_Conc, WO2_Solvent2_Conc, WO3_Solvent2_Conc, WO4_Solvent2_Conc, WO5_Solvent2_Conc, WO6_Solvent2_Conc,\
           WO7_Solvent2_Conc, WO8_Solvent2_Conc, WO9_Solvent2_Conc, WO10_Solvent2_Conc, WO11_Solvent2_Conc, WO12_Solvent2_Conc,\
           WO13_Solvent2_Conc, WO14_Solvent2_Conc, WO15_Solvent2_Conc, WO16_Solvent2_Conc, WO17_Solvent2_Conc, WO18_Solvent2_Conc,\
           WO19_Solvent2_Conc, WO20_Solvent2_Conc, WO21_Solvent2_Conc, WO22_Solvent2_Conc, WO23_Solvent2_Conc, WO24_Solvent2_Conc,\
           WP1_Solvent2_Conc, WP2_Solvent2_Conc, WP3_Solvent2_Conc, WP4_Solvent2_Conc, WP5_Solvent2_Conc, WP6_Solvent2_Conc,\
           WP7_Solvent2_Conc, WP8_Solvent2_Conc, WP9_Solvent2_Conc, WP10_Solvent2_Conc, WP11_Solvent2_Conc, WP12_Solvent2_Conc,\
           WP13_Solvent2_Conc, WP14_Solvent2_Conc, WP15_Solvent2_Conc, WP16_Solvent2_Conc, WP17_Solvent2_Conc, WP18_Solvent2_Conc,\
           WP19_Solvent2_Conc, WP20_Solvent2_Conc, WP21_Solvent2_Conc, WP22_Solvent2_Conc, WP23_Solvent2_Conc, WP24_Solvent2_Conc,\
           WA1_SS_Conc, WA2_SS_Conc, WA3_SS_Conc, WA4_SS_Conc, WA5_SS_Conc, WA6_SS_Conc,\
           WA7_SS_Conc, WA8_SS_Conc, WA9_SS_Conc, WA10_SS_Conc, WA11_SS_Conc, WA12_SS_Conc,\
           WA13_SS_Conc, WA14_SS_Conc, WA15_SS_Conc, WA16_SS_Conc, WA17_SS_Conc, WA18_SS_Conc,\
           WA19_SS_Conc, WA20_SS_Conc, WA21_SS_Conc, WA22_SS_Conc, WA23_SS_Conc, WA24_SS_Conc,\
           WB1_SS_Conc, WB2_SS_Conc, WB3_SS_Conc, WB4_SS_Conc, WB5_SS_Conc, WB6_SS_Conc,\
           WB7_SS_Conc, WB8_SS_Conc, WB9_SS_Conc, WB10_SS_Conc, WB11_SS_Conc, WB12_SS_Conc,\
           WB13_SS_Conc, WB14_SS_Conc, WB15_SS_Conc, WB16_SS_Conc, WB17_SS_Conc, WB18_SS_Conc,\
           WB19_SS_Conc, WB20_SS_Conc, WB21_SS_Conc, WB22_SS_Conc, WB23_SS_Conc, WB24_SS_Conc,\
           WC1_SS_Conc, WC2_SS_Conc, WC3_SS_Conc, WC4_SS_Conc, WC5_SS_Conc, WC6_SS_Conc,\
           WC7_SS_Conc, WC8_SS_Conc, WC9_SS_Conc, WC10_SS_Conc, WC11_SS_Conc, WC12_SS_Conc,\
           WC13_SS_Conc, WC14_SS_Conc, WC15_SS_Conc, WC16_SS_Conc, WC17_SS_Conc, WC18_SS_Conc,\
           WC19_SS_Conc, WC20_SS_Conc, WC21_SS_Conc, WC22_SS_Conc, WC23_SS_Conc, WC24_SS_Conc,\
           WD1_SS_Conc, WD2_SS_Conc, WD3_SS_Conc, WD4_SS_Conc, WD5_SS_Conc, WD6_SS_Conc,\
           WD7_SS_Conc, WD8_SS_Conc, WD9_SS_Conc, WD10_SS_Conc, WD11_SS_Conc, WD12_SS_Conc,\
           WD13_SS_Conc, WD14_SS_Conc, WD15_SS_Conc, WD16_SS_Conc, WD17_SS_Conc, WD18_SS_Conc,\
           WD19_SS_Conc, WD20_SS_Conc, WD21_SS_Conc, WD22_SS_Conc, WD23_SS_Conc, WD24_SS_Conc,\
           WE1_SS_Conc, WE2_SS_Conc, WE3_SS_Conc, WE4_SS_Conc, WE5_SS_Conc, WE6_SS_Conc,\
           WE7_SS_Conc, WE8_SS_Conc, WE9_SS_Conc, WE10_SS_Conc, WE11_SS_Conc, WE12_SS_Conc,\
           WE13_SS_Conc, WE14_SS_Conc, WE15_SS_Conc, WE16_SS_Conc, WE17_SS_Conc, WE18_SS_Conc,\
           WE19_SS_Conc, WE20_SS_Conc, WE21_SS_Conc, WE22_SS_Conc, WE23_SS_Conc, WE24_SS_Conc,\
           WF1_SS_Conc, WF2_SS_Conc, WF3_SS_Conc, WF4_SS_Conc, WF5_SS_Conc, WF6_SS_Conc,\
           WF7_SS_Conc, WF8_SS_Conc, WF9_SS_Conc, WF10_SS_Conc, WF11_SS_Conc, WF12_SS_Conc,\
           WF13_SS_Conc, WF14_SS_Conc, WF15_SS_Conc, WF16_SS_Conc, WF17_SS_Conc, WF18_SS_Conc,\
           WF19_SS_Conc, WF20_SS_Conc, WF21_SS_Conc, WF22_SS_Conc, WF23_SS_Conc, WF24_SS_Conc,\
           WG1_SS_Conc, WG2_SS_Conc, WG3_SS_Conc, WG4_SS_Conc, WG5_SS_Conc, WG6_SS_Conc,\
           WG7_SS_Conc, WG8_SS_Conc, WG9_SS_Conc, WG10_SS_Conc, WG11_SS_Conc, WG12_SS_Conc,\
           WG13_SS_Conc, WG14_SS_Conc, WG15_SS_Conc, WG16_SS_Conc, WG17_SS_Conc, WG18_SS_Conc,\
           WG19_SS_Conc, WG20_SS_Conc, WG21_SS_Conc, WG22_SS_Conc, WG23_SS_Conc, WG24_SS_Conc,\
           WH1_SS_Conc, WH2_SS_Conc, WH3_SS_Conc, WH4_SS_Conc, WH5_SS_Conc, WH6_SS_Conc,\
           WH7_SS_Conc, WH8_SS_Conc, WH9_SS_Conc, WH10_SS_Conc, WH11_SS_Conc, WH12_SS_Conc,\
           WH13_SS_Conc, WH14_SS_Conc, WH15_SS_Conc, WH16_SS_Conc, WH17_SS_Conc, WH18_SS_Conc,\
           WH19_SS_Conc, WH20_SS_Conc, WH21_SS_Conc, WH22_SS_Conc, WH23_SS_Conc, WH24_SS_Conc,\
           WI1_SS_Conc, WI2_SS_Conc, WI3_SS_Conc, WI4_SS_Conc, WI5_SS_Conc, WI6_SS_Conc,\
           WI7_SS_Conc, WI8_SS_Conc, WI9_SS_Conc, WI10_SS_Conc, WI11_SS_Conc, WI12_SS_Conc,\
           WI13_SS_Conc, WI14_SS_Conc, WI15_SS_Conc, WI16_SS_Conc, WI17_SS_Conc, WI18_SS_Conc,\
           WI19_SS_Conc, WI20_SS_Conc, WI21_SS_Conc, WI22_SS_Conc, WI23_SS_Conc, WI24_SS_Conc,\
           WJ1_SS_Conc, WJ2_SS_Conc, WJ3_SS_Conc, WJ4_SS_Conc, WJ5_SS_Conc, WJ6_SS_Conc,\
           WJ7_SS_Conc, WJ8_SS_Conc, WJ9_SS_Conc, WJ10_SS_Conc, WJ11_SS_Conc, WJ12_SS_Conc,\
           WJ13_SS_Conc, WJ14_SS_Conc, WJ15_SS_Conc, WJ16_SS_Conc, WJ17_SS_Conc, WJ18_SS_Conc,\
           WJ19_SS_Conc, WJ20_SS_Conc, WJ21_SS_Conc, WJ22_SS_Conc, WJ23_SS_Conc, WJ24_SS_Conc,\
           WK1_SS_Conc, WK2_SS_Conc, WK3_SS_Conc, WK4_SS_Conc, WK5_SS_Conc, WK6_SS_Conc,\
           WK7_SS_Conc, WK8_SS_Conc, WK9_SS_Conc, WK10_SS_Conc, WK11_SS_Conc, WK12_SS_Conc,\
           WK13_SS_Conc, WK14_SS_Conc, WK15_SS_Conc, WK16_SS_Conc, WK17_SS_Conc, WK18_SS_Conc,\
           WK19_SS_Conc, WK20_SS_Conc, WK21_SS_Conc, WK22_SS_Conc, WK23_SS_Conc, WK24_SS_Conc,\
           WL1_SS_Conc, WL2_SS_Conc, WL3_SS_Conc, WL4_SS_Conc, WL5_SS_Conc, WL6_SS_Conc,\
           WL7_SS_Conc, WL8_SS_Conc, WL9_SS_Conc, WL10_SS_Conc, WL11_SS_Conc, WL12_SS_Conc,\
           WL13_SS_Conc, WL14_SS_Conc, WL15_SS_Conc, WL16_SS_Conc, WL17_SS_Conc, WL18_SS_Conc,\
           WL19_SS_Conc, WL20_SS_Conc, WL21_SS_Conc, WL22_SS_Conc, WL23_SS_Conc, WL24_SS_Conc,\
           WM1_SS_Conc, WM2_SS_Conc, WM3_SS_Conc, WM4_SS_Conc, WM5_SS_Conc, WM6_SS_Conc,\
           WM7_SS_Conc, WM8_SS_Conc, WM9_SS_Conc, WM10_SS_Conc, WM11_SS_Conc, WM12_SS_Conc,\
           WM13_SS_Conc, WM14_SS_Conc, WM15_SS_Conc, WM16_SS_Conc, WM17_SS_Conc, WM18_SS_Conc,\
           WM19_SS_Conc, WM20_SS_Conc, WM21_SS_Conc, WM22_SS_Conc, WM23_SS_Conc, WM24_SS_Conc,\
           WN1_SS_Conc, WN2_SS_Conc, WN3_SS_Conc, WN4_SS_Conc, WN5_SS_Conc, WN6_SS_Conc,\
           WN7_SS_Conc, WN8_SS_Conc, WN9_SS_Conc, WN10_SS_Conc, WN11_SS_Conc, WN12_SS_Conc,\
           WN13_SS_Conc, WN14_SS_Conc, WN15_SS_Conc, WN16_SS_Conc, WN17_SS_Conc, WN18_SS_Conc,\
           WN19_SS_Conc, WN20_SS_Conc, WN21_SS_Conc, WN22_SS_Conc, WN23_SS_Conc, WN24_SS_Conc,\
           WO1_SS_Conc, WO2_SS_Conc, WO3_SS_Conc, WO4_SS_Conc, WO5_SS_Conc, WO6_SS_Conc,\
           WO7_SS_Conc, WO8_SS_Conc, WO9_SS_Conc, WO10_SS_Conc, WO11_SS_Conc, WO12_SS_Conc,\
           WO13_SS_Conc, WO14_SS_Conc, WO15_SS_Conc, WO16_SS_Conc, WO17_SS_Conc, WO18_SS_Conc,\
           WO19_SS_Conc, WO20_SS_Conc, WO21_SS_Conc, WO22_SS_Conc, WO23_SS_Conc, WO24_SS_Conc,\
           WP1_SS_Conc, WP2_SS_Conc, WP3_SS_Conc, WP4_SS_Conc, WP5_SS_Conc, WP6_SS_Conc,\
           WP7_SS_Conc, WP8_SS_Conc, WP9_SS_Conc, WP10_SS_Conc, WP11_SS_Conc, WP12_SS_Conc,\
           WP13_SS_Conc, WP14_SS_Conc, WP15_SS_Conc, WP16_SS_Conc, WP17_SS_Conc, WP18_SS_Conc,\
           WP19_SS_Conc, WP20_SS_Conc, WP21_SS_Conc, WP22_SS_Conc, WP23_SS_Conc, WP24_SS_Conc,\
           WA1_Vol, WA2_Vol, WA3_Vol, WA4_Vol, WA5_Vol, WA6_Vol,\
           WA7_Vol, WA8_Vol, WA9_Vol, WA10_Vol, WA11_Vol, WA12_Vol,\
           WA13_Vol, WA14_Vol, WA15_Vol, WA16_Vol, WA17_Vol, WA18_Vol,\
           WA19_Vol, WA20_Vol, WA21_Vol, WA22_Vol, WA23_Vol, WA24_Vol,\
           WB1_Vol, WB2_Vol, WB3_Vol, WB4_Vol, WB5_Vol, WB6_Vol,\
           WB7_Vol, WB8_Vol, WB9_Vol, WB10_Vol, WB11_Vol, WB12_Vol,\
           WB13_Vol, WB14_Vol, WB15_Vol, WB16_Vol, WB17_Vol, WB18_Vol,\
           WB19_Vol, WB20_Vol, WB21_Vol, WB22_Vol, WB23_Vol, WB24_Vol,\
           WC1_Vol, WC2_Vol, WC3_Vol, WC4_Vol, WC5_Vol, WC6_Vol,\
           WC7_Vol, WC8_Vol, WC9_Vol, WC10_Vol, WC11_Vol, WC12_Vol,\
           WC13_Vol, WC14_Vol, WC15_Vol, WC16_Vol, WC17_Vol, WC18_Vol,\
           WC19_Vol, WC20_Vol, WC21_Vol, WC22_Vol, WC23_Vol, WC24_Vol,\
           WD1_Vol, WD2_Vol, WD3_Vol, WD4_Vol, WD5_Vol, WD6_Vol,\
           WD7_Vol, WD8_Vol, WD9_Vol, WD10_Vol, WD11_Vol, WD12_Vol,\
           WD13_Vol, WD14_Vol, WD15_Vol, WD16_Vol, WD17_Vol, WD18_Vol,\
           WD19_Vol, WD20_Vol, WD21_Vol, WD22_Vol, WD23_Vol, WD24_Vol,\
           WE1_Vol, WE2_Vol, WE3_Vol, WE4_Vol, WE5_Vol, WE6_Vol,\
           WE7_Vol, WE8_Vol, WE9_Vol, WE10_Vol, WE11_Vol, WE12_Vol,\
           WE13_Vol, WE14_Vol, WE15_Vol, WE16_Vol, WE17_Vol, WE18_Vol,\
           WE19_Vol, WE20_Vol, WE21_Vol, WE22_Vol, WE23_Vol, WE24_Vol,\
           WF1_Vol, WF2_Vol, WF3_Vol, WF4_Vol, WF5_Vol, WF6_Vol,\
           WF7_Vol, WF8_Vol, WF9_Vol, WF10_Vol, WF11_Vol, WF12_Vol,\
           WF13_Vol, WF14_Vol, WF15_Vol, WF16_Vol, WF17_Vol, WF18_Vol,\
           WF19_Vol, WF20_Vol, WF21_Vol, WF22_Vol, WF23_Vol, WF24_Vol,\
           WG1_Vol, WG2_Vol, WG3_Vol, WG4_Vol, WG5_Vol, WG6_Vol,\
           WG7_Vol, WG8_Vol, WG9_Vol, WG10_Vol, WG11_Vol, WG12_Vol,\
           WG13_Vol, WG14_Vol, WG15_Vol, WG16_Vol, WG17_Vol, WG18_Vol,\
           WG19_Vol, WG20_Vol, WG21_Vol, WG22_Vol, WG23_Vol, WG24_Vol,\
           WH1_Vol, WH2_Vol, WH3_Vol, WH4_Vol, WH5_Vol, WH6_Vol,\
           WH7_Vol, WH8_Vol, WH9_Vol, WH10_Vol, WH11_Vol, WH12_Vol,\
           WH13_Vol, WH14_Vol, WH15_Vol, WH16_Vol, WH17_Vol, WH18_Vol,\
           WH19_Vol, WH20_Vol, WH21_Vol, WH22_Vol, WH23_Vol, WH24_Vol,\
           WI1_Vol, WI2_Vol, WI3_Vol, WI4_Vol, WI5_Vol, WI6_Vol,\
           WI7_Vol, WI8_Vol, WI9_Vol, WI10_Vol, WI11_Vol, WI12_Vol,\
           WI13_Vol, WI14_Vol, WI15_Vol, WI16_Vol, WI17_Vol, WI18_Vol,\
           WI19_Vol, WI20_Vol, WI21_Vol, WI22_Vol, WI23_Vol, WI24_Vol,\
           WJ1_Vol, WJ2_Vol, WJ3_Vol, WJ4_Vol, WJ5_Vol, WJ6_Vol,\
           WJ7_Vol, WJ8_Vol, WJ9_Vol, WJ10_Vol, WJ11_Vol, WJ12_Vol,\
           WJ13_Vol, WJ14_Vol, WJ15_Vol, WJ16_Vol, WJ17_Vol, WJ18_Vol,\
           WJ19_Vol, WJ20_Vol, WJ21_Vol, WJ22_Vol, WJ23_Vol, WJ24_Vol,\
           WK1_Vol, WK2_Vol, WK3_Vol, WK4_Vol, WK5_Vol, WK6_Vol,\
           WK7_Vol, WK8_Vol, WK9_Vol, WK10_Vol, WK11_Vol, WK12_Vol,\
           WK13_Vol, WK14_Vol, WK15_Vol, WK16_Vol, WK17_Vol, WK18_Vol,\
           WK19_Vol, WK20_Vol, WK21_Vol, WK22_Vol, WK23_Vol, WK24_Vol,\
           WL1_Vol, WL2_Vol, WL3_Vol, WL4_Vol, WL5_Vol, WL6_Vol,\
           WL7_Vol, WL8_Vol, WL9_Vol, WL10_Vol, WL11_Vol, WL12_Vol,\
           WL13_Vol, WL14_Vol, WL15_Vol, WL16_Vol, WL17_Vol, WL18_Vol,\
           WL19_Vol, WL20_Vol, WL21_Vol, WL22_Vol, WL23_Vol, WL24_Vol,\
           WM1_Vol, WM2_Vol, WM3_Vol, WM4_Vol, WM5_Vol, WM6_Vol,\
           WM7_Vol, WM8_Vol, WM9_Vol, WM10_Vol, WM11_Vol, WM12_Vol,\
           WM13_Vol, WM14_Vol, WM15_Vol, WM16_Vol, WM17_Vol, WM18_Vol,\
           WM19_Vol, WM20_Vol, WM21_Vol, WM22_Vol, WM23_Vol, WM24_Vol,\
           WN1_Vol, WN2_Vol, WN3_Vol, WN4_Vol, WN5_Vol, WN6_Vol,\
           WN7_Vol, WN8_Vol, WN9_Vol, WN10_Vol, WN11_Vol, WN12_Vol,\
           WN13_Vol, WN14_Vol, WN15_Vol, WN16_Vol, WN17_Vol, WN18_Vol,\
           WN19_Vol, WN20_Vol, WN21_Vol, WN22_Vol, WN23_Vol, WN24_Vol,\
           WO1_Vol, WO2_Vol, WO3_Vol, WO4_Vol, WO5_Vol, WO6_Vol,\
           WO7_Vol, WO8_Vol, WO9_Vol, WO10_Vol, WO11_Vol, WO12_Vol,\
           WO13_Vol, WO14_Vol, WO15_Vol, WO16_Vol, WO17_Vol, WO18_Vol,\
           WO19_Vol, WO20_Vol, WO21_Vol, WO22_Vol, WO23_Vol, WO24_Vol,\
           WP1_Vol, WP2_Vol, WP3_Vol, WP4_Vol, WP5_Vol, WP6_Vol,\
           WP7_Vol, WP8_Vol, WP9_Vol, WP10_Vol, WP11_Vol, WP12_Vol,\
           WP13_Vol, WP14_Vol, WP15_Vol, WP16_Vol, WP17_Vol, WP18_Vol,\
           WP19_Vol, WP20_Vol, WP21_Vol, WP22_Vol, WP23_Vol, WP24_Vol,\
           WA1_IngrMenu, WA2_IngrMenu, WA3_IngrMenu, WA4_IngrMenu, WA5_IngrMenu, WA6_IngrMenu,\
           WA7_IngrMenu, WA8_IngrMenu, WA9_IngrMenu, WA10_IngrMenu, WA11_IngrMenu, WA12_IngrMenu,\
           WA13_IngrMenu, WA14_IngrMenu, WA15_IngrMenu, WA16_IngrMenu, WA17_IngrMenu, WA18_IngrMenu,\
           WA19_IngrMenu, WA20_IngrMenu, WA21_IngrMenu, WA22_IngrMenu, WA23_IngrMenu, WA24_IngrMenu,\
           WB1_IngrMenu, WB2_IngrMenu, WB3_IngrMenu, WB4_IngrMenu, WB5_IngrMenu, WB6_IngrMenu,\
           WB7_IngrMenu, WB8_IngrMenu, WB9_IngrMenu, WB10_IngrMenu, WB11_IngrMenu, WB12_IngrMenu,\
           WB13_IngrMenu, WB14_IngrMenu, WB15_IngrMenu, WB16_IngrMenu, WB17_IngrMenu, WB18_IngrMenu,\
           WB19_IngrMenu, WB20_IngrMenu, WB21_IngrMenu, WB22_IngrMenu, WB23_IngrMenu, WB24_IngrMenu,\
           WC1_IngrMenu, WC2_IngrMenu, WC3_IngrMenu, WC4_IngrMenu, WC5_IngrMenu, WC6_IngrMenu,\
           WC7_IngrMenu, WC8_IngrMenu, WC9_IngrMenu, WC10_IngrMenu, WC11_IngrMenu, WC12_IngrMenu,\
           WC13_IngrMenu, WC14_IngrMenu, WC15_IngrMenu, WC16_IngrMenu, WC17_IngrMenu, WC18_IngrMenu,\
           WC19_IngrMenu, WC20_IngrMenu, WC21_IngrMenu, WC22_IngrMenu, WC23_IngrMenu, WC24_IngrMenu,\
           WD1_IngrMenu, WD2_IngrMenu, WD3_IngrMenu, WD4_IngrMenu, WD5_IngrMenu, WD6_IngrMenu,\
           WD7_IngrMenu, WD8_IngrMenu, WD9_IngrMenu, WD10_IngrMenu, WD11_IngrMenu, WD12_IngrMenu,\
           WD13_IngrMenu, WD14_IngrMenu, WD15_IngrMenu, WD16_IngrMenu, WD17_IngrMenu, WD18_IngrMenu,\
           WD19_IngrMenu, WD20_IngrMenu, WD21_IngrMenu, WD22_IngrMenu, WD23_IngrMenu, WD24_IngrMenu,\
           WE1_IngrMenu, WE2_IngrMenu, WE3_IngrMenu, WE4_IngrMenu, WE5_IngrMenu, WE6_IngrMenu,\
           WE7_IngrMenu, WE8_IngrMenu, WE9_IngrMenu, WE10_IngrMenu, WE11_IngrMenu, WE12_IngrMenu,\
           WE13_IngrMenu, WE14_IngrMenu, WE15_IngrMenu, WE16_IngrMenu, WE17_IngrMenu, WE18_IngrMenu,\
           WE19_IngrMenu, WE20_IngrMenu, WE21_IngrMenu, WE22_IngrMenu, WE23_IngrMenu, WE24_IngrMenu,\
           WF1_IngrMenu, WF2_IngrMenu, WF3_IngrMenu, WF4_IngrMenu, WF5_IngrMenu, WF6_IngrMenu,\
           WF7_IngrMenu, WF8_IngrMenu, WF9_IngrMenu, WF10_IngrMenu, WF11_IngrMenu, WF12_IngrMenu,\
           WF13_IngrMenu, WF14_IngrMenu, WF15_IngrMenu, WF16_IngrMenu, WF17_IngrMenu, WF18_IngrMenu,\
           WF19_IngrMenu, WF20_IngrMenu, WF21_IngrMenu, WF22_IngrMenu, WF23_IngrMenu, WF24_IngrMenu,\
           WG1_IngrMenu, WG2_IngrMenu, WG3_IngrMenu, WG4_IngrMenu, WG5_IngrMenu, WG6_IngrMenu,\
           WG7_IngrMenu, WG8_IngrMenu, WG9_IngrMenu, WG10_IngrMenu, WG11_IngrMenu, WG12_IngrMenu,\
           WG13_IngrMenu, WG14_IngrMenu, WG15_IngrMenu, WG16_IngrMenu, WG17_IngrMenu, WG18_IngrMenu,\
           WG19_IngrMenu, WG20_IngrMenu, WG21_IngrMenu, WG22_IngrMenu, WG23_IngrMenu, WG24_IngrMenu,\
           WH1_IngrMenu, WH2_IngrMenu, WH3_IngrMenu, WH4_IngrMenu, WH5_IngrMenu, WH6_IngrMenu,\
           WH7_IngrMenu, WH8_IngrMenu, WH9_IngrMenu, WH10_IngrMenu, WH11_IngrMenu, WH12_IngrMenu,\
           WH13_IngrMenu, WH14_IngrMenu, WH15_IngrMenu, WH16_IngrMenu, WH17_IngrMenu, WH18_IngrMenu,\
           WH19_IngrMenu, WH20_IngrMenu, WH21_IngrMenu, WH22_IngrMenu, WH23_IngrMenu, WH24_IngrMenu,\
           WI1_IngrMenu, WI2_IngrMenu, WI3_IngrMenu, WI4_IngrMenu, WI5_IngrMenu, WI6_IngrMenu,\
           WI7_IngrMenu, WI8_IngrMenu, WI9_IngrMenu, WI10_IngrMenu, WI11_IngrMenu, WI12_IngrMenu,\
           WI13_IngrMenu, WI14_IngrMenu, WI15_IngrMenu, WI16_IngrMenu, WI17_IngrMenu, WI18_IngrMenu,\
           WI19_IngrMenu, WI20_IngrMenu, WI21_IngrMenu, WI22_IngrMenu, WI23_IngrMenu, WI24_IngrMenu,\
           WJ1_IngrMenu, WJ2_IngrMenu, WJ3_IngrMenu, WJ4_IngrMenu, WJ5_IngrMenu, WJ6_IngrMenu,\
           WJ7_IngrMenu, WJ8_IngrMenu, WJ9_IngrMenu, WJ10_IngrMenu, WJ11_IngrMenu, WJ12_IngrMenu,\
           WJ13_IngrMenu, WJ14_IngrMenu, WJ15_IngrMenu, WJ16_IngrMenu, WJ17_IngrMenu, WJ18_IngrMenu,\
           WJ19_IngrMenu, WJ20_IngrMenu, WJ21_IngrMenu, WJ22_IngrMenu, WJ23_IngrMenu, WJ24_IngrMenu,\
           WK1_IngrMenu, WK2_IngrMenu, WK3_IngrMenu, WK4_IngrMenu, WK5_IngrMenu, WK6_IngrMenu,\
           WK7_IngrMenu, WK8_IngrMenu, WK9_IngrMenu, WK10_IngrMenu, WK11_IngrMenu, WK12_IngrMenu,\
           WK13_IngrMenu, WK14_IngrMenu, WK15_IngrMenu, WK16_IngrMenu, WK17_IngrMenu, WK18_IngrMenu,\
           WK19_IngrMenu, WK20_IngrMenu, WK21_IngrMenu, WK22_IngrMenu, WK23_IngrMenu, WK24_IngrMenu,\
           WL1_IngrMenu, WL2_IngrMenu, WL3_IngrMenu, WL4_IngrMenu, WL5_IngrMenu, WL6_IngrMenu,\
           WL7_IngrMenu, WL8_IngrMenu, WL9_IngrMenu, WL10_IngrMenu, WL11_IngrMenu, WL12_IngrMenu,\
           WL13_IngrMenu, WL14_IngrMenu, WL15_IngrMenu, WL16_IngrMenu, WL17_IngrMenu, WL18_IngrMenu,\
           WL19_IngrMenu, WL20_IngrMenu, WL21_IngrMenu, WL22_IngrMenu, WL23_IngrMenu, WL24_IngrMenu,\
           WM1_IngrMenu, WM2_IngrMenu, WM3_IngrMenu, WM4_IngrMenu, WM5_IngrMenu, WM6_IngrMenu,\
           WM7_IngrMenu, WM8_IngrMenu, WM9_IngrMenu, WM10_IngrMenu, WM11_IngrMenu, WM12_IngrMenu,\
           WM13_IngrMenu, WM14_IngrMenu, WM15_IngrMenu, WM16_IngrMenu, WM17_IngrMenu, WM18_IngrMenu,\
           WM19_IngrMenu, WM20_IngrMenu, WM21_IngrMenu, WM22_IngrMenu, WM23_IngrMenu, WM24_IngrMenu,\
           WN1_IngrMenu, WN2_IngrMenu, WN3_IngrMenu, WN4_IngrMenu, WN5_IngrMenu, WN6_IngrMenu,\
           WN7_IngrMenu, WN8_IngrMenu, WN9_IngrMenu, WN10_IngrMenu, WN11_IngrMenu, WN12_IngrMenu,\
           WN13_IngrMenu, WN14_IngrMenu, WN15_IngrMenu, WN16_IngrMenu, WN17_IngrMenu, WN18_IngrMenu,\
           WN19_IngrMenu, WN20_IngrMenu, WN21_IngrMenu, WN22_IngrMenu, WN23_IngrMenu, WN24_IngrMenu,\
           WO1_IngrMenu, WO2_IngrMenu, WO3_IngrMenu, WO4_IngrMenu, WO5_IngrMenu, WO6_IngrMenu,\
           WO7_IngrMenu, WO8_IngrMenu, WO9_IngrMenu, WO10_IngrMenu, WO11_IngrMenu, WO12_IngrMenu,\
           WO13_IngrMenu, WO14_IngrMenu, WO15_IngrMenu, WO16_IngrMenu, WO17_IngrMenu, WO18_IngrMenu,\
           WO19_IngrMenu, WO20_IngrMenu, WO21_IngrMenu, WO22_IngrMenu, WO23_IngrMenu, WO24_IngrMenu,\
           WP1_IngrMenu, WP2_IngrMenu, WP3_IngrMenu, WP4_IngrMenu, WP5_IngrMenu, WP6_IngrMenu,\
           WP7_IngrMenu, WP8_IngrMenu, WP9_IngrMenu, WP10_IngrMenu, WP11_IngrMenu, WP12_IngrMenu,\
           WP13_IngrMenu, WP14_IngrMenu, WP15_IngrMenu, WP16_IngrMenu, WP17_IngrMenu, WP18_IngrMenu,\
           WP19_IngrMenu, WP20_IngrMenu, WP21_IngrMenu, WP22_IngrMenu, WP23_IngrMenu, WP24_IngrMenu,\
           WA1_SS, WA2_SS, WA3_SS, WA4_SS, WA5_SS, WA6_SS, WA7_SS, WA8_SS,\
           WA9_SS, WA10_SS, WA11_SS, WA12_SS, WA13_SS, WA14_SS, WA15_SS, WA16_SS,\
           WA17_SS, WA18_SS, WA19_SS, WA20_SS, WA21_SS, WA22_SS, WA23_SS, WA24_SS,\
           WB1_SS, WB2_SS, WB3_SS, WB4_SS, WB5_SS, WB6_SS, WB7_SS, WB8_SS,\
           WB9_SS, WB10_SS, WB11_SS, WB12_SS, WB13_SS, WB14_SS, WB15_SS, WB16_SS,\
           WB17_SS, WB18_SS, WB19_SS, WB20_SS, WB21_SS, WB22_SS, WB23_SS, WB24_SS,\
           WC1_SS, WC2_SS, WC3_SS, WC4_SS, WC5_SS, WC6_SS, WC7_SS, WC8_SS,\
           WC9_SS, WC10_SS, WC11_SS, WC12_SS, WC13_SS, WC14_SS, WC15_SS, WC16_SS,\
           WC17_SS, WC18_SS, WC19_SS, WC20_SS, WC21_SS, WC22_SS, WC23_SS, WC24_SS,\
           WD1_SS, WD2_SS, WD3_SS, WD4_SS, WD5_SS, WD6_SS, WD7_SS, WD8_SS,\
           WD9_SS, WD10_SS, WD11_SS, WD12_SS, WD13_SS, WD14_SS, WD15_SS, WD16_SS,\
           WD17_SS, WD18_SS, WD19_SS, WD20_SS, WD21_SS, WD22_SS, WD23_SS, WD24_SS,\
           WE1_SS, WE2_SS, WE3_SS, WE4_SS, WE5_SS, WE6_SS, WE7_SS, WE8_SS,\
           WE9_SS, WE10_SS, WE11_SS, WE12_SS, WE13_SS, WE14_SS, WE15_SS, WE16_SS,\
           WE17_SS, WE18_SS, WE19_SS, WE20_SS, WE21_SS, WE22_SS, WE23_SS, WE24_SS,\
           WF1_SS, WF2_SS, WF3_SS, WF4_SS, WF5_SS, WF6_SS, WF7_SS, WF8_SS,\
           WF9_SS, WF10_SS, WF11_SS, WF12_SS, WF13_SS, WF14_SS, WF15_SS, WF16_SS,\
           WF17_SS, WF18_SS, WF19_SS, WF20_SS, WF21_SS, WF22_SS, WF23_SS, WF24_SS,\
           WG1_SS, WG2_SS, WG3_SS, WG4_SS, WG5_SS, WG6_SS, WG7_SS, WG8_SS,\
           WG9_SS, WG10_SS, WG11_SS, WG12_SS, WG13_SS, WG14_SS, WG15_SS, WG16_SS,\
           WG17_SS, WG18_SS, WG19_SS, WG20_SS, WG21_SS, WG22_SS, WG23_SS, WG24_SS,\
           WH1_SS, WH2_SS, WH3_SS, WH4_SS, WH5_SS, WH6_SS, WH7_SS, WH8_SS,\
           WH9_SS, WH10_SS, WH11_SS, WH12_SS, WH13_SS, WH14_SS, WH15_SS, WH16_SS,\
           WH17_SS, WH18_SS, WH19_SS, WH20_SS, WH21_SS, WH22_SS, WH23_SS, WH24_SS,\
           WI1_SS, WI2_SS, WI3_SS, WI4_SS, WI5_SS, WI6_SS, WI7_SS, WI8_SS,\
           WI9_SS, WI10_SS, WI11_SS, WI12_SS, WI13_SS, WI14_SS, WI15_SS, WI16_SS,\
           WI17_SS, WI18_SS, WI19_SS, WI20_SS, WI21_SS, WI22_SS, WI23_SS, WI24_SS,\
           WJ1_SS, WJ2_SS, WJ3_SS, WJ4_SS, WJ5_SS, WJ6_SS, WJ7_SS, WJ8_SS,\
           WJ9_SS, WJ10_SS, WJ11_SS, WJ12_SS, WJ13_SS, WJ14_SS, WJ15_SS, WJ16_SS,\
           WJ17_SS, WJ18_SS, WJ19_SS, WJ20_SS, WJ21_SS, WJ22_SS, WJ23_SS, WJ24_SS,\
           WK1_SS, WK2_SS, WK3_SS, WK4_SS, WK5_SS, WK6_SS, WK7_SS, WK8_SS,\
           WK9_SS, WK10_SS, WK11_SS, WK12_SS, WK13_SS, WK14_SS, WK15_SS, WK16_SS,\
           WK17_SS, WK18_SS, WK19_SS, WK20_SS, WK21_SS, WK22_SS, WK23_SS, WK24_SS,\
           WL1_SS, WL2_SS, WL3_SS, WL4_SS, WL5_SS, WL6_SS, WL7_SS, WL8_SS,\
           WL9_SS, WL10_SS, WL11_SS, WL12_SS, WL13_SS, WL14_SS, WL15_SS, WL16_SS,\
           WL17_SS, WL18_SS, WL19_SS, WL20_SS, WL21_SS, WL22_SS, WL23_SS, WL24_SS,\
           WM1_SS, WM2_SS, WM3_SS, WM4_SS, WM5_SS, WM6_SS, WM7_SS, WM8_SS,\
           WM9_SS, WM10_SS, WM11_SS, WM12_SS, WM13_SS, WM14_SS, WM15_SS, WM16_SS,\
           WM17_SS, WM18_SS, WM19_SS, WM20_SS, WM21_SS, WM22_SS, WM23_SS, WM24_SS,\
           WN1_SS, WN2_SS, WN3_SS, WN4_SS, WN5_SS, WN6_SS, WN7_SS, WN8_SS,\
           WN9_SS, WN10_SS, WN11_SS, WN12_SS, WN13_SS, WN14_SS, WN15_SS, WN16_SS,\
           WN17_SS, WN18_SS, WN19_SS, WN20_SS, WN21_SS, WN22_SS, WN23_SS, WN24_SS,\
           WO1_SS, WO2_SS, WO3_SS, WO4_SS, WO5_SS, WO6_SS, WO7_SS, WO8_SS,\
           WO9_SS, WO10_SS, WO11_SS, WO12_SS, WO13_SS, WO14_SS, WO15_SS, WO16_SS,\
           WO17_SS, WO18_SS, WO19_SS, WO20_SS, WO21_SS, WO22_SS, WO23_SS, WO24_SS,\
           WP1_SS, WP2_SS, WP3_SS, WP4_SS, WP5_SS, WP6_SS, WP7_SS, WP8_SS,\
           WP9_SS, WP10_SS, WP11_SS, WP12_SS, WP13_SS, WP14_SS, WP15_SS, WP16_SS,\
           WP17_SS, WP18_SS, WP19_SS, WP20_SS, WP21_SS, WP22_SS, WP23_SS, WP24_SS,\
           WA1_SSMenu, WA2_SSMenu, WA3_SSMenu, WA4_SSMenu, WA5_SSMenu, WA6_SSMenu, WA7_SSMenu, WA8_SSMenu,\
           WA9_SSMenu, WA10_SSMenu, WA11_SSMenu, WA12_SSMenu, WA13_SSMenu, WA14_SSMenu, WA15_SSMenu, WA16_SSMenu,\
           WA17_SSMenu, WA18_SSMenu, WA19_SSMenu, WA20_SSMenu, WA21_SSMenu, WA22_SSMenu, WA23_SSMenu, WA24_SSMenu,\
           WB1_SSMenu, WB2_SSMenu, WB3_SSMenu, WB4_SSMenu, WB5_SSMenu, WB6_SSMenu, WB7_SSMenu, WB8_SSMenu,\
           WB9_SSMenu, WB10_SSMenu, WB11_SSMenu, WB12_SSMenu, WB13_SSMenu, WB14_SSMenu, WB15_SSMenu, WB16_SSMenu,\
           WB17_SSMenu, WB18_SSMenu, WB19_SSMenu, WB20_SSMenu, WB21_SSMenu, WB22_SSMenu, WB23_SSMenu, WB24_SSMenu,\
           WC1_SSMenu, WC2_SSMenu, WC3_SSMenu, WC4_SSMenu, WC5_SSMenu, WC6_SSMenu, WC7_SSMenu, WC8_SSMenu,\
           WC9_SSMenu, WC10_SSMenu, WC11_SSMenu, WC12_SSMenu, WC13_SSMenu, WC14_SSMenu, WC15_SSMenu, WC16_SSMenu,\
           WC17_SSMenu, WC18_SSMenu, WC19_SSMenu, WC20_SSMenu, WC21_SSMenu, WC22_SSMenu, WC23_SSMenu, WC24_SSMenu,\
           WD1_SSMenu, WD2_SSMenu, WD3_SSMenu, WD4_SSMenu, WD5_SSMenu, WD6_SSMenu, WD7_SSMenu, WD8_SSMenu,\
           WD9_SSMenu, WD10_SSMenu, WD11_SSMenu, WD12_SSMenu, WD13_SSMenu, WD14_SSMenu, WD15_SSMenu, WD16_SSMenu,\
           WD17_SSMenu, WD18_SSMenu, WD19_SSMenu, WD20_SSMenu, WD21_SSMenu, WD22_SSMenu, WD23_SSMenu, WD24_SSMenu,\
           WE1_SSMenu, WE2_SSMenu, WE3_SSMenu, WE4_SSMenu, WE5_SSMenu, WE6_SSMenu, WE7_SSMenu, WE8_SSMenu,\
           WE9_SSMenu, WE10_SSMenu, WE11_SSMenu, WE12_SSMenu, WE13_SSMenu, WE14_SSMenu, WE15_SSMenu, WE16_SSMenu,\
           WE17_SSMenu, WE18_SSMenu, WE19_SSMenu, WE20_SSMenu, WE21_SSMenu, WE22_SSMenu, WE23_SSMenu, WE24_SSMenu,\
           WF1_SSMenu, WF2_SSMenu, WF3_SSMenu, WF4_SSMenu, WF5_SSMenu, WF6_SSMenu, WF7_SSMenu, WF8_SSMenu,\
           WF9_SSMenu, WF10_SSMenu, WF11_SSMenu, WF12_SSMenu, WF13_SSMenu, WF14_SSMenu, WF15_SSMenu, WF16_SSMenu,\
           WF17_SSMenu, WF18_SSMenu, WF19_SSMenu, WF20_SSMenu, WF21_SSMenu, WF22_SSMenu, WF23_SSMenu, WF24_SSMenu,\
           WG1_SSMenu, WG2_SSMenu, WG3_SSMenu, WG4_SSMenu, WG5_SSMenu, WG6_SSMenu, WG7_SSMenu, WG8_SSMenu,\
           WG9_SSMenu, WG10_SSMenu, WG11_SSMenu, WG12_SSMenu, WG13_SSMenu, WG14_SSMenu, WG15_SSMenu, WG16_SSMenu,\
           WG17_SSMenu, WG18_SSMenu, WG19_SSMenu, WG20_SSMenu, WG21_SSMenu, WG22_SSMenu, WG23_SSMenu, WG24_SSMenu,\
           WH1_SSMenu, WH2_SSMenu, WH3_SSMenu, WH4_SSMenu, WH5_SSMenu, WH6_SSMenu, WH7_SSMenu, WH8_SSMenu,\
           WH9_SSMenu, WH10_SSMenu, WH11_SSMenu, WH12_SSMenu, WH13_SSMenu, WH14_SSMenu, WH15_SSMenu, WH16_SSMenu,\
           WH17_SSMenu, WH18_SSMenu, WH19_SSMenu, WH20_SSMenu, WH21_SSMenu, WH22_SSMenu, WH23_SSMenu, WH24_SSMenu,\
           WI1_SSMenu, WI2_SSMenu, WI3_SSMenu, WI4_SSMenu, WI5_SSMenu, WI6_SSMenu, WI7_SSMenu, WI8_SSMenu,\
           WI9_SSMenu, WI10_SSMenu, WI11_SSMenu, WI12_SSMenu, WI13_SSMenu, WI14_SSMenu, WI15_SSMenu, WI16_SSMenu,\
           WI17_SSMenu, WI18_SSMenu, WI19_SSMenu, WI20_SSMenu, WI21_SSMenu, WI22_SSMenu, WI23_SSMenu, WI24_SSMenu,\
           WJ1_SSMenu, WJ2_SSMenu, WJ3_SSMenu, WJ4_SSMenu, WJ5_SSMenu, WJ6_SSMenu, WJ7_SSMenu, WJ8_SSMenu,\
           WJ9_SSMenu, WJ10_SSMenu, WJ11_SSMenu, WJ12_SSMenu, WJ13_SSMenu, WJ14_SSMenu, WJ15_SSMenu, WJ16_SSMenu,\
           WJ17_SSMenu, WJ18_SSMenu, WJ19_SSMenu, WJ20_SSMenu, WJ21_SSMenu, WJ22_SSMenu, WJ23_SSMenu, WJ24_SSMenu,\
           WK1_SSMenu, WK2_SSMenu, WK3_SSMenu, WK4_SSMenu, WK5_SSMenu, WK6_SSMenu, WK7_SSMenu, WK8_SSMenu,\
           WK9_SSMenu, WK10_SSMenu, WK11_SSMenu, WK12_SSMenu, WK13_SSMenu, WK14_SSMenu, WK15_SSMenu, WK16_SSMenu,\
           WK17_SSMenu, WK18_SSMenu, WK19_SSMenu, WK20_SSMenu, WK21_SSMenu, WK22_SSMenu, WK23_SSMenu, WK24_SSMenu,\
           WL1_SSMenu, WL2_SSMenu, WL3_SSMenu, WL4_SSMenu, WL5_SSMenu, WL6_SSMenu, WL7_SSMenu, WL8_SSMenu,\
           WL9_SSMenu, WL10_SSMenu, WL11_SSMenu, WL12_SSMenu, WL13_SSMenu, WL14_SSMenu, WL15_SSMenu, WL16_SSMenu,\
           WL17_SSMenu, WL18_SSMenu, WL19_SSMenu, WL20_SSMenu, WL21_SSMenu, WL22_SSMenu, WL23_SSMenu, WL24_SSMenu,\
           WM1_SSMenu, WM2_SSMenu, WM3_SSMenu, WM4_SSMenu, WM5_SSMenu, WM6_SSMenu, WM7_SSMenu, WM8_SSMenu,\
           WM9_SSMenu, WM10_SSMenu, WM11_SSMenu, WM12_SSMenu, WM13_SSMenu, WM14_SSMenu, WM15_SSMenu, WM16_SSMenu,\
           WM17_SSMenu, WM18_SSMenu, WM19_SSMenu, WM20_SSMenu, WM21_SSMenu, WM22_SSMenu, WM23_SSMenu, WM24_SSMenu,\
           WN1_SSMenu, WN2_SSMenu, WN3_SSMenu, WN4_SSMenu, WN5_SSMenu, WN6_SSMenu, WN7_SSMenu, WN8_SSMenu,\
           WN9_SSMenu, WN10_SSMenu, WN11_SSMenu, WN12_SSMenu, WN13_SSMenu, WN14_SSMenu, WN15_SSMenu, WN16_SSMenu,\
           WN17_SSMenu, WN18_SSMenu, WN19_SSMenu, WN20_SSMenu, WN21_SSMenu, WN22_SSMenu, WN23_SSMenu, WN24_SSMenu,\
           WO1_SSMenu, WO2_SSMenu, WO3_SSMenu, WO4_SSMenu, WO5_SSMenu, WO6_SSMenu, WO7_SSMenu, WO8_SSMenu,\
           WO9_SSMenu, WO10_SSMenu, WO11_SSMenu, WO12_SSMenu, WO13_SSMenu, WO14_SSMenu, WO15_SSMenu, WO16_SSMenu,\
           WO17_SSMenu, WO18_SSMenu, WO19_SSMenu, WO20_SSMenu, WO21_SSMenu, WO22_SSMenu, WO23_SSMenu, WO24_SSMenu,\
           WP1_SSMenu, WP2_SSMenu, WP3_SSMenu, WP4_SSMenu, WP5_SSMenu, WP6_SSMenu, WP7_SSMenu, WP8_SSMenu,\
           WP9_SSMenu, WP10_SSMenu, WP11_SSMenu, WP12_SSMenu, WP13_SSMenu, WP14_SSMenu, WP15_SSMenu, WP16_SSMenu,\
           WP17_SSMenu, WP18_SSMenu, WP19_SSMenu, WP20_SSMenu, WP21_SSMenu, WP22_SSMenu, WP23_SSMenu, WP24_SSMenu,\
           WA1_Dilu, WA2_Dilu, WA3_Dilu, WA4_Dilu, WA5_Dilu, WA6_Dilu, WA7_Dilu, WA8_Dilu,\
           WA9_Dilu, WA10_Dilu, WA11_Dilu, WA12_Dilu, WA13_Dilu, WA14_Dilu, WA15_Dilu, WA16_Dilu,\
           WA17_Dilu, WA18_Dilu, WA19_Dilu, WA20_Dilu, WA21_Dilu, WA22_Dilu, WA23_Dilu, WA24_Dilu,\
           WB1_Dilu, WB2_Dilu, WB3_Dilu, WB4_Dilu, WB5_Dilu, WB6_Dilu, WB7_Dilu, WB8_Dilu,\
           WB9_Dilu, WB10_Dilu, WB11_Dilu, WB12_Dilu, WB13_Dilu, WB14_Dilu, WB15_Dilu, WB16_Dilu,\
           WB17_Dilu, WB18_Dilu, WB19_Dilu, WB20_Dilu, WB21_Dilu, WB22_Dilu, WB23_Dilu, WB24_Dilu,\
           WC1_Dilu, WC2_Dilu, WC3_Dilu, WC4_Dilu, WC5_Dilu, WC6_Dilu, WC7_Dilu, WC8_Dilu,\
           WC9_Dilu, WC10_Dilu, WC11_Dilu, WC12_Dilu, WC13_Dilu, WC14_Dilu, WC15_Dilu, WC16_Dilu,\
           WC17_Dilu, WC18_Dilu, WC19_Dilu, WC20_Dilu, WC21_Dilu, WC22_Dilu, WC23_Dilu, WC24_Dilu,\
           WD1_Dilu, WD2_Dilu, WD3_Dilu, WD4_Dilu, WD5_Dilu, WD6_Dilu, WD7_Dilu, WD8_Dilu,\
           WD9_Dilu, WD10_Dilu, WD11_Dilu, WD12_Dilu, WD13_Dilu, WD14_Dilu, WD15_Dilu, WD16_Dilu,\
           WD17_Dilu, WD18_Dilu, WD19_Dilu, WD20_Dilu, WD21_Dilu, WD22_Dilu, WD23_Dilu, WD24_Dilu,\
           WE1_Dilu, WE2_Dilu, WE3_Dilu, WE4_Dilu, WE5_Dilu, WE6_Dilu, WE7_Dilu, WE8_Dilu,\
           WE9_Dilu, WE10_Dilu, WE11_Dilu, WE12_Dilu, WE13_Dilu, WE14_Dilu, WE15_Dilu, WE16_Dilu,\
           WE17_Dilu, WE18_Dilu, WE19_Dilu, WE20_Dilu, WE21_Dilu, WE22_Dilu, WE23_Dilu, WE24_Dilu,\
           WF1_Dilu, WF2_Dilu, WF3_Dilu, WF4_Dilu, WF5_Dilu, WF6_Dilu, WF7_Dilu, WF8_Dilu,\
           WF9_Dilu, WF10_Dilu, WF11_Dilu, WF12_Dilu, WF13_Dilu, WF14_Dilu, WF15_Dilu, WF16_Dilu,\
           WF17_Dilu, WF18_Dilu, WF19_Dilu, WF20_Dilu, WF21_Dilu, WF22_Dilu, WF23_Dilu, WF24_Dilu,\
           WG1_Dilu, WG2_Dilu, WG3_Dilu, WG4_Dilu, WG5_Dilu, WG6_Dilu, WG7_Dilu, WG8_Dilu,\
           WG9_Dilu, WG10_Dilu, WG11_Dilu, WG12_Dilu, WG13_Dilu, WG14_Dilu, WG15_Dilu, WG16_Dilu,\
           WG17_Dilu, WG18_Dilu, WG19_Dilu, WG20_Dilu, WG21_Dilu, WG22_Dilu, WG23_Dilu, WG24_Dilu,\
           WH1_Dilu, WH2_Dilu, WH3_Dilu, WH4_Dilu, WH5_Dilu, WH6_Dilu, WH7_Dilu, WH8_Dilu,\
           WH9_Dilu, WH10_Dilu, WH11_Dilu, WH12_Dilu, WH13_Dilu, WH14_Dilu, WH15_Dilu, WH16_Dilu,\
           WH17_Dilu, WH18_Dilu, WH19_Dilu, WH20_Dilu, WH21_Dilu, WH22_Dilu, WH23_Dilu, WH24_Dilu,\
           WI1_Dilu, WI2_Dilu, WI3_Dilu, WI4_Dilu, WI5_Dilu, WI6_Dilu, WI7_Dilu, WI8_Dilu,\
           WI9_Dilu, WI10_Dilu, WI11_Dilu, WI12_Dilu, WI13_Dilu, WI14_Dilu, WI15_Dilu, WI16_Dilu,\
           WI17_Dilu, WI18_Dilu, WI19_Dilu, WI20_Dilu, WI21_Dilu, WI22_Dilu, WI23_Dilu, WI24_Dilu,\
           WJ1_Dilu, WJ2_Dilu, WJ3_Dilu, WJ4_Dilu, WJ5_Dilu, WJ6_Dilu, WJ7_Dilu, WJ8_Dilu,\
           WJ9_Dilu, WJ10_Dilu, WJ11_Dilu, WJ12_Dilu, WJ13_Dilu, WJ14_Dilu, WJ15_Dilu, WJ16_Dilu,\
           WJ17_Dilu, WJ18_Dilu, WJ19_Dilu, WJ20_Dilu, WJ21_Dilu, WJ22_Dilu, WJ23_Dilu, WJ24_Dilu,\
           WK1_Dilu, WK2_Dilu, WK3_Dilu, WK4_Dilu, WK5_Dilu, WK6_Dilu, WK7_Dilu, WK8_Dilu,\
           WK9_Dilu, WK10_Dilu, WK11_Dilu, WK12_Dilu, WK13_Dilu, WK14_Dilu, WK15_Dilu, WK16_Dilu,\
           WK17_Dilu, WK18_Dilu, WK19_Dilu, WK20_Dilu, WK21_Dilu, WK22_Dilu, WK23_Dilu, WK24_Dilu,\
           WL1_Dilu, WL2_Dilu, WL3_Dilu, WL4_Dilu, WL5_Dilu, WL6_Dilu, WL7_Dilu, WL8_Dilu,\
           WL9_Dilu, WL10_Dilu, WL11_Dilu, WL12_Dilu, WL13_Dilu, WL14_Dilu, WL15_Dilu, WL16_Dilu,\
           WL17_Dilu, WL18_Dilu, WL19_Dilu, WL20_Dilu, WL21_Dilu, WL22_Dilu, WL23_Dilu, WL24_Dilu,\
           WM1_Dilu, WM2_Dilu, WM3_Dilu, WM4_Dilu, WM5_Dilu, WM6_Dilu, WM7_Dilu, WM8_Dilu,\
           WM9_Dilu, WM10_Dilu, WM11_Dilu, WM12_Dilu, WM13_Dilu, WM14_Dilu, WM15_Dilu, WM16_Dilu,\
           WM17_Dilu, WM18_Dilu, WM19_Dilu, WM20_Dilu, WM21_Dilu, WM22_Dilu, WM23_Dilu, WM24_Dilu,\
           WN1_Dilu, WN2_Dilu, WN3_Dilu, WN4_Dilu, WN5_Dilu, WN6_Dilu, WN7_Dilu, WN8_Dilu,\
           WN9_Dilu, WN10_Dilu, WN11_Dilu, WN12_Dilu, WN13_Dilu, WN14_Dilu, WN15_Dilu, WN16_Dilu,\
           WN17_Dilu, WN18_Dilu, WN19_Dilu, WN20_Dilu, WN21_Dilu, WN22_Dilu, WN23_Dilu, WN24_Dilu,\
           WO1_Dilu, WO2_Dilu, WO3_Dilu, WO4_Dilu, WO5_Dilu, WO6_Dilu, WO7_Dilu, WO8_Dilu,\
           WO9_Dilu, WO10_Dilu, WO11_Dilu, WO12_Dilu, WO13_Dilu, WO14_Dilu, WO15_Dilu, WO16_Dilu,\
           WO17_Dilu, WO18_Dilu, WO19_Dilu, WO20_Dilu, WO21_Dilu, WO22_Dilu, WO23_Dilu, WO24_Dilu,\
           WP1_Dilu, WP2_Dilu, WP3_Dilu, WP4_Dilu, WP5_Dilu, WP6_Dilu, WP7_Dilu, WP8_Dilu,\
           WP9_Dilu, WP10_Dilu, WP11_Dilu, WP12_Dilu, WP13_Dilu, WP14_Dilu, WP15_Dilu, WP16_Dilu,\
           WP17_Dilu, WP18_Dilu, WP19_Dilu, WP20_Dilu, WP21_Dilu, WP22_Dilu, WP23_Dilu, WP24_Dilu,\
           WA1_DiluMenu, WA2_DiluMenu, WA3_DiluMenu, WA4_DiluMenu, WA5_DiluMenu, WA6_DiluMenu, WA7_DiluMenu, WA8_DiluMenu,\
           WA9_DiluMenu, WA10_DiluMenu, WA11_DiluMenu, WA12_DiluMenu, WA13_DiluMenu, WA14_DiluMenu, WA15_DiluMenu, WA16_DiluMenu,\
           WA17_DiluMenu, WA18_DiluMenu, WA19_DiluMenu, WA20_DiluMenu, WA21_DiluMenu, WA22_DiluMenu, WA23_DiluMenu, WA24_DiluMenu,\
           WB1_DiluMenu, WB2_DiluMenu, WB3_DiluMenu, WB4_DiluMenu, WB5_DiluMenu, WB6_DiluMenu, WB7_DiluMenu, WB8_DiluMenu,\
           WB9_DiluMenu, WB10_DiluMenu, WB11_DiluMenu, WB12_DiluMenu, WB13_DiluMenu, WB14_DiluMenu, WB15_DiluMenu, WB16_DiluMenu,\
           WB17_DiluMenu, WB18_DiluMenu, WB19_DiluMenu, WB20_DiluMenu, WB21_DiluMenu, WB22_DiluMenu, WB23_DiluMenu, WB24_DiluMenu,\
           WC1_DiluMenu, WC2_DiluMenu, WC3_DiluMenu, WC4_DiluMenu, WC5_DiluMenu, WC6_DiluMenu, WC7_DiluMenu, WC8_DiluMenu,\
           WC9_DiluMenu, WC10_DiluMenu, WC11_DiluMenu, WC12_DiluMenu, WC13_DiluMenu, WC14_DiluMenu, WC15_DiluMenu, WC16_DiluMenu,\
           WC17_DiluMenu, WC18_DiluMenu, WC19_DiluMenu, WC20_DiluMenu, WC21_DiluMenu, WC22_DiluMenu, WC23_DiluMenu, WC24_DiluMenu,\
           WD1_DiluMenu, WD2_DiluMenu, WD3_DiluMenu, WD4_DiluMenu, WD5_DiluMenu, WD6_DiluMenu, WD7_DiluMenu, WD8_DiluMenu,\
           WD9_DiluMenu, WD10_DiluMenu, WD11_DiluMenu, WD12_DiluMenu, WD13_DiluMenu, WD14_DiluMenu, WD15_DiluMenu, WD16_DiluMenu,\
           WD17_DiluMenu, WD18_DiluMenu, WD19_DiluMenu, WD20_DiluMenu, WD21_DiluMenu, WD22_DiluMenu, WD23_DiluMenu, WD24_DiluMenu,\
           WE1_DiluMenu, WE2_DiluMenu, WE3_DiluMenu, WE4_DiluMenu, WE5_DiluMenu, WE6_DiluMenu, WE7_DiluMenu, WE8_DiluMenu,\
           WE9_DiluMenu, WE10_DiluMenu, WE11_DiluMenu, WE12_DiluMenu, WE13_DiluMenu, WE14_DiluMenu, WE15_DiluMenu, WE16_DiluMenu,\
           WE17_DiluMenu, WE18_DiluMenu, WE19_DiluMenu, WE20_DiluMenu, WE21_DiluMenu, WE22_DiluMenu, WE23_DiluMenu, WE24_DiluMenu,\
           WF1_DiluMenu, WF2_DiluMenu, WF3_DiluMenu, WF4_DiluMenu, WF5_DiluMenu, WF6_DiluMenu, WF7_DiluMenu, WF8_DiluMenu,\
           WF9_DiluMenu, WF10_DiluMenu, WF11_DiluMenu, WF12_DiluMenu, WF13_DiluMenu, WF14_DiluMenu, WF15_DiluMenu, WF16_DiluMenu,\
           WF17_DiluMenu, WF18_DiluMenu, WF19_DiluMenu, WF20_DiluMenu, WF21_DiluMenu, WF22_DiluMenu, WF23_DiluMenu, WF24_DiluMenu,\
           WG1_DiluMenu, WG2_DiluMenu, WG3_DiluMenu, WG4_DiluMenu, WG5_DiluMenu, WG6_DiluMenu, WG7_DiluMenu, WG8_DiluMenu,\
           WG9_DiluMenu, WG10_DiluMenu, WG11_DiluMenu, WG12_DiluMenu, WG13_DiluMenu, WG14_DiluMenu, WG15_DiluMenu, WG16_DiluMenu,\
           WG17_DiluMenu, WG18_DiluMenu, WG19_DiluMenu, WG20_DiluMenu, WG21_DiluMenu, WG22_DiluMenu, WG23_DiluMenu, WG24_DiluMenu,\
           WH1_DiluMenu, WH2_DiluMenu, WH3_DiluMenu, WH4_DiluMenu, WH5_DiluMenu, WH6_DiluMenu, WH7_DiluMenu, WH8_DiluMenu,\
           WH9_DiluMenu, WH10_DiluMenu, WH11_DiluMenu, WH12_DiluMenu, WH13_DiluMenu, WH14_DiluMenu, WH15_DiluMenu, WH16_DiluMenu,\
           WH17_DiluMenu, WH18_DiluMenu, WH19_DiluMenu, WH20_DiluMenu, WH21_DiluMenu, WH22_DiluMenu, WH23_DiluMenu, WH24_DiluMenu,\
           WI1_DiluMenu, WI2_DiluMenu, WI3_DiluMenu, WI4_DiluMenu, WI5_DiluMenu, WI6_DiluMenu, WI7_DiluMenu, WI8_DiluMenu,\
           WI9_DiluMenu, WI10_DiluMenu, WI11_DiluMenu, WI12_DiluMenu, WI13_DiluMenu, WI14_DiluMenu, WI15_DiluMenu, WI16_DiluMenu,\
           WI17_DiluMenu, WI18_DiluMenu, WI19_DiluMenu, WI20_DiluMenu, WI21_DiluMenu, WI22_DiluMenu, WI23_DiluMenu, WI24_DiluMenu,\
           WJ1_DiluMenu, WJ2_DiluMenu, WJ3_DiluMenu, WJ4_DiluMenu, WJ5_DiluMenu, WJ6_DiluMenu, WJ7_DiluMenu, WJ8_DiluMenu,\
           WJ9_DiluMenu, WJ10_DiluMenu, WJ11_DiluMenu, WJ12_DiluMenu, WJ13_DiluMenu, WJ14_DiluMenu, WJ15_DiluMenu, WJ16_DiluMenu,\
           WJ17_DiluMenu, WJ18_DiluMenu, WJ19_DiluMenu, WJ20_DiluMenu, WJ21_DiluMenu, WJ22_DiluMenu, WJ23_DiluMenu, WJ24_DiluMenu,\
           WK1_DiluMenu, WK2_DiluMenu, WK3_DiluMenu, WK4_DiluMenu, WK5_DiluMenu, WK6_DiluMenu, WK7_DiluMenu, WK8_DiluMenu,\
           WK9_DiluMenu, WK10_DiluMenu, WK11_DiluMenu, WK12_DiluMenu, WK13_DiluMenu, WK14_DiluMenu, WK15_DiluMenu, WK16_DiluMenu,\
           WK17_DiluMenu, WK18_DiluMenu, WK19_DiluMenu, WK20_DiluMenu, WK21_DiluMenu, WK22_DiluMenu, WK23_DiluMenu, WK24_DiluMenu,\
           WL1_DiluMenu, WL2_DiluMenu, WL3_DiluMenu, WL4_DiluMenu, WL5_DiluMenu, WL6_DiluMenu, WL7_DiluMenu, WL8_DiluMenu,\
           WL9_DiluMenu, WL10_DiluMenu, WL11_DiluMenu, WL12_DiluMenu, WL13_DiluMenu, WL14_DiluMenu, WL15_DiluMenu, WL16_DiluMenu,\
           WL17_DiluMenu, WL18_DiluMenu, WL19_DiluMenu, WL20_DiluMenu, WL21_DiluMenu, WL22_DiluMenu, WL23_DiluMenu, WL24_DiluMenu,\
           WM1_DiluMenu, WM2_DiluMenu, WM3_DiluMenu, WM4_DiluMenu, WM5_DiluMenu, WM6_DiluMenu, WM7_DiluMenu, WM8_DiluMenu,\
           WM9_DiluMenu, WM10_DiluMenu, WM11_DiluMenu, WM12_DiluMenu, WM13_DiluMenu, WM14_DiluMenu, WM15_DiluMenu, WM16_DiluMenu,\
           WM17_DiluMenu, WM18_DiluMenu, WM19_DiluMenu, WM20_DiluMenu, WM21_DiluMenu, WM22_DiluMenu, WM23_DiluMenu, WM24_DiluMenu,\
           WN1_DiluMenu, WN2_DiluMenu, WN3_DiluMenu, WN4_DiluMenu, WN5_DiluMenu, WN6_DiluMenu, WN7_DiluMenu, WN8_DiluMenu,\
           WN9_DiluMenu, WN10_DiluMenu, WN11_DiluMenu, WN12_DiluMenu, WN13_DiluMenu, WN14_DiluMenu, WN15_DiluMenu, WN16_DiluMenu,\
           WN17_DiluMenu, WN18_DiluMenu, WN19_DiluMenu, WN20_DiluMenu, WN21_DiluMenu, WN22_DiluMenu, WN23_DiluMenu, WN24_DiluMenu,\
           WO1_DiluMenu, WO2_DiluMenu, WO3_DiluMenu, WO4_DiluMenu, WO5_DiluMenu, WO6_DiluMenu, WO7_DiluMenu, WO8_DiluMenu,\
           WO9_DiluMenu, WO10_DiluMenu, WO11_DiluMenu, WO12_DiluMenu, WO13_DiluMenu, WO14_DiluMenu, WO15_DiluMenu, WO16_DiluMenu,\
           WO17_DiluMenu, WO18_DiluMenu, WO19_DiluMenu, WO20_DiluMenu, WO21_DiluMenu, WO22_DiluMenu, WO23_DiluMenu, WO24_DiluMenu,\
           WP1_DiluMenu, WP2_DiluMenu, WP3_DiluMenu, WP4_DiluMenu, WP5_DiluMenu, WP6_DiluMenu, WP7_DiluMenu, WP8_DiluMenu,\
           WP9_DiluMenu, WP10_DiluMenu, WP11_DiluMenu, WP12_DiluMenu, WP13_DiluMenu, WP14_DiluMenu, WP15_DiluMenu, WP16_DiluMenu,\
           WP17_DiluMenu, WP18_DiluMenu, WP19_DiluMenu, WP20_DiluMenu, WP21_DiluMenu, WP22_DiluMenu, WP23_DiluMenu, WP24_DiluMenu,\
           IngrMenu_List, SSMenu_List, DiluMenu_List, Ingr_List, Solvent1_Conc_List, Solvent2_Conc_List, SS_Conc_List, Vol_List, SS_List, Dilu_List,\
           Ingr_Label_List, Solvent1_Conc_Label_List, Solvent2_Conc_Label_List, SS_Conc_Label_List, Vol_Label_List, SS_Label_List, Dilu_Label_List,\
           Next_Button

    ingr_text = 'Ingredients'
    conc_text = 'Concentration (%)'
    SS_text = 'SSinitiator (%)'
    vol_text = 'Volume (uL)'
    conc_text2 = 'Concentration (%)'
    SS_text = 'SSInitiator Type'
    dilu_text = 'Selected Diluent'
    

    Row1_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row1_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row1_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row1_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row1_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row1_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row1_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row2_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row2_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row2_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row2_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row2_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row2_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row2_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row3_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row3_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row3_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row3_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row3_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row3_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row3_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row4_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row4_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row4_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row4_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row4_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row4_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row4_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row5_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row5_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row5_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row5_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row5_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row5_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row5_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row6_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row6_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row6_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row6_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row6_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row6_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row6_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row7_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row7_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row7_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row7_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row7_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row7_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row7_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row8_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row8_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row8_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row8_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row8_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row8_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row8_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row9_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row9_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row9_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row9_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row9_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row9_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row9_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row10_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row10_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row10_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row10_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row10_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row10_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row10_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row11_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row11_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row11_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row11_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row11_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row11_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row11_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    Row12_Ingr_Label = Label(OT,text=ingr_text, font = small_font, bg = bgcolour)
    Row12_Solvent1_Conc_Label = Label(OT,text=conc_text, font = small_font, bg = bgcolour)
    Row12_Solvent2_Conc_Label = Label(OT,text=conc_text2, font = small_font, bg = bgcolour)
    Row12_SS_Conc_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row12_Vol_Label = Label(OT,text=vol_text, font = small_font, bg = bgcolour)
    Row12_SS_Label = Label(OT,text=SS_text, font = small_font, bg = bgcolour)
    Row12_Dilu_Label = Label(OT,text=dilu_text, font = small_font, bg = bgcolour)

    # Inputs
    WA1_Vol = Entry()
    WA2_Vol = Entry()
    WA3_Vol = Entry()
    WA4_Vol = Entry()
    WA5_Vol = Entry()
    WA6_Vol = Entry()
    WA7_Vol = Entry()
    WA8_Vol = Entry()
    WA9_Vol = Entry()
    WA10_Vol = Entry()
    WA11_Vol = Entry()
    WA12_Vol = Entry()
    WA13_Vol = Entry()
    WA14_Vol = Entry()
    WA15_Vol = Entry()
    WA16_Vol = Entry()
    WA17_Vol = Entry()
    WA18_Vol = Entry()
    WA19_Vol = Entry()
    WA20_Vol = Entry()
    WA21_Vol = Entry()
    WA22_Vol = Entry()
    WA23_Vol = Entry()
    WA24_Vol = Entry()

    WA1_Solvent1_Conc = Entry()
    WA2_Solvent1_Conc = Entry()
    WA3_Solvent1_Conc = Entry()
    WA4_Solvent1_Conc = Entry()
    WA5_Solvent1_Conc = Entry()
    WA6_Solvent1_Conc = Entry()
    WA7_Solvent1_Conc = Entry()
    WA8_Solvent1_Conc = Entry()
    WA9_Solvent1_Conc = Entry()
    WA10_Solvent1_Conc = Entry()
    WA11_Solvent1_Conc = Entry()
    WA12_Solvent1_Conc = Entry()
    WA13_Solvent1_Conc = Entry()
    WA14_Solvent1_Conc = Entry()
    WA15_Solvent1_Conc = Entry()
    WA16_Solvent1_Conc = Entry()
    WA17_Solvent1_Conc = Entry()
    WA18_Solvent1_Conc = Entry()
    WA19_Solvent1_Conc = Entry()
    WA20_Solvent1_Conc = Entry()
    WA21_Solvent1_Conc = Entry()
    WA22_Solvent1_Conc = Entry()
    WA23_Solvent1_Conc = Entry()
    WA24_Solvent1_Conc = Entry()
    
    WA1_Solvent2_Conc = Entry()
    WA2_Solvent2_Conc = Entry()
    WA3_Solvent2_Conc = Entry()
    WA4_Solvent2_Conc = Entry()
    WA5_Solvent2_Conc = Entry()
    WA6_Solvent2_Conc = Entry()
    WA7_Solvent2_Conc = Entry()
    WA8_Solvent2_Conc = Entry()
    WA9_Solvent2_Conc = Entry()
    WA10_Solvent2_Conc = Entry()
    WA11_Solvent2_Conc = Entry()
    WA12_Solvent2_Conc = Entry()
    WA13_Solvent2_Conc = Entry()
    WA14_Solvent2_Conc = Entry()
    WA15_Solvent2_Conc = Entry()
    WA16_Solvent2_Conc = Entry()
    WA17_Solvent2_Conc = Entry()
    WA18_Solvent2_Conc = Entry()
    WA19_Solvent2_Conc = Entry()
    WA20_Solvent2_Conc = Entry()
    WA21_Solvent2_Conc = Entry()
    WA22_Solvent2_Conc = Entry()
    WA23_Solvent2_Conc = Entry()
    WA24_Solvent2_Conc = Entry()

    WA1_SS_Conc = Entry()
    WA2_SS_Conc = Entry()
    WA3_SS_Conc = Entry()
    WA4_SS_Conc = Entry()
    WA5_SS_Conc = Entry()
    WA6_SS_Conc = Entry()
    WA7_SS_Conc = Entry()
    WA8_SS_Conc = Entry()
    WA9_SS_Conc = Entry()
    WA10_SS_Conc = Entry()
    WA11_SS_Conc = Entry()
    WA12_SS_Conc = Entry()
    WA13_SS_Conc = Entry()
    WA14_SS_Conc = Entry()
    WA15_SS_Conc = Entry()
    WA16_SS_Conc = Entry()
    WA17_SS_Conc = Entry()
    WA18_SS_Conc = Entry()
    WA19_SS_Conc = Entry()
    WA20_SS_Conc = Entry()
    WA21_SS_Conc = Entry()
    WA22_SS_Conc = Entry()
    WA23_SS_Conc = Entry()
    WA24_SS_Conc = Entry()

    WA1_Ingr = StringVar(OT)
    WA1_IngrMenu = OptionMenu(OT,WA1_Ingr,*Ingrs)
    WA2_Ingr = StringVar(OT)
    WA2_IngrMenu = OptionMenu(OT,WA2_Ingr,*Ingrs)
    WA3_Ingr = StringVar(OT)
    WA3_IngrMenu = OptionMenu(OT,WA3_Ingr,*Ingrs)
    WA4_Ingr = StringVar(OT)
    WA4_IngrMenu = OptionMenu(OT,WA4_Ingr,*Ingrs)
    WA5_Ingr = StringVar(OT)
    WA5_IngrMenu = OptionMenu(OT,WA5_Ingr,*Ingrs)
    WA6_Ingr = StringVar(OT)
    WA6_IngrMenu = OptionMenu(OT,WA6_Ingr,*Ingrs)
    WA7_Ingr = StringVar(OT)
    WA7_IngrMenu = OptionMenu(OT,WA7_Ingr,*Ingrs)
    WA8_Ingr = StringVar(OT)
    WA8_IngrMenu = OptionMenu(OT,WA8_Ingr,*Ingrs)
    WA9_Ingr = StringVar(OT)
    WA9_IngrMenu = OptionMenu(OT,WA9_Ingr,*Ingrs)
    WA10_Ingr = StringVar(OT)
    WA10_IngrMenu = OptionMenu(OT,WA10_Ingr,*Ingrs)
    WA11_Ingr = StringVar(OT)
    WA11_IngrMenu = OptionMenu(OT,WA11_Ingr,*Ingrs)
    WA12_Ingr = StringVar(OT)
    WA12_IngrMenu = OptionMenu(OT,WA12_Ingr,*Ingrs)
    WA13_Ingr = StringVar(OT)
    WA13_IngrMenu = OptionMenu(OT,WA13_Ingr,*Ingrs)
    WA14_Ingr = StringVar(OT)
    WA14_IngrMenu = OptionMenu(OT,WA14_Ingr,*Ingrs)
    WA15_Ingr = StringVar(OT)
    WA15_IngrMenu = OptionMenu(OT,WA15_Ingr,*Ingrs)
    WA16_Ingr = StringVar(OT)
    WA16_IngrMenu = OptionMenu(OT,WA16_Ingr,*Ingrs)
    WA17_Ingr = StringVar(OT)
    WA17_IngrMenu = OptionMenu(OT,WA17_Ingr,*Ingrs)
    WA18_Ingr = StringVar(OT)
    WA18_IngrMenu = OptionMenu(OT,WA18_Ingr,*Ingrs)
    WA19_Ingr = StringVar(OT)
    WA19_IngrMenu = OptionMenu(OT,WA19_Ingr,*Ingrs)
    WA20_Ingr = StringVar(OT)
    WA20_IngrMenu = OptionMenu(OT,WA20_Ingr,*Ingrs)
    WA21_Ingr = StringVar(OT)
    WA21_IngrMenu = OptionMenu(OT,WA21_Ingr,*Ingrs)
    WA22_Ingr = StringVar(OT)
    WA22_IngrMenu = OptionMenu(OT,WA22_Ingr,*Ingrs)
    WA23_Ingr = StringVar(OT)
    WA23_IngrMenu = OptionMenu(OT,WA23_Ingr,*Ingrs)
    WA24_Ingr = StringVar(OT)
    WA24_IngrMenu = OptionMenu(OT,WA24_Ingr,*Ingrs)

    WA1_SS = StringVar(OT)
    WA1_SSMenu = OptionMenu(OT,WA1_SS,*SSInitiators)
    WA2_SS = StringVar(OT)
    WA2_SSMenu = OptionMenu(OT,WA2_SS,*SSInitiators)
    WA3_SS = StringVar(OT)
    WA3_SSMenu = OptionMenu(OT,WA3_SS,*SSInitiators)
    WA4_SS = StringVar(OT)
    WA4_SSMenu = OptionMenu(OT,WA4_SS,*SSInitiators)
    WA5_SS = StringVar(OT)
    WA5_SSMenu = OptionMenu(OT,WA5_SS,*SSInitiators)
    WA6_SS = StringVar(OT)
    WA6_SSMenu = OptionMenu(OT,WA6_SS,*SSInitiators)
    WA7_SS = StringVar(OT)
    WA7_SSMenu = OptionMenu(OT,WA7_SS,*SSInitiators)
    WA8_SS = StringVar(OT)
    WA8_SSMenu = OptionMenu(OT,WA8_SS,*SSInitiators)
    WA9_SS = StringVar(OT)
    WA9_SSMenu = OptionMenu(OT,WA9_SS,*SSInitiators)
    WA10_SS = StringVar(OT)
    WA10_SSMenu = OptionMenu(OT,WA10_SS,*SSInitiators)
    WA11_SS = StringVar(OT)
    WA11_SSMenu = OptionMenu(OT,WA11_SS,*SSInitiators)
    WA12_SS = StringVar(OT)
    WA12_SSMenu = OptionMenu(OT,WA12_SS,*SSInitiators)
    WA13_SS = StringVar(OT)
    WA13_SSMenu = OptionMenu(OT,WA13_SS,*SSInitiators)
    WA14_SS = StringVar(OT)
    WA14_SSMenu = OptionMenu(OT,WA14_SS,*SSInitiators)
    WA15_SS = StringVar(OT)
    WA15_SSMenu = OptionMenu(OT,WA15_SS,*SSInitiators)
    WA16_SS = StringVar(OT)
    WA16_SSMenu = OptionMenu(OT,WA16_SS,*SSInitiators)
    WA17_SS = StringVar(OT)
    WA17_SSMenu = OptionMenu(OT,WA17_SS,*SSInitiators)
    WA18_SS = StringVar(OT)
    WA18_SSMenu = OptionMenu(OT,WA18_SS,*SSInitiators)
    WA19_SS = StringVar(OT)
    WA19_SSMenu = OptionMenu(OT,WA19_SS,*SSInitiators)
    WA20_SS = StringVar(OT)
    WA20_SSMenu = OptionMenu(OT,WA20_SS,*SSInitiators)
    WA21_SS = StringVar(OT)
    WA21_SSMenu = OptionMenu(OT,WA21_SS,*SSInitiators)
    WA22_SS = StringVar(OT)
    WA22_SSMenu = OptionMenu(OT,WA22_SS,*SSInitiators)
    WA23_SS = StringVar(OT)
    WA23_SSMenu = OptionMenu(OT,WA23_SS,*SSInitiators)
    WA24_SS = StringVar(OT)
    WA24_SSMenu = OptionMenu(OT,WA24_SS,*SSInitiators)

    WA1_Dilu = StringVar(OT)
    WA1_DiluMenu = OptionMenu(OT,WA1_Dilu,*Diluents)
    WA2_Dilu = StringVar(OT)
    WA2_DiluMenu = OptionMenu(OT,WA2_Dilu,*Diluents)
    WA3_Dilu = StringVar(OT)
    WA3_DiluMenu = OptionMenu(OT,WA3_Dilu,*Diluents)
    WA4_Dilu = StringVar(OT)
    WA4_DiluMenu = OptionMenu(OT,WA4_Dilu,*Diluents)
    WA5_Dilu = StringVar(OT)
    WA5_DiluMenu = OptionMenu(OT,WA5_Dilu,*Diluents)
    WA6_Dilu = StringVar(OT)
    WA6_DiluMenu = OptionMenu(OT,WA6_Dilu,*Diluents)
    WA7_Dilu = StringVar(OT)
    WA7_DiluMenu = OptionMenu(OT,WA7_Dilu,*Diluents)
    WA8_Dilu = StringVar(OT)
    WA8_DiluMenu = OptionMenu(OT,WA8_Dilu,*Diluents)
    WA9_Dilu = StringVar(OT)
    WA9_DiluMenu = OptionMenu(OT,WA9_Dilu,*Diluents)
    WA10_Dilu = StringVar(OT)
    WA10_DiluMenu = OptionMenu(OT,WA10_Dilu,*Diluents)
    WA11_Dilu = StringVar(OT)
    WA11_DiluMenu = OptionMenu(OT,WA11_Dilu,*Diluents)
    WA12_Dilu = StringVar(OT)
    WA12_DiluMenu = OptionMenu(OT,WA12_Dilu,*Diluents)
    WA13_Dilu = StringVar(OT)
    WA13_DiluMenu = OptionMenu(OT,WA13_Dilu,*Diluents)
    WA14_Dilu = StringVar(OT)
    WA14_DiluMenu = OptionMenu(OT,WA14_Dilu,*Diluents)
    WA15_Dilu = StringVar(OT)
    WA15_DiluMenu = OptionMenu(OT,WA15_Dilu,*Diluents)
    WA16_Dilu = StringVar(OT)
    WA16_DiluMenu = OptionMenu(OT,WA16_Dilu,*Diluents)
    WA17_Dilu = StringVar(OT)
    WA17_DiluMenu = OptionMenu(OT,WA17_Dilu,*Diluents)
    WA18_Dilu = StringVar(OT)
    WA18_DiluMenu = OptionMenu(OT,WA18_Dilu,*Diluents)
    WA19_Dilu = StringVar(OT)
    WA19_DiluMenu = OptionMenu(OT,WA19_Dilu,*Diluents)
    WA20_Dilu = StringVar(OT)
    WA20_DiluMenu = OptionMenu(OT,WA20_Dilu,*Diluents)
    WA21_Dilu = StringVar(OT)
    WA21_DiluMenu = OptionMenu(OT,WA21_Dilu,*Diluents)
    WA22_Dilu = StringVar(OT)
    WA22_DiluMenu = OptionMenu(OT,WA22_Dilu,*Diluents)
    WA23_Dilu = StringVar(OT)
    WA23_DiluMenu = OptionMenu(OT,WA23_Dilu,*Diluents)
    WA24_Dilu = StringVar(OT)
    WA24_DiluMenu = OptionMenu(OT,WA24_Dilu,*Diluents)

    
    WB1_Vol = Entry()
    WB2_Vol = Entry()
    WB3_Vol = Entry()
    WB4_Vol = Entry()
    WB5_Vol = Entry()
    WB6_Vol = Entry()
    WB7_Vol = Entry()
    WB8_Vol = Entry()
    WB9_Vol = Entry()
    WB10_Vol = Entry()
    WB11_Vol = Entry()
    WB12_Vol = Entry()
    WB13_Vol = Entry()
    WB14_Vol = Entry()
    WB15_Vol = Entry()
    WB16_Vol = Entry()
    WB17_Vol = Entry()
    WB18_Vol = Entry()
    WB19_Vol = Entry()
    WB20_Vol = Entry()
    WB21_Vol = Entry()
    WB22_Vol = Entry()
    WB23_Vol = Entry()
    WB24_Vol = Entry()

    WB1_Solvent1_Conc = Entry()
    WB2_Solvent1_Conc = Entry()
    WB3_Solvent1_Conc = Entry()
    WB4_Solvent1_Conc = Entry()
    WB5_Solvent1_Conc = Entry()
    WB6_Solvent1_Conc = Entry()
    WB7_Solvent1_Conc = Entry()
    WB8_Solvent1_Conc = Entry()
    WB9_Solvent1_Conc = Entry()
    WB10_Solvent1_Conc = Entry()
    WB11_Solvent1_Conc = Entry()
    WB12_Solvent1_Conc = Entry()
    WB13_Solvent1_Conc = Entry()
    WB14_Solvent1_Conc = Entry()
    WB15_Solvent1_Conc = Entry()
    WB16_Solvent1_Conc = Entry()
    WB17_Solvent1_Conc = Entry()
    WB18_Solvent1_Conc = Entry()
    WB19_Solvent1_Conc = Entry()
    WB20_Solvent1_Conc = Entry()
    WB21_Solvent1_Conc = Entry()
    WB22_Solvent1_Conc = Entry()
    WB23_Solvent1_Conc = Entry()
    WB24_Solvent1_Conc = Entry()
    
    WB1_Solvent2_Conc = Entry()
    WB2_Solvent2_Conc = Entry()
    WB3_Solvent2_Conc = Entry()
    WB4_Solvent2_Conc = Entry()
    WB5_Solvent2_Conc = Entry()
    WB6_Solvent2_Conc = Entry()
    WB7_Solvent2_Conc = Entry()
    WB8_Solvent2_Conc = Entry()
    WB9_Solvent2_Conc = Entry()
    WB10_Solvent2_Conc = Entry()
    WB11_Solvent2_Conc = Entry()
    WB12_Solvent2_Conc = Entry()
    WB13_Solvent2_Conc = Entry()
    WB14_Solvent2_Conc = Entry()
    WB15_Solvent2_Conc = Entry()
    WB16_Solvent2_Conc = Entry()
    WB17_Solvent2_Conc = Entry()
    WB18_Solvent2_Conc = Entry()
    WB19_Solvent2_Conc = Entry()
    WB20_Solvent2_Conc = Entry()
    WB21_Solvent2_Conc = Entry()
    WB22_Solvent2_Conc = Entry()
    WB23_Solvent2_Conc = Entry()
    WB24_Solvent2_Conc = Entry()
    
    WB1_SS_Conc = Entry()
    WB2_SS_Conc = Entry()
    WB3_SS_Conc = Entry()
    WB4_SS_Conc = Entry()
    WB5_SS_Conc = Entry()
    WB6_SS_Conc = Entry()
    WB7_SS_Conc = Entry()
    WB8_SS_Conc = Entry()
    WB9_SS_Conc = Entry()
    WB10_SS_Conc = Entry()
    WB11_SS_Conc = Entry()
    WB12_SS_Conc = Entry()
    WB13_SS_Conc = Entry()
    WB14_SS_Conc = Entry()
    WB15_SS_Conc = Entry()
    WB16_SS_Conc = Entry()
    WB17_SS_Conc = Entry()
    WB18_SS_Conc = Entry()
    WB19_SS_Conc = Entry()
    WB20_SS_Conc = Entry()
    WB21_SS_Conc = Entry()
    WB22_SS_Conc = Entry()
    WB23_SS_Conc = Entry()
    WB24_SS_Conc = Entry()

    WB1_Ingr = StringVar(OT)
    WB1_IngrMenu = OptionMenu(OT,WB1_Ingr,*Ingrs)
    WB2_Ingr = StringVar(OT)
    WB2_IngrMenu = OptionMenu(OT,WB2_Ingr,*Ingrs)
    WB3_Ingr = StringVar(OT)
    WB3_IngrMenu = OptionMenu(OT,WB3_Ingr,*Ingrs)
    WB4_Ingr = StringVar(OT)
    WB4_IngrMenu = OptionMenu(OT,WB4_Ingr,*Ingrs)
    WB5_Ingr = StringVar(OT)
    WB5_IngrMenu = OptionMenu(OT,WB5_Ingr,*Ingrs)
    WB6_Ingr = StringVar(OT)
    WB6_IngrMenu = OptionMenu(OT,WB6_Ingr,*Ingrs)
    WB7_Ingr = StringVar(OT)
    WB7_IngrMenu = OptionMenu(OT,WB7_Ingr,*Ingrs)
    WB8_Ingr = StringVar(OT)
    WB8_IngrMenu = OptionMenu(OT,WB8_Ingr,*Ingrs)
    WB9_Ingr = StringVar(OT)
    WB9_IngrMenu = OptionMenu(OT,WB9_Ingr,*Ingrs)
    WB10_Ingr = StringVar(OT)
    WB10_IngrMenu = OptionMenu(OT,WB10_Ingr,*Ingrs)
    WB11_Ingr = StringVar(OT)
    WB11_IngrMenu = OptionMenu(OT,WB11_Ingr,*Ingrs)
    WB12_Ingr = StringVar(OT)
    WB12_IngrMenu = OptionMenu(OT,WB12_Ingr,*Ingrs)
    WB13_Ingr = StringVar(OT)
    WB13_IngrMenu = OptionMenu(OT,WB13_Ingr,*Ingrs)
    WB14_Ingr = StringVar(OT)
    WB14_IngrMenu = OptionMenu(OT,WB14_Ingr,*Ingrs)
    WB15_Ingr = StringVar(OT)
    WB15_IngrMenu = OptionMenu(OT,WB15_Ingr,*Ingrs)
    WB16_Ingr = StringVar(OT)
    WB16_IngrMenu = OptionMenu(OT,WB16_Ingr,*Ingrs)
    WB17_Ingr = StringVar(OT)
    WB17_IngrMenu = OptionMenu(OT,WB17_Ingr,*Ingrs)
    WB18_Ingr = StringVar(OT)
    WB18_IngrMenu = OptionMenu(OT,WB18_Ingr,*Ingrs)
    WB19_Ingr = StringVar(OT)
    WB19_IngrMenu = OptionMenu(OT,WB19_Ingr,*Ingrs)
    WB20_Ingr = StringVar(OT)
    WB20_IngrMenu = OptionMenu(OT,WB20_Ingr,*Ingrs)
    WB21_Ingr = StringVar(OT)
    WB21_IngrMenu = OptionMenu(OT,WB21_Ingr,*Ingrs)
    WB22_Ingr = StringVar(OT)
    WB22_IngrMenu = OptionMenu(OT,WB22_Ingr,*Ingrs)
    WB23_Ingr = StringVar(OT)
    WB23_IngrMenu = OptionMenu(OT,WB23_Ingr,*Ingrs)
    WB24_Ingr = StringVar(OT)
    WB24_IngrMenu = OptionMenu(OT,WB24_Ingr,*Ingrs)

    WB1_SS = StringVar(OT)
    WB1_SSMenu = OptionMenu(OT,WB1_SS,*SSInitiators)
    WB2_SS = StringVar(OT)
    WB2_SSMenu = OptionMenu(OT,WB2_SS,*SSInitiators)
    WB3_SS = StringVar(OT)
    WB3_SSMenu = OptionMenu(OT,WB3_SS,*SSInitiators)
    WB4_SS = StringVar(OT)
    WB4_SSMenu = OptionMenu(OT,WB4_SS,*SSInitiators)
    WB5_SS = StringVar(OT)
    WB5_SSMenu = OptionMenu(OT,WB5_SS,*SSInitiators)
    WB6_SS = StringVar(OT)
    WB6_SSMenu = OptionMenu(OT,WB6_SS,*SSInitiators)
    WB7_SS = StringVar(OT)
    WB7_SSMenu = OptionMenu(OT,WB7_SS,*SSInitiators)
    WB8_SS = StringVar(OT)
    WB8_SSMenu = OptionMenu(OT,WB8_SS,*SSInitiators)
    WB9_SS = StringVar(OT)
    WB9_SSMenu = OptionMenu(OT,WB9_SS,*SSInitiators)
    WB10_SS = StringVar(OT)
    WB10_SSMenu = OptionMenu(OT,WB10_SS,*SSInitiators)
    WB11_SS = StringVar(OT)
    WB11_SSMenu = OptionMenu(OT,WB11_SS,*SSInitiators)
    WB12_SS = StringVar(OT)
    WB12_SSMenu = OptionMenu(OT,WB12_SS,*SSInitiators)
    WB13_SS = StringVar(OT)
    WB13_SSMenu = OptionMenu(OT,WB13_SS,*SSInitiators)
    WB14_SS = StringVar(OT)
    WB14_SSMenu = OptionMenu(OT,WB14_SS,*SSInitiators)
    WB15_SS = StringVar(OT)
    WB15_SSMenu = OptionMenu(OT,WB15_SS,*SSInitiators)
    WB16_SS = StringVar(OT)
    WB16_SSMenu = OptionMenu(OT,WB16_SS,*SSInitiators)
    WB17_SS = StringVar(OT)
    WB17_SSMenu = OptionMenu(OT,WB17_SS,*SSInitiators)
    WB18_SS = StringVar(OT)
    WB18_SSMenu = OptionMenu(OT,WB18_SS,*SSInitiators)
    WB19_SS = StringVar(OT)
    WB19_SSMenu = OptionMenu(OT,WB19_SS,*SSInitiators)
    WB20_SS = StringVar(OT)
    WB20_SSMenu = OptionMenu(OT,WB20_SS,*SSInitiators)
    WB21_SS = StringVar(OT)
    WB21_SSMenu = OptionMenu(OT,WB21_SS,*SSInitiators)
    WB22_SS = StringVar(OT)
    WB22_SSMenu = OptionMenu(OT,WB22_SS,*SSInitiators)
    WB23_SS = StringVar(OT)
    WB23_SSMenu = OptionMenu(OT,WB23_SS,*SSInitiators)
    WB24_SS = StringVar(OT)
    WB24_SSMenu = OptionMenu(OT,WB24_SS,*SSInitiators)

    WB1_Dilu = StringVar(OT)
    WB1_DiluMenu = OptionMenu(OT,WB1_Dilu,*Diluents)
    WB2_Dilu = StringVar(OT)
    WB2_DiluMenu = OptionMenu(OT,WB2_Dilu,*Diluents)
    WB3_Dilu = StringVar(OT)
    WB3_DiluMenu = OptionMenu(OT,WB3_Dilu,*Diluents)
    WB4_Dilu = StringVar(OT)
    WB4_DiluMenu = OptionMenu(OT,WB4_Dilu,*Diluents)
    WB5_Dilu = StringVar(OT)
    WB5_DiluMenu = OptionMenu(OT,WB5_Dilu,*Diluents)
    WB6_Dilu = StringVar(OT)
    WB6_DiluMenu = OptionMenu(OT,WB6_Dilu,*Diluents)
    WB7_Dilu = StringVar(OT)
    WB7_DiluMenu = OptionMenu(OT,WB7_Dilu,*Diluents)
    WB8_Dilu = StringVar(OT)
    WB8_DiluMenu = OptionMenu(OT,WB8_Dilu,*Diluents)
    WB9_Dilu = StringVar(OT)
    WB9_DiluMenu = OptionMenu(OT,WB9_Dilu,*Diluents)
    WB10_Dilu = StringVar(OT)
    WB10_DiluMenu = OptionMenu(OT,WB10_Dilu,*Diluents)
    WB11_Dilu = StringVar(OT)
    WB11_DiluMenu = OptionMenu(OT,WB11_Dilu,*Diluents)
    WB12_Dilu = StringVar(OT)
    WB12_DiluMenu = OptionMenu(OT,WB12_Dilu,*Diluents)
    WB13_Dilu = StringVar(OT)
    WB13_DiluMenu = OptionMenu(OT,WB13_Dilu,*Diluents)
    WB14_Dilu = StringVar(OT)
    WB14_DiluMenu = OptionMenu(OT,WB14_Dilu,*Diluents)
    WB15_Dilu = StringVar(OT)
    WB15_DiluMenu = OptionMenu(OT,WB15_Dilu,*Diluents)
    WB16_Dilu = StringVar(OT)
    WB16_DiluMenu = OptionMenu(OT,WB16_Dilu,*Diluents)
    WB17_Dilu = StringVar(OT)
    WB17_DiluMenu = OptionMenu(OT,WB17_Dilu,*Diluents)
    WB18_Dilu = StringVar(OT)
    WB18_DiluMenu = OptionMenu(OT,WB18_Dilu,*Diluents)
    WB19_Dilu = StringVar(OT)
    WB19_DiluMenu = OptionMenu(OT,WB19_Dilu,*Diluents)
    WB20_Dilu = StringVar(OT)
    WB20_DiluMenu = OptionMenu(OT,WB20_Dilu,*Diluents)
    WB21_Dilu = StringVar(OT)
    WB21_DiluMenu = OptionMenu(OT,WB21_Dilu,*Diluents)
    WB22_Dilu = StringVar(OT)
    WB22_DiluMenu = OptionMenu(OT,WB22_Dilu,*Diluents)
    WB23_Dilu = StringVar(OT)
    WB23_DiluMenu = OptionMenu(OT,WB23_Dilu,*Diluents)
    WB24_Dilu = StringVar(OT)
    WB24_DiluMenu = OptionMenu(OT,WB24_Dilu,*Diluents)

    WC1_Vol = Entry()
    WC2_Vol = Entry()
    WC3_Vol = Entry()
    WC4_Vol = Entry()
    WC5_Vol = Entry()
    WC6_Vol = Entry()
    WC7_Vol = Entry()
    WC8_Vol = Entry()
    WC9_Vol = Entry()
    WC10_Vol = Entry()
    WC11_Vol = Entry()
    WC12_Vol = Entry()
    WC13_Vol = Entry()
    WC14_Vol = Entry()
    WC15_Vol = Entry()
    WC16_Vol = Entry()
    WC17_Vol = Entry()
    WC18_Vol = Entry()
    WC19_Vol = Entry()
    WC20_Vol = Entry()
    WC21_Vol = Entry()
    WC22_Vol = Entry()
    WC23_Vol = Entry()
    WC24_Vol = Entry()

    WC1_Solvent1_Conc = Entry()
    WC2_Solvent1_Conc = Entry()
    WC3_Solvent1_Conc = Entry()
    WC4_Solvent1_Conc = Entry()
    WC5_Solvent1_Conc = Entry()
    WC6_Solvent1_Conc = Entry()
    WC7_Solvent1_Conc = Entry()
    WC8_Solvent1_Conc = Entry()
    WC9_Solvent1_Conc = Entry()
    WC10_Solvent1_Conc = Entry()
    WC11_Solvent1_Conc = Entry()
    WC12_Solvent1_Conc = Entry()
    WC13_Solvent1_Conc = Entry()
    WC14_Solvent1_Conc = Entry()
    WC15_Solvent1_Conc = Entry()
    WC16_Solvent1_Conc = Entry()
    WC17_Solvent1_Conc = Entry()
    WC18_Solvent1_Conc = Entry()
    WC19_Solvent1_Conc = Entry()
    WC20_Solvent1_Conc = Entry()
    WC21_Solvent1_Conc = Entry()
    WC22_Solvent1_Conc = Entry()
    WC23_Solvent1_Conc = Entry()
    WC24_Solvent1_Conc = Entry()
    
    WC1_Solvent2_Conc = Entry()
    WC2_Solvent2_Conc = Entry()
    WC3_Solvent2_Conc = Entry()
    WC4_Solvent2_Conc = Entry()
    WC5_Solvent2_Conc = Entry()
    WC6_Solvent2_Conc = Entry()
    WC7_Solvent2_Conc = Entry()
    WC8_Solvent2_Conc = Entry()
    WC9_Solvent2_Conc = Entry()
    WC10_Solvent2_Conc = Entry()
    WC11_Solvent2_Conc = Entry()
    WC12_Solvent2_Conc = Entry()
    WC13_Solvent2_Conc = Entry()
    WC14_Solvent2_Conc = Entry()
    WC15_Solvent2_Conc = Entry()
    WC16_Solvent2_Conc = Entry()
    WC17_Solvent2_Conc = Entry()
    WC18_Solvent2_Conc = Entry()
    WC19_Solvent2_Conc = Entry()
    WC20_Solvent2_Conc = Entry()
    WC21_Solvent2_Conc = Entry()
    WC22_Solvent2_Conc = Entry()
    WC23_Solvent2_Conc = Entry()
    WC24_Solvent2_Conc = Entry()
    
    WC1_SS_Conc = Entry()
    WC2_SS_Conc = Entry()
    WC3_SS_Conc = Entry()
    WC4_SS_Conc = Entry()
    WC5_SS_Conc = Entry()
    WC6_SS_Conc = Entry()
    WC7_SS_Conc = Entry()
    WC8_SS_Conc = Entry()
    WC9_SS_Conc = Entry()
    WC10_SS_Conc = Entry()
    WC11_SS_Conc = Entry()
    WC12_SS_Conc = Entry()
    WC13_SS_Conc = Entry()
    WC14_SS_Conc = Entry()
    WC15_SS_Conc = Entry()
    WC16_SS_Conc = Entry()
    WC17_SS_Conc = Entry()
    WC18_SS_Conc = Entry()
    WC19_SS_Conc = Entry()
    WC20_SS_Conc = Entry()
    WC21_SS_Conc = Entry()
    WC22_SS_Conc = Entry()
    WC23_SS_Conc = Entry()
    WC24_SS_Conc = Entry()

    WC1_Ingr = StringVar(OT)
    WC1_IngrMenu = OptionMenu(OT,WC1_Ingr,*Ingrs)
    WC2_Ingr = StringVar(OT)
    WC2_IngrMenu = OptionMenu(OT,WC2_Ingr,*Ingrs)
    WC3_Ingr = StringVar(OT)
    WC3_IngrMenu = OptionMenu(OT,WC3_Ingr,*Ingrs)
    WC4_Ingr = StringVar(OT)
    WC4_IngrMenu = OptionMenu(OT,WC4_Ingr,*Ingrs)
    WC5_Ingr = StringVar(OT)
    WC5_IngrMenu = OptionMenu(OT,WC5_Ingr,*Ingrs)
    WC6_Ingr = StringVar(OT)
    WC6_IngrMenu = OptionMenu(OT,WC6_Ingr,*Ingrs)
    WC7_Ingr = StringVar(OT)
    WC7_IngrMenu = OptionMenu(OT,WC7_Ingr,*Ingrs)
    WC8_Ingr = StringVar(OT)
    WC8_IngrMenu = OptionMenu(OT,WC8_Ingr,*Ingrs)
    WC9_Ingr = StringVar(OT)
    WC9_IngrMenu = OptionMenu(OT,WC9_Ingr,*Ingrs)
    WC10_Ingr = StringVar(OT)
    WC10_IngrMenu = OptionMenu(OT,WC10_Ingr,*Ingrs)
    WC11_Ingr = StringVar(OT)
    WC11_IngrMenu = OptionMenu(OT,WC11_Ingr,*Ingrs)
    WC12_Ingr = StringVar(OT)
    WC12_IngrMenu = OptionMenu(OT,WC12_Ingr,*Ingrs)
    WC13_Ingr = StringVar(OT)
    WC13_IngrMenu = OptionMenu(OT,WC13_Ingr,*Ingrs)
    WC14_Ingr = StringVar(OT)
    WC14_IngrMenu = OptionMenu(OT,WC14_Ingr,*Ingrs)
    WC15_Ingr = StringVar(OT)
    WC15_IngrMenu = OptionMenu(OT,WC15_Ingr,*Ingrs)
    WC16_Ingr = StringVar(OT)
    WC16_IngrMenu = OptionMenu(OT,WC16_Ingr,*Ingrs)
    WC17_Ingr = StringVar(OT)
    WC17_IngrMenu = OptionMenu(OT,WC17_Ingr,*Ingrs)
    WC18_Ingr = StringVar(OT)
    WC18_IngrMenu = OptionMenu(OT,WC18_Ingr,*Ingrs)
    WC19_Ingr = StringVar(OT)
    WC19_IngrMenu = OptionMenu(OT,WC19_Ingr,*Ingrs)
    WC20_Ingr = StringVar(OT)
    WC20_IngrMenu = OptionMenu(OT,WC20_Ingr,*Ingrs)
    WC21_Ingr = StringVar(OT)
    WC21_IngrMenu = OptionMenu(OT,WC21_Ingr,*Ingrs)
    WC22_Ingr = StringVar(OT)
    WC22_IngrMenu = OptionMenu(OT,WC22_Ingr,*Ingrs)
    WC23_Ingr = StringVar(OT)
    WC23_IngrMenu = OptionMenu(OT,WC23_Ingr,*Ingrs)
    WC24_Ingr = StringVar(OT)
    WC24_IngrMenu = OptionMenu(OT,WC24_Ingr,*Ingrs)

    WC1_SS = StringVar(OT)
    WC1_SSMenu = OptionMenu(OT,WC1_SS,*SSInitiators)
    WC2_SS = StringVar(OT)
    WC2_SSMenu = OptionMenu(OT,WC2_SS,*SSInitiators)
    WC3_SS = StringVar(OT)
    WC3_SSMenu = OptionMenu(OT,WC3_SS,*SSInitiators)
    WC4_SS = StringVar(OT)
    WC4_SSMenu = OptionMenu(OT,WC4_SS,*SSInitiators)
    WC5_SS = StringVar(OT)
    WC5_SSMenu = OptionMenu(OT,WC5_SS,*SSInitiators)
    WC6_SS = StringVar(OT)
    WC6_SSMenu = OptionMenu(OT,WC6_SS,*SSInitiators)
    WC7_SS = StringVar(OT)
    WC7_SSMenu = OptionMenu(OT,WC7_SS,*SSInitiators)
    WC8_SS = StringVar(OT)
    WC8_SSMenu = OptionMenu(OT,WC8_SS,*SSInitiators)
    WC9_SS = StringVar(OT)
    WC9_SSMenu = OptionMenu(OT,WC9_SS,*SSInitiators)
    WC10_SS = StringVar(OT)
    WC10_SSMenu = OptionMenu(OT,WC10_SS,*SSInitiators)
    WC11_SS = StringVar(OT)
    WC11_SSMenu = OptionMenu(OT,WC11_SS,*SSInitiators)
    WC12_SS = StringVar(OT)
    WC12_SSMenu = OptionMenu(OT,WC12_SS,*SSInitiators)
    WC13_SS = StringVar(OT)
    WC13_SSMenu = OptionMenu(OT,WC13_SS,*SSInitiators)
    WC14_SS = StringVar(OT)
    WC14_SSMenu = OptionMenu(OT,WC14_SS,*SSInitiators)
    WC15_SS = StringVar(OT)
    WC15_SSMenu = OptionMenu(OT,WC15_SS,*SSInitiators)
    WC16_SS = StringVar(OT)
    WC16_SSMenu = OptionMenu(OT,WC16_SS,*SSInitiators)
    WC17_SS = StringVar(OT)
    WC17_SSMenu = OptionMenu(OT,WC17_SS,*SSInitiators)
    WC18_SS = StringVar(OT)
    WC18_SSMenu = OptionMenu(OT,WC18_SS,*SSInitiators)
    WC19_SS = StringVar(OT)
    WC19_SSMenu = OptionMenu(OT,WC19_SS,*SSInitiators)
    WC20_SS = StringVar(OT)
    WC20_SSMenu = OptionMenu(OT,WC20_SS,*SSInitiators)
    WC21_SS = StringVar(OT)
    WC21_SSMenu = OptionMenu(OT,WC21_SS,*SSInitiators)
    WC22_SS = StringVar(OT)
    WC22_SSMenu = OptionMenu(OT,WC22_SS,*SSInitiators)
    WC23_SS = StringVar(OT)
    WC23_SSMenu = OptionMenu(OT,WC23_SS,*SSInitiators)
    WC24_SS = StringVar(OT)
    WC24_SSMenu = OptionMenu(OT,WC24_SS,*SSInitiators)

    WC1_Dilu = StringVar(OT)
    WC1_DiluMenu = OptionMenu(OT,WC1_Dilu,*Diluents)
    WC2_Dilu = StringVar(OT)
    WC2_DiluMenu = OptionMenu(OT,WC2_Dilu,*Diluents)
    WC3_Dilu = StringVar(OT)
    WC3_DiluMenu = OptionMenu(OT,WC3_Dilu,*Diluents)
    WC4_Dilu = StringVar(OT)
    WC4_DiluMenu = OptionMenu(OT,WC4_Dilu,*Diluents)
    WC5_Dilu = StringVar(OT)
    WC5_DiluMenu = OptionMenu(OT,WC5_Dilu,*Diluents)
    WC6_Dilu = StringVar(OT)
    WC6_DiluMenu = OptionMenu(OT,WC6_Dilu,*Diluents)
    WC7_Dilu = StringVar(OT)
    WC7_DiluMenu = OptionMenu(OT,WC7_Dilu,*Diluents)
    WC8_Dilu = StringVar(OT)
    WC8_DiluMenu = OptionMenu(OT,WC8_Dilu,*Diluents)
    WC9_Dilu = StringVar(OT)
    WC9_DiluMenu = OptionMenu(OT,WC9_Dilu,*Diluents)
    WC10_Dilu = StringVar(OT)
    WC10_DiluMenu = OptionMenu(OT,WC10_Dilu,*Diluents)
    WC11_Dilu = StringVar(OT)
    WC11_DiluMenu = OptionMenu(OT,WC11_Dilu,*Diluents)
    WC12_Dilu = StringVar(OT)
    WC12_DiluMenu = OptionMenu(OT,WC12_Dilu,*Diluents)
    WC13_Dilu = StringVar(OT)
    WC13_DiluMenu = OptionMenu(OT,WC13_Dilu,*Diluents)
    WC14_Dilu = StringVar(OT)
    WC14_DiluMenu = OptionMenu(OT,WC14_Dilu,*Diluents)
    WC15_Dilu = StringVar(OT)
    WC15_DiluMenu = OptionMenu(OT,WC15_Dilu,*Diluents)
    WC16_Dilu = StringVar(OT)
    WC16_DiluMenu = OptionMenu(OT,WC16_Dilu,*Diluents)
    WC17_Dilu = StringVar(OT)
    WC17_DiluMenu = OptionMenu(OT,WC17_Dilu,*Diluents)
    WC18_Dilu = StringVar(OT)
    WC18_DiluMenu = OptionMenu(OT,WC18_Dilu,*Diluents)
    WC19_Dilu = StringVar(OT)
    WC19_DiluMenu = OptionMenu(OT,WC19_Dilu,*Diluents)
    WC20_Dilu = StringVar(OT)
    WC20_DiluMenu = OptionMenu(OT,WC20_Dilu,*Diluents)
    WC21_Dilu = StringVar(OT)
    WC21_DiluMenu = OptionMenu(OT,WC21_Dilu,*Diluents)
    WC22_Dilu = StringVar(OT)
    WC22_DiluMenu = OptionMenu(OT,WC22_Dilu,*Diluents)
    WC23_Dilu = StringVar(OT)
    WC23_DiluMenu = OptionMenu(OT,WC23_Dilu,*Diluents)
    WC24_Dilu = StringVar(OT)
    WC24_DiluMenu = OptionMenu(OT,WC24_Dilu,*Diluents)

    WD1_Vol = Entry()
    WD2_Vol = Entry()
    WD3_Vol = Entry()
    WD4_Vol = Entry()
    WD5_Vol = Entry()
    WD6_Vol = Entry()
    WD7_Vol = Entry()
    WD8_Vol = Entry()
    WD9_Vol = Entry()
    WD10_Vol = Entry()
    WD11_Vol = Entry()
    WD12_Vol = Entry()
    WD13_Vol = Entry()
    WD14_Vol = Entry()
    WD15_Vol = Entry()
    WD16_Vol = Entry()
    WD17_Vol = Entry()
    WD18_Vol = Entry()
    WD19_Vol = Entry()
    WD20_Vol = Entry()
    WD21_Vol = Entry()
    WD22_Vol = Entry()
    WD23_Vol = Entry()
    WD24_Vol = Entry()

    WD1_Solvent1_Conc = Entry()
    WD2_Solvent1_Conc = Entry()
    WD3_Solvent1_Conc = Entry()
    WD4_Solvent1_Conc = Entry()
    WD5_Solvent1_Conc = Entry()
    WD6_Solvent1_Conc = Entry()
    WD7_Solvent1_Conc = Entry()
    WD8_Solvent1_Conc = Entry()
    WD9_Solvent1_Conc = Entry()
    WD10_Solvent1_Conc = Entry()
    WD11_Solvent1_Conc = Entry()
    WD12_Solvent1_Conc = Entry()
    WD13_Solvent1_Conc = Entry()
    WD14_Solvent1_Conc = Entry()
    WD15_Solvent1_Conc = Entry()
    WD16_Solvent1_Conc = Entry()
    WD17_Solvent1_Conc = Entry()
    WD18_Solvent1_Conc = Entry()
    WD19_Solvent1_Conc = Entry()
    WD20_Solvent1_Conc = Entry()
    WD21_Solvent1_Conc = Entry()
    WD22_Solvent1_Conc = Entry()
    WD23_Solvent1_Conc = Entry()
    WD24_Solvent1_Conc = Entry()
    
    WD1_Solvent2_Conc = Entry()
    WD2_Solvent2_Conc = Entry()
    WD3_Solvent2_Conc = Entry()
    WD4_Solvent2_Conc = Entry()
    WD5_Solvent2_Conc = Entry()
    WD6_Solvent2_Conc = Entry()
    WD7_Solvent2_Conc = Entry()
    WD8_Solvent2_Conc = Entry()
    WD9_Solvent2_Conc = Entry()
    WD10_Solvent2_Conc = Entry()
    WD11_Solvent2_Conc = Entry()
    WD12_Solvent2_Conc = Entry()
    WD13_Solvent2_Conc = Entry()
    WD14_Solvent2_Conc = Entry()
    WD15_Solvent2_Conc = Entry()
    WD16_Solvent2_Conc = Entry()
    WD17_Solvent2_Conc = Entry()
    WD18_Solvent2_Conc = Entry()
    WD19_Solvent2_Conc = Entry()
    WD20_Solvent2_Conc = Entry()
    WD21_Solvent2_Conc = Entry()
    WD22_Solvent2_Conc = Entry()
    WD23_Solvent2_Conc = Entry()
    WD24_Solvent2_Conc = Entry()

    WD1_SS_Conc = Entry()
    WD2_SS_Conc = Entry()
    WD3_SS_Conc = Entry()
    WD4_SS_Conc = Entry()
    WD5_SS_Conc = Entry()
    WD6_SS_Conc = Entry()
    WD7_SS_Conc = Entry()
    WD8_SS_Conc = Entry()
    WD9_SS_Conc = Entry()
    WD10_SS_Conc = Entry()
    WD11_SS_Conc = Entry()
    WD12_SS_Conc = Entry()
    WD13_SS_Conc = Entry()
    WD14_SS_Conc = Entry()
    WD15_SS_Conc = Entry()
    WD16_SS_Conc = Entry()
    WD17_SS_Conc = Entry()
    WD18_SS_Conc = Entry()
    WD19_SS_Conc = Entry()
    WD20_SS_Conc = Entry()
    WD21_SS_Conc = Entry()
    WD22_SS_Conc = Entry()
    WD23_SS_Conc = Entry()
    WD24_SS_Conc = Entry()

    WD1_Ingr = StringVar(OT)
    WD1_IngrMenu = OptionMenu(OT,WD1_Ingr,*Ingrs)
    WD2_Ingr = StringVar(OT)
    WD2_IngrMenu = OptionMenu(OT,WD2_Ingr,*Ingrs)
    WD3_Ingr = StringVar(OT)
    WD3_IngrMenu = OptionMenu(OT,WD3_Ingr,*Ingrs)
    WD4_Ingr = StringVar(OT)
    WD4_IngrMenu = OptionMenu(OT,WD4_Ingr,*Ingrs)
    WD5_Ingr = StringVar(OT)
    WD5_IngrMenu = OptionMenu(OT,WD5_Ingr,*Ingrs)
    WD6_Ingr = StringVar(OT)
    WD6_IngrMenu = OptionMenu(OT,WD6_Ingr,*Ingrs)
    WD7_Ingr = StringVar(OT)
    WD7_IngrMenu = OptionMenu(OT,WD7_Ingr,*Ingrs)
    WD8_Ingr = StringVar(OT)
    WD8_IngrMenu = OptionMenu(OT,WD8_Ingr,*Ingrs)
    WD9_Ingr = StringVar(OT)
    WD9_IngrMenu = OptionMenu(OT,WD9_Ingr,*Ingrs)
    WD10_Ingr = StringVar(OT)
    WD10_IngrMenu = OptionMenu(OT,WD10_Ingr,*Ingrs)
    WD11_Ingr = StringVar(OT)
    WD11_IngrMenu = OptionMenu(OT,WD11_Ingr,*Ingrs)
    WD12_Ingr = StringVar(OT)
    WD12_IngrMenu = OptionMenu(OT,WD12_Ingr,*Ingrs)
    WD13_Ingr = StringVar(OT)
    WD13_IngrMenu = OptionMenu(OT,WD13_Ingr,*Ingrs)
    WD14_Ingr = StringVar(OT)
    WD14_IngrMenu = OptionMenu(OT,WD14_Ingr,*Ingrs)
    WD15_Ingr = StringVar(OT)
    WD15_IngrMenu = OptionMenu(OT,WD15_Ingr,*Ingrs)
    WD16_Ingr = StringVar(OT)
    WD16_IngrMenu = OptionMenu(OT,WD16_Ingr,*Ingrs)
    WD17_Ingr = StringVar(OT)
    WD17_IngrMenu = OptionMenu(OT,WD17_Ingr,*Ingrs)
    WD18_Ingr = StringVar(OT)
    WD18_IngrMenu = OptionMenu(OT,WD18_Ingr,*Ingrs)
    WD19_Ingr = StringVar(OT)
    WD19_IngrMenu = OptionMenu(OT,WD19_Ingr,*Ingrs)
    WD20_Ingr = StringVar(OT)
    WD20_IngrMenu = OptionMenu(OT,WD20_Ingr,*Ingrs)
    WD21_Ingr = StringVar(OT)
    WD21_IngrMenu = OptionMenu(OT,WD21_Ingr,*Ingrs)
    WD22_Ingr = StringVar(OT)
    WD22_IngrMenu = OptionMenu(OT,WD22_Ingr,*Ingrs)
    WD23_Ingr = StringVar(OT)
    WD23_IngrMenu = OptionMenu(OT,WD23_Ingr,*Ingrs)
    WD24_Ingr = StringVar(OT)
    WD24_IngrMenu = OptionMenu(OT,WD24_Ingr,*Ingrs)

    WD1_SS = StringVar(OT)
    WD1_SSMenu = OptionMenu(OT,WD1_SS,*SSInitiators)
    WD2_SS = StringVar(OT)
    WD2_SSMenu = OptionMenu(OT,WD2_SS,*SSInitiators)
    WD3_SS = StringVar(OT)
    WD3_SSMenu = OptionMenu(OT,WD3_SS,*SSInitiators)
    WD4_SS = StringVar(OT)
    WD4_SSMenu = OptionMenu(OT,WD4_SS,*SSInitiators)
    WD5_SS = StringVar(OT)
    WD5_SSMenu = OptionMenu(OT,WD5_SS,*SSInitiators)
    WD6_SS = StringVar(OT)
    WD6_SSMenu = OptionMenu(OT,WD6_SS,*SSInitiators)
    WD7_SS = StringVar(OT)
    WD7_SSMenu = OptionMenu(OT,WD7_SS,*SSInitiators)
    WD8_SS = StringVar(OT)
    WD8_SSMenu = OptionMenu(OT,WD8_SS,*SSInitiators)
    WD9_SS = StringVar(OT)
    WD9_SSMenu = OptionMenu(OT,WD9_SS,*SSInitiators)
    WD10_SS = StringVar(OT)
    WD10_SSMenu = OptionMenu(OT,WD10_SS,*SSInitiators)
    WD11_SS = StringVar(OT)
    WD11_SSMenu = OptionMenu(OT,WD11_SS,*SSInitiators)
    WD12_SS = StringVar(OT)
    WD12_SSMenu = OptionMenu(OT,WD12_SS,*SSInitiators)
    WD13_SS = StringVar(OT)
    WD13_SSMenu = OptionMenu(OT,WD13_SS,*SSInitiators)
    WD14_SS = StringVar(OT)
    WD14_SSMenu = OptionMenu(OT,WD14_SS,*SSInitiators)
    WD15_SS = StringVar(OT)
    WD15_SSMenu = OptionMenu(OT,WD15_SS,*SSInitiators)
    WD16_SS = StringVar(OT)
    WD16_SSMenu = OptionMenu(OT,WD16_SS,*SSInitiators)
    WD17_SS = StringVar(OT)
    WD17_SSMenu = OptionMenu(OT,WD17_SS,*SSInitiators)
    WD18_SS = StringVar(OT)
    WD18_SSMenu = OptionMenu(OT,WD18_SS,*SSInitiators)
    WD19_SS = StringVar(OT)
    WD19_SSMenu = OptionMenu(OT,WD19_SS,*SSInitiators)
    WD20_SS = StringVar(OT)
    WD20_SSMenu = OptionMenu(OT,WD20_SS,*SSInitiators)
    WD21_SS = StringVar(OT)
    WD21_SSMenu = OptionMenu(OT,WD21_SS,*SSInitiators)
    WD22_SS = StringVar(OT)
    WD22_SSMenu = OptionMenu(OT,WD22_SS,*SSInitiators)
    WD23_SS = StringVar(OT)
    WD23_SSMenu = OptionMenu(OT,WD23_SS,*SSInitiators)
    WD24_SS = StringVar(OT)
    WD24_SSMenu = OptionMenu(OT,WD24_SS,*SSInitiators)

    WD1_Dilu = StringVar(OT)
    WD1_DiluMenu = OptionMenu(OT,WD1_Dilu,*Diluents)
    WD2_Dilu = StringVar(OT)
    WD2_DiluMenu = OptionMenu(OT,WD2_Dilu,*Diluents)
    WD3_Dilu = StringVar(OT)
    WD3_DiluMenu = OptionMenu(OT,WD3_Dilu,*Diluents)
    WD4_Dilu = StringVar(OT)
    WD4_DiluMenu = OptionMenu(OT,WD4_Dilu,*Diluents)
    WD5_Dilu = StringVar(OT)
    WD5_DiluMenu = OptionMenu(OT,WD5_Dilu,*Diluents)
    WD6_Dilu = StringVar(OT)
    WD6_DiluMenu = OptionMenu(OT,WD6_Dilu,*Diluents)
    WD7_Dilu = StringVar(OT)
    WD7_DiluMenu = OptionMenu(OT,WD7_Dilu,*Diluents)
    WD8_Dilu = StringVar(OT)
    WD8_DiluMenu = OptionMenu(OT,WD8_Dilu,*Diluents)
    WD9_Dilu = StringVar(OT)
    WD9_DiluMenu = OptionMenu(OT,WD9_Dilu,*Diluents)
    WD10_Dilu = StringVar(OT)
    WD10_DiluMenu = OptionMenu(OT,WD10_Dilu,*Diluents)
    WD11_Dilu = StringVar(OT)
    WD11_DiluMenu = OptionMenu(OT,WD11_Dilu,*Diluents)
    WD12_Dilu = StringVar(OT)
    WD12_DiluMenu = OptionMenu(OT,WD12_Dilu,*Diluents)
    WD13_Dilu = StringVar(OT)
    WD13_DiluMenu = OptionMenu(OT,WD13_Dilu,*Diluents)
    WD14_Dilu = StringVar(OT)
    WD14_DiluMenu = OptionMenu(OT,WD14_Dilu,*Diluents)
    WD15_Dilu = StringVar(OT)
    WD15_DiluMenu = OptionMenu(OT,WD15_Dilu,*Diluents)
    WD16_Dilu = StringVar(OT)
    WD16_DiluMenu = OptionMenu(OT,WD16_Dilu,*Diluents)
    WD17_Dilu = StringVar(OT)
    WD17_DiluMenu = OptionMenu(OT,WD17_Dilu,*Diluents)
    WD18_Dilu = StringVar(OT)
    WD18_DiluMenu = OptionMenu(OT,WD18_Dilu,*Diluents)
    WD19_Dilu = StringVar(OT)
    WD19_DiluMenu = OptionMenu(OT,WD19_Dilu,*Diluents)
    WD20_Dilu = StringVar(OT)
    WD20_DiluMenu = OptionMenu(OT,WD20_Dilu,*Diluents)
    WD21_Dilu = StringVar(OT)
    WD21_DiluMenu = OptionMenu(OT,WD21_Dilu,*Diluents)
    WD22_Dilu = StringVar(OT)
    WD22_DiluMenu = OptionMenu(OT,WD22_Dilu,*Diluents)
    WD23_Dilu = StringVar(OT)
    WD23_DiluMenu = OptionMenu(OT,WD23_Dilu,*Diluents)
    WD24_Dilu = StringVar(OT)
    WD24_DiluMenu = OptionMenu(OT,WD24_Dilu,*Diluents)

    WE1_Vol = Entry()
    WE2_Vol = Entry()
    WE3_Vol = Entry()
    WE4_Vol = Entry()
    WE5_Vol = Entry()
    WE6_Vol = Entry()
    WE7_Vol = Entry()
    WE8_Vol = Entry()
    WE9_Vol = Entry()
    WE10_Vol = Entry()
    WE11_Vol = Entry()
    WE12_Vol = Entry()
    WE13_Vol = Entry()
    WE14_Vol = Entry()
    WE15_Vol = Entry()
    WE16_Vol = Entry()
    WE17_Vol = Entry()
    WE18_Vol = Entry()
    WE19_Vol = Entry()
    WE20_Vol = Entry()
    WE21_Vol = Entry()
    WE22_Vol = Entry()
    WE23_Vol = Entry()
    WE24_Vol = Entry()

    WE1_Solvent1_Conc = Entry()
    WE2_Solvent1_Conc = Entry()
    WE3_Solvent1_Conc = Entry()
    WE4_Solvent1_Conc = Entry()
    WE5_Solvent1_Conc = Entry()
    WE6_Solvent1_Conc = Entry()
    WE7_Solvent1_Conc = Entry()
    WE8_Solvent1_Conc = Entry()
    WE9_Solvent1_Conc = Entry()
    WE10_Solvent1_Conc = Entry()
    WE11_Solvent1_Conc = Entry()
    WE12_Solvent1_Conc = Entry()
    WE13_Solvent1_Conc = Entry()
    WE14_Solvent1_Conc = Entry()
    WE15_Solvent1_Conc = Entry()
    WE16_Solvent1_Conc = Entry()
    WE17_Solvent1_Conc = Entry()
    WE18_Solvent1_Conc = Entry()
    WE19_Solvent1_Conc = Entry()
    WE20_Solvent1_Conc = Entry()
    WE21_Solvent1_Conc = Entry()
    WE22_Solvent1_Conc = Entry()
    WE23_Solvent1_Conc = Entry()
    WE24_Solvent1_Conc = Entry()
    
    WE1_Solvent2_Conc = Entry()
    WE2_Solvent2_Conc = Entry()
    WE3_Solvent2_Conc = Entry()
    WE4_Solvent2_Conc = Entry()
    WE5_Solvent2_Conc = Entry()
    WE6_Solvent2_Conc = Entry()
    WE7_Solvent2_Conc = Entry()
    WE8_Solvent2_Conc = Entry()
    WE9_Solvent2_Conc = Entry()
    WE10_Solvent2_Conc = Entry()
    WE11_Solvent2_Conc = Entry()
    WE12_Solvent2_Conc = Entry()
    WE13_Solvent2_Conc = Entry()
    WE14_Solvent2_Conc = Entry()
    WE15_Solvent2_Conc = Entry()
    WE16_Solvent2_Conc = Entry()
    WE17_Solvent2_Conc = Entry()
    WE18_Solvent2_Conc = Entry()
    WE19_Solvent2_Conc = Entry()
    WE20_Solvent2_Conc = Entry()
    WE21_Solvent2_Conc = Entry()
    WE22_Solvent2_Conc = Entry()
    WE23_Solvent2_Conc = Entry()
    WE24_Solvent2_Conc = Entry()

    WE1_SS_Conc = Entry()
    WE2_SS_Conc = Entry()
    WE3_SS_Conc = Entry()
    WE4_SS_Conc = Entry()
    WE5_SS_Conc = Entry()
    WE6_SS_Conc = Entry()
    WE7_SS_Conc = Entry()
    WE8_SS_Conc = Entry()
    WE9_SS_Conc = Entry()
    WE10_SS_Conc = Entry()
    WE11_SS_Conc = Entry()
    WE12_SS_Conc = Entry()
    WE13_SS_Conc = Entry()
    WE14_SS_Conc = Entry()
    WE15_SS_Conc = Entry()
    WE16_SS_Conc = Entry()
    WE17_SS_Conc = Entry()
    WE18_SS_Conc = Entry()
    WE19_SS_Conc = Entry()
    WE20_SS_Conc = Entry()
    WE21_SS_Conc = Entry()
    WE22_SS_Conc = Entry()
    WE23_SS_Conc = Entry()
    WE24_SS_Conc = Entry()

    WE1_Ingr = StringVar(OT)
    WE1_IngrMenu = OptionMenu(OT,WE1_Ingr,*Ingrs)
    WE2_Ingr = StringVar(OT)
    WE2_IngrMenu = OptionMenu(OT,WE2_Ingr,*Ingrs)
    WE3_Ingr = StringVar(OT)
    WE3_IngrMenu = OptionMenu(OT,WE3_Ingr,*Ingrs)
    WE4_Ingr = StringVar(OT)
    WE4_IngrMenu = OptionMenu(OT,WE4_Ingr,*Ingrs)
    WE5_Ingr = StringVar(OT)
    WE5_IngrMenu = OptionMenu(OT,WE5_Ingr,*Ingrs)
    WE6_Ingr = StringVar(OT)
    WE6_IngrMenu = OptionMenu(OT,WE6_Ingr,*Ingrs)
    WE7_Ingr = StringVar(OT)
    WE7_IngrMenu = OptionMenu(OT,WE7_Ingr,*Ingrs)
    WE8_Ingr = StringVar(OT)
    WE8_IngrMenu = OptionMenu(OT,WE8_Ingr,*Ingrs)
    WE9_Ingr = StringVar(OT)
    WE9_IngrMenu = OptionMenu(OT,WE9_Ingr,*Ingrs)
    WE10_Ingr = StringVar(OT)
    WE10_IngrMenu = OptionMenu(OT,WE10_Ingr,*Ingrs)
    WE11_Ingr = StringVar(OT)
    WE11_IngrMenu = OptionMenu(OT,WE11_Ingr,*Ingrs)
    WE12_Ingr = StringVar(OT)
    WE12_IngrMenu = OptionMenu(OT,WE12_Ingr,*Ingrs)
    WE13_Ingr = StringVar(OT)
    WE13_IngrMenu = OptionMenu(OT,WE13_Ingr,*Ingrs)
    WE14_Ingr = StringVar(OT)
    WE14_IngrMenu = OptionMenu(OT,WE14_Ingr,*Ingrs)
    WE15_Ingr = StringVar(OT)
    WE15_IngrMenu = OptionMenu(OT,WE15_Ingr,*Ingrs)
    WE16_Ingr = StringVar(OT)
    WE16_IngrMenu = OptionMenu(OT,WE16_Ingr,*Ingrs)
    WE17_Ingr = StringVar(OT)
    WE17_IngrMenu = OptionMenu(OT,WE17_Ingr,*Ingrs)
    WE18_Ingr = StringVar(OT)
    WE18_IngrMenu = OptionMenu(OT,WE18_Ingr,*Ingrs)
    WE19_Ingr = StringVar(OT)
    WE19_IngrMenu = OptionMenu(OT,WE19_Ingr,*Ingrs)
    WE20_Ingr = StringVar(OT)
    WE20_IngrMenu = OptionMenu(OT,WE20_Ingr,*Ingrs)
    WE21_Ingr = StringVar(OT)
    WE21_IngrMenu = OptionMenu(OT,WE21_Ingr,*Ingrs)
    WE22_Ingr = StringVar(OT)
    WE22_IngrMenu = OptionMenu(OT,WE22_Ingr,*Ingrs)
    WE23_Ingr = StringVar(OT)
    WE23_IngrMenu = OptionMenu(OT,WE23_Ingr,*Ingrs)
    WE24_Ingr = StringVar(OT)
    WE24_IngrMenu = OptionMenu(OT,WE24_Ingr,*Ingrs)

    WE1_SS = StringVar(OT)
    WE1_SSMenu = OptionMenu(OT,WE1_SS,*SSInitiators)
    WE2_SS = StringVar(OT)
    WE2_SSMenu = OptionMenu(OT,WE2_SS,*SSInitiators)
    WE3_SS = StringVar(OT)
    WE3_SSMenu = OptionMenu(OT,WE3_SS,*SSInitiators)
    WE4_SS = StringVar(OT)
    WE4_SSMenu = OptionMenu(OT,WE4_SS,*SSInitiators)
    WE5_SS = StringVar(OT)
    WE5_SSMenu = OptionMenu(OT,WE5_SS,*SSInitiators)
    WE6_SS = StringVar(OT)
    WE6_SSMenu = OptionMenu(OT,WE6_SS,*SSInitiators)
    WE7_SS = StringVar(OT)
    WE7_SSMenu = OptionMenu(OT,WE7_SS,*SSInitiators)
    WE8_SS = StringVar(OT)
    WE8_SSMenu = OptionMenu(OT,WE8_SS,*SSInitiators)
    WE9_SS = StringVar(OT)
    WE9_SSMenu = OptionMenu(OT,WE9_SS,*SSInitiators)
    WE10_SS = StringVar(OT)
    WE10_SSMenu = OptionMenu(OT,WE10_SS,*SSInitiators)
    WE11_SS = StringVar(OT)
    WE11_SSMenu = OptionMenu(OT,WE11_SS,*SSInitiators)
    WE12_SS = StringVar(OT)
    WE12_SSMenu = OptionMenu(OT,WE12_SS,*SSInitiators)
    WE13_SS = StringVar(OT)
    WE13_SSMenu = OptionMenu(OT,WE13_SS,*SSInitiators)
    WE14_SS = StringVar(OT)
    WE14_SSMenu = OptionMenu(OT,WE14_SS,*SSInitiators)
    WE15_SS = StringVar(OT)
    WE15_SSMenu = OptionMenu(OT,WE15_SS,*SSInitiators)
    WE16_SS = StringVar(OT)
    WE16_SSMenu = OptionMenu(OT,WE16_SS,*SSInitiators)
    WE17_SS = StringVar(OT)
    WE17_SSMenu = OptionMenu(OT,WE17_SS,*SSInitiators)
    WE18_SS = StringVar(OT)
    WE18_SSMenu = OptionMenu(OT,WE18_SS,*SSInitiators)
    WE19_SS = StringVar(OT)
    WE19_SSMenu = OptionMenu(OT,WE19_SS,*SSInitiators)
    WE20_SS = StringVar(OT)
    WE20_SSMenu = OptionMenu(OT,WE20_SS,*SSInitiators)
    WE21_SS = StringVar(OT)
    WE21_SSMenu = OptionMenu(OT,WE21_SS,*SSInitiators)
    WE22_SS = StringVar(OT)
    WE22_SSMenu = OptionMenu(OT,WE22_SS,*SSInitiators)
    WE23_SS = StringVar(OT)
    WE23_SSMenu = OptionMenu(OT,WE23_SS,*SSInitiators)
    WE24_SS = StringVar(OT)
    WE24_SSMenu = OptionMenu(OT,WE24_SS,*SSInitiators)

    WE1_Dilu = StringVar(OT)
    WE1_DiluMenu = OptionMenu(OT,WE1_Dilu,*Diluents)
    WE2_Dilu = StringVar(OT)
    WE2_DiluMenu = OptionMenu(OT,WE2_Dilu,*Diluents)
    WE3_Dilu = StringVar(OT)
    WE3_DiluMenu = OptionMenu(OT,WE3_Dilu,*Diluents)
    WE4_Dilu = StringVar(OT)
    WE4_DiluMenu = OptionMenu(OT,WE4_Dilu,*Diluents)
    WE5_Dilu = StringVar(OT)
    WE5_DiluMenu = OptionMenu(OT,WE5_Dilu,*Diluents)
    WE6_Dilu = StringVar(OT)
    WE6_DiluMenu = OptionMenu(OT,WE6_Dilu,*Diluents)
    WE7_Dilu = StringVar(OT)
    WE7_DiluMenu = OptionMenu(OT,WE7_Dilu,*Diluents)
    WE8_Dilu = StringVar(OT)
    WE8_DiluMenu = OptionMenu(OT,WE8_Dilu,*Diluents)
    WE9_Dilu = StringVar(OT)
    WE9_DiluMenu = OptionMenu(OT,WE9_Dilu,*Diluents)
    WE10_Dilu = StringVar(OT)
    WE10_DiluMenu = OptionMenu(OT,WE10_Dilu,*Diluents)
    WE11_Dilu = StringVar(OT)
    WE11_DiluMenu = OptionMenu(OT,WE11_Dilu,*Diluents)
    WE12_Dilu = StringVar(OT)
    WE12_DiluMenu = OptionMenu(OT,WE12_Dilu,*Diluents)
    WE13_Dilu = StringVar(OT)
    WE13_DiluMenu = OptionMenu(OT,WE13_Dilu,*Diluents)
    WE14_Dilu = StringVar(OT)
    WE14_DiluMenu = OptionMenu(OT,WE14_Dilu,*Diluents)
    WE15_Dilu = StringVar(OT)
    WE15_DiluMenu = OptionMenu(OT,WE15_Dilu,*Diluents)
    WE16_Dilu = StringVar(OT)
    WE16_DiluMenu = OptionMenu(OT,WE16_Dilu,*Diluents)
    WE17_Dilu = StringVar(OT)
    WE17_DiluMenu = OptionMenu(OT,WE17_Dilu,*Diluents)
    WE18_Dilu = StringVar(OT)
    WE18_DiluMenu = OptionMenu(OT,WE18_Dilu,*Diluents)
    WE19_Dilu = StringVar(OT)
    WE19_DiluMenu = OptionMenu(OT,WE19_Dilu,*Diluents)
    WE20_Dilu = StringVar(OT)
    WE20_DiluMenu = OptionMenu(OT,WE20_Dilu,*Diluents)
    WE21_Dilu = StringVar(OT)
    WE21_DiluMenu = OptionMenu(OT,WE21_Dilu,*Diluents)
    WE22_Dilu = StringVar(OT)
    WE22_DiluMenu = OptionMenu(OT,WE22_Dilu,*Diluents)
    WE23_Dilu = StringVar(OT)
    WE23_DiluMenu = OptionMenu(OT,WE23_Dilu,*Diluents)
    WE24_Dilu = StringVar(OT)
    WE24_DiluMenu = OptionMenu(OT,WE24_Dilu,*Diluents)

    WF1_Vol = Entry()
    WF2_Vol = Entry()
    WF3_Vol = Entry()
    WF4_Vol = Entry()
    WF5_Vol = Entry()
    WF6_Vol = Entry()
    WF7_Vol = Entry()
    WF8_Vol = Entry()
    WF9_Vol = Entry()
    WF10_Vol = Entry()
    WF11_Vol = Entry()
    WF12_Vol = Entry()
    WF13_Vol = Entry()
    WF14_Vol = Entry()
    WF15_Vol = Entry()
    WF16_Vol = Entry()
    WF17_Vol = Entry()
    WF18_Vol = Entry()
    WF19_Vol = Entry()
    WF20_Vol = Entry()
    WF21_Vol = Entry()
    WF22_Vol = Entry()
    WF23_Vol = Entry()
    WF24_Vol = Entry()

    WF1_Solvent1_Conc = Entry()
    WF2_Solvent1_Conc = Entry()
    WF3_Solvent1_Conc = Entry()
    WF4_Solvent1_Conc = Entry()
    WF5_Solvent1_Conc = Entry()
    WF6_Solvent1_Conc = Entry()
    WF7_Solvent1_Conc = Entry()
    WF8_Solvent1_Conc = Entry()
    WF9_Solvent1_Conc = Entry()
    WF10_Solvent1_Conc = Entry()
    WF11_Solvent1_Conc = Entry()
    WF12_Solvent1_Conc = Entry()
    WF13_Solvent1_Conc = Entry()
    WF14_Solvent1_Conc = Entry()
    WF15_Solvent1_Conc = Entry()
    WF16_Solvent1_Conc = Entry()
    WF17_Solvent1_Conc = Entry()
    WF18_Solvent1_Conc = Entry()
    WF19_Solvent1_Conc = Entry()
    WF20_Solvent1_Conc = Entry()
    WF21_Solvent1_Conc = Entry()
    WF22_Solvent1_Conc = Entry()
    WF23_Solvent1_Conc = Entry()
    WF24_Solvent1_Conc = Entry()
    
    WF1_Solvent2_Conc = Entry()
    WF2_Solvent2_Conc = Entry()
    WF3_Solvent2_Conc = Entry()
    WF4_Solvent2_Conc = Entry()
    WF5_Solvent2_Conc = Entry()
    WF6_Solvent2_Conc = Entry()
    WF7_Solvent2_Conc = Entry()
    WF8_Solvent2_Conc = Entry()
    WF9_Solvent2_Conc = Entry()
    WF10_Solvent2_Conc = Entry()
    WF11_Solvent2_Conc = Entry()
    WF12_Solvent2_Conc = Entry()
    WF13_Solvent2_Conc = Entry()
    WF14_Solvent2_Conc = Entry()
    WF15_Solvent2_Conc = Entry()
    WF16_Solvent2_Conc = Entry()
    WF17_Solvent2_Conc = Entry()
    WF18_Solvent2_Conc = Entry()
    WF19_Solvent2_Conc = Entry()
    WF20_Solvent2_Conc = Entry()
    WF21_Solvent2_Conc = Entry()
    WF22_Solvent2_Conc = Entry()
    WF23_Solvent2_Conc = Entry()
    WF24_Solvent2_Conc = Entry()

    WF1_SS_Conc = Entry()
    WF2_SS_Conc = Entry()
    WF3_SS_Conc = Entry()
    WF4_SS_Conc = Entry()
    WF5_SS_Conc = Entry()
    WF6_SS_Conc = Entry()
    WF7_SS_Conc = Entry()
    WF8_SS_Conc = Entry()
    WF9_SS_Conc = Entry()
    WF10_SS_Conc = Entry()
    WF11_SS_Conc = Entry()
    WF12_SS_Conc = Entry()
    WF13_SS_Conc = Entry()
    WF14_SS_Conc = Entry()
    WF15_SS_Conc = Entry()
    WF16_SS_Conc = Entry()
    WF17_SS_Conc = Entry()
    WF18_SS_Conc = Entry()
    WF19_SS_Conc = Entry()
    WF20_SS_Conc = Entry()
    WF21_SS_Conc = Entry()
    WF22_SS_Conc = Entry()
    WF23_SS_Conc = Entry()
    WF24_SS_Conc = Entry()

    WF1_Ingr = StringVar(OT)
    WF1_IngrMenu = OptionMenu(OT,WF1_Ingr,*Ingrs)
    WF2_Ingr = StringVar(OT)
    WF2_IngrMenu = OptionMenu(OT,WF2_Ingr,*Ingrs)
    WF3_Ingr = StringVar(OT)
    WF3_IngrMenu = OptionMenu(OT,WF3_Ingr,*Ingrs)
    WF4_Ingr = StringVar(OT)
    WF4_IngrMenu = OptionMenu(OT,WF4_Ingr,*Ingrs)
    WF5_Ingr = StringVar(OT)
    WF5_IngrMenu = OptionMenu(OT,WF5_Ingr,*Ingrs)
    WF6_Ingr = StringVar(OT)
    WF6_IngrMenu = OptionMenu(OT,WF6_Ingr,*Ingrs)
    WF7_Ingr = StringVar(OT)
    WF7_IngrMenu = OptionMenu(OT,WF7_Ingr,*Ingrs)
    WF8_Ingr = StringVar(OT)
    WF8_IngrMenu = OptionMenu(OT,WF8_Ingr,*Ingrs)
    WF9_Ingr = StringVar(OT)
    WF9_IngrMenu = OptionMenu(OT,WF9_Ingr,*Ingrs)
    WF10_Ingr = StringVar(OT)
    WF10_IngrMenu = OptionMenu(OT,WF10_Ingr,*Ingrs)
    WF11_Ingr = StringVar(OT)
    WF11_IngrMenu = OptionMenu(OT,WF11_Ingr,*Ingrs)
    WF12_Ingr = StringVar(OT)
    WF12_IngrMenu = OptionMenu(OT,WF12_Ingr,*Ingrs)
    WF13_Ingr = StringVar(OT)
    WF13_IngrMenu = OptionMenu(OT,WF13_Ingr,*Ingrs)
    WF14_Ingr = StringVar(OT)
    WF14_IngrMenu = OptionMenu(OT,WF14_Ingr,*Ingrs)
    WF15_Ingr = StringVar(OT)
    WF15_IngrMenu = OptionMenu(OT,WF15_Ingr,*Ingrs)
    WF16_Ingr = StringVar(OT)
    WF16_IngrMenu = OptionMenu(OT,WF16_Ingr,*Ingrs)
    WF17_Ingr = StringVar(OT)
    WF17_IngrMenu = OptionMenu(OT,WF17_Ingr,*Ingrs)
    WF18_Ingr = StringVar(OT)
    WF18_IngrMenu = OptionMenu(OT,WF18_Ingr,*Ingrs)
    WF19_Ingr = StringVar(OT)
    WF19_IngrMenu = OptionMenu(OT,WF19_Ingr,*Ingrs)
    WF20_Ingr = StringVar(OT)
    WF20_IngrMenu = OptionMenu(OT,WF20_Ingr,*Ingrs)
    WF21_Ingr = StringVar(OT)
    WF21_IngrMenu = OptionMenu(OT,WF21_Ingr,*Ingrs)
    WF22_Ingr = StringVar(OT)
    WF22_IngrMenu = OptionMenu(OT,WF22_Ingr,*Ingrs)
    WF23_Ingr = StringVar(OT)
    WF23_IngrMenu = OptionMenu(OT,WF23_Ingr,*Ingrs)
    WF24_Ingr = StringVar(OT)
    WF24_IngrMenu = OptionMenu(OT,WF24_Ingr,*Ingrs)

    WF1_SS = StringVar(OT)
    WF1_SSMenu = OptionMenu(OT,WF1_SS,*SSInitiators)
    WF2_SS = StringVar(OT)
    WF2_SSMenu = OptionMenu(OT,WF2_SS,*SSInitiators)
    WF3_SS = StringVar(OT)
    WF3_SSMenu = OptionMenu(OT,WF3_SS,*SSInitiators)
    WF4_SS = StringVar(OT)
    WF4_SSMenu = OptionMenu(OT,WF4_SS,*SSInitiators)
    WF5_SS = StringVar(OT)
    WF5_SSMenu = OptionMenu(OT,WF5_SS,*SSInitiators)
    WF6_SS = StringVar(OT)
    WF6_SSMenu = OptionMenu(OT,WF6_SS,*SSInitiators)
    WF7_SS = StringVar(OT)
    WF7_SSMenu = OptionMenu(OT,WF7_SS,*SSInitiators)
    WF8_SS = StringVar(OT)
    WF8_SSMenu = OptionMenu(OT,WF8_SS,*SSInitiators)
    WF9_SS = StringVar(OT)
    WF9_SSMenu = OptionMenu(OT,WF9_SS,*SSInitiators)
    WF10_SS = StringVar(OT)
    WF10_SSMenu = OptionMenu(OT,WF10_SS,*SSInitiators)
    WF11_SS = StringVar(OT)
    WF11_SSMenu = OptionMenu(OT,WF11_SS,*SSInitiators)
    WF12_SS = StringVar(OT)
    WF12_SSMenu = OptionMenu(OT,WF12_SS,*SSInitiators)
    WF13_SS = StringVar(OT)
    WF13_SSMenu = OptionMenu(OT,WF13_SS,*SSInitiators)
    WF14_SS = StringVar(OT)
    WF14_SSMenu = OptionMenu(OT,WF14_SS,*SSInitiators)
    WF15_SS = StringVar(OT)
    WF15_SSMenu = OptionMenu(OT,WF15_SS,*SSInitiators)
    WF16_SS = StringVar(OT)
    WF16_SSMenu = OptionMenu(OT,WF16_SS,*SSInitiators)
    WF17_SS = StringVar(OT)
    WF17_SSMenu = OptionMenu(OT,WF17_SS,*SSInitiators)
    WF18_SS = StringVar(OT)
    WF18_SSMenu = OptionMenu(OT,WF18_SS,*SSInitiators)
    WF19_SS = StringVar(OT)
    WF19_SSMenu = OptionMenu(OT,WF19_SS,*SSInitiators)
    WF20_SS = StringVar(OT)
    WF20_SSMenu = OptionMenu(OT,WF20_SS,*SSInitiators)
    WF21_SS = StringVar(OT)
    WF21_SSMenu = OptionMenu(OT,WF21_SS,*SSInitiators)
    WF22_SS = StringVar(OT)
    WF22_SSMenu = OptionMenu(OT,WF22_SS,*SSInitiators)
    WF23_SS = StringVar(OT)
    WF23_SSMenu = OptionMenu(OT,WF23_SS,*SSInitiators)
    WF24_SS = StringVar(OT)
    WF24_SSMenu = OptionMenu(OT,WF24_SS,*SSInitiators)

    WF1_Dilu = StringVar(OT)
    WF1_DiluMenu = OptionMenu(OT,WF1_Dilu,*Diluents)
    WF2_Dilu = StringVar(OT)
    WF2_DiluMenu = OptionMenu(OT,WF2_Dilu,*Diluents)
    WF3_Dilu = StringVar(OT)
    WF3_DiluMenu = OptionMenu(OT,WF3_Dilu,*Diluents)
    WF4_Dilu = StringVar(OT)
    WF4_DiluMenu = OptionMenu(OT,WF4_Dilu,*Diluents)
    WF5_Dilu = StringVar(OT)
    WF5_DiluMenu = OptionMenu(OT,WF5_Dilu,*Diluents)
    WF6_Dilu = StringVar(OT)
    WF6_DiluMenu = OptionMenu(OT,WF6_Dilu,*Diluents)
    WF7_Dilu = StringVar(OT)
    WF7_DiluMenu = OptionMenu(OT,WF7_Dilu,*Diluents)
    WF8_Dilu = StringVar(OT)
    WF8_DiluMenu = OptionMenu(OT,WF8_Dilu,*Diluents)
    WF9_Dilu = StringVar(OT)
    WF9_DiluMenu = OptionMenu(OT,WF9_Dilu,*Diluents)
    WF10_Dilu = StringVar(OT)
    WF10_DiluMenu = OptionMenu(OT,WF10_Dilu,*Diluents)
    WF11_Dilu = StringVar(OT)
    WF11_DiluMenu = OptionMenu(OT,WF11_Dilu,*Diluents)
    WF12_Dilu = StringVar(OT)
    WF12_DiluMenu = OptionMenu(OT,WF12_Dilu,*Diluents)
    WF13_Dilu = StringVar(OT)
    WF13_DiluMenu = OptionMenu(OT,WF13_Dilu,*Diluents)
    WF14_Dilu = StringVar(OT)
    WF14_DiluMenu = OptionMenu(OT,WF14_Dilu,*Diluents)
    WF15_Dilu = StringVar(OT)
    WF15_DiluMenu = OptionMenu(OT,WF15_Dilu,*Diluents)
    WF16_Dilu = StringVar(OT)
    WF16_DiluMenu = OptionMenu(OT,WF16_Dilu,*Diluents)
    WF17_Dilu = StringVar(OT)
    WF17_DiluMenu = OptionMenu(OT,WF17_Dilu,*Diluents)
    WF18_Dilu = StringVar(OT)
    WF18_DiluMenu = OptionMenu(OT,WF18_Dilu,*Diluents)
    WF19_Dilu = StringVar(OT)
    WF19_DiluMenu = OptionMenu(OT,WF19_Dilu,*Diluents)
    WF20_Dilu = StringVar(OT)
    WF20_DiluMenu = OptionMenu(OT,WF20_Dilu,*Diluents)
    WF21_Dilu = StringVar(OT)
    WF21_DiluMenu = OptionMenu(OT,WF21_Dilu,*Diluents)
    WF22_Dilu = StringVar(OT)
    WF22_DiluMenu = OptionMenu(OT,WF22_Dilu,*Diluents)
    WF23_Dilu = StringVar(OT)
    WF23_DiluMenu = OptionMenu(OT,WF23_Dilu,*Diluents)
    WF24_Dilu = StringVar(OT)
    WF24_DiluMenu = OptionMenu(OT,WF24_Dilu,*Diluents)

    WG1_Vol = Entry()
    WG2_Vol = Entry()
    WG3_Vol = Entry()
    WG4_Vol = Entry()
    WG5_Vol = Entry()
    WG6_Vol = Entry()
    WG7_Vol = Entry()
    WG8_Vol = Entry()
    WG9_Vol = Entry()
    WG10_Vol = Entry()
    WG11_Vol = Entry()
    WG12_Vol = Entry()
    WG13_Vol = Entry()
    WG14_Vol = Entry()
    WG15_Vol = Entry()
    WG16_Vol = Entry()
    WG17_Vol = Entry()
    WG18_Vol = Entry()
    WG19_Vol = Entry()
    WG20_Vol = Entry()
    WG21_Vol = Entry()
    WG22_Vol = Entry()
    WG23_Vol = Entry()
    WG24_Vol = Entry()

    WG1_Solvent1_Conc = Entry()
    WG2_Solvent1_Conc = Entry()
    WG3_Solvent1_Conc = Entry()
    WG4_Solvent1_Conc = Entry()
    WG5_Solvent1_Conc = Entry()
    WG6_Solvent1_Conc = Entry()
    WG7_Solvent1_Conc = Entry()
    WG8_Solvent1_Conc = Entry()
    WG9_Solvent1_Conc = Entry()
    WG10_Solvent1_Conc = Entry()
    WG11_Solvent1_Conc = Entry()
    WG12_Solvent1_Conc = Entry()
    WG13_Solvent1_Conc = Entry()
    WG14_Solvent1_Conc = Entry()
    WG15_Solvent1_Conc = Entry()
    WG16_Solvent1_Conc = Entry()
    WG17_Solvent1_Conc = Entry()
    WG18_Solvent1_Conc = Entry()
    WG19_Solvent1_Conc = Entry()
    WG20_Solvent1_Conc = Entry()
    WG21_Solvent1_Conc = Entry()
    WG22_Solvent1_Conc = Entry()
    WG23_Solvent1_Conc = Entry()
    WG24_Solvent1_Conc = Entry()
    
    WG1_Solvent2_Conc = Entry()
    WG2_Solvent2_Conc = Entry()
    WG3_Solvent2_Conc = Entry()
    WG4_Solvent2_Conc = Entry()
    WG5_Solvent2_Conc = Entry()
    WG6_Solvent2_Conc = Entry()
    WG7_Solvent2_Conc = Entry()
    WG8_Solvent2_Conc = Entry()
    WG9_Solvent2_Conc = Entry()
    WG10_Solvent2_Conc = Entry()
    WG11_Solvent2_Conc = Entry()
    WG12_Solvent2_Conc = Entry()
    WG13_Solvent2_Conc = Entry()
    WG14_Solvent2_Conc = Entry()
    WG15_Solvent2_Conc = Entry()
    WG16_Solvent2_Conc = Entry()
    WG17_Solvent2_Conc = Entry()
    WG18_Solvent2_Conc = Entry()
    WG19_Solvent2_Conc = Entry()
    WG20_Solvent2_Conc = Entry()
    WG21_Solvent2_Conc = Entry()
    WG22_Solvent2_Conc = Entry()
    WG23_Solvent2_Conc = Entry()
    WG24_Solvent2_Conc = Entry()
    
    WG1_SS_Conc = Entry()
    WG2_SS_Conc = Entry()
    WG3_SS_Conc = Entry()
    WG4_SS_Conc = Entry()
    WG5_SS_Conc = Entry()
    WG6_SS_Conc = Entry()
    WG7_SS_Conc = Entry()
    WG8_SS_Conc = Entry()
    WG9_SS_Conc = Entry()
    WG10_SS_Conc = Entry()
    WG11_SS_Conc = Entry()
    WG12_SS_Conc = Entry()
    WG13_SS_Conc = Entry()
    WG14_SS_Conc = Entry()
    WG15_SS_Conc = Entry()
    WG16_SS_Conc = Entry()
    WG17_SS_Conc = Entry()
    WG18_SS_Conc = Entry()
    WG19_SS_Conc = Entry()
    WG20_SS_Conc = Entry()
    WG21_SS_Conc = Entry()
    WG22_SS_Conc = Entry()
    WG23_SS_Conc = Entry()
    WG24_SS_Conc = Entry()

    WG1_Ingr = StringVar(OT)
    WG1_IngrMenu = OptionMenu(OT,WG1_Ingr,*Ingrs)
    WG2_Ingr = StringVar(OT)
    WG2_IngrMenu = OptionMenu(OT,WG2_Ingr,*Ingrs)
    WG3_Ingr = StringVar(OT)
    WG3_IngrMenu = OptionMenu(OT,WG3_Ingr,*Ingrs)
    WG4_Ingr = StringVar(OT)
    WG4_IngrMenu = OptionMenu(OT,WG4_Ingr,*Ingrs)
    WG5_Ingr = StringVar(OT)
    WG5_IngrMenu = OptionMenu(OT,WG5_Ingr,*Ingrs)
    WG6_Ingr = StringVar(OT)
    WG6_IngrMenu = OptionMenu(OT,WG6_Ingr,*Ingrs)
    WG7_Ingr = StringVar(OT)
    WG7_IngrMenu = OptionMenu(OT,WG7_Ingr,*Ingrs)
    WG8_Ingr = StringVar(OT)
    WG8_IngrMenu = OptionMenu(OT,WG8_Ingr,*Ingrs)
    WG9_Ingr = StringVar(OT)
    WG9_IngrMenu = OptionMenu(OT,WG9_Ingr,*Ingrs)
    WG10_Ingr = StringVar(OT)
    WG10_IngrMenu = OptionMenu(OT,WG10_Ingr,*Ingrs)
    WG11_Ingr = StringVar(OT)
    WG11_IngrMenu = OptionMenu(OT,WG11_Ingr,*Ingrs)
    WG12_Ingr = StringVar(OT)
    WG12_IngrMenu = OptionMenu(OT,WG12_Ingr,*Ingrs)
    WG13_Ingr = StringVar(OT)
    WG13_IngrMenu = OptionMenu(OT,WG13_Ingr,*Ingrs)
    WG14_Ingr = StringVar(OT)
    WG14_IngrMenu = OptionMenu(OT,WG14_Ingr,*Ingrs)
    WG15_Ingr = StringVar(OT)
    WG15_IngrMenu = OptionMenu(OT,WG15_Ingr,*Ingrs)
    WG16_Ingr = StringVar(OT)
    WG16_IngrMenu = OptionMenu(OT,WG16_Ingr,*Ingrs)
    WG17_Ingr = StringVar(OT)
    WG17_IngrMenu = OptionMenu(OT,WG17_Ingr,*Ingrs)
    WG18_Ingr = StringVar(OT)
    WG18_IngrMenu = OptionMenu(OT,WG18_Ingr,*Ingrs)
    WG19_Ingr = StringVar(OT)
    WG19_IngrMenu = OptionMenu(OT,WG19_Ingr,*Ingrs)
    WG20_Ingr = StringVar(OT)
    WG20_IngrMenu = OptionMenu(OT,WG20_Ingr,*Ingrs)
    WG21_Ingr = StringVar(OT)
    WG21_IngrMenu = OptionMenu(OT,WG21_Ingr,*Ingrs)
    WG22_Ingr = StringVar(OT)
    WG22_IngrMenu = OptionMenu(OT,WG22_Ingr,*Ingrs)
    WG23_Ingr = StringVar(OT)
    WG23_IngrMenu = OptionMenu(OT,WG23_Ingr,*Ingrs)
    WG24_Ingr = StringVar(OT)
    WG24_IngrMenu = OptionMenu(OT,WG24_Ingr,*Ingrs)

    WG1_SS = StringVar(OT)
    WG1_SSMenu = OptionMenu(OT,WG1_SS,*SSInitiators)
    WG2_SS = StringVar(OT)
    WG2_SSMenu = OptionMenu(OT,WG2_SS,*SSInitiators)
    WG3_SS = StringVar(OT)
    WG3_SSMenu = OptionMenu(OT,WG3_SS,*SSInitiators)
    WG4_SS = StringVar(OT)
    WG4_SSMenu = OptionMenu(OT,WG4_SS,*SSInitiators)
    WG5_SS = StringVar(OT)
    WG5_SSMenu = OptionMenu(OT,WG5_SS,*SSInitiators)
    WG6_SS = StringVar(OT)
    WG6_SSMenu = OptionMenu(OT,WG6_SS,*SSInitiators)
    WG7_SS = StringVar(OT)
    WG7_SSMenu = OptionMenu(OT,WG7_SS,*SSInitiators)
    WG8_SS = StringVar(OT)
    WG8_SSMenu = OptionMenu(OT,WG8_SS,*SSInitiators)
    WG9_SS = StringVar(OT)
    WG9_SSMenu = OptionMenu(OT,WG9_SS,*SSInitiators)
    WG10_SS = StringVar(OT)
    WG10_SSMenu = OptionMenu(OT,WG10_SS,*SSInitiators)
    WG11_SS = StringVar(OT)
    WG11_SSMenu = OptionMenu(OT,WG11_SS,*SSInitiators)
    WG12_SS = StringVar(OT)
    WG12_SSMenu = OptionMenu(OT,WG12_SS,*SSInitiators)
    WG13_SS = StringVar(OT)
    WG13_SSMenu = OptionMenu(OT,WG13_SS,*SSInitiators)
    WG14_SS = StringVar(OT)
    WG14_SSMenu = OptionMenu(OT,WG14_SS,*SSInitiators)
    WG15_SS = StringVar(OT)
    WG15_SSMenu = OptionMenu(OT,WG15_SS,*SSInitiators)
    WG16_SS = StringVar(OT)
    WG16_SSMenu = OptionMenu(OT,WG16_SS,*SSInitiators)
    WG17_SS = StringVar(OT)
    WG17_SSMenu = OptionMenu(OT,WG17_SS,*SSInitiators)
    WG18_SS = StringVar(OT)
    WG18_SSMenu = OptionMenu(OT,WG18_SS,*SSInitiators)
    WG19_SS = StringVar(OT)
    WG19_SSMenu = OptionMenu(OT,WG19_SS,*SSInitiators)
    WG20_SS = StringVar(OT)
    WG20_SSMenu = OptionMenu(OT,WG20_SS,*SSInitiators)
    WG21_SS = StringVar(OT)
    WG21_SSMenu = OptionMenu(OT,WG21_SS,*SSInitiators)
    WG22_SS = StringVar(OT)
    WG22_SSMenu = OptionMenu(OT,WG22_SS,*SSInitiators)
    WG23_SS = StringVar(OT)
    WG23_SSMenu = OptionMenu(OT,WG23_SS,*SSInitiators)
    WG24_SS = StringVar(OT)
    WG24_SSMenu = OptionMenu(OT,WG24_SS,*SSInitiators)

    WG1_Dilu = StringVar(OT)
    WG1_DiluMenu = OptionMenu(OT,WG1_Dilu,*Diluents)
    WG2_Dilu = StringVar(OT)
    WG2_DiluMenu = OptionMenu(OT,WG2_Dilu,*Diluents)
    WG3_Dilu = StringVar(OT)
    WG3_DiluMenu = OptionMenu(OT,WG3_Dilu,*Diluents)
    WG4_Dilu = StringVar(OT)
    WG4_DiluMenu = OptionMenu(OT,WG4_Dilu,*Diluents)
    WG5_Dilu = StringVar(OT)
    WG5_DiluMenu = OptionMenu(OT,WG5_Dilu,*Diluents)
    WG6_Dilu = StringVar(OT)
    WG6_DiluMenu = OptionMenu(OT,WG6_Dilu,*Diluents)
    WG7_Dilu = StringVar(OT)
    WG7_DiluMenu = OptionMenu(OT,WG7_Dilu,*Diluents)
    WG8_Dilu = StringVar(OT)
    WG8_DiluMenu = OptionMenu(OT,WG8_Dilu,*Diluents)
    WG9_Dilu = StringVar(OT)
    WG9_DiluMenu = OptionMenu(OT,WG9_Dilu,*Diluents)
    WG10_Dilu = StringVar(OT)
    WG10_DiluMenu = OptionMenu(OT,WG10_Dilu,*Diluents)
    WG11_Dilu = StringVar(OT)
    WG11_DiluMenu = OptionMenu(OT,WG11_Dilu,*Diluents)
    WG12_Dilu = StringVar(OT)
    WG12_DiluMenu = OptionMenu(OT,WG12_Dilu,*Diluents)
    WG13_Dilu = StringVar(OT)
    WG13_DiluMenu = OptionMenu(OT,WG13_Dilu,*Diluents)
    WG14_Dilu = StringVar(OT)
    WG14_DiluMenu = OptionMenu(OT,WG14_Dilu,*Diluents)
    WG15_Dilu = StringVar(OT)
    WG15_DiluMenu = OptionMenu(OT,WG15_Dilu,*Diluents)
    WG16_Dilu = StringVar(OT)
    WG16_DiluMenu = OptionMenu(OT,WG16_Dilu,*Diluents)
    WG17_Dilu = StringVar(OT)
    WG17_DiluMenu = OptionMenu(OT,WG17_Dilu,*Diluents)
    WG18_Dilu = StringVar(OT)
    WG18_DiluMenu = OptionMenu(OT,WG18_Dilu,*Diluents)
    WG19_Dilu = StringVar(OT)
    WG19_DiluMenu = OptionMenu(OT,WG19_Dilu,*Diluents)
    WG20_Dilu = StringVar(OT)
    WG20_DiluMenu = OptionMenu(OT,WG20_Dilu,*Diluents)
    WG21_Dilu = StringVar(OT)
    WG21_DiluMenu = OptionMenu(OT,WG21_Dilu,*Diluents)
    WG22_Dilu = StringVar(OT)
    WG22_DiluMenu = OptionMenu(OT,WG22_Dilu,*Diluents)
    WG23_Dilu = StringVar(OT)
    WG23_DiluMenu = OptionMenu(OT,WG23_Dilu,*Diluents)
    WG24_Dilu = StringVar(OT)
    WG24_DiluMenu = OptionMenu(OT,WG24_Dilu,*Diluents)

    WH1_Vol = Entry()
    WH2_Vol = Entry()
    WH3_Vol = Entry()
    WH4_Vol = Entry()
    WH5_Vol = Entry()
    WH6_Vol = Entry()
    WH7_Vol = Entry()
    WH8_Vol = Entry()
    WH9_Vol = Entry()
    WH10_Vol = Entry()
    WH11_Vol = Entry()
    WH12_Vol = Entry()
    WH13_Vol = Entry()
    WH14_Vol = Entry()
    WH15_Vol = Entry()
    WH16_Vol = Entry()
    WH17_Vol = Entry()
    WH18_Vol = Entry()
    WH19_Vol = Entry()
    WH20_Vol = Entry()
    WH21_Vol = Entry()
    WH22_Vol = Entry()
    WH23_Vol = Entry()
    WH24_Vol = Entry()

    WH1_Solvent1_Conc = Entry()
    WH2_Solvent1_Conc = Entry()
    WH3_Solvent1_Conc = Entry()
    WH4_Solvent1_Conc = Entry()
    WH5_Solvent1_Conc = Entry()
    WH6_Solvent1_Conc = Entry()
    WH7_Solvent1_Conc = Entry()
    WH8_Solvent1_Conc = Entry()
    WH9_Solvent1_Conc = Entry()
    WH10_Solvent1_Conc = Entry()
    WH11_Solvent1_Conc = Entry()
    WH12_Solvent1_Conc = Entry()
    WH13_Solvent1_Conc = Entry()
    WH14_Solvent1_Conc = Entry()
    WH15_Solvent1_Conc = Entry()
    WH16_Solvent1_Conc = Entry()
    WH17_Solvent1_Conc = Entry()
    WH18_Solvent1_Conc = Entry()
    WH19_Solvent1_Conc = Entry()
    WH20_Solvent1_Conc = Entry()
    WH21_Solvent1_Conc = Entry()
    WH22_Solvent1_Conc = Entry()
    WH23_Solvent1_Conc = Entry()
    WH24_Solvent1_Conc = Entry()
    
    WH1_Solvent2_Conc = Entry()
    WH2_Solvent2_Conc = Entry()
    WH3_Solvent2_Conc = Entry()
    WH4_Solvent2_Conc = Entry()
    WH5_Solvent2_Conc = Entry()
    WH6_Solvent2_Conc = Entry()
    WH7_Solvent2_Conc = Entry()
    WH8_Solvent2_Conc = Entry()
    WH9_Solvent2_Conc = Entry()
    WH10_Solvent2_Conc = Entry()
    WH11_Solvent2_Conc = Entry()
    WH12_Solvent2_Conc = Entry()
    WH13_Solvent2_Conc = Entry()
    WH14_Solvent2_Conc = Entry()
    WH15_Solvent2_Conc = Entry()
    WH16_Solvent2_Conc = Entry()
    WH17_Solvent2_Conc = Entry()
    WH18_Solvent2_Conc = Entry()
    WH19_Solvent2_Conc = Entry()
    WH20_Solvent2_Conc = Entry()
    WH21_Solvent2_Conc = Entry()
    WH22_Solvent2_Conc = Entry()
    WH23_Solvent2_Conc = Entry()
    WH24_Solvent2_Conc = Entry()
    
    WH1_SS_Conc = Entry()
    WH2_SS_Conc = Entry()
    WH3_SS_Conc = Entry()
    WH4_SS_Conc = Entry()
    WH5_SS_Conc = Entry()
    WH6_SS_Conc = Entry()
    WH7_SS_Conc = Entry()
    WH8_SS_Conc = Entry()
    WH9_SS_Conc = Entry()
    WH10_SS_Conc = Entry()
    WH11_SS_Conc = Entry()
    WH12_SS_Conc = Entry()
    WH13_SS_Conc = Entry()
    WH14_SS_Conc = Entry()
    WH15_SS_Conc = Entry()
    WH16_SS_Conc = Entry()
    WH17_SS_Conc = Entry()
    WH18_SS_Conc = Entry()
    WH19_SS_Conc = Entry()
    WH20_SS_Conc = Entry()
    WH21_SS_Conc = Entry()
    WH22_SS_Conc = Entry()
    WH23_SS_Conc = Entry()
    WH24_SS_Conc = Entry()

    WH1_Ingr = StringVar(OT)
    WH1_IngrMenu = OptionMenu(OT,WH1_Ingr,*Ingrs)
    WH2_Ingr = StringVar(OT)
    WH2_IngrMenu = OptionMenu(OT,WH2_Ingr,*Ingrs)
    WH3_Ingr = StringVar(OT)
    WH3_IngrMenu = OptionMenu(OT,WH3_Ingr,*Ingrs)
    WH4_Ingr = StringVar(OT)
    WH4_IngrMenu = OptionMenu(OT,WH4_Ingr,*Ingrs)
    WH5_Ingr = StringVar(OT)
    WH5_IngrMenu = OptionMenu(OT,WH5_Ingr,*Ingrs)
    WH6_Ingr = StringVar(OT)
    WH6_IngrMenu = OptionMenu(OT,WH6_Ingr,*Ingrs)
    WH7_Ingr = StringVar(OT)
    WH7_IngrMenu = OptionMenu(OT,WH7_Ingr,*Ingrs)
    WH8_Ingr = StringVar(OT)
    WH8_IngrMenu = OptionMenu(OT,WH8_Ingr,*Ingrs)
    WH9_Ingr = StringVar(OT)
    WH9_IngrMenu = OptionMenu(OT,WH9_Ingr,*Ingrs)
    WH10_Ingr = StringVar(OT)
    WH10_IngrMenu = OptionMenu(OT,WH10_Ingr,*Ingrs)
    WH11_Ingr = StringVar(OT)
    WH11_IngrMenu = OptionMenu(OT,WH11_Ingr,*Ingrs)
    WH12_Ingr = StringVar(OT)
    WH12_IngrMenu = OptionMenu(OT,WH12_Ingr,*Ingrs)
    WH13_Ingr = StringVar(OT)
    WH13_IngrMenu = OptionMenu(OT,WH13_Ingr,*Ingrs)
    WH14_Ingr = StringVar(OT)
    WH14_IngrMenu = OptionMenu(OT,WH14_Ingr,*Ingrs)
    WH15_Ingr = StringVar(OT)
    WH15_IngrMenu = OptionMenu(OT,WH15_Ingr,*Ingrs)
    WH16_Ingr = StringVar(OT)
    WH16_IngrMenu = OptionMenu(OT,WH16_Ingr,*Ingrs)
    WH17_Ingr = StringVar(OT)
    WH17_IngrMenu = OptionMenu(OT,WH17_Ingr,*Ingrs)
    WH18_Ingr = StringVar(OT)
    WH18_IngrMenu = OptionMenu(OT,WH18_Ingr,*Ingrs)
    WH19_Ingr = StringVar(OT)
    WH19_IngrMenu = OptionMenu(OT,WH19_Ingr,*Ingrs)
    WH20_Ingr = StringVar(OT)
    WH20_IngrMenu = OptionMenu(OT,WH20_Ingr,*Ingrs)
    WH21_Ingr = StringVar(OT)
    WH21_IngrMenu = OptionMenu(OT,WH21_Ingr,*Ingrs)
    WH22_Ingr = StringVar(OT)
    WH22_IngrMenu = OptionMenu(OT,WH22_Ingr,*Ingrs)
    WH23_Ingr = StringVar(OT)
    WH23_IngrMenu = OptionMenu(OT,WH23_Ingr,*Ingrs)
    WH24_Ingr = StringVar(OT)
    WH24_IngrMenu = OptionMenu(OT,WH24_Ingr,*Ingrs)

    WH1_SS = StringVar(OT)
    WH1_SSMenu = OptionMenu(OT,WH1_SS,*SSInitiators)
    WH2_SS = StringVar(OT)
    WH2_SSMenu = OptionMenu(OT,WH2_SS,*SSInitiators)
    WH3_SS = StringVar(OT)
    WH3_SSMenu = OptionMenu(OT,WH3_SS,*SSInitiators)
    WH4_SS = StringVar(OT)
    WH4_SSMenu = OptionMenu(OT,WH4_SS,*SSInitiators)
    WH5_SS = StringVar(OT)
    WH5_SSMenu = OptionMenu(OT,WH5_SS,*SSInitiators)
    WH6_SS = StringVar(OT)
    WH6_SSMenu = OptionMenu(OT,WH6_SS,*SSInitiators)
    WH7_SS = StringVar(OT)
    WH7_SSMenu = OptionMenu(OT,WH7_SS,*SSInitiators)
    WH8_SS = StringVar(OT)
    WH8_SSMenu = OptionMenu(OT,WH8_SS,*SSInitiators)
    WH9_SS = StringVar(OT)
    WH9_SSMenu = OptionMenu(OT,WH9_SS,*SSInitiators)
    WH10_SS = StringVar(OT)
    WH10_SSMenu = OptionMenu(OT,WH10_SS,*SSInitiators)
    WH11_SS = StringVar(OT)
    WH11_SSMenu = OptionMenu(OT,WH11_SS,*SSInitiators)
    WH12_SS = StringVar(OT)
    WH12_SSMenu = OptionMenu(OT,WH12_SS,*SSInitiators)
    WH13_SS = StringVar(OT)
    WH13_SSMenu = OptionMenu(OT,WH13_SS,*SSInitiators)
    WH14_SS = StringVar(OT)
    WH14_SSMenu = OptionMenu(OT,WH14_SS,*SSInitiators)
    WH15_SS = StringVar(OT)
    WH15_SSMenu = OptionMenu(OT,WH15_SS,*SSInitiators)
    WH16_SS = StringVar(OT)
    WH16_SSMenu = OptionMenu(OT,WH16_SS,*SSInitiators)
    WH17_SS = StringVar(OT)
    WH17_SSMenu = OptionMenu(OT,WH17_SS,*SSInitiators)
    WH18_SS = StringVar(OT)
    WH18_SSMenu = OptionMenu(OT,WH18_SS,*SSInitiators)
    WH19_SS = StringVar(OT)
    WH19_SSMenu = OptionMenu(OT,WH19_SS,*SSInitiators)
    WH20_SS = StringVar(OT)
    WH20_SSMenu = OptionMenu(OT,WH20_SS,*SSInitiators)
    WH21_SS = StringVar(OT)
    WH21_SSMenu = OptionMenu(OT,WH21_SS,*SSInitiators)
    WH22_SS = StringVar(OT)
    WH22_SSMenu = OptionMenu(OT,WH22_SS,*SSInitiators)
    WH23_SS = StringVar(OT)
    WH23_SSMenu = OptionMenu(OT,WH23_SS,*SSInitiators)
    WH24_SS = StringVar(OT)
    WH24_SSMenu = OptionMenu(OT,WH24_SS,*SSInitiators)

    WH1_Dilu = StringVar(OT)
    WH1_DiluMenu = OptionMenu(OT,WH1_Dilu,*Diluents)
    WH2_Dilu = StringVar(OT)
    WH2_DiluMenu = OptionMenu(OT,WH2_Dilu,*Diluents)
    WH3_Dilu = StringVar(OT)
    WH3_DiluMenu = OptionMenu(OT,WH3_Dilu,*Diluents)
    WH4_Dilu = StringVar(OT)
    WH4_DiluMenu = OptionMenu(OT,WH4_Dilu,*Diluents)
    WH5_Dilu = StringVar(OT)
    WH5_DiluMenu = OptionMenu(OT,WH5_Dilu,*Diluents)
    WH6_Dilu = StringVar(OT)
    WH6_DiluMenu = OptionMenu(OT,WH6_Dilu,*Diluents)
    WH7_Dilu = StringVar(OT)
    WH7_DiluMenu = OptionMenu(OT,WH7_Dilu,*Diluents)
    WH8_Dilu = StringVar(OT)
    WH8_DiluMenu = OptionMenu(OT,WH8_Dilu,*Diluents)
    WH9_Dilu = StringVar(OT)
    WH9_DiluMenu = OptionMenu(OT,WH9_Dilu,*Diluents)
    WH10_Dilu = StringVar(OT)
    WH10_DiluMenu = OptionMenu(OT,WH10_Dilu,*Diluents)
    WH11_Dilu = StringVar(OT)
    WH11_DiluMenu = OptionMenu(OT,WH11_Dilu,*Diluents)
    WH12_Dilu = StringVar(OT)
    WH12_DiluMenu = OptionMenu(OT,WH12_Dilu,*Diluents)
    WH13_Dilu = StringVar(OT)
    WH13_DiluMenu = OptionMenu(OT,WH13_Dilu,*Diluents)
    WH14_Dilu = StringVar(OT)
    WH14_DiluMenu = OptionMenu(OT,WH14_Dilu,*Diluents)
    WH15_Dilu = StringVar(OT)
    WH15_DiluMenu = OptionMenu(OT,WH15_Dilu,*Diluents)
    WH16_Dilu = StringVar(OT)
    WH16_DiluMenu = OptionMenu(OT,WH16_Dilu,*Diluents)
    WH17_Dilu = StringVar(OT)
    WH17_DiluMenu = OptionMenu(OT,WH17_Dilu,*Diluents)
    WH18_Dilu = StringVar(OT)
    WH18_DiluMenu = OptionMenu(OT,WH18_Dilu,*Diluents)
    WH19_Dilu = StringVar(OT)
    WH19_DiluMenu = OptionMenu(OT,WH19_Dilu,*Diluents)
    WH20_Dilu = StringVar(OT)
    WH20_DiluMenu = OptionMenu(OT,WH20_Dilu,*Diluents)
    WH21_Dilu = StringVar(OT)
    WH21_DiluMenu = OptionMenu(OT,WH21_Dilu,*Diluents)
    WH22_Dilu = StringVar(OT)
    WH22_DiluMenu = OptionMenu(OT,WH22_Dilu,*Diluents)
    WH23_Dilu = StringVar(OT)
    WH23_DiluMenu = OptionMenu(OT,WH23_Dilu,*Diluents)
    WH24_Dilu = StringVar(OT)
    WH24_DiluMenu = OptionMenu(OT,WH24_Dilu,*Diluents)

    WI1_Vol = Entry()
    WI2_Vol = Entry()
    WI3_Vol = Entry()
    WI4_Vol = Entry()
    WI5_Vol = Entry()
    WI6_Vol = Entry()
    WI7_Vol = Entry()
    WI8_Vol = Entry()
    WI9_Vol = Entry()
    WI10_Vol = Entry()
    WI11_Vol = Entry()
    WI12_Vol = Entry()
    WI13_Vol = Entry()
    WI14_Vol = Entry()
    WI15_Vol = Entry()
    WI16_Vol = Entry()
    WI17_Vol = Entry()
    WI18_Vol = Entry()
    WI19_Vol = Entry()
    WI20_Vol = Entry()
    WI21_Vol = Entry()
    WI22_Vol = Entry()
    WI23_Vol = Entry()
    WI24_Vol = Entry()

    WI1_Solvent1_Conc = Entry()
    WI2_Solvent1_Conc = Entry()
    WI3_Solvent1_Conc = Entry()
    WI4_Solvent1_Conc = Entry()
    WI5_Solvent1_Conc = Entry()
    WI6_Solvent1_Conc = Entry()
    WI7_Solvent1_Conc = Entry()
    WI8_Solvent1_Conc = Entry()
    WI9_Solvent1_Conc = Entry()
    WI10_Solvent1_Conc = Entry()
    WI11_Solvent1_Conc = Entry()
    WI12_Solvent1_Conc = Entry()
    WI13_Solvent1_Conc = Entry()
    WI14_Solvent1_Conc = Entry()
    WI15_Solvent1_Conc = Entry()
    WI16_Solvent1_Conc = Entry()
    WI17_Solvent1_Conc = Entry()
    WI18_Solvent1_Conc = Entry()
    WI19_Solvent1_Conc = Entry()
    WI20_Solvent1_Conc = Entry()
    WI21_Solvent1_Conc = Entry()
    WI22_Solvent1_Conc = Entry()
    WI23_Solvent1_Conc = Entry()
    WI24_Solvent1_Conc = Entry()
    
    WI1_Solvent2_Conc = Entry()
    WI2_Solvent2_Conc = Entry()
    WI3_Solvent2_Conc = Entry()
    WI4_Solvent2_Conc = Entry()
    WI5_Solvent2_Conc = Entry()
    WI6_Solvent2_Conc = Entry()
    WI7_Solvent2_Conc = Entry()
    WI8_Solvent2_Conc = Entry()
    WI9_Solvent2_Conc = Entry()
    WI10_Solvent2_Conc = Entry()
    WI11_Solvent2_Conc = Entry()
    WI12_Solvent2_Conc = Entry()
    WI13_Solvent2_Conc = Entry()
    WI14_Solvent2_Conc = Entry()
    WI15_Solvent2_Conc = Entry()
    WI16_Solvent2_Conc = Entry()
    WI17_Solvent2_Conc = Entry()
    WI18_Solvent2_Conc = Entry()
    WI19_Solvent2_Conc = Entry()
    WI20_Solvent2_Conc = Entry()
    WI21_Solvent2_Conc = Entry()
    WI22_Solvent2_Conc = Entry()
    WI23_Solvent2_Conc = Entry()
    WI24_Solvent2_Conc = Entry()
    
    WI1_SS_Conc = Entry()
    WI2_SS_Conc = Entry()
    WI3_SS_Conc = Entry()
    WI4_SS_Conc = Entry()
    WI5_SS_Conc = Entry()
    WI6_SS_Conc = Entry()
    WI7_SS_Conc = Entry()
    WI8_SS_Conc = Entry()
    WI9_SS_Conc = Entry()
    WI10_SS_Conc = Entry()
    WI11_SS_Conc = Entry()
    WI12_SS_Conc = Entry()
    WI13_SS_Conc = Entry()
    WI14_SS_Conc = Entry()
    WI15_SS_Conc = Entry()
    WI16_SS_Conc = Entry()
    WI17_SS_Conc = Entry()
    WI18_SS_Conc = Entry()
    WI19_SS_Conc = Entry()
    WI20_SS_Conc = Entry()
    WI21_SS_Conc = Entry()
    WI22_SS_Conc = Entry()
    WI23_SS_Conc = Entry()
    WI24_SS_Conc = Entry()

    WI1_Ingr = StringVar(OT)
    WI1_IngrMenu = OptionMenu(OT,WI1_Ingr,*Ingrs)
    WI2_Ingr = StringVar(OT)
    WI2_IngrMenu = OptionMenu(OT,WI2_Ingr,*Ingrs)
    WI3_Ingr = StringVar(OT)
    WI3_IngrMenu = OptionMenu(OT,WI3_Ingr,*Ingrs)
    WI4_Ingr = StringVar(OT)
    WI4_IngrMenu = OptionMenu(OT,WI4_Ingr,*Ingrs)
    WI5_Ingr = StringVar(OT)
    WI5_IngrMenu = OptionMenu(OT,WI5_Ingr,*Ingrs)
    WI6_Ingr = StringVar(OT)
    WI6_IngrMenu = OptionMenu(OT,WI6_Ingr,*Ingrs)
    WI7_Ingr = StringVar(OT)
    WI7_IngrMenu = OptionMenu(OT,WI7_Ingr,*Ingrs)
    WI8_Ingr = StringVar(OT)
    WI8_IngrMenu = OptionMenu(OT,WI8_Ingr,*Ingrs)
    WI9_Ingr = StringVar(OT)
    WI9_IngrMenu = OptionMenu(OT,WI9_Ingr,*Ingrs)
    WI10_Ingr = StringVar(OT)
    WI10_IngrMenu = OptionMenu(OT,WI10_Ingr,*Ingrs)
    WI11_Ingr = StringVar(OT)
    WI11_IngrMenu = OptionMenu(OT,WI11_Ingr,*Ingrs)
    WI12_Ingr = StringVar(OT)
    WI12_IngrMenu = OptionMenu(OT,WI12_Ingr,*Ingrs)
    WI13_Ingr = StringVar(OT)
    WI13_IngrMenu = OptionMenu(OT,WI13_Ingr,*Ingrs)
    WI14_Ingr = StringVar(OT)
    WI14_IngrMenu = OptionMenu(OT,WI14_Ingr,*Ingrs)
    WI15_Ingr = StringVar(OT)
    WI15_IngrMenu = OptionMenu(OT,WI15_Ingr,*Ingrs)
    WI16_Ingr = StringVar(OT)
    WI16_IngrMenu = OptionMenu(OT,WI16_Ingr,*Ingrs)
    WI17_Ingr = StringVar(OT)
    WI17_IngrMenu = OptionMenu(OT,WI17_Ingr,*Ingrs)
    WI18_Ingr = StringVar(OT)
    WI18_IngrMenu = OptionMenu(OT,WI18_Ingr,*Ingrs)
    WI19_Ingr = StringVar(OT)
    WI19_IngrMenu = OptionMenu(OT,WI19_Ingr,*Ingrs)
    WI20_Ingr = StringVar(OT)
    WI20_IngrMenu = OptionMenu(OT,WI20_Ingr,*Ingrs)
    WI21_Ingr = StringVar(OT)
    WI21_IngrMenu = OptionMenu(OT,WI21_Ingr,*Ingrs)
    WI22_Ingr = StringVar(OT)
    WI22_IngrMenu = OptionMenu(OT,WI22_Ingr,*Ingrs)
    WI23_Ingr = StringVar(OT)
    WI23_IngrMenu = OptionMenu(OT,WI23_Ingr,*Ingrs)
    WI24_Ingr = StringVar(OT)
    WI24_IngrMenu = OptionMenu(OT,WI24_Ingr,*Ingrs)
    
    WI1_SS = StringVar(OT)
    WI1_SSMenu = OptionMenu(OT,WI1_SS,*SSInitiators)
    WI2_SS = StringVar(OT)
    WI2_SSMenu = OptionMenu(OT,WI2_SS,*SSInitiators)
    WI3_SS = StringVar(OT)
    WI3_SSMenu = OptionMenu(OT,WI3_SS,*SSInitiators)
    WI4_SS = StringVar(OT)
    WI4_SSMenu = OptionMenu(OT,WI4_SS,*SSInitiators)
    WI5_SS = StringVar(OT)
    WI5_SSMenu = OptionMenu(OT,WI5_SS,*SSInitiators)
    WI6_SS = StringVar(OT)
    WI6_SSMenu = OptionMenu(OT,WI6_SS,*SSInitiators)
    WI7_SS = StringVar(OT)
    WI7_SSMenu = OptionMenu(OT,WI7_SS,*SSInitiators)
    WI8_SS = StringVar(OT)
    WI8_SSMenu = OptionMenu(OT,WI8_SS,*SSInitiators)
    WI9_SS = StringVar(OT)
    WI9_SSMenu = OptionMenu(OT,WI9_SS,*SSInitiators)
    WI10_SS = StringVar(OT)
    WI10_SSMenu = OptionMenu(OT,WI10_SS,*SSInitiators)
    WI11_SS = StringVar(OT)
    WI11_SSMenu = OptionMenu(OT,WI11_SS,*SSInitiators)
    WI12_SS = StringVar(OT)
    WI12_SSMenu = OptionMenu(OT,WI12_SS,*SSInitiators)
    WI13_SS = StringVar(OT)
    WI13_SSMenu = OptionMenu(OT,WI13_SS,*SSInitiators)
    WI14_SS = StringVar(OT)
    WI14_SSMenu = OptionMenu(OT,WI14_SS,*SSInitiators)
    WI15_SS = StringVar(OT)
    WI15_SSMenu = OptionMenu(OT,WI15_SS,*SSInitiators)
    WI16_SS = StringVar(OT)
    WI16_SSMenu = OptionMenu(OT,WI16_SS,*SSInitiators)
    WI17_SS = StringVar(OT)
    WI17_SSMenu = OptionMenu(OT,WI17_SS,*SSInitiators)
    WI18_SS = StringVar(OT)
    WI18_SSMenu = OptionMenu(OT,WI18_SS,*SSInitiators)
    WI19_SS = StringVar(OT)
    WI19_SSMenu = OptionMenu(OT,WI19_SS,*SSInitiators)
    WI20_SS = StringVar(OT)
    WI20_SSMenu = OptionMenu(OT,WI20_SS,*SSInitiators)
    WI21_SS = StringVar(OT)
    WI21_SSMenu = OptionMenu(OT,WI21_SS,*SSInitiators)
    WI22_SS = StringVar(OT)
    WI22_SSMenu = OptionMenu(OT,WI22_SS,*SSInitiators)
    WI23_SS = StringVar(OT)
    WI23_SSMenu = OptionMenu(OT,WI23_SS,*SSInitiators)
    WI24_SS = StringVar(OT)
    WI24_SSMenu = OptionMenu(OT,WI24_SS,*SSInitiators)

    WI1_Dilu = StringVar(OT)
    WI1_DiluMenu = OptionMenu(OT,WI1_Dilu,*Diluents)
    WI2_Dilu = StringVar(OT)
    WI2_DiluMenu = OptionMenu(OT,WI2_Dilu,*Diluents)
    WI3_Dilu = StringVar(OT)
    WI3_DiluMenu = OptionMenu(OT,WI3_Dilu,*Diluents)
    WI4_Dilu = StringVar(OT)
    WI4_DiluMenu = OptionMenu(OT,WI4_Dilu,*Diluents)
    WI5_Dilu = StringVar(OT)
    WI5_DiluMenu = OptionMenu(OT,WI5_Dilu,*Diluents)
    WI6_Dilu = StringVar(OT)
    WI6_DiluMenu = OptionMenu(OT,WI6_Dilu,*Diluents)
    WI7_Dilu = StringVar(OT)
    WI7_DiluMenu = OptionMenu(OT,WI7_Dilu,*Diluents)
    WI8_Dilu = StringVar(OT)
    WI8_DiluMenu = OptionMenu(OT,WI8_Dilu,*Diluents)
    WI9_Dilu = StringVar(OT)
    WI9_DiluMenu = OptionMenu(OT,WI9_Dilu,*Diluents)
    WI10_Dilu = StringVar(OT)
    WI10_DiluMenu = OptionMenu(OT,WI10_Dilu,*Diluents)
    WI11_Dilu = StringVar(OT)
    WI11_DiluMenu = OptionMenu(OT,WI11_Dilu,*Diluents)
    WI12_Dilu = StringVar(OT)
    WI12_DiluMenu = OptionMenu(OT,WI12_Dilu,*Diluents)
    WI13_Dilu = StringVar(OT)
    WI13_DiluMenu = OptionMenu(OT,WI13_Dilu,*Diluents)
    WI14_Dilu = StringVar(OT)
    WI14_DiluMenu = OptionMenu(OT,WI14_Dilu,*Diluents)
    WI15_Dilu = StringVar(OT)
    WI15_DiluMenu = OptionMenu(OT,WI15_Dilu,*Diluents)
    WI16_Dilu = StringVar(OT)
    WI16_DiluMenu = OptionMenu(OT,WI16_Dilu,*Diluents)
    WI17_Dilu = StringVar(OT)
    WI17_DiluMenu = OptionMenu(OT,WI17_Dilu,*Diluents)
    WI18_Dilu = StringVar(OT)
    WI18_DiluMenu = OptionMenu(OT,WI18_Dilu,*Diluents)
    WI19_Dilu = StringVar(OT)
    WI19_DiluMenu = OptionMenu(OT,WI19_Dilu,*Diluents)
    WI20_Dilu = StringVar(OT)
    WI20_DiluMenu = OptionMenu(OT,WI20_Dilu,*Diluents)
    WI21_Dilu = StringVar(OT)
    WI21_DiluMenu = OptionMenu(OT,WI21_Dilu,*Diluents)
    WI22_Dilu = StringVar(OT)
    WI22_DiluMenu = OptionMenu(OT,WI22_Dilu,*Diluents)
    WI23_Dilu = StringVar(OT)
    WI23_DiluMenu = OptionMenu(OT,WI23_Dilu,*Diluents)
    WI24_Dilu = StringVar(OT)
    WI24_DiluMenu = OptionMenu(OT,WI24_Dilu,*Diluents)

    WJ1_Vol = Entry()
    WJ2_Vol = Entry()
    WJ3_Vol = Entry()
    WJ4_Vol = Entry()
    WJ5_Vol = Entry()
    WJ6_Vol = Entry()
    WJ7_Vol = Entry()
    WJ8_Vol = Entry()
    WJ9_Vol = Entry()
    WJ10_Vol = Entry()
    WJ11_Vol = Entry()
    WJ12_Vol = Entry()
    WJ13_Vol = Entry()
    WJ14_Vol = Entry()
    WJ15_Vol = Entry()
    WJ16_Vol = Entry()
    WJ17_Vol = Entry()
    WJ18_Vol = Entry()
    WJ19_Vol = Entry()
    WJ20_Vol = Entry()
    WJ21_Vol = Entry()
    WJ22_Vol = Entry()
    WJ23_Vol = Entry()
    WJ24_Vol = Entry()

    WJ1_Solvent1_Conc = Entry()
    WJ2_Solvent1_Conc = Entry()
    WJ3_Solvent1_Conc = Entry()
    WJ4_Solvent1_Conc = Entry()
    WJ5_Solvent1_Conc = Entry()
    WJ6_Solvent1_Conc = Entry()
    WJ7_Solvent1_Conc = Entry()
    WJ8_Solvent1_Conc = Entry()
    WJ9_Solvent1_Conc = Entry()
    WJ10_Solvent1_Conc = Entry()
    WJ11_Solvent1_Conc = Entry()
    WJ12_Solvent1_Conc = Entry()
    WJ13_Solvent1_Conc = Entry()
    WJ14_Solvent1_Conc = Entry()
    WJ15_Solvent1_Conc = Entry()
    WJ16_Solvent1_Conc = Entry()
    WJ17_Solvent1_Conc = Entry()
    WJ18_Solvent1_Conc = Entry()
    WJ19_Solvent1_Conc = Entry()
    WJ20_Solvent1_Conc = Entry()
    WJ21_Solvent1_Conc = Entry()
    WJ22_Solvent1_Conc = Entry()
    WJ23_Solvent1_Conc = Entry()
    WJ24_Solvent1_Conc = Entry()
    
    WJ1_Solvent2_Conc = Entry()
    WJ2_Solvent2_Conc = Entry()
    WJ3_Solvent2_Conc = Entry()
    WJ4_Solvent2_Conc = Entry()
    WJ5_Solvent2_Conc = Entry()
    WJ6_Solvent2_Conc = Entry()
    WJ7_Solvent2_Conc = Entry()
    WJ8_Solvent2_Conc = Entry()
    WJ9_Solvent2_Conc = Entry()
    WJ10_Solvent2_Conc = Entry()
    WJ11_Solvent2_Conc = Entry()
    WJ12_Solvent2_Conc = Entry()
    WJ13_Solvent2_Conc = Entry()
    WJ14_Solvent2_Conc = Entry()
    WJ15_Solvent2_Conc = Entry()
    WJ16_Solvent2_Conc = Entry()
    WJ17_Solvent2_Conc = Entry()
    WJ18_Solvent2_Conc = Entry()
    WJ19_Solvent2_Conc = Entry()
    WJ20_Solvent2_Conc = Entry()
    WJ21_Solvent2_Conc = Entry()
    WJ22_Solvent2_Conc = Entry()
    WJ23_Solvent2_Conc = Entry()
    WJ24_Solvent2_Conc = Entry()
    
    WJ1_SS_Conc = Entry()
    WJ2_SS_Conc = Entry()
    WJ3_SS_Conc = Entry()
    WJ4_SS_Conc = Entry()
    WJ5_SS_Conc = Entry()
    WJ6_SS_Conc = Entry()
    WJ7_SS_Conc = Entry()
    WJ8_SS_Conc = Entry()
    WJ9_SS_Conc = Entry()
    WJ10_SS_Conc = Entry()
    WJ11_SS_Conc = Entry()
    WJ12_SS_Conc = Entry()
    WJ13_SS_Conc = Entry()
    WJ14_SS_Conc = Entry()
    WJ15_SS_Conc = Entry()
    WJ16_SS_Conc = Entry()
    WJ17_SS_Conc = Entry()
    WJ18_SS_Conc = Entry()
    WJ19_SS_Conc = Entry()
    WJ20_SS_Conc = Entry()
    WJ21_SS_Conc = Entry()
    WJ22_SS_Conc = Entry()
    WJ23_SS_Conc = Entry()
    WJ24_SS_Conc = Entry()

    WJ1_Ingr = StringVar(OT)
    WJ1_IngrMenu = OptionMenu(OT,WJ1_Ingr,*Ingrs)
    WJ2_Ingr = StringVar(OT)
    WJ2_IngrMenu = OptionMenu(OT,WJ2_Ingr,*Ingrs)
    WJ3_Ingr = StringVar(OT)
    WJ3_IngrMenu = OptionMenu(OT,WJ3_Ingr,*Ingrs)
    WJ4_Ingr = StringVar(OT)
    WJ4_IngrMenu = OptionMenu(OT,WJ4_Ingr,*Ingrs)
    WJ5_Ingr = StringVar(OT)
    WJ5_IngrMenu = OptionMenu(OT,WJ5_Ingr,*Ingrs)
    WJ6_Ingr = StringVar(OT)
    WJ6_IngrMenu = OptionMenu(OT,WJ6_Ingr,*Ingrs)
    WJ7_Ingr = StringVar(OT)
    WJ7_IngrMenu = OptionMenu(OT,WJ7_Ingr,*Ingrs)
    WJ8_Ingr = StringVar(OT)
    WJ8_IngrMenu = OptionMenu(OT,WJ8_Ingr,*Ingrs)
    WJ9_Ingr = StringVar(OT)
    WJ9_IngrMenu = OptionMenu(OT,WJ9_Ingr,*Ingrs)
    WJ10_Ingr = StringVar(OT)
    WJ10_IngrMenu = OptionMenu(OT,WJ10_Ingr,*Ingrs)
    WJ11_Ingr = StringVar(OT)
    WJ11_IngrMenu = OptionMenu(OT,WJ11_Ingr,*Ingrs)
    WJ12_Ingr = StringVar(OT)
    WJ12_IngrMenu = OptionMenu(OT,WJ12_Ingr,*Ingrs)
    WJ13_Ingr = StringVar(OT)
    WJ13_IngrMenu = OptionMenu(OT,WJ13_Ingr,*Ingrs)
    WJ14_Ingr = StringVar(OT)
    WJ14_IngrMenu = OptionMenu(OT,WJ14_Ingr,*Ingrs)
    WJ15_Ingr = StringVar(OT)
    WJ15_IngrMenu = OptionMenu(OT,WJ15_Ingr,*Ingrs)
    WJ16_Ingr = StringVar(OT)
    WJ16_IngrMenu = OptionMenu(OT,WJ16_Ingr,*Ingrs)
    WJ17_Ingr = StringVar(OT)
    WJ17_IngrMenu = OptionMenu(OT,WJ17_Ingr,*Ingrs)
    WJ18_Ingr = StringVar(OT)
    WJ18_IngrMenu = OptionMenu(OT,WJ18_Ingr,*Ingrs)
    WJ19_Ingr = StringVar(OT)
    WJ19_IngrMenu = OptionMenu(OT,WJ19_Ingr,*Ingrs)
    WJ20_Ingr = StringVar(OT)
    WJ20_IngrMenu = OptionMenu(OT,WJ20_Ingr,*Ingrs)
    WJ21_Ingr = StringVar(OT)
    WJ21_IngrMenu = OptionMenu(OT,WJ21_Ingr,*Ingrs)
    WJ22_Ingr = StringVar(OT)
    WJ22_IngrMenu = OptionMenu(OT,WJ22_Ingr,*Ingrs)
    WJ23_Ingr = StringVar(OT)
    WJ23_IngrMenu = OptionMenu(OT,WJ23_Ingr,*Ingrs)
    WJ24_Ingr = StringVar(OT)
    WJ24_IngrMenu = OptionMenu(OT,WJ24_Ingr,*Ingrs)

    WJ1_SS = StringVar(OT)
    WJ1_SSMenu = OptionMenu(OT,WJ1_SS,*SSInitiators)
    WJ2_SS = StringVar(OT)
    WJ2_SSMenu = OptionMenu(OT,WJ2_SS,*SSInitiators)
    WJ3_SS = StringVar(OT)
    WJ3_SSMenu = OptionMenu(OT,WJ3_SS,*SSInitiators)
    WJ4_SS = StringVar(OT)
    WJ4_SSMenu = OptionMenu(OT,WJ4_SS,*SSInitiators)
    WJ5_SS = StringVar(OT)
    WJ5_SSMenu = OptionMenu(OT,WJ5_SS,*SSInitiators)
    WJ6_SS = StringVar(OT)
    WJ6_SSMenu = OptionMenu(OT,WJ6_SS,*SSInitiators)
    WJ7_SS = StringVar(OT)
    WJ7_SSMenu = OptionMenu(OT,WJ7_SS,*SSInitiators)
    WJ8_SS = StringVar(OT)
    WJ8_SSMenu = OptionMenu(OT,WJ8_SS,*SSInitiators)
    WJ9_SS = StringVar(OT)
    WJ9_SSMenu = OptionMenu(OT,WJ9_SS,*SSInitiators)
    WJ10_SS = StringVar(OT)
    WJ10_SSMenu = OptionMenu(OT,WJ10_SS,*SSInitiators)
    WJ11_SS = StringVar(OT)
    WJ11_SSMenu = OptionMenu(OT,WJ11_SS,*SSInitiators)
    WJ12_SS = StringVar(OT)
    WJ12_SSMenu = OptionMenu(OT,WJ12_SS,*SSInitiators)
    WJ13_SS = StringVar(OT)
    WJ13_SSMenu = OptionMenu(OT,WJ13_SS,*SSInitiators)
    WJ14_SS = StringVar(OT)
    WJ14_SSMenu = OptionMenu(OT,WJ14_SS,*SSInitiators)
    WJ15_SS = StringVar(OT)
    WJ15_SSMenu = OptionMenu(OT,WJ15_SS,*SSInitiators)
    WJ16_SS = StringVar(OT)
    WJ16_SSMenu = OptionMenu(OT,WJ16_SS,*SSInitiators)
    WJ17_SS = StringVar(OT)
    WJ17_SSMenu = OptionMenu(OT,WJ17_SS,*SSInitiators)
    WJ18_SS = StringVar(OT)
    WJ18_SSMenu = OptionMenu(OT,WJ18_SS,*SSInitiators)
    WJ19_SS = StringVar(OT)
    WJ19_SSMenu = OptionMenu(OT,WJ19_SS,*SSInitiators)
    WJ20_SS = StringVar(OT)
    WJ20_SSMenu = OptionMenu(OT,WJ20_SS,*SSInitiators)
    WJ21_SS = StringVar(OT)
    WJ21_SSMenu = OptionMenu(OT,WJ21_SS,*SSInitiators)
    WJ22_SS = StringVar(OT)
    WJ22_SSMenu = OptionMenu(OT,WJ22_SS,*SSInitiators)
    WJ23_SS = StringVar(OT)
    WJ23_SSMenu = OptionMenu(OT,WJ23_SS,*SSInitiators)
    WJ24_SS = StringVar(OT)
    WJ24_SSMenu = OptionMenu(OT,WJ24_SS,*SSInitiators)

    WJ1_Dilu = StringVar(OT)
    WJ1_DiluMenu = OptionMenu(OT,WJ1_Dilu,*Diluents)
    WJ2_Dilu = StringVar(OT)
    WJ2_DiluMenu = OptionMenu(OT,WJ2_Dilu,*Diluents)
    WJ3_Dilu = StringVar(OT)
    WJ3_DiluMenu = OptionMenu(OT,WJ3_Dilu,*Diluents)
    WJ4_Dilu = StringVar(OT)
    WJ4_DiluMenu = OptionMenu(OT,WJ4_Dilu,*Diluents)
    WJ5_Dilu = StringVar(OT)
    WJ5_DiluMenu = OptionMenu(OT,WJ5_Dilu,*Diluents)
    WJ6_Dilu = StringVar(OT)
    WJ6_DiluMenu = OptionMenu(OT,WJ6_Dilu,*Diluents)
    WJ7_Dilu = StringVar(OT)
    WJ7_DiluMenu = OptionMenu(OT,WJ7_Dilu,*Diluents)
    WJ8_Dilu = StringVar(OT)
    WJ8_DiluMenu = OptionMenu(OT,WJ8_Dilu,*Diluents)
    WJ9_Dilu = StringVar(OT)
    WJ9_DiluMenu = OptionMenu(OT,WJ9_Dilu,*Diluents)
    WJ10_Dilu = StringVar(OT)
    WJ10_DiluMenu = OptionMenu(OT,WJ10_Dilu,*Diluents)
    WJ11_Dilu = StringVar(OT)
    WJ11_DiluMenu = OptionMenu(OT,WJ11_Dilu,*Diluents)
    WJ12_Dilu = StringVar(OT)
    WJ12_DiluMenu = OptionMenu(OT,WJ12_Dilu,*Diluents)
    WJ13_Dilu = StringVar(OT)
    WJ13_DiluMenu = OptionMenu(OT,WJ13_Dilu,*Diluents)
    WJ14_Dilu = StringVar(OT)
    WJ14_DiluMenu = OptionMenu(OT,WJ14_Dilu,*Diluents)
    WJ15_Dilu = StringVar(OT)
    WJ15_DiluMenu = OptionMenu(OT,WJ15_Dilu,*Diluents)
    WJ16_Dilu = StringVar(OT)
    WJ16_DiluMenu = OptionMenu(OT,WJ16_Dilu,*Diluents)
    WJ17_Dilu = StringVar(OT)
    WJ17_DiluMenu = OptionMenu(OT,WJ17_Dilu,*Diluents)
    WJ18_Dilu = StringVar(OT)
    WJ18_DiluMenu = OptionMenu(OT,WJ18_Dilu,*Diluents)
    WJ19_Dilu = StringVar(OT)
    WJ19_DiluMenu = OptionMenu(OT,WJ19_Dilu,*Diluents)
    WJ20_Dilu = StringVar(OT)
    WJ20_DiluMenu = OptionMenu(OT,WJ20_Dilu,*Diluents)
    WJ21_Dilu = StringVar(OT)
    WJ21_DiluMenu = OptionMenu(OT,WJ21_Dilu,*Diluents)
    WJ22_Dilu = StringVar(OT)
    WJ22_DiluMenu = OptionMenu(OT,WJ22_Dilu,*Diluents)
    WJ23_Dilu = StringVar(OT)
    WJ23_DiluMenu = OptionMenu(OT,WJ23_Dilu,*Diluents)
    WJ24_Dilu = StringVar(OT)
    WJ24_DiluMenu = OptionMenu(OT,WJ24_Dilu,*Diluents)

    WK1_Vol = Entry()
    WK2_Vol = Entry()
    WK3_Vol = Entry()
    WK4_Vol = Entry()
    WK5_Vol = Entry()
    WK6_Vol = Entry()
    WK7_Vol = Entry()
    WK8_Vol = Entry()
    WK9_Vol = Entry()
    WK10_Vol = Entry()
    WK11_Vol = Entry()
    WK12_Vol = Entry()
    WK13_Vol = Entry()
    WK14_Vol = Entry()
    WK15_Vol = Entry()
    WK16_Vol = Entry()
    WK17_Vol = Entry()
    WK18_Vol = Entry()
    WK19_Vol = Entry()
    WK20_Vol = Entry()
    WK21_Vol = Entry()
    WK22_Vol = Entry()
    WK23_Vol = Entry()
    WK24_Vol = Entry()

    WK1_Solvent1_Conc = Entry()
    WK2_Solvent1_Conc = Entry()
    WK3_Solvent1_Conc = Entry()
    WK4_Solvent1_Conc = Entry()
    WK5_Solvent1_Conc = Entry()
    WK6_Solvent1_Conc = Entry()
    WK7_Solvent1_Conc = Entry()
    WK8_Solvent1_Conc = Entry()
    WK9_Solvent1_Conc = Entry()
    WK10_Solvent1_Conc = Entry()
    WK11_Solvent1_Conc = Entry()
    WK12_Solvent1_Conc = Entry()
    WK13_Solvent1_Conc = Entry()
    WK14_Solvent1_Conc = Entry()
    WK15_Solvent1_Conc = Entry()
    WK16_Solvent1_Conc = Entry()
    WK17_Solvent1_Conc = Entry()
    WK18_Solvent1_Conc = Entry()
    WK19_Solvent1_Conc = Entry()
    WK20_Solvent1_Conc = Entry()
    WK21_Solvent1_Conc = Entry()
    WK22_Solvent1_Conc = Entry()
    WK23_Solvent1_Conc = Entry()
    WK24_Solvent1_Conc = Entry()
    
    WK1_Solvent2_Conc = Entry()
    WK2_Solvent2_Conc = Entry()
    WK3_Solvent2_Conc = Entry()
    WK4_Solvent2_Conc = Entry()
    WK5_Solvent2_Conc = Entry()
    WK6_Solvent2_Conc = Entry()
    WK7_Solvent2_Conc = Entry()
    WK8_Solvent2_Conc = Entry()
    WK9_Solvent2_Conc = Entry()
    WK10_Solvent2_Conc = Entry()
    WK11_Solvent2_Conc = Entry()
    WK12_Solvent2_Conc = Entry()
    WK13_Solvent2_Conc = Entry()
    WK14_Solvent2_Conc = Entry()
    WK15_Solvent2_Conc = Entry()
    WK16_Solvent2_Conc = Entry()
    WK17_Solvent2_Conc = Entry()
    WK18_Solvent2_Conc = Entry()
    WK19_Solvent2_Conc = Entry()
    WK20_Solvent2_Conc = Entry()
    WK21_Solvent2_Conc = Entry()
    WK22_Solvent2_Conc = Entry()
    WK23_Solvent2_Conc = Entry()
    WK24_Solvent2_Conc = Entry()

    
    WK1_SS_Conc = Entry()
    WK2_SS_Conc = Entry()
    WK3_SS_Conc = Entry()
    WK4_SS_Conc = Entry()
    WK5_SS_Conc = Entry()
    WK6_SS_Conc = Entry()
    WK7_SS_Conc = Entry()
    WK8_SS_Conc = Entry()
    WK9_SS_Conc = Entry()
    WK10_SS_Conc = Entry()
    WK11_SS_Conc = Entry()
    WK12_SS_Conc = Entry()
    WK13_SS_Conc = Entry()
    WK14_SS_Conc = Entry()
    WK15_SS_Conc = Entry()
    WK16_SS_Conc = Entry()
    WK17_SS_Conc = Entry()
    WK18_SS_Conc = Entry()
    WK19_SS_Conc = Entry()
    WK20_SS_Conc = Entry()
    WK21_SS_Conc = Entry()
    WK22_SS_Conc = Entry()
    WK23_SS_Conc = Entry()
    WK24_SS_Conc = Entry()

    WK1_Ingr = StringVar(OT)
    WK1_IngrMenu = OptionMenu(OT,WK1_Ingr,*Ingrs)
    WK2_Ingr = StringVar(OT)
    WK2_IngrMenu = OptionMenu(OT,WK2_Ingr,*Ingrs)
    WK3_Ingr = StringVar(OT)
    WK3_IngrMenu = OptionMenu(OT,WK3_Ingr,*Ingrs)
    WK4_Ingr = StringVar(OT)
    WK4_IngrMenu = OptionMenu(OT,WK4_Ingr,*Ingrs)
    WK5_Ingr = StringVar(OT)
    WK5_IngrMenu = OptionMenu(OT,WK5_Ingr,*Ingrs)
    WK6_Ingr = StringVar(OT)
    WK6_IngrMenu = OptionMenu(OT,WK6_Ingr,*Ingrs)
    WK7_Ingr = StringVar(OT)
    WK7_IngrMenu = OptionMenu(OT,WK7_Ingr,*Ingrs)
    WK8_Ingr = StringVar(OT)
    WK8_IngrMenu = OptionMenu(OT,WK8_Ingr,*Ingrs)
    WK9_Ingr = StringVar(OT)
    WK9_IngrMenu = OptionMenu(OT,WK9_Ingr,*Ingrs)
    WK10_Ingr = StringVar(OT)
    WK10_IngrMenu = OptionMenu(OT,WK10_Ingr,*Ingrs)
    WK11_Ingr = StringVar(OT)
    WK11_IngrMenu = OptionMenu(OT,WK11_Ingr,*Ingrs)
    WK12_Ingr = StringVar(OT)
    WK12_IngrMenu = OptionMenu(OT,WK12_Ingr,*Ingrs)
    WK13_Ingr = StringVar(OT)
    WK13_IngrMenu = OptionMenu(OT,WK13_Ingr,*Ingrs)
    WK14_Ingr = StringVar(OT)
    WK14_IngrMenu = OptionMenu(OT,WK14_Ingr,*Ingrs)
    WK15_Ingr = StringVar(OT)
    WK15_IngrMenu = OptionMenu(OT,WK15_Ingr,*Ingrs)
    WK16_Ingr = StringVar(OT)
    WK16_IngrMenu = OptionMenu(OT,WK16_Ingr,*Ingrs)
    WK17_Ingr = StringVar(OT)
    WK17_IngrMenu = OptionMenu(OT,WK17_Ingr,*Ingrs)
    WK18_Ingr = StringVar(OT)
    WK18_IngrMenu = OptionMenu(OT,WK18_Ingr,*Ingrs)
    WK19_Ingr = StringVar(OT)
    WK19_IngrMenu = OptionMenu(OT,WK19_Ingr,*Ingrs)
    WK20_Ingr = StringVar(OT)
    WK20_IngrMenu = OptionMenu(OT,WK20_Ingr,*Ingrs)
    WK21_Ingr = StringVar(OT)
    WK21_IngrMenu = OptionMenu(OT,WK21_Ingr,*Ingrs)
    WK22_Ingr = StringVar(OT)
    WK22_IngrMenu = OptionMenu(OT,WK22_Ingr,*Ingrs)
    WK23_Ingr = StringVar(OT)
    WK23_IngrMenu = OptionMenu(OT,WK23_Ingr,*Ingrs)
    WK24_Ingr = StringVar(OT)
    WK24_IngrMenu = OptionMenu(OT,WK24_Ingr,*Ingrs)

    WK1_SS = StringVar(OT)
    WK1_SSMenu = OptionMenu(OT,WK1_SS,*SSInitiators)
    WK2_SS = StringVar(OT)
    WK2_SSMenu = OptionMenu(OT,WK2_SS,*SSInitiators)
    WK3_SS = StringVar(OT)
    WK3_SSMenu = OptionMenu(OT,WK3_SS,*SSInitiators)
    WK4_SS = StringVar(OT)
    WK4_SSMenu = OptionMenu(OT,WK4_SS,*SSInitiators)
    WK5_SS = StringVar(OT)
    WK5_SSMenu = OptionMenu(OT,WK5_SS,*SSInitiators)
    WK6_SS = StringVar(OT)
    WK6_SSMenu = OptionMenu(OT,WK6_SS,*SSInitiators)
    WK7_SS = StringVar(OT)
    WK7_SSMenu = OptionMenu(OT,WK7_SS,*SSInitiators)
    WK8_SS = StringVar(OT)
    WK8_SSMenu = OptionMenu(OT,WK8_SS,*SSInitiators)
    WK9_SS = StringVar(OT)
    WK9_SSMenu = OptionMenu(OT,WK9_SS,*SSInitiators)
    WK10_SS = StringVar(OT)
    WK10_SSMenu = OptionMenu(OT,WK10_SS,*SSInitiators)
    WK11_SS = StringVar(OT)
    WK11_SSMenu = OptionMenu(OT,WK11_SS,*SSInitiators)
    WK12_SS = StringVar(OT)
    WK12_SSMenu = OptionMenu(OT,WK12_SS,*SSInitiators)
    WK13_SS = StringVar(OT)
    WK13_SSMenu = OptionMenu(OT,WK13_SS,*SSInitiators)
    WK14_SS = StringVar(OT)
    WK14_SSMenu = OptionMenu(OT,WK14_SS,*SSInitiators)
    WK15_SS = StringVar(OT)
    WK15_SSMenu = OptionMenu(OT,WK15_SS,*SSInitiators)
    WK16_SS = StringVar(OT)
    WK16_SSMenu = OptionMenu(OT,WK16_SS,*SSInitiators)
    WK17_SS = StringVar(OT)
    WK17_SSMenu = OptionMenu(OT,WK17_SS,*SSInitiators)
    WK18_SS = StringVar(OT)
    WK18_SSMenu = OptionMenu(OT,WK18_SS,*SSInitiators)
    WK19_SS = StringVar(OT)
    WK19_SSMenu = OptionMenu(OT,WK19_SS,*SSInitiators)
    WK20_SS = StringVar(OT)
    WK20_SSMenu = OptionMenu(OT,WK20_SS,*SSInitiators)
    WK21_SS = StringVar(OT)
    WK21_SSMenu = OptionMenu(OT,WK21_SS,*SSInitiators)
    WK22_SS = StringVar(OT)
    WK22_SSMenu = OptionMenu(OT,WK22_SS,*SSInitiators)
    WK23_SS = StringVar(OT)
    WK23_SSMenu = OptionMenu(OT,WK23_SS,*SSInitiators)
    WK24_SS = StringVar(OT)
    WK24_SSMenu = OptionMenu(OT,WK24_SS,*SSInitiators)

    WK1_Dilu = StringVar(OT)
    WK1_DiluMenu = OptionMenu(OT,WK1_Dilu,*Diluents)
    WK2_Dilu = StringVar(OT)
    WK2_DiluMenu = OptionMenu(OT,WK2_Dilu,*Diluents)
    WK3_Dilu = StringVar(OT)
    WK3_DiluMenu = OptionMenu(OT,WK3_Dilu,*Diluents)
    WK4_Dilu = StringVar(OT)
    WK4_DiluMenu = OptionMenu(OT,WK4_Dilu,*Diluents)
    WK5_Dilu = StringVar(OT)
    WK5_DiluMenu = OptionMenu(OT,WK5_Dilu,*Diluents)
    WK6_Dilu = StringVar(OT)
    WK6_DiluMenu = OptionMenu(OT,WK6_Dilu,*Diluents)
    WK7_Dilu = StringVar(OT)
    WK7_DiluMenu = OptionMenu(OT,WK7_Dilu,*Diluents)
    WK8_Dilu = StringVar(OT)
    WK8_DiluMenu = OptionMenu(OT,WK8_Dilu,*Diluents)
    WK9_Dilu = StringVar(OT)
    WK9_DiluMenu = OptionMenu(OT,WK9_Dilu,*Diluents)
    WK10_Dilu = StringVar(OT)
    WK10_DiluMenu = OptionMenu(OT,WK10_Dilu,*Diluents)
    WK11_Dilu = StringVar(OT)
    WK11_DiluMenu = OptionMenu(OT,WK11_Dilu,*Diluents)
    WK12_Dilu = StringVar(OT)
    WK12_DiluMenu = OptionMenu(OT,WK12_Dilu,*Diluents)
    WK13_Dilu = StringVar(OT)
    WK13_DiluMenu = OptionMenu(OT,WK13_Dilu,*Diluents)
    WK14_Dilu = StringVar(OT)
    WK14_DiluMenu = OptionMenu(OT,WK14_Dilu,*Diluents)
    WK15_Dilu = StringVar(OT)
    WK15_DiluMenu = OptionMenu(OT,WK15_Dilu,*Diluents)
    WK16_Dilu = StringVar(OT)
    WK16_DiluMenu = OptionMenu(OT,WK16_Dilu,*Diluents)
    WK17_Dilu = StringVar(OT)
    WK17_DiluMenu = OptionMenu(OT,WK17_Dilu,*Diluents)
    WK18_Dilu = StringVar(OT)
    WK18_DiluMenu = OptionMenu(OT,WK18_Dilu,*Diluents)
    WK19_Dilu = StringVar(OT)
    WK19_DiluMenu = OptionMenu(OT,WK19_Dilu,*Diluents)
    WK20_Dilu = StringVar(OT)
    WK20_DiluMenu = OptionMenu(OT,WK20_Dilu,*Diluents)
    WK21_Dilu = StringVar(OT)
    WK21_DiluMenu = OptionMenu(OT,WK21_Dilu,*Diluents)
    WK22_Dilu = StringVar(OT)
    WK22_DiluMenu = OptionMenu(OT,WK22_Dilu,*Diluents)
    WK23_Dilu = StringVar(OT)
    WK23_DiluMenu = OptionMenu(OT,WK23_Dilu,*Diluents)
    WK24_Dilu = StringVar(OT)
    WK24_DiluMenu = OptionMenu(OT,WK24_Dilu,*Diluents)

    WL1_Vol = Entry()
    WL2_Vol = Entry()
    WL3_Vol = Entry()
    WL4_Vol = Entry()
    WL5_Vol = Entry()
    WL6_Vol = Entry()
    WL7_Vol = Entry()
    WL8_Vol = Entry()
    WL9_Vol = Entry()
    WL10_Vol = Entry()
    WL11_Vol = Entry()
    WL12_Vol = Entry()
    WL13_Vol = Entry()
    WL14_Vol = Entry()
    WL15_Vol = Entry()
    WL16_Vol = Entry()
    WL17_Vol = Entry()
    WL18_Vol = Entry()
    WL19_Vol = Entry()
    WL20_Vol = Entry()
    WL21_Vol = Entry()
    WL22_Vol = Entry()
    WL23_Vol = Entry()
    WL24_Vol = Entry()

    WL1_Solvent1_Conc = Entry()
    WL2_Solvent1_Conc = Entry()
    WL3_Solvent1_Conc = Entry()
    WL4_Solvent1_Conc = Entry()
    WL5_Solvent1_Conc = Entry()
    WL6_Solvent1_Conc = Entry()
    WL7_Solvent1_Conc = Entry()
    WL8_Solvent1_Conc = Entry()
    WL9_Solvent1_Conc = Entry()
    WL10_Solvent1_Conc = Entry()
    WL11_Solvent1_Conc = Entry()
    WL12_Solvent1_Conc = Entry()
    WL13_Solvent1_Conc = Entry()
    WL14_Solvent1_Conc = Entry()
    WL15_Solvent1_Conc = Entry()
    WL16_Solvent1_Conc = Entry()
    WL17_Solvent1_Conc = Entry()
    WL18_Solvent1_Conc = Entry()
    WL19_Solvent1_Conc = Entry()
    WL20_Solvent1_Conc = Entry()
    WL21_Solvent1_Conc = Entry()
    WL22_Solvent1_Conc = Entry()
    WL23_Solvent1_Conc = Entry()
    WL24_Solvent1_Conc = Entry()
    
    WL1_Solvent2_Conc = Entry()
    WL2_Solvent2_Conc = Entry()
    WL3_Solvent2_Conc = Entry()
    WL4_Solvent2_Conc = Entry()
    WL5_Solvent2_Conc = Entry()
    WL6_Solvent2_Conc = Entry()
    WL7_Solvent2_Conc = Entry()
    WL8_Solvent2_Conc = Entry()
    WL9_Solvent2_Conc = Entry()
    WL10_Solvent2_Conc = Entry()
    WL11_Solvent2_Conc = Entry()
    WL12_Solvent2_Conc = Entry()
    WL13_Solvent2_Conc = Entry()
    WL14_Solvent2_Conc = Entry()
    WL15_Solvent2_Conc = Entry()
    WL16_Solvent2_Conc = Entry()
    WL17_Solvent2_Conc = Entry()
    WL18_Solvent2_Conc = Entry()
    WL19_Solvent2_Conc = Entry()
    WL20_Solvent2_Conc = Entry()
    WL21_Solvent2_Conc = Entry()
    WL22_Solvent2_Conc = Entry()
    WL23_Solvent2_Conc = Entry()
    WL24_Solvent2_Conc = Entry()

    
    WL1_SS_Conc = Entry()
    WL2_SS_Conc = Entry()
    WL3_SS_Conc = Entry()
    WL4_SS_Conc = Entry()
    WL5_SS_Conc = Entry()
    WL6_SS_Conc = Entry()
    WL7_SS_Conc = Entry()
    WL8_SS_Conc = Entry()
    WL9_SS_Conc = Entry()
    WL10_SS_Conc = Entry()
    WL11_SS_Conc = Entry()
    WL12_SS_Conc = Entry()
    WL13_SS_Conc = Entry()
    WL14_SS_Conc = Entry()
    WL15_SS_Conc = Entry()
    WL16_SS_Conc = Entry()
    WL17_SS_Conc = Entry()
    WL18_SS_Conc = Entry()
    WL19_SS_Conc = Entry()
    WL20_SS_Conc = Entry()
    WL21_SS_Conc = Entry()
    WL22_SS_Conc = Entry()
    WL23_SS_Conc = Entry()
    WL24_SS_Conc = Entry()

    WL1_Ingr = StringVar(OT)
    WL1_IngrMenu = OptionMenu(OT,WL1_Ingr,*Ingrs)
    WL2_Ingr = StringVar(OT)
    WL2_IngrMenu = OptionMenu(OT,WL2_Ingr,*Ingrs)
    WL3_Ingr = StringVar(OT)
    WL3_IngrMenu = OptionMenu(OT,WL3_Ingr,*Ingrs)
    WL4_Ingr = StringVar(OT)
    WL4_IngrMenu = OptionMenu(OT,WL4_Ingr,*Ingrs)
    WL5_Ingr = StringVar(OT)
    WL5_IngrMenu = OptionMenu(OT,WL5_Ingr,*Ingrs)
    WL6_Ingr = StringVar(OT)
    WL6_IngrMenu = OptionMenu(OT,WL6_Ingr,*Ingrs)
    WL7_Ingr = StringVar(OT)
    WL7_IngrMenu = OptionMenu(OT,WL7_Ingr,*Ingrs)
    WL8_Ingr = StringVar(OT)
    WL8_IngrMenu = OptionMenu(OT,WL8_Ingr,*Ingrs)
    WL9_Ingr = StringVar(OT)
    WL9_IngrMenu = OptionMenu(OT,WL9_Ingr,*Ingrs)
    WL10_Ingr = StringVar(OT)
    WL10_IngrMenu = OptionMenu(OT,WL10_Ingr,*Ingrs)
    WL11_Ingr = StringVar(OT)
    WL11_IngrMenu = OptionMenu(OT,WL11_Ingr,*Ingrs)
    WL12_Ingr = StringVar(OT)
    WL12_IngrMenu = OptionMenu(OT,WL12_Ingr,*Ingrs)
    WL13_Ingr = StringVar(OT)
    WL13_IngrMenu = OptionMenu(OT,WL13_Ingr,*Ingrs)
    WL14_Ingr = StringVar(OT)
    WL14_IngrMenu = OptionMenu(OT,WL14_Ingr,*Ingrs)
    WL15_Ingr = StringVar(OT)
    WL15_IngrMenu = OptionMenu(OT,WL15_Ingr,*Ingrs)
    WL16_Ingr = StringVar(OT)
    WL16_IngrMenu = OptionMenu(OT,WL16_Ingr,*Ingrs)
    WL17_Ingr = StringVar(OT)
    WL17_IngrMenu = OptionMenu(OT,WL17_Ingr,*Ingrs)
    WL18_Ingr = StringVar(OT)
    WL18_IngrMenu = OptionMenu(OT,WL18_Ingr,*Ingrs)
    WL19_Ingr = StringVar(OT)
    WL19_IngrMenu = OptionMenu(OT,WL19_Ingr,*Ingrs)
    WL20_Ingr = StringVar(OT)
    WL20_IngrMenu = OptionMenu(OT,WL20_Ingr,*Ingrs)
    WL21_Ingr = StringVar(OT)
    WL21_IngrMenu = OptionMenu(OT,WL21_Ingr,*Ingrs)
    WL22_Ingr = StringVar(OT)
    WL22_IngrMenu = OptionMenu(OT,WL22_Ingr,*Ingrs)
    WL23_Ingr = StringVar(OT)
    WL23_IngrMenu = OptionMenu(OT,WL23_Ingr,*Ingrs)
    WL24_Ingr = StringVar(OT)
    WL24_IngrMenu = OptionMenu(OT,WL24_Ingr,*Ingrs)

    WL1_SS = StringVar(OT)
    WL1_SSMenu = OptionMenu(OT,WL1_SS,*SSInitiators)
    WL2_SS = StringVar(OT)
    WL2_SSMenu = OptionMenu(OT,WL2_SS,*SSInitiators)
    WL3_SS = StringVar(OT)
    WL3_SSMenu = OptionMenu(OT,WL3_SS,*SSInitiators)
    WL4_SS = StringVar(OT)
    WL4_SSMenu = OptionMenu(OT,WL4_SS,*SSInitiators)
    WL5_SS = StringVar(OT)
    WL5_SSMenu = OptionMenu(OT,WL5_SS,*SSInitiators)
    WL6_SS = StringVar(OT)
    WL6_SSMenu = OptionMenu(OT,WL6_SS,*SSInitiators)
    WL7_SS = StringVar(OT)
    WL7_SSMenu = OptionMenu(OT,WL7_SS,*SSInitiators)
    WL8_SS = StringVar(OT)
    WL8_SSMenu = OptionMenu(OT,WL8_SS,*SSInitiators)
    WL9_SS = StringVar(OT)
    WL9_SSMenu = OptionMenu(OT,WL9_SS,*SSInitiators)
    WL10_SS = StringVar(OT)
    WL10_SSMenu = OptionMenu(OT,WL10_SS,*SSInitiators)
    WL11_SS = StringVar(OT)
    WL11_SSMenu = OptionMenu(OT,WL11_SS,*SSInitiators)
    WL12_SS = StringVar(OT)
    WL12_SSMenu = OptionMenu(OT,WL12_SS,*SSInitiators)
    WL13_SS = StringVar(OT)
    WL13_SSMenu = OptionMenu(OT,WL13_SS,*SSInitiators)
    WL14_SS = StringVar(OT)
    WL14_SSMenu = OptionMenu(OT,WL14_SS,*SSInitiators)
    WL15_SS = StringVar(OT)
    WL15_SSMenu = OptionMenu(OT,WL15_SS,*SSInitiators)
    WL16_SS = StringVar(OT)
    WL16_SSMenu = OptionMenu(OT,WL16_SS,*SSInitiators)
    WL17_SS = StringVar(OT)
    WL17_SSMenu = OptionMenu(OT,WL17_SS,*SSInitiators)
    WL18_SS = StringVar(OT)
    WL18_SSMenu = OptionMenu(OT,WL18_SS,*SSInitiators)
    WL19_SS = StringVar(OT)
    WL19_SSMenu = OptionMenu(OT,WL19_SS,*SSInitiators)
    WL20_SS = StringVar(OT)
    WL20_SSMenu = OptionMenu(OT,WL20_SS,*SSInitiators)
    WL21_SS = StringVar(OT)
    WL21_SSMenu = OptionMenu(OT,WL21_SS,*SSInitiators)
    WL22_SS = StringVar(OT)
    WL22_SSMenu = OptionMenu(OT,WL22_SS,*SSInitiators)
    WL23_SS = StringVar(OT)
    WL23_SSMenu = OptionMenu(OT,WL23_SS,*SSInitiators)
    WL24_SS = StringVar(OT)
    WL24_SSMenu = OptionMenu(OT,WL24_SS,*SSInitiators)

    WL1_Dilu = StringVar(OT)
    WL1_DiluMenu = OptionMenu(OT,WL1_Dilu,*Diluents)
    WL2_Dilu = StringVar(OT)
    WL2_DiluMenu = OptionMenu(OT,WL2_Dilu,*Diluents)
    WL3_Dilu = StringVar(OT)
    WL3_DiluMenu = OptionMenu(OT,WL3_Dilu,*Diluents)
    WL4_Dilu = StringVar(OT)
    WL4_DiluMenu = OptionMenu(OT,WL4_Dilu,*Diluents)
    WL5_Dilu = StringVar(OT)
    WL5_DiluMenu = OptionMenu(OT,WL5_Dilu,*Diluents)
    WL6_Dilu = StringVar(OT)
    WL6_DiluMenu = OptionMenu(OT,WL6_Dilu,*Diluents)
    WL7_Dilu = StringVar(OT)
    WL7_DiluMenu = OptionMenu(OT,WL7_Dilu,*Diluents)
    WL8_Dilu = StringVar(OT)
    WL8_DiluMenu = OptionMenu(OT,WL8_Dilu,*Diluents)
    WL9_Dilu = StringVar(OT)
    WL9_DiluMenu = OptionMenu(OT,WL9_Dilu,*Diluents)
    WL10_Dilu = StringVar(OT)
    WL10_DiluMenu = OptionMenu(OT,WL10_Dilu,*Diluents)
    WL11_Dilu = StringVar(OT)
    WL11_DiluMenu = OptionMenu(OT,WL11_Dilu,*Diluents)
    WL12_Dilu = StringVar(OT)
    WL12_DiluMenu = OptionMenu(OT,WL12_Dilu,*Diluents)
    WL13_Dilu = StringVar(OT)
    WL13_DiluMenu = OptionMenu(OT,WL13_Dilu,*Diluents)
    WL14_Dilu = StringVar(OT)
    WL14_DiluMenu = OptionMenu(OT,WL14_Dilu,*Diluents)
    WL15_Dilu = StringVar(OT)
    WL15_DiluMenu = OptionMenu(OT,WL15_Dilu,*Diluents)
    WL16_Dilu = StringVar(OT)
    WL16_DiluMenu = OptionMenu(OT,WL16_Dilu,*Diluents)
    WL17_Dilu = StringVar(OT)
    WL17_DiluMenu = OptionMenu(OT,WL17_Dilu,*Diluents)
    WL18_Dilu = StringVar(OT)
    WL18_DiluMenu = OptionMenu(OT,WL18_Dilu,*Diluents)
    WL19_Dilu = StringVar(OT)
    WL19_DiluMenu = OptionMenu(OT,WL19_Dilu,*Diluents)
    WL20_Dilu = StringVar(OT)
    WL20_DiluMenu = OptionMenu(OT,WL20_Dilu,*Diluents)
    WL21_Dilu = StringVar(OT)
    WL21_DiluMenu = OptionMenu(OT,WL21_Dilu,*Diluents)
    WL22_Dilu = StringVar(OT)
    WL22_DiluMenu = OptionMenu(OT,WL22_Dilu,*Diluents)
    WL23_Dilu = StringVar(OT)
    WL23_DiluMenu = OptionMenu(OT,WL23_Dilu,*Diluents)
    WL24_Dilu = StringVar(OT)
    WL24_DiluMenu = OptionMenu(OT,WL24_Dilu,*Diluents)

    WM1_Vol = Entry()
    WM2_Vol = Entry()
    WM3_Vol = Entry()
    WM4_Vol = Entry()
    WM5_Vol = Entry()
    WM6_Vol = Entry()
    WM7_Vol = Entry()
    WM8_Vol = Entry()
    WM9_Vol = Entry()
    WM10_Vol = Entry()
    WM11_Vol = Entry()
    WM12_Vol = Entry()
    WM13_Vol = Entry()
    WM14_Vol = Entry()
    WM15_Vol = Entry()
    WM16_Vol = Entry()
    WM17_Vol = Entry()
    WM18_Vol = Entry()
    WM19_Vol = Entry()
    WM20_Vol = Entry()
    WM21_Vol = Entry()
    WM22_Vol = Entry()
    WM23_Vol = Entry()
    WM24_Vol = Entry()

    WM1_Solvent1_Conc = Entry()
    WM2_Solvent1_Conc = Entry()
    WM3_Solvent1_Conc = Entry()
    WM4_Solvent1_Conc = Entry()
    WM5_Solvent1_Conc = Entry()
    WM6_Solvent1_Conc = Entry()
    WM7_Solvent1_Conc = Entry()
    WM8_Solvent1_Conc = Entry()
    WM9_Solvent1_Conc = Entry()
    WM10_Solvent1_Conc = Entry()
    WM11_Solvent1_Conc = Entry()
    WM12_Solvent1_Conc = Entry()
    WM13_Solvent1_Conc = Entry()
    WM14_Solvent1_Conc = Entry()
    WM15_Solvent1_Conc = Entry()
    WM16_Solvent1_Conc = Entry()
    WM17_Solvent1_Conc = Entry()
    WM18_Solvent1_Conc = Entry()
    WM19_Solvent1_Conc = Entry()
    WM20_Solvent1_Conc = Entry()
    WM21_Solvent1_Conc = Entry()
    WM22_Solvent1_Conc = Entry()
    WM23_Solvent1_Conc = Entry()
    WM24_Solvent1_Conc = Entry()
    
    WM1_Solvent2_Conc = Entry()
    WM2_Solvent2_Conc = Entry()
    WM3_Solvent2_Conc = Entry()
    WM4_Solvent2_Conc = Entry()
    WM5_Solvent2_Conc = Entry()
    WM6_Solvent2_Conc = Entry()
    WM7_Solvent2_Conc = Entry()
    WM8_Solvent2_Conc = Entry()
    WM9_Solvent2_Conc = Entry()
    WM10_Solvent2_Conc = Entry()
    WM11_Solvent2_Conc = Entry()
    WM12_Solvent2_Conc = Entry()
    WM13_Solvent2_Conc = Entry()
    WM14_Solvent2_Conc = Entry()
    WM15_Solvent2_Conc = Entry()
    WM16_Solvent2_Conc = Entry()
    WM17_Solvent2_Conc = Entry()
    WM18_Solvent2_Conc = Entry()
    WM19_Solvent2_Conc = Entry()
    WM20_Solvent2_Conc = Entry()
    WM21_Solvent2_Conc = Entry()
    WM22_Solvent2_Conc = Entry()
    WM23_Solvent2_Conc = Entry()
    WM24_Solvent2_Conc = Entry()
    
    WM1_SS_Conc = Entry()
    WM2_SS_Conc = Entry()
    WM3_SS_Conc = Entry()
    WM4_SS_Conc = Entry()
    WM5_SS_Conc = Entry()
    WM6_SS_Conc = Entry()
    WM7_SS_Conc = Entry()
    WM8_SS_Conc = Entry()
    WM9_SS_Conc = Entry()
    WM10_SS_Conc = Entry()
    WM11_SS_Conc = Entry()
    WM12_SS_Conc = Entry()
    WM13_SS_Conc = Entry()
    WM14_SS_Conc = Entry()
    WM15_SS_Conc = Entry()
    WM16_SS_Conc = Entry()
    WM17_SS_Conc = Entry()
    WM18_SS_Conc = Entry()
    WM19_SS_Conc = Entry()
    WM20_SS_Conc = Entry()
    WM21_SS_Conc = Entry()
    WM22_SS_Conc = Entry()
    WM23_SS_Conc = Entry()
    WM24_SS_Conc = Entry()

    WM1_Ingr = StringVar(OT)
    WM1_IngrMenu = OptionMenu(OT,WM1_Ingr,*Ingrs)
    WM2_Ingr = StringVar(OT)
    WM2_IngrMenu = OptionMenu(OT,WM2_Ingr,*Ingrs)
    WM3_Ingr = StringVar(OT)
    WM3_IngrMenu = OptionMenu(OT,WM3_Ingr,*Ingrs)
    WM4_Ingr = StringVar(OT)
    WM4_IngrMenu = OptionMenu(OT,WM4_Ingr,*Ingrs)
    WM5_Ingr = StringVar(OT)
    WM5_IngrMenu = OptionMenu(OT,WM5_Ingr,*Ingrs)
    WM6_Ingr = StringVar(OT)
    WM6_IngrMenu = OptionMenu(OT,WM6_Ingr,*Ingrs)
    WM7_Ingr = StringVar(OT)
    WM7_IngrMenu = OptionMenu(OT,WM7_Ingr,*Ingrs)
    WM8_Ingr = StringVar(OT)
    WM8_IngrMenu = OptionMenu(OT,WM8_Ingr,*Ingrs)
    WM9_Ingr = StringVar(OT)
    WM9_IngrMenu = OptionMenu(OT,WM9_Ingr,*Ingrs)
    WM10_Ingr = StringVar(OT)
    WM10_IngrMenu = OptionMenu(OT,WM10_Ingr,*Ingrs)
    WM11_Ingr = StringVar(OT)
    WM11_IngrMenu = OptionMenu(OT,WM11_Ingr,*Ingrs)
    WM12_Ingr = StringVar(OT)
    WM12_IngrMenu = OptionMenu(OT,WM12_Ingr,*Ingrs)
    WM13_Ingr = StringVar(OT)
    WM13_IngrMenu = OptionMenu(OT,WM13_Ingr,*Ingrs)
    WM14_Ingr = StringVar(OT)
    WM14_IngrMenu = OptionMenu(OT,WM14_Ingr,*Ingrs)
    WM15_Ingr = StringVar(OT)
    WM15_IngrMenu = OptionMenu(OT,WM15_Ingr,*Ingrs)
    WM16_Ingr = StringVar(OT)
    WM16_IngrMenu = OptionMenu(OT,WM16_Ingr,*Ingrs)
    WM17_Ingr = StringVar(OT)
    WM17_IngrMenu = OptionMenu(OT,WM17_Ingr,*Ingrs)
    WM18_Ingr = StringVar(OT)
    WM18_IngrMenu = OptionMenu(OT,WM18_Ingr,*Ingrs)
    WM19_Ingr = StringVar(OT)
    WM19_IngrMenu = OptionMenu(OT,WM19_Ingr,*Ingrs)
    WM20_Ingr = StringVar(OT)
    WM20_IngrMenu = OptionMenu(OT,WM20_Ingr,*Ingrs)
    WM21_Ingr = StringVar(OT)
    WM21_IngrMenu = OptionMenu(OT,WM21_Ingr,*Ingrs)
    WM22_Ingr = StringVar(OT)
    WM22_IngrMenu = OptionMenu(OT,WM22_Ingr,*Ingrs)
    WM23_Ingr = StringVar(OT)
    WM23_IngrMenu = OptionMenu(OT,WM23_Ingr,*Ingrs)
    WM24_Ingr = StringVar(OT)
    WM24_IngrMenu = OptionMenu(OT,WM24_Ingr,*Ingrs)

    WM1_SS = StringVar(OT)
    WM1_SSMenu = OptionMenu(OT,WM1_SS,*SSInitiators)
    WM2_SS = StringVar(OT)
    WM2_SSMenu = OptionMenu(OT,WM2_SS,*SSInitiators)
    WM3_SS = StringVar(OT)
    WM3_SSMenu = OptionMenu(OT,WM3_SS,*SSInitiators)
    WM4_SS = StringVar(OT)
    WM4_SSMenu = OptionMenu(OT,WM4_SS,*SSInitiators)
    WM5_SS = StringVar(OT)
    WM5_SSMenu = OptionMenu(OT,WM5_SS,*SSInitiators)
    WM6_SS = StringVar(OT)
    WM6_SSMenu = OptionMenu(OT,WM6_SS,*SSInitiators)
    WM7_SS = StringVar(OT)
    WM7_SSMenu = OptionMenu(OT,WM7_SS,*SSInitiators)
    WM8_SS = StringVar(OT)
    WM8_SSMenu = OptionMenu(OT,WM8_SS,*SSInitiators)
    WM9_SS = StringVar(OT)
    WM9_SSMenu = OptionMenu(OT,WM9_SS,*SSInitiators)
    WM10_SS = StringVar(OT)
    WM10_SSMenu = OptionMenu(OT,WM10_SS,*SSInitiators)
    WM11_SS = StringVar(OT)
    WM11_SSMenu = OptionMenu(OT,WM11_SS,*SSInitiators)
    WM12_SS = StringVar(OT)
    WM12_SSMenu = OptionMenu(OT,WM12_SS,*SSInitiators)
    WM13_SS = StringVar(OT)
    WM13_SSMenu = OptionMenu(OT,WM13_SS,*SSInitiators)
    WM14_SS = StringVar(OT)
    WM14_SSMenu = OptionMenu(OT,WM14_SS,*SSInitiators)
    WM15_SS = StringVar(OT)
    WM15_SSMenu = OptionMenu(OT,WM15_SS,*SSInitiators)
    WM16_SS = StringVar(OT)
    WM16_SSMenu = OptionMenu(OT,WM16_SS,*SSInitiators)
    WM17_SS = StringVar(OT)
    WM17_SSMenu = OptionMenu(OT,WM17_SS,*SSInitiators)
    WM18_SS = StringVar(OT)
    WM18_SSMenu = OptionMenu(OT,WM18_SS,*SSInitiators)
    WM19_SS = StringVar(OT)
    WM19_SSMenu = OptionMenu(OT,WM19_SS,*SSInitiators)
    WM20_SS = StringVar(OT)
    WM20_SSMenu = OptionMenu(OT,WM20_SS,*SSInitiators)
    WM21_SS = StringVar(OT)
    WM21_SSMenu = OptionMenu(OT,WM21_SS,*SSInitiators)
    WM22_SS = StringVar(OT)
    WM22_SSMenu = OptionMenu(OT,WM22_SS,*SSInitiators)
    WM23_SS = StringVar(OT)
    WM23_SSMenu = OptionMenu(OT,WM23_SS,*SSInitiators)
    WM24_SS = StringVar(OT)
    WM24_SSMenu = OptionMenu(OT,WM24_SS,*SSInitiators)

    WM1_Dilu = StringVar(OT)
    WM1_DiluMenu = OptionMenu(OT,WM1_Dilu,*Diluents)
    WM2_Dilu = StringVar(OT)
    WM2_DiluMenu = OptionMenu(OT,WM2_Dilu,*Diluents)
    WM3_Dilu = StringVar(OT)
    WM3_DiluMenu = OptionMenu(OT,WM3_Dilu,*Diluents)
    WM4_Dilu = StringVar(OT)
    WM4_DiluMenu = OptionMenu(OT,WM4_Dilu,*Diluents)
    WM5_Dilu = StringVar(OT)
    WM5_DiluMenu = OptionMenu(OT,WM5_Dilu,*Diluents)
    WM6_Dilu = StringVar(OT)
    WM6_DiluMenu = OptionMenu(OT,WM6_Dilu,*Diluents)
    WM7_Dilu = StringVar(OT)
    WM7_DiluMenu = OptionMenu(OT,WM7_Dilu,*Diluents)
    WM8_Dilu = StringVar(OT)
    WM8_DiluMenu = OptionMenu(OT,WM8_Dilu,*Diluents)
    WM9_Dilu = StringVar(OT)
    WM9_DiluMenu = OptionMenu(OT,WM9_Dilu,*Diluents)
    WM10_Dilu = StringVar(OT)
    WM10_DiluMenu = OptionMenu(OT,WM10_Dilu,*Diluents)
    WM11_Dilu = StringVar(OT)
    WM11_DiluMenu = OptionMenu(OT,WM11_Dilu,*Diluents)
    WM12_Dilu = StringVar(OT)
    WM12_DiluMenu = OptionMenu(OT,WM12_Dilu,*Diluents)
    WM13_Dilu = StringVar(OT)
    WM13_DiluMenu = OptionMenu(OT,WM13_Dilu,*Diluents)
    WM14_Dilu = StringVar(OT)
    WM14_DiluMenu = OptionMenu(OT,WM14_Dilu,*Diluents)
    WM15_Dilu = StringVar(OT)
    WM15_DiluMenu = OptionMenu(OT,WM15_Dilu,*Diluents)
    WM16_Dilu = StringVar(OT)
    WM16_DiluMenu = OptionMenu(OT,WM16_Dilu,*Diluents)
    WM17_Dilu = StringVar(OT)
    WM17_DiluMenu = OptionMenu(OT,WM17_Dilu,*Diluents)
    WM18_Dilu = StringVar(OT)
    WM18_DiluMenu = OptionMenu(OT,WM18_Dilu,*Diluents)
    WM19_Dilu = StringVar(OT)
    WM19_DiluMenu = OptionMenu(OT,WM19_Dilu,*Diluents)
    WM20_Dilu = StringVar(OT)
    WM20_DiluMenu = OptionMenu(OT,WM20_Dilu,*Diluents)
    WM21_Dilu = StringVar(OT)
    WM21_DiluMenu = OptionMenu(OT,WM21_Dilu,*Diluents)
    WM22_Dilu = StringVar(OT)
    WM22_DiluMenu = OptionMenu(OT,WM22_Dilu,*Diluents)
    WM23_Dilu = StringVar(OT)
    WM23_DiluMenu = OptionMenu(OT,WM23_Dilu,*Diluents)
    WM24_Dilu = StringVar(OT)
    WM24_DiluMenu = OptionMenu(OT,WM24_Dilu,*Diluents)

    WN1_Vol = Entry()
    WN2_Vol = Entry()
    WN3_Vol = Entry()
    WN4_Vol = Entry()
    WN5_Vol = Entry()
    WN6_Vol = Entry()
    WN7_Vol = Entry()
    WN8_Vol = Entry()
    WN9_Vol = Entry()
    WN10_Vol = Entry()
    WN11_Vol = Entry()
    WN12_Vol = Entry()
    WN13_Vol = Entry()
    WN14_Vol = Entry()
    WN15_Vol = Entry()
    WN16_Vol = Entry()
    WN17_Vol = Entry()
    WN18_Vol = Entry()
    WN19_Vol = Entry()
    WN20_Vol = Entry()
    WN21_Vol = Entry()
    WN22_Vol = Entry()
    WN23_Vol = Entry()
    WN24_Vol = Entry()

    WN1_Solvent1_Conc = Entry()
    WN2_Solvent1_Conc = Entry()
    WN3_Solvent1_Conc = Entry()
    WN4_Solvent1_Conc = Entry()
    WN5_Solvent1_Conc = Entry()
    WN6_Solvent1_Conc = Entry()
    WN7_Solvent1_Conc = Entry()
    WN8_Solvent1_Conc = Entry()
    WN9_Solvent1_Conc = Entry()
    WN10_Solvent1_Conc = Entry()
    WN11_Solvent1_Conc = Entry()
    WN12_Solvent1_Conc = Entry()
    WN13_Solvent1_Conc = Entry()
    WN14_Solvent1_Conc = Entry()
    WN15_Solvent1_Conc = Entry()
    WN16_Solvent1_Conc = Entry()
    WN17_Solvent1_Conc = Entry()
    WN18_Solvent1_Conc = Entry()
    WN19_Solvent1_Conc = Entry()
    WN20_Solvent1_Conc = Entry()
    WN21_Solvent1_Conc = Entry()
    WN22_Solvent1_Conc = Entry()
    WN23_Solvent1_Conc = Entry()
    WN24_Solvent1_Conc = Entry()
    
    WN1_Solvent2_Conc = Entry()
    WN2_Solvent2_Conc = Entry()
    WN3_Solvent2_Conc = Entry()
    WN4_Solvent2_Conc = Entry()
    WN5_Solvent2_Conc = Entry()
    WN6_Solvent2_Conc = Entry()
    WN7_Solvent2_Conc = Entry()
    WN8_Solvent2_Conc = Entry()
    WN9_Solvent2_Conc = Entry()
    WN10_Solvent2_Conc = Entry()
    WN11_Solvent2_Conc = Entry()
    WN12_Solvent2_Conc = Entry()
    WN13_Solvent2_Conc = Entry()
    WN14_Solvent2_Conc = Entry()
    WN15_Solvent2_Conc = Entry()
    WN16_Solvent2_Conc = Entry()
    WN17_Solvent2_Conc = Entry()
    WN18_Solvent2_Conc = Entry()
    WN19_Solvent2_Conc = Entry()
    WN20_Solvent2_Conc = Entry()
    WN21_Solvent2_Conc = Entry()
    WN22_Solvent2_Conc = Entry()
    WN23_Solvent2_Conc = Entry()
    WN24_Solvent2_Conc = Entry()

    WN1_SS_Conc = Entry()
    WN2_SS_Conc = Entry()
    WN3_SS_Conc = Entry()
    WN4_SS_Conc = Entry()
    WN5_SS_Conc = Entry()
    WN6_SS_Conc = Entry()
    WN7_SS_Conc = Entry()
    WN8_SS_Conc = Entry()
    WN9_SS_Conc = Entry()
    WN10_SS_Conc = Entry()
    WN11_SS_Conc = Entry()
    WN12_SS_Conc = Entry()
    WN13_SS_Conc = Entry()
    WN14_SS_Conc = Entry()
    WN15_SS_Conc = Entry()
    WN16_SS_Conc = Entry()
    WN17_SS_Conc = Entry()
    WN18_SS_Conc = Entry()
    WN19_SS_Conc = Entry()
    WN20_SS_Conc = Entry()
    WN21_SS_Conc = Entry()
    WN22_SS_Conc = Entry()
    WN23_SS_Conc = Entry()
    WN24_SS_Conc = Entry()

    WN1_Ingr = StringVar(OT)
    WN1_IngrMenu = OptionMenu(OT,WN1_Ingr,*Ingrs)
    WN2_Ingr = StringVar(OT)
    WN2_IngrMenu = OptionMenu(OT,WN2_Ingr,*Ingrs)
    WN3_Ingr = StringVar(OT)
    WN3_IngrMenu = OptionMenu(OT,WN3_Ingr,*Ingrs)
    WN4_Ingr = StringVar(OT)
    WN4_IngrMenu = OptionMenu(OT,WN4_Ingr,*Ingrs)
    WN5_Ingr = StringVar(OT)
    WN5_IngrMenu = OptionMenu(OT,WN5_Ingr,*Ingrs)
    WN6_Ingr = StringVar(OT)
    WN6_IngrMenu = OptionMenu(OT,WN6_Ingr,*Ingrs)
    WN7_Ingr = StringVar(OT)
    WN7_IngrMenu = OptionMenu(OT,WN7_Ingr,*Ingrs)
    WN8_Ingr = StringVar(OT)
    WN8_IngrMenu = OptionMenu(OT,WN8_Ingr,*Ingrs)
    WN9_Ingr = StringVar(OT)
    WN9_IngrMenu = OptionMenu(OT,WN9_Ingr,*Ingrs)
    WN10_Ingr = StringVar(OT)
    WN10_IngrMenu = OptionMenu(OT,WN10_Ingr,*Ingrs)
    WN11_Ingr = StringVar(OT)
    WN11_IngrMenu = OptionMenu(OT,WN11_Ingr,*Ingrs)
    WN12_Ingr = StringVar(OT)
    WN12_IngrMenu = OptionMenu(OT,WN12_Ingr,*Ingrs)
    WN13_Ingr = StringVar(OT)
    WN13_IngrMenu = OptionMenu(OT,WN13_Ingr,*Ingrs)
    WN14_Ingr = StringVar(OT)
    WN14_IngrMenu = OptionMenu(OT,WN14_Ingr,*Ingrs)
    WN15_Ingr = StringVar(OT)
    WN15_IngrMenu = OptionMenu(OT,WN15_Ingr,*Ingrs)
    WN16_Ingr = StringVar(OT)
    WN16_IngrMenu = OptionMenu(OT,WN16_Ingr,*Ingrs)
    WN17_Ingr = StringVar(OT)
    WN17_IngrMenu = OptionMenu(OT,WN17_Ingr,*Ingrs)
    WN18_Ingr = StringVar(OT)
    WN18_IngrMenu = OptionMenu(OT,WN18_Ingr,*Ingrs)
    WN19_Ingr = StringVar(OT)
    WN19_IngrMenu = OptionMenu(OT,WN19_Ingr,*Ingrs)
    WN20_Ingr = StringVar(OT)
    WN20_IngrMenu = OptionMenu(OT,WN20_Ingr,*Ingrs)
    WN21_Ingr = StringVar(OT)
    WN21_IngrMenu = OptionMenu(OT,WN21_Ingr,*Ingrs)
    WN22_Ingr = StringVar(OT)
    WN22_IngrMenu = OptionMenu(OT,WN22_Ingr,*Ingrs)
    WN23_Ingr = StringVar(OT)
    WN23_IngrMenu = OptionMenu(OT,WN23_Ingr,*Ingrs)
    WN24_Ingr = StringVar(OT)
    WN24_IngrMenu = OptionMenu(OT,WN24_Ingr,*Ingrs)

    WN1_SS = StringVar(OT)
    WN1_SSMenu = OptionMenu(OT,WN1_SS,*SSInitiators)
    WN2_SS = StringVar(OT)
    WN2_SSMenu = OptionMenu(OT,WN2_SS,*SSInitiators)
    WN3_SS = StringVar(OT)
    WN3_SSMenu = OptionMenu(OT,WN3_SS,*SSInitiators)
    WN4_SS = StringVar(OT)
    WN4_SSMenu = OptionMenu(OT,WN4_SS,*SSInitiators)
    WN5_SS = StringVar(OT)
    WN5_SSMenu = OptionMenu(OT,WN5_SS,*SSInitiators)
    WN6_SS = StringVar(OT)
    WN6_SSMenu = OptionMenu(OT,WN6_SS,*SSInitiators)
    WN7_SS = StringVar(OT)
    WN7_SSMenu = OptionMenu(OT,WN7_SS,*SSInitiators)
    WN8_SS = StringVar(OT)
    WN8_SSMenu = OptionMenu(OT,WN8_SS,*SSInitiators)
    WN9_SS = StringVar(OT)
    WN9_SSMenu = OptionMenu(OT,WN9_SS,*SSInitiators)
    WN10_SS = StringVar(OT)
    WN10_SSMenu = OptionMenu(OT,WN10_SS,*SSInitiators)
    WN11_SS = StringVar(OT)
    WN11_SSMenu = OptionMenu(OT,WN11_SS,*SSInitiators)
    WN12_SS = StringVar(OT)
    WN12_SSMenu = OptionMenu(OT,WN12_SS,*SSInitiators)
    WN13_SS = StringVar(OT)
    WN13_SSMenu = OptionMenu(OT,WN13_SS,*SSInitiators)
    WN14_SS = StringVar(OT)
    WN14_SSMenu = OptionMenu(OT,WN14_SS,*SSInitiators)
    WN15_SS = StringVar(OT)
    WN15_SSMenu = OptionMenu(OT,WN15_SS,*SSInitiators)
    WN16_SS = StringVar(OT)
    WN16_SSMenu = OptionMenu(OT,WN16_SS,*SSInitiators)
    WN17_SS = StringVar(OT)
    WN17_SSMenu = OptionMenu(OT,WN17_SS,*SSInitiators)
    WN18_SS = StringVar(OT)
    WN18_SSMenu = OptionMenu(OT,WN18_SS,*SSInitiators)
    WN19_SS = StringVar(OT)
    WN19_SSMenu = OptionMenu(OT,WN19_SS,*SSInitiators)
    WN20_SS = StringVar(OT)
    WN20_SSMenu = OptionMenu(OT,WN20_SS,*SSInitiators)
    WN21_SS = StringVar(OT)
    WN21_SSMenu = OptionMenu(OT,WN21_SS,*SSInitiators)
    WN22_SS = StringVar(OT)
    WN22_SSMenu = OptionMenu(OT,WN22_SS,*SSInitiators)
    WN23_SS = StringVar(OT)
    WN23_SSMenu = OptionMenu(OT,WN23_SS,*SSInitiators)
    WN24_SS = StringVar(OT)
    WN24_SSMenu = OptionMenu(OT,WN24_SS,*SSInitiators)

    WN1_Dilu = StringVar(OT)
    WN1_DiluMenu = OptionMenu(OT,WN1_Dilu,*Diluents)
    WN2_Dilu = StringVar(OT)
    WN2_DiluMenu = OptionMenu(OT,WN2_Dilu,*Diluents)
    WN3_Dilu = StringVar(OT)
    WN3_DiluMenu = OptionMenu(OT,WN3_Dilu,*Diluents)
    WN4_Dilu = StringVar(OT)
    WN4_DiluMenu = OptionMenu(OT,WN4_Dilu,*Diluents)
    WN5_Dilu = StringVar(OT)
    WN5_DiluMenu = OptionMenu(OT,WN5_Dilu,*Diluents)
    WN6_Dilu = StringVar(OT)
    WN6_DiluMenu = OptionMenu(OT,WN6_Dilu,*Diluents)
    WN7_Dilu = StringVar(OT)
    WN7_DiluMenu = OptionMenu(OT,WN7_Dilu,*Diluents)
    WN8_Dilu = StringVar(OT)
    WN8_DiluMenu = OptionMenu(OT,WN8_Dilu,*Diluents)
    WN9_Dilu = StringVar(OT)
    WN9_DiluMenu = OptionMenu(OT,WN9_Dilu,*Diluents)
    WN10_Dilu = StringVar(OT)
    WN10_DiluMenu = OptionMenu(OT,WN10_Dilu,*Diluents)
    WN11_Dilu = StringVar(OT)
    WN11_DiluMenu = OptionMenu(OT,WN11_Dilu,*Diluents)
    WN12_Dilu = StringVar(OT)
    WN12_DiluMenu = OptionMenu(OT,WN12_Dilu,*Diluents)
    WN13_Dilu = StringVar(OT)
    WN13_DiluMenu = OptionMenu(OT,WN13_Dilu,*Diluents)
    WN14_Dilu = StringVar(OT)
    WN14_DiluMenu = OptionMenu(OT,WN14_Dilu,*Diluents)
    WN15_Dilu = StringVar(OT)
    WN15_DiluMenu = OptionMenu(OT,WN15_Dilu,*Diluents)
    WN16_Dilu = StringVar(OT)
    WN16_DiluMenu = OptionMenu(OT,WN16_Dilu,*Diluents)
    WN17_Dilu = StringVar(OT)
    WN17_DiluMenu = OptionMenu(OT,WN17_Dilu,*Diluents)
    WN18_Dilu = StringVar(OT)
    WN18_DiluMenu = OptionMenu(OT,WN18_Dilu,*Diluents)
    WN19_Dilu = StringVar(OT)
    WN19_DiluMenu = OptionMenu(OT,WN19_Dilu,*Diluents)
    WN20_Dilu = StringVar(OT)
    WN20_DiluMenu = OptionMenu(OT,WN20_Dilu,*Diluents)
    WN21_Dilu = StringVar(OT)
    WN21_DiluMenu = OptionMenu(OT,WN21_Dilu,*Diluents)
    WN22_Dilu = StringVar(OT)
    WN22_DiluMenu = OptionMenu(OT,WN22_Dilu,*Diluents)
    WN23_Dilu = StringVar(OT)
    WN23_DiluMenu = OptionMenu(OT,WN23_Dilu,*Diluents)
    WN24_Dilu = StringVar(OT)
    WN24_DiluMenu = OptionMenu(OT,WN24_Dilu,*Diluents)

    WO1_Vol = Entry()
    WO2_Vol = Entry()
    WO3_Vol = Entry()
    WO4_Vol = Entry()
    WO5_Vol = Entry()
    WO6_Vol = Entry()
    WO7_Vol = Entry()
    WO8_Vol = Entry()
    WO9_Vol = Entry()
    WO10_Vol = Entry()
    WO11_Vol = Entry()
    WO12_Vol = Entry()
    WO13_Vol = Entry()
    WO14_Vol = Entry()
    WO15_Vol = Entry()
    WO16_Vol = Entry()
    WO17_Vol = Entry()
    WO18_Vol = Entry()
    WO19_Vol = Entry()
    WO20_Vol = Entry()
    WO21_Vol = Entry()
    WO22_Vol = Entry()
    WO23_Vol = Entry()
    WO24_Vol = Entry()

    WO1_Solvent1_Conc = Entry()
    WO2_Solvent1_Conc = Entry()
    WO3_Solvent1_Conc = Entry()
    WO4_Solvent1_Conc = Entry()
    WO5_Solvent1_Conc = Entry()
    WO6_Solvent1_Conc = Entry()
    WO7_Solvent1_Conc = Entry()
    WO8_Solvent1_Conc = Entry()
    WO9_Solvent1_Conc = Entry()
    WO10_Solvent1_Conc = Entry()
    WO11_Solvent1_Conc = Entry()
    WO12_Solvent1_Conc = Entry()
    WO13_Solvent1_Conc = Entry()
    WO14_Solvent1_Conc = Entry()
    WO15_Solvent1_Conc = Entry()
    WO16_Solvent1_Conc = Entry()
    WO17_Solvent1_Conc = Entry()
    WO18_Solvent1_Conc = Entry()
    WO19_Solvent1_Conc = Entry()
    WO20_Solvent1_Conc = Entry()
    WO21_Solvent1_Conc = Entry()
    WO22_Solvent1_Conc = Entry()
    WO23_Solvent1_Conc = Entry()
    WO24_Solvent1_Conc = Entry()

    WO1_Solvent2_Conc = Entry()
    WO2_Solvent2_Conc = Entry()
    WO3_Solvent2_Conc = Entry()
    WO4_Solvent2_Conc = Entry()
    WO5_Solvent2_Conc = Entry()
    WO6_Solvent2_Conc = Entry()
    WO7_Solvent2_Conc = Entry()
    WO8_Solvent2_Conc = Entry()
    WO9_Solvent2_Conc = Entry()
    WO10_Solvent2_Conc = Entry()
    WO11_Solvent2_Conc = Entry()
    WO12_Solvent2_Conc = Entry()
    WO13_Solvent2_Conc = Entry()
    WO14_Solvent2_Conc = Entry()
    WO15_Solvent2_Conc = Entry()
    WO16_Solvent2_Conc = Entry()
    WO17_Solvent2_Conc = Entry()
    WO18_Solvent2_Conc = Entry()
    WO19_Solvent2_Conc = Entry()
    WO20_Solvent2_Conc = Entry()
    WO21_Solvent2_Conc = Entry()
    WO22_Solvent2_Conc = Entry()
    WO23_Solvent2_Conc = Entry()
    WO24_Solvent2_Conc = Entry()

    WO1_SS_Conc = Entry()
    WO2_SS_Conc = Entry()
    WO3_SS_Conc = Entry()
    WO4_SS_Conc = Entry()
    WO5_SS_Conc = Entry()
    WO6_SS_Conc = Entry()
    WO7_SS_Conc = Entry()
    WO8_SS_Conc = Entry()
    WO9_SS_Conc = Entry()
    WO10_SS_Conc = Entry()
    WO11_SS_Conc = Entry()
    WO12_SS_Conc = Entry()
    WO13_SS_Conc = Entry()
    WO14_SS_Conc = Entry()
    WO15_SS_Conc = Entry()
    WO16_SS_Conc = Entry()
    WO17_SS_Conc = Entry()
    WO18_SS_Conc = Entry()
    WO19_SS_Conc = Entry()
    WO20_SS_Conc = Entry()
    WO21_SS_Conc = Entry()
    WO22_SS_Conc = Entry()
    WO23_SS_Conc = Entry()
    WO24_SS_Conc = Entry()

    WO1_Ingr = StringVar(OT)
    WO1_IngrMenu = OptionMenu(OT,WO1_Ingr,*Ingrs)
    WO2_Ingr = StringVar(OT)
    WO2_IngrMenu = OptionMenu(OT,WO2_Ingr,*Ingrs)
    WO3_Ingr = StringVar(OT)
    WO3_IngrMenu = OptionMenu(OT,WO3_Ingr,*Ingrs)
    WO4_Ingr = StringVar(OT)
    WO4_IngrMenu = OptionMenu(OT,WO4_Ingr,*Ingrs)
    WO5_Ingr = StringVar(OT)
    WO5_IngrMenu = OptionMenu(OT,WO5_Ingr,*Ingrs)
    WO6_Ingr = StringVar(OT)
    WO6_IngrMenu = OptionMenu(OT,WO6_Ingr,*Ingrs)
    WO7_Ingr = StringVar(OT)
    WO7_IngrMenu = OptionMenu(OT,WO7_Ingr,*Ingrs)
    WO8_Ingr = StringVar(OT)
    WO8_IngrMenu = OptionMenu(OT,WO8_Ingr,*Ingrs)
    WO9_Ingr = StringVar(OT)
    WO9_IngrMenu = OptionMenu(OT,WO9_Ingr,*Ingrs)
    WO10_Ingr = StringVar(OT)
    WO10_IngrMenu = OptionMenu(OT,WO10_Ingr,*Ingrs)
    WO11_Ingr = StringVar(OT)
    WO11_IngrMenu = OptionMenu(OT,WO11_Ingr,*Ingrs)
    WO12_Ingr = StringVar(OT)
    WO12_IngrMenu = OptionMenu(OT,WO12_Ingr,*Ingrs)
    WO13_Ingr = StringVar(OT)
    WO13_IngrMenu = OptionMenu(OT,WO13_Ingr,*Ingrs)
    WO14_Ingr = StringVar(OT)
    WO14_IngrMenu = OptionMenu(OT,WO14_Ingr,*Ingrs)
    WO15_Ingr = StringVar(OT)
    WO15_IngrMenu = OptionMenu(OT,WO15_Ingr,*Ingrs)
    WO16_Ingr = StringVar(OT)
    WO16_IngrMenu = OptionMenu(OT,WO16_Ingr,*Ingrs)
    WO17_Ingr = StringVar(OT)
    WO17_IngrMenu = OptionMenu(OT,WO17_Ingr,*Ingrs)
    WO18_Ingr = StringVar(OT)
    WO18_IngrMenu = OptionMenu(OT,WO18_Ingr,*Ingrs)
    WO19_Ingr = StringVar(OT)
    WO19_IngrMenu = OptionMenu(OT,WO19_Ingr,*Ingrs)
    WO20_Ingr = StringVar(OT)
    WO20_IngrMenu = OptionMenu(OT,WO20_Ingr,*Ingrs)
    WO21_Ingr = StringVar(OT)
    WO21_IngrMenu = OptionMenu(OT,WO21_Ingr,*Ingrs)
    WO22_Ingr = StringVar(OT)
    WO22_IngrMenu = OptionMenu(OT,WO22_Ingr,*Ingrs)
    WO23_Ingr = StringVar(OT)
    WO23_IngrMenu = OptionMenu(OT,WO23_Ingr,*Ingrs)
    WO24_Ingr = StringVar(OT)
    WO24_IngrMenu = OptionMenu(OT,WO24_Ingr,*Ingrs)

    WO1_SS = StringVar(OT)
    WO1_SSMenu = OptionMenu(OT,WO1_SS,*SSInitiators)
    WO2_SS = StringVar(OT)
    WO2_SSMenu = OptionMenu(OT,WO2_SS,*SSInitiators)
    WO3_SS = StringVar(OT)
    WO3_SSMenu = OptionMenu(OT,WO3_SS,*SSInitiators)
    WO4_SS = StringVar(OT)
    WO4_SSMenu = OptionMenu(OT,WO4_SS,*SSInitiators)
    WO5_SS = StringVar(OT)
    WO5_SSMenu = OptionMenu(OT,WO5_SS,*SSInitiators)
    WO6_SS = StringVar(OT)
    WO6_SSMenu = OptionMenu(OT,WO6_SS,*SSInitiators)
    WO7_SS = StringVar(OT)
    WO7_SSMenu = OptionMenu(OT,WO7_SS,*SSInitiators)
    WO8_SS = StringVar(OT)
    WO8_SSMenu = OptionMenu(OT,WO8_SS,*SSInitiators)
    WO9_SS = StringVar(OT)
    WO9_SSMenu = OptionMenu(OT,WO9_SS,*SSInitiators)
    WO10_SS = StringVar(OT)
    WO10_SSMenu = OptionMenu(OT,WO10_SS,*SSInitiators)
    WO11_SS = StringVar(OT)
    WO11_SSMenu = OptionMenu(OT,WO11_SS,*SSInitiators)
    WO12_SS = StringVar(OT)
    WO12_SSMenu = OptionMenu(OT,WO12_SS,*SSInitiators)
    WO13_SS = StringVar(OT)
    WO13_SSMenu = OptionMenu(OT,WO13_SS,*SSInitiators)
    WO14_SS = StringVar(OT)
    WO14_SSMenu = OptionMenu(OT,WO14_SS,*SSInitiators)
    WO15_SS = StringVar(OT)
    WO15_SSMenu = OptionMenu(OT,WO15_SS,*SSInitiators)
    WO16_SS = StringVar(OT)
    WO16_SSMenu = OptionMenu(OT,WO16_SS,*SSInitiators)
    WO17_SS = StringVar(OT)
    WO17_SSMenu = OptionMenu(OT,WO17_SS,*SSInitiators)
    WO18_SS = StringVar(OT)
    WO18_SSMenu = OptionMenu(OT,WO18_SS,*SSInitiators)
    WO19_SS = StringVar(OT)
    WO19_SSMenu = OptionMenu(OT,WO19_SS,*SSInitiators)
    WO20_SS = StringVar(OT)
    WO20_SSMenu = OptionMenu(OT,WO20_SS,*SSInitiators)
    WO21_SS = StringVar(OT)
    WO21_SSMenu = OptionMenu(OT,WO21_SS,*SSInitiators)
    WO22_SS = StringVar(OT)
    WO22_SSMenu = OptionMenu(OT,WO22_SS,*SSInitiators)
    WO23_SS = StringVar(OT)
    WO23_SSMenu = OptionMenu(OT,WO23_SS,*SSInitiators)
    WO24_SS = StringVar(OT)
    WO24_SSMenu = OptionMenu(OT,WO24_SS,*SSInitiators)

    WO1_Dilu = StringVar(OT)
    WO1_DiluMenu = OptionMenu(OT,WO1_Dilu,*Diluents)
    WO2_Dilu = StringVar(OT)
    WO2_DiluMenu = OptionMenu(OT,WO2_Dilu,*Diluents)
    WO3_Dilu = StringVar(OT)
    WO3_DiluMenu = OptionMenu(OT,WO3_Dilu,*Diluents)
    WO4_Dilu = StringVar(OT)
    WO4_DiluMenu = OptionMenu(OT,WO4_Dilu,*Diluents)
    WO5_Dilu = StringVar(OT)
    WO5_DiluMenu = OptionMenu(OT,WO5_Dilu,*Diluents)
    WO6_Dilu = StringVar(OT)
    WO6_DiluMenu = OptionMenu(OT,WO6_Dilu,*Diluents)
    WO7_Dilu = StringVar(OT)
    WO7_DiluMenu = OptionMenu(OT,WO7_Dilu,*Diluents)
    WO8_Dilu = StringVar(OT)
    WO8_DiluMenu = OptionMenu(OT,WO8_Dilu,*Diluents)
    WO9_Dilu = StringVar(OT)
    WO9_DiluMenu = OptionMenu(OT,WO9_Dilu,*Diluents)
    WO10_Dilu = StringVar(OT)
    WO10_DiluMenu = OptionMenu(OT,WO10_Dilu,*Diluents)
    WO11_Dilu = StringVar(OT)
    WO11_DiluMenu = OptionMenu(OT,WO11_Dilu,*Diluents)
    WO12_Dilu = StringVar(OT)
    WO12_DiluMenu = OptionMenu(OT,WO12_Dilu,*Diluents)
    WO13_Dilu = StringVar(OT)
    WO13_DiluMenu = OptionMenu(OT,WO13_Dilu,*Diluents)
    WO14_Dilu = StringVar(OT)
    WO14_DiluMenu = OptionMenu(OT,WO14_Dilu,*Diluents)
    WO15_Dilu = StringVar(OT)
    WO15_DiluMenu = OptionMenu(OT,WO15_Dilu,*Diluents)
    WO16_Dilu = StringVar(OT)
    WO16_DiluMenu = OptionMenu(OT,WO16_Dilu,*Diluents)
    WO17_Dilu = StringVar(OT)
    WO17_DiluMenu = OptionMenu(OT,WO17_Dilu,*Diluents)
    WO18_Dilu = StringVar(OT)
    WO18_DiluMenu = OptionMenu(OT,WO18_Dilu,*Diluents)
    WO19_Dilu = StringVar(OT)
    WO19_DiluMenu = OptionMenu(OT,WO19_Dilu,*Diluents)
    WO20_Dilu = StringVar(OT)
    WO20_DiluMenu = OptionMenu(OT,WO20_Dilu,*Diluents)
    WO21_Dilu = StringVar(OT)
    WO21_DiluMenu = OptionMenu(OT,WO21_Dilu,*Diluents)
    WO22_Dilu = StringVar(OT)
    WO22_DiluMenu = OptionMenu(OT,WO22_Dilu,*Diluents)
    WO23_Dilu = StringVar(OT)
    WO23_DiluMenu = OptionMenu(OT,WO23_Dilu,*Diluents)
    WO24_Dilu = StringVar(OT)
    WO24_DiluMenu = OptionMenu(OT,WO24_Dilu,*Diluents)

    WP1_Vol = Entry()
    WP2_Vol = Entry()
    WP3_Vol = Entry()
    WP4_Vol = Entry()
    WP5_Vol = Entry()
    WP6_Vol = Entry()
    WP7_Vol = Entry()
    WP8_Vol = Entry()
    WP9_Vol = Entry()
    WP10_Vol = Entry()
    WP11_Vol = Entry()
    WP12_Vol = Entry()
    WP13_Vol = Entry()
    WP14_Vol = Entry()
    WP15_Vol = Entry()
    WP16_Vol = Entry()
    WP17_Vol = Entry()
    WP18_Vol = Entry()
    WP19_Vol = Entry()
    WP20_Vol = Entry()
    WP21_Vol = Entry()
    WP22_Vol = Entry()
    WP23_Vol = Entry()
    WP24_Vol = Entry()

    WP1_Solvent1_Conc = Entry()
    WP2_Solvent1_Conc = Entry()
    WP3_Solvent1_Conc = Entry()
    WP4_Solvent1_Conc = Entry()
    WP5_Solvent1_Conc = Entry()
    WP6_Solvent1_Conc = Entry()
    WP7_Solvent1_Conc = Entry()
    WP8_Solvent1_Conc = Entry()
    WP9_Solvent1_Conc = Entry()
    WP10_Solvent1_Conc = Entry()
    WP11_Solvent1_Conc = Entry()
    WP12_Solvent1_Conc = Entry()
    WP13_Solvent1_Conc = Entry()
    WP14_Solvent1_Conc = Entry()
    WP15_Solvent1_Conc = Entry()
    WP16_Solvent1_Conc = Entry()
    WP17_Solvent1_Conc = Entry()
    WP18_Solvent1_Conc = Entry()
    WP19_Solvent1_Conc = Entry()
    WP20_Solvent1_Conc = Entry()
    WP21_Solvent1_Conc = Entry()
    WP22_Solvent1_Conc = Entry()
    WP23_Solvent1_Conc = Entry()
    WP24_Solvent1_Conc = Entry()
    
    WP1_Solvent2_Conc = Entry()
    WP2_Solvent2_Conc = Entry()
    WP3_Solvent2_Conc = Entry()
    WP4_Solvent2_Conc = Entry()
    WP5_Solvent2_Conc = Entry()
    WP6_Solvent2_Conc = Entry()
    WP7_Solvent2_Conc = Entry()
    WP8_Solvent2_Conc = Entry()
    WP9_Solvent2_Conc = Entry()
    WP10_Solvent2_Conc = Entry()
    WP11_Solvent2_Conc = Entry()
    WP12_Solvent2_Conc = Entry()
    WP13_Solvent2_Conc = Entry()
    WP14_Solvent2_Conc = Entry()
    WP15_Solvent2_Conc = Entry()
    WP16_Solvent2_Conc = Entry()
    WP17_Solvent2_Conc = Entry()
    WP18_Solvent2_Conc = Entry()
    WP19_Solvent2_Conc = Entry()
    WP20_Solvent2_Conc = Entry()
    WP21_Solvent2_Conc = Entry()
    WP22_Solvent2_Conc = Entry()
    WP23_Solvent2_Conc = Entry()
    WP24_Solvent2_Conc = Entry()

    
    WP1_SS_Conc = Entry()
    WP2_SS_Conc = Entry()
    WP3_SS_Conc = Entry()
    WP4_SS_Conc = Entry()
    WP5_SS_Conc = Entry()
    WP6_SS_Conc = Entry()
    WP7_SS_Conc = Entry()
    WP8_SS_Conc = Entry()
    WP9_SS_Conc = Entry()
    WP10_SS_Conc = Entry()
    WP11_SS_Conc = Entry()
    WP12_SS_Conc = Entry()
    WP13_SS_Conc = Entry()
    WP14_SS_Conc = Entry()
    WP15_SS_Conc = Entry()
    WP16_SS_Conc = Entry()
    WP17_SS_Conc = Entry()
    WP18_SS_Conc = Entry()
    WP19_SS_Conc = Entry()
    WP20_SS_Conc = Entry()
    WP21_SS_Conc = Entry()
    WP22_SS_Conc = Entry()
    WP23_SS_Conc = Entry()
    WP24_SS_Conc = Entry()

    WP1_Ingr = StringVar(OT)
    WP1_IngrMenu = OptionMenu(OT,WP1_Ingr,*Ingrs)
    WP2_Ingr = StringVar(OT)
    WP2_IngrMenu = OptionMenu(OT,WP2_Ingr,*Ingrs)
    WP3_Ingr = StringVar(OT)
    WP3_IngrMenu = OptionMenu(OT,WP3_Ingr,*Ingrs)
    WP4_Ingr = StringVar(OT)
    WP4_IngrMenu = OptionMenu(OT,WP4_Ingr,*Ingrs)
    WP5_Ingr = StringVar(OT)
    WP5_IngrMenu = OptionMenu(OT,WP5_Ingr,*Ingrs)
    WP6_Ingr = StringVar(OT)
    WP6_IngrMenu = OptionMenu(OT,WP6_Ingr,*Ingrs)
    WP7_Ingr = StringVar(OT)
    WP7_IngrMenu = OptionMenu(OT,WP7_Ingr,*Ingrs)
    WP8_Ingr = StringVar(OT)
    WP8_IngrMenu = OptionMenu(OT,WP8_Ingr,*Ingrs)
    WP9_Ingr = StringVar(OT)
    WP9_IngrMenu = OptionMenu(OT,WP9_Ingr,*Ingrs)
    WP10_Ingr = StringVar(OT)
    WP10_IngrMenu = OptionMenu(OT,WP10_Ingr,*Ingrs)
    WP11_Ingr = StringVar(OT)
    WP11_IngrMenu = OptionMenu(OT,WP11_Ingr,*Ingrs)
    WP12_Ingr = StringVar(OT)
    WP12_IngrMenu = OptionMenu(OT,WP12_Ingr,*Ingrs)
    WP13_Ingr = StringVar(OT)
    WP13_IngrMenu = OptionMenu(OT,WP13_Ingr,*Ingrs)
    WP14_Ingr = StringVar(OT)
    WP14_IngrMenu = OptionMenu(OT,WP14_Ingr,*Ingrs)
    WP15_Ingr = StringVar(OT)
    WP15_IngrMenu = OptionMenu(OT,WP15_Ingr,*Ingrs)
    WP16_Ingr = StringVar(OT)
    WP16_IngrMenu = OptionMenu(OT,WP16_Ingr,*Ingrs)
    WP17_Ingr = StringVar(OT)
    WP17_IngrMenu = OptionMenu(OT,WP17_Ingr,*Ingrs)
    WP18_Ingr = StringVar(OT)
    WP18_IngrMenu = OptionMenu(OT,WP18_Ingr,*Ingrs)
    WP19_Ingr = StringVar(OT)
    WP19_IngrMenu = OptionMenu(OT,WP19_Ingr,*Ingrs)
    WP20_Ingr = StringVar(OT)
    WP20_IngrMenu = OptionMenu(OT,WP20_Ingr,*Ingrs)
    WP21_Ingr = StringVar(OT)
    WP21_IngrMenu = OptionMenu(OT,WP21_Ingr,*Ingrs)
    WP22_Ingr = StringVar(OT)
    WP22_IngrMenu = OptionMenu(OT,WP22_Ingr,*Ingrs)
    WP23_Ingr = StringVar(OT)
    WP23_IngrMenu = OptionMenu(OT,WP23_Ingr,*Ingrs)
    WP24_Ingr = StringVar(OT)
    WP24_IngrMenu = OptionMenu(OT,WP24_Ingr,*Ingrs)

    WP1_SS = StringVar(OT)
    WP1_SSMenu = OptionMenu(OT,WP1_SS,*SSInitiators)
    WP2_SS = StringVar(OT)
    WP2_SSMenu = OptionMenu(OT,WP2_SS,*SSInitiators)
    WP3_SS = StringVar(OT)
    WP3_SSMenu = OptionMenu(OT,WP3_SS,*SSInitiators)
    WP4_SS = StringVar(OT)
    WP4_SSMenu = OptionMenu(OT,WP4_SS,*SSInitiators)
    WP5_SS = StringVar(OT)
    WP5_SSMenu = OptionMenu(OT,WP5_SS,*SSInitiators)
    WP6_SS = StringVar(OT)
    WP6_SSMenu = OptionMenu(OT,WP6_SS,*SSInitiators)
    WP7_SS = StringVar(OT)
    WP7_SSMenu = OptionMenu(OT,WP7_SS,*SSInitiators)
    WP8_SS = StringVar(OT)
    WP8_SSMenu = OptionMenu(OT,WP8_SS,*SSInitiators)
    WP9_SS = StringVar(OT)
    WP9_SSMenu = OptionMenu(OT,WP9_SS,*SSInitiators)
    WP10_SS = StringVar(OT)
    WP10_SSMenu = OptionMenu(OT,WP10_SS,*SSInitiators)
    WP11_SS = StringVar(OT)
    WP11_SSMenu = OptionMenu(OT,WP11_SS,*SSInitiators)
    WP12_SS = StringVar(OT)
    WP12_SSMenu = OptionMenu(OT,WP12_SS,*SSInitiators)
    WP13_SS = StringVar(OT)
    WP13_SSMenu = OptionMenu(OT,WP13_SS,*SSInitiators)
    WP14_SS = StringVar(OT)
    WP14_SSMenu = OptionMenu(OT,WP14_SS,*SSInitiators)
    WP15_SS = StringVar(OT)
    WP15_SSMenu = OptionMenu(OT,WP15_SS,*SSInitiators)
    WP16_SS = StringVar(OT)
    WP16_SSMenu = OptionMenu(OT,WP16_SS,*SSInitiators)
    WP17_SS = StringVar(OT)
    WP17_SSMenu = OptionMenu(OT,WP17_SS,*SSInitiators)
    WP18_SS = StringVar(OT)
    WP18_SSMenu = OptionMenu(OT,WP18_SS,*SSInitiators)
    WP19_SS = StringVar(OT)
    WP19_SSMenu = OptionMenu(OT,WP19_SS,*SSInitiators)
    WP20_SS = StringVar(OT)
    WP20_SSMenu = OptionMenu(OT,WP20_SS,*SSInitiators)
    WP21_SS = StringVar(OT)
    WP21_SSMenu = OptionMenu(OT,WP21_SS,*SSInitiators)
    WP22_SS = StringVar(OT)
    WP22_SSMenu = OptionMenu(OT,WP22_SS,*SSInitiators)
    WP23_SS = StringVar(OT)
    WP23_SSMenu = OptionMenu(OT,WP23_SS,*SSInitiators)
    WP24_SS = StringVar(OT)
    WP24_SSMenu = OptionMenu(OT,WP24_SS,*SSInitiators)

    WP1_Dilu = StringVar(OT)
    WP1_DiluMenu = OptionMenu(OT,WP1_Dilu,*Diluents)
    WP2_Dilu = StringVar(OT)
    WP2_DiluMenu = OptionMenu(OT,WP2_Dilu,*Diluents)
    WP3_Dilu = StringVar(OT)
    WP3_DiluMenu = OptionMenu(OT,WP3_Dilu,*Diluents)
    WP4_Dilu = StringVar(OT)
    WP4_DiluMenu = OptionMenu(OT,WP4_Dilu,*Diluents)
    WP5_Dilu = StringVar(OT)
    WP5_DiluMenu = OptionMenu(OT,WP5_Dilu,*Diluents)
    WP6_Dilu = StringVar(OT)
    WP6_DiluMenu = OptionMenu(OT,WP6_Dilu,*Diluents)
    WP7_Dilu = StringVar(OT)
    WP7_DiluMenu = OptionMenu(OT,WP7_Dilu,*Diluents)
    WP8_Dilu = StringVar(OT)
    WP8_DiluMenu = OptionMenu(OT,WP8_Dilu,*Diluents)
    WP9_Dilu = StringVar(OT)
    WP9_DiluMenu = OptionMenu(OT,WP9_Dilu,*Diluents)
    WP10_Dilu = StringVar(OT)
    WP10_DiluMenu = OptionMenu(OT,WP10_Dilu,*Diluents)
    WP11_Dilu = StringVar(OT)
    WP11_DiluMenu = OptionMenu(OT,WP11_Dilu,*Diluents)
    WP12_Dilu = StringVar(OT)
    WP12_DiluMenu = OptionMenu(OT,WP12_Dilu,*Diluents)
    WP13_Dilu = StringVar(OT)
    WP13_DiluMenu = OptionMenu(OT,WP13_Dilu,*Diluents)
    WP14_Dilu = StringVar(OT)
    WP14_DiluMenu = OptionMenu(OT,WP14_Dilu,*Diluents)
    WP15_Dilu = StringVar(OT)
    WP15_DiluMenu = OptionMenu(OT,WP15_Dilu,*Diluents)
    WP16_Dilu = StringVar(OT)
    WP16_DiluMenu = OptionMenu(OT,WP16_Dilu,*Diluents)
    WP17_Dilu = StringVar(OT)
    WP17_DiluMenu = OptionMenu(OT,WP17_Dilu,*Diluents)
    WP18_Dilu = StringVar(OT)
    WP18_DiluMenu = OptionMenu(OT,WP18_Dilu,*Diluents)
    WP19_Dilu = StringVar(OT)
    WP19_DiluMenu = OptionMenu(OT,WP19_Dilu,*Diluents)
    WP20_Dilu = StringVar(OT)
    WP20_DiluMenu = OptionMenu(OT,WP20_Dilu,*Diluents)
    WP21_Dilu = StringVar(OT)
    WP21_DiluMenu = OptionMenu(OT,WP21_Dilu,*Diluents)
    WP22_Dilu = StringVar(OT)
    WP22_DiluMenu = OptionMenu(OT,WP22_Dilu,*Diluents)
    WP23_Dilu = StringVar(OT)
    WP23_DiluMenu = OptionMenu(OT,WP23_Dilu,*Diluents)
    WP24_Dilu = StringVar(OT)
    WP24_DiluMenu = OptionMenu(OT,WP24_Dilu,*Diluents)

    Inputs_List = [In_Out_Tray_Label,\
           Row1_Label, Row2_Label, Row3_Label, Row4_Label, Row5_Label, Row6_Label, Row7_Label, Row8_Label, Row9_Label,\
           Row10_Label, Row11_Label, Row12_Label, Row13_Label, Row14_Label, Row15_Label, Row16_Label, Row17_Label,\
           Row18_Label, Row19_Label, Row20_Label, Row21_Label, Row22_Label, Row23_Label, Row24_Label,\
           ColumnA_Label,ColumnB_Label,ColumnC_Label,ColumnD_Label,ColumnE_Label,ColumnF_Label, ColumnG_Label,\
           ColumnH_Label,ColumnI_Label,ColumnJ_Label,ColumnK_Label,ColumnL_Label,ColumnM_Label,ColumnN_Label,\
           ColumnO_Label,ColumnP_Label,\
           Row_Label,Column_Label,\
           Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
           Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
           Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,\
           Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,\
           Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
           Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,\
           Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,\
           Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
           Row1_SS_Conc_Label,Row2_SS_Conc_Label,Row3_SS_Conc_Label,Row4_SS_Conc_Label,Row5_SS_Conc_Label,Row6_SS_Conc_Label,\
           Row7_SS_Conc_Label,Row8_SS_Conc_Label,Row9_SS_Conc_Label,Row10_SS_Conc_Label,Row11_SS_Conc_Label,Row12_SS_Conc_Label,\
           Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
           Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
           Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
           Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
           Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
           Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
           WA1_Ingr, WA2_Ingr, WA3_Ingr, WA4_Ingr, WA5_Ingr, WA6_Ingr,\
           WA7_Ingr, WA8_Ingr, WA9_Ingr, WA10_Ingr, WA11_Ingr, WA12_Ingr,\
           WA13_Ingr, WA14_Ingr, WA15_Ingr, WA16_Ingr, WA17_Ingr, WA18_Ingr,\
           WA19_Ingr, WA20_Ingr, WA21_Ingr, WA22_Ingr, WA23_Ingr, WA24_Ingr,\
           WB1_Ingr, WB2_Ingr, WB3_Ingr, WB4_Ingr, WB5_Ingr, WB6_Ingr,\
           WB7_Ingr, WB8_Ingr, WB9_Ingr, WB10_Ingr, WB11_Ingr, WB12_Ingr,\
           WB13_Ingr, WB14_Ingr, WB15_Ingr, WB16_Ingr, WB17_Ingr, WB18_Ingr,\
           WB19_Ingr, WB20_Ingr, WB21_Ingr, WB22_Ingr, WB23_Ingr, WB24_Ingr,\
           WC1_Ingr, WC2_Ingr, WC3_Ingr, WC4_Ingr, WC5_Ingr, WC6_Ingr,\
           WC7_Ingr, WC8_Ingr, WC9_Ingr, WC10_Ingr, WC11_Ingr, WC12_Ingr,\
           WC13_Ingr, WC14_Ingr, WC15_Ingr, WC16_Ingr, WC17_Ingr, WC18_Ingr,\
           WC19_Ingr, WC20_Ingr, WC21_Ingr, WC22_Ingr, WC23_Ingr, WC24_Ingr,\
           WD1_Ingr, WD2_Ingr, WD3_Ingr, WD4_Ingr, WD5_Ingr, WD6_Ingr,\
           WD7_Ingr, WD8_Ingr, WD9_Ingr, WD10_Ingr, WD11_Ingr, WD12_Ingr,\
           WD13_Ingr, WD14_Ingr, WD15_Ingr, WD16_Ingr, WD17_Ingr, WD18_Ingr,\
           WD19_Ingr, WD20_Ingr, WD21_Ingr, WD22_Ingr, WD23_Ingr, WD24_Ingr,\
           WE1_Ingr, WE2_Ingr, WE3_Ingr, WE4_Ingr, WE5_Ingr, WE6_Ingr,\
           WE7_Ingr, WE8_Ingr, WE9_Ingr, WE10_Ingr, WE11_Ingr, WE12_Ingr,\
           WE13_Ingr, WE14_Ingr, WE15_Ingr, WE16_Ingr, WE17_Ingr, WE18_Ingr,\
           WE19_Ingr, WE20_Ingr, WE21_Ingr, WE22_Ingr, WE23_Ingr, WE24_Ingr,\
           WF1_Ingr, WF2_Ingr, WF3_Ingr, WF4_Ingr, WF5_Ingr, WF6_Ingr,\
           WF7_Ingr, WF8_Ingr, WF9_Ingr, WF10_Ingr, WF11_Ingr, WF12_Ingr,\
           WF13_Ingr, WF14_Ingr, WF15_Ingr, WF16_Ingr, WF17_Ingr, WF18_Ingr,\
           WF19_Ingr, WF20_Ingr, WF21_Ingr, WF22_Ingr, WF23_Ingr, WF24_Ingr,\
           WG1_Ingr, WG2_Ingr, WG3_Ingr, WG4_Ingr, WG5_Ingr, WG6_Ingr,\
           WG7_Ingr, WG8_Ingr, WG9_Ingr, WG10_Ingr, WG11_Ingr, WG12_Ingr,\
           WG13_Ingr, WG14_Ingr, WG15_Ingr, WG16_Ingr, WG17_Ingr, WG18_Ingr,\
           WG19_Ingr, WG20_Ingr, WG21_Ingr, WG22_Ingr, WG23_Ingr, WG24_Ingr,\
           WH1_Ingr, WH2_Ingr, WH3_Ingr, WH4_Ingr, WH5_Ingr, WH6_Ingr,\
           WH7_Ingr, WH8_Ingr, WH9_Ingr, WH10_Ingr, WH11_Ingr, WH12_Ingr,\
           WH13_Ingr, WH14_Ingr, WH15_Ingr, WH16_Ingr, WH17_Ingr, WH18_Ingr,\
           WH19_Ingr, WH20_Ingr, WH21_Ingr, WH22_Ingr, WH23_Ingr, WH24_Ingr,\
           WI1_Ingr, WI2_Ingr, WI3_Ingr, WI4_Ingr, WI5_Ingr, WI6_Ingr,\
           WI7_Ingr, WI8_Ingr, WI9_Ingr, WI10_Ingr, WI11_Ingr, WI12_Ingr,\
           WI13_Ingr, WI14_Ingr, WI15_Ingr, WI16_Ingr, WI17_Ingr, WI18_Ingr,\
           WI19_Ingr, WI20_Ingr, WI21_Ingr, WI22_Ingr, WI23_Ingr, WI24_Ingr,\
           WJ1_Ingr, WJ2_Ingr, WJ3_Ingr, WJ4_Ingr, WJ5_Ingr, WJ6_Ingr,\
           WJ7_Ingr, WJ8_Ingr, WJ9_Ingr, WJ10_Ingr, WJ11_Ingr, WJ12_Ingr,\
           WJ13_Ingr, WJ14_Ingr, WJ15_Ingr, WJ16_Ingr, WJ17_Ingr, WJ18_Ingr,\
           WJ19_Ingr, WJ20_Ingr, WJ21_Ingr, WJ22_Ingr, WJ23_Ingr, WJ24_Ingr,\
           WK1_Ingr, WK2_Ingr, WK3_Ingr, WK4_Ingr, WK5_Ingr, WK6_Ingr,\
           WK7_Ingr, WK8_Ingr, WK9_Ingr, WK10_Ingr, WK11_Ingr, WK12_Ingr,\
           WK13_Ingr, WK14_Ingr, WK15_Ingr, WK16_Ingr, WK17_Ingr, WK18_Ingr,\
           WK19_Ingr, WK20_Ingr, WK21_Ingr, WK22_Ingr, WK23_Ingr, WK24_Ingr,\
           WL1_Ingr, WL2_Ingr, WL3_Ingr, WL4_Ingr, WL5_Ingr, WL6_Ingr,\
           WL7_Ingr, WL8_Ingr, WL9_Ingr, WL10_Ingr, WL11_Ingr, WL12_Ingr,\
           WL13_Ingr, WL14_Ingr, WL15_Ingr, WL16_Ingr, WL17_Ingr, WL18_Ingr,\
           WL19_Ingr, WL20_Ingr, WL21_Ingr, WL22_Ingr, WL23_Ingr, WL24_Ingr,\
           WM1_Ingr, WM2_Ingr, WM3_Ingr, WM4_Ingr, WM5_Ingr, WM6_Ingr,\
           WM7_Ingr, WM8_Ingr, WM9_Ingr, WM10_Ingr, WM11_Ingr, WM12_Ingr,\
           WM13_Ingr, WM14_Ingr, WM15_Ingr, WM16_Ingr, WM17_Ingr, WM18_Ingr,\
           WM19_Ingr, WM20_Ingr, WM21_Ingr, WM22_Ingr, WM23_Ingr, WM24_Ingr,\
           WN1_Ingr, WN2_Ingr, WN3_Ingr, WN4_Ingr, WN5_Ingr, WN6_Ingr,\
           WN7_Ingr, WN8_Ingr, WN9_Ingr, WN10_Ingr, WN11_Ingr, WN12_Ingr,\
           WN13_Ingr, WN14_Ingr, WN15_Ingr, WN16_Ingr, WN17_Ingr, WN18_Ingr,\
           WN19_Ingr, WN20_Ingr, WN21_Ingr, WN22_Ingr, WN23_Ingr, WN24_Ingr,\
           WO1_Ingr, WO2_Ingr, WO3_Ingr, WO4_Ingr, WO5_Ingr, WO6_Ingr,\
           WO7_Ingr, WO8_Ingr, WO9_Ingr, WO10_Ingr, WO11_Ingr, WO12_Ingr,\
           WO13_Ingr, WO14_Ingr, WO15_Ingr, WO16_Ingr, WO17_Ingr, WO18_Ingr,\
           WO19_Ingr, WO20_Ingr, WO21_Ingr, WO22_Ingr, WO23_Ingr, WO24_Ingr,\
           WP1_Ingr, WP2_Ingr, WP3_Ingr, WP4_Ingr, WP5_Ingr, WP6_Ingr,\
           WP7_Ingr, WP8_Ingr, WP9_Ingr, WP10_Ingr, WP11_Ingr, WP12_Ingr,\
           WP13_Ingr, WP14_Ingr, WP15_Ingr, WP16_Ingr, WP17_Ingr, WP18_Ingr,\
           WP19_Ingr, WP20_Ingr, WP21_Ingr, WP22_Ingr, WP23_Ingr, WP24_Ingr,\
           WA1_Solvent1_Conc, WA2_Solvent1_Conc, WA3_Solvent1_Conc, WA4_Solvent1_Conc, WA5_Solvent1_Conc, WA6_Solvent1_Conc,\
           WA7_Solvent1_Conc, WA8_Solvent1_Conc, WA9_Solvent1_Conc, WA10_Solvent1_Conc, WA11_Solvent1_Conc, WA12_Solvent1_Conc,\
           WA13_Solvent1_Conc, WA14_Solvent1_Conc, WA15_Solvent1_Conc, WA16_Solvent1_Conc, WA17_Solvent1_Conc, WA18_Solvent1_Conc,\
           WA19_Solvent1_Conc, WA20_Solvent1_Conc, WA21_Solvent1_Conc, WA22_Solvent1_Conc, WA23_Solvent1_Conc, WA24_Solvent1_Conc,\
           WB1_Solvent1_Conc, WB2_Solvent1_Conc, WB3_Solvent1_Conc, WB4_Solvent1_Conc, WB5_Solvent1_Conc, WB6_Solvent1_Conc,\
           WB7_Solvent1_Conc, WB8_Solvent1_Conc, WB9_Solvent1_Conc, WB10_Solvent1_Conc, WB11_Solvent1_Conc, WB12_Solvent1_Conc,\
           WB13_Solvent1_Conc, WB14_Solvent1_Conc, WB15_Solvent1_Conc, WB16_Solvent1_Conc, WB17_Solvent1_Conc, WB18_Solvent1_Conc,\
           WB19_Solvent1_Conc, WB20_Solvent1_Conc, WB21_Solvent1_Conc, WB22_Solvent1_Conc, WB23_Solvent1_Conc, WB24_Solvent1_Conc,\
           WC1_Solvent1_Conc, WC2_Solvent1_Conc, WC3_Solvent1_Conc, WC4_Solvent1_Conc, WC5_Solvent1_Conc, WC6_Solvent1_Conc,\
           WC7_Solvent1_Conc, WC8_Solvent1_Conc, WC9_Solvent1_Conc, WC10_Solvent1_Conc, WC11_Solvent1_Conc, WC12_Solvent1_Conc,\
           WC13_Solvent1_Conc, WC14_Solvent1_Conc, WC15_Solvent1_Conc, WC16_Solvent1_Conc, WC17_Solvent1_Conc, WC18_Solvent1_Conc,\
           WC19_Solvent1_Conc, WC20_Solvent1_Conc, WC21_Solvent1_Conc, WC22_Solvent1_Conc, WC23_Solvent1_Conc, WC24_Solvent1_Conc,\
           WD1_Solvent1_Conc, WD2_Solvent1_Conc, WD3_Solvent1_Conc, WD4_Solvent1_Conc, WD5_Solvent1_Conc, WD6_Solvent1_Conc,\
           WD7_Solvent1_Conc, WD8_Solvent1_Conc, WD9_Solvent1_Conc, WD10_Solvent1_Conc, WD11_Solvent1_Conc, WD12_Solvent1_Conc,\
           WD13_Solvent1_Conc, WD14_Solvent1_Conc, WD15_Solvent1_Conc, WD16_Solvent1_Conc, WD17_Solvent1_Conc, WD18_Solvent1_Conc,\
           WD19_Solvent1_Conc, WD20_Solvent1_Conc, WD21_Solvent1_Conc, WD22_Solvent1_Conc, WD23_Solvent1_Conc, WD24_Solvent1_Conc,\
           WE1_Solvent1_Conc, WE2_Solvent1_Conc, WE3_Solvent1_Conc, WE4_Solvent1_Conc, WE5_Solvent1_Conc, WE6_Solvent1_Conc,\
           WE7_Solvent1_Conc, WE8_Solvent1_Conc, WE9_Solvent1_Conc, WE10_Solvent1_Conc, WE11_Solvent1_Conc, WE12_Solvent1_Conc,\
           WE13_Solvent1_Conc, WE14_Solvent1_Conc, WE15_Solvent1_Conc, WE16_Solvent1_Conc, WE17_Solvent1_Conc, WE18_Solvent1_Conc,\
           WE19_Solvent1_Conc, WE20_Solvent1_Conc, WE21_Solvent1_Conc, WE22_Solvent1_Conc, WE23_Solvent1_Conc, WE24_Solvent1_Conc,\
           WF1_Solvent1_Conc, WF2_Solvent1_Conc, WF3_Solvent1_Conc, WF4_Solvent1_Conc, WF5_Solvent1_Conc, WF6_Solvent1_Conc,\
           WF7_Solvent1_Conc, WF8_Solvent1_Conc, WF9_Solvent1_Conc, WF10_Solvent1_Conc, WF11_Solvent1_Conc, WF12_Solvent1_Conc,\
           WF13_Solvent1_Conc, WF14_Solvent1_Conc, WF15_Solvent1_Conc, WF16_Solvent1_Conc, WF17_Solvent1_Conc, WF18_Solvent1_Conc,\
           WF19_Solvent1_Conc, WF20_Solvent1_Conc, WF21_Solvent1_Conc, WF22_Solvent1_Conc, WF23_Solvent1_Conc, WF24_Solvent1_Conc,\
           WG1_Solvent1_Conc, WG2_Solvent1_Conc, WG3_Solvent1_Conc, WG4_Solvent1_Conc, WG5_Solvent1_Conc, WG6_Solvent1_Conc,\
           WG7_Solvent1_Conc, WG8_Solvent1_Conc, WG9_Solvent1_Conc, WG10_Solvent1_Conc, WG11_Solvent1_Conc, WG12_Solvent1_Conc,\
           WG13_Solvent1_Conc, WG14_Solvent1_Conc, WG15_Solvent1_Conc, WG16_Solvent1_Conc, WG17_Solvent1_Conc, WG18_Solvent1_Conc,\
           WG19_Solvent1_Conc, WG20_Solvent1_Conc, WG21_Solvent1_Conc, WG22_Solvent1_Conc, WG23_Solvent1_Conc, WG24_Solvent1_Conc,\
           WH1_Solvent1_Conc, WH2_Solvent1_Conc, WH3_Solvent1_Conc, WH4_Solvent1_Conc, WH5_Solvent1_Conc, WH6_Solvent1_Conc,\
           WH7_Solvent1_Conc, WH8_Solvent1_Conc, WH9_Solvent1_Conc, WH10_Solvent1_Conc, WH11_Solvent1_Conc, WH12_Solvent1_Conc,\
           WH13_Solvent1_Conc, WH14_Solvent1_Conc, WH15_Solvent1_Conc, WH16_Solvent1_Conc, WH17_Solvent1_Conc, WH18_Solvent1_Conc,\
           WH19_Solvent1_Conc, WH20_Solvent1_Conc, WH21_Solvent1_Conc, WH22_Solvent1_Conc, WH23_Solvent1_Conc, WH24_Solvent1_Conc,\
           WI1_Solvent1_Conc, WI2_Solvent1_Conc, WI3_Solvent1_Conc, WI4_Solvent1_Conc, WI5_Solvent1_Conc, WI6_Solvent1_Conc,\
           WI7_Solvent1_Conc, WI8_Solvent1_Conc, WI9_Solvent1_Conc, WI10_Solvent1_Conc, WI11_Solvent1_Conc, WI12_Solvent1_Conc,\
           WI13_Solvent1_Conc, WI14_Solvent1_Conc, WI15_Solvent1_Conc, WI16_Solvent1_Conc, WI17_Solvent1_Conc, WI18_Solvent1_Conc,\
           WI19_Solvent1_Conc, WI20_Solvent1_Conc, WI21_Solvent1_Conc, WI22_Solvent1_Conc, WI23_Solvent1_Conc, WI24_Solvent1_Conc,\
           WJ1_Solvent1_Conc, WJ2_Solvent1_Conc, WJ3_Solvent1_Conc, WJ4_Solvent1_Conc, WJ5_Solvent1_Conc, WJ6_Solvent1_Conc,\
           WJ7_Solvent1_Conc, WJ8_Solvent1_Conc, WJ9_Solvent1_Conc, WJ10_Solvent1_Conc, WJ11_Solvent1_Conc, WJ12_Solvent1_Conc,\
           WJ13_Solvent1_Conc, WJ14_Solvent1_Conc, WJ15_Solvent1_Conc, WJ16_Solvent1_Conc, WJ17_Solvent1_Conc, WJ18_Solvent1_Conc,\
           WJ19_Solvent1_Conc, WJ20_Solvent1_Conc, WJ21_Solvent1_Conc, WJ22_Solvent1_Conc, WJ23_Solvent1_Conc, WJ24_Solvent1_Conc,\
           WK1_Solvent1_Conc, WK2_Solvent1_Conc, WK3_Solvent1_Conc, WK4_Solvent1_Conc, WK5_Solvent1_Conc, WK6_Solvent1_Conc,\
           WK7_Solvent1_Conc, WK8_Solvent1_Conc, WK9_Solvent1_Conc, WK10_Solvent1_Conc, WK11_Solvent1_Conc, WK12_Solvent1_Conc,\
           WK13_Solvent1_Conc, WK14_Solvent1_Conc, WK15_Solvent1_Conc, WK16_Solvent1_Conc, WK17_Solvent1_Conc, WK18_Solvent1_Conc,\
           WK19_Solvent1_Conc, WK20_Solvent1_Conc, WK21_Solvent1_Conc, WK22_Solvent1_Conc, WK23_Solvent1_Conc, WK24_Solvent1_Conc,\
           WL1_Solvent1_Conc, WL2_Solvent1_Conc, WL3_Solvent1_Conc, WL4_Solvent1_Conc, WL5_Solvent1_Conc, WL6_Solvent1_Conc,\
           WL7_Solvent1_Conc, WL8_Solvent1_Conc, WL9_Solvent1_Conc, WL10_Solvent1_Conc, WL11_Solvent1_Conc, WL12_Solvent1_Conc,\
           WL13_Solvent1_Conc, WL14_Solvent1_Conc, WL15_Solvent1_Conc, WL16_Solvent1_Conc, WL17_Solvent1_Conc, WL18_Solvent1_Conc,\
           WL19_Solvent1_Conc, WL20_Solvent1_Conc, WL21_Solvent1_Conc, WL22_Solvent1_Conc, WL23_Solvent1_Conc, WL24_Solvent1_Conc,\
           WM1_Solvent1_Conc, WM2_Solvent1_Conc, WM3_Solvent1_Conc, WM4_Solvent1_Conc, WM5_Solvent1_Conc, WM6_Solvent1_Conc,\
           WM7_Solvent1_Conc, WM8_Solvent1_Conc, WM9_Solvent1_Conc, WM10_Solvent1_Conc, WM11_Solvent1_Conc, WM12_Solvent1_Conc,\
           WM13_Solvent1_Conc, WM14_Solvent1_Conc, WM15_Solvent1_Conc, WM16_Solvent1_Conc, WM17_Solvent1_Conc, WM18_Solvent1_Conc,\
           WM19_Solvent1_Conc, WM20_Solvent1_Conc, WM21_Solvent1_Conc, WM22_Solvent1_Conc, WM23_Solvent1_Conc, WM24_Solvent1_Conc,\
           WN1_Solvent1_Conc, WN2_Solvent1_Conc, WN3_Solvent1_Conc, WN4_Solvent1_Conc, WN5_Solvent1_Conc, WN6_Solvent1_Conc,\
           WN7_Solvent1_Conc, WN8_Solvent1_Conc, WN9_Solvent1_Conc, WN10_Solvent1_Conc, WN11_Solvent1_Conc, WN12_Solvent1_Conc,\
           WN13_Solvent1_Conc, WN14_Solvent1_Conc, WN15_Solvent1_Conc, WN16_Solvent1_Conc, WN17_Solvent1_Conc, WN18_Solvent1_Conc,\
           WN19_Solvent1_Conc, WN20_Solvent1_Conc, WN21_Solvent1_Conc, WN22_Solvent1_Conc, WN23_Solvent1_Conc, WN24_Solvent1_Conc,\
           WO1_Solvent1_Conc, WO2_Solvent1_Conc, WO3_Solvent1_Conc, WO4_Solvent1_Conc, WO5_Solvent1_Conc, WO6_Solvent1_Conc,\
           WO7_Solvent1_Conc, WO8_Solvent1_Conc, WO9_Solvent1_Conc, WO10_Solvent1_Conc, WO11_Solvent1_Conc, WO12_Solvent1_Conc,\
           WO13_Solvent1_Conc, WO14_Solvent1_Conc, WO15_Solvent1_Conc, WO16_Solvent1_Conc, WO17_Solvent1_Conc, WO18_Solvent1_Conc,\
           WO19_Solvent1_Conc, WO20_Solvent1_Conc, WO21_Solvent1_Conc, WO22_Solvent1_Conc, WO23_Solvent1_Conc, WO24_Solvent1_Conc,\
           WP1_Solvent1_Conc, WP2_Solvent1_Conc, WP3_Solvent1_Conc, WP4_Solvent1_Conc, WP5_Solvent1_Conc, WP6_Solvent1_Conc,\
           WP7_Solvent1_Conc, WP8_Solvent1_Conc, WP9_Solvent1_Conc, WP10_Solvent1_Conc, WP11_Solvent1_Conc, WP12_Solvent1_Conc,\
           WP13_Solvent1_Conc, WP14_Solvent1_Conc, WP15_Solvent1_Conc, WP16_Solvent1_Conc, WP17_Solvent1_Conc, WP18_Solvent1_Conc,\
           WP19_Solvent1_Conc, WP20_Solvent1_Conc, WP21_Solvent1_Conc, WP22_Solvent1_Conc, WP23_Solvent1_Conc, WP24_Solvent1_Conc,\
           WA1_Solvent2_Conc, WA2_Solvent2_Conc, WA3_Solvent2_Conc, WA4_Solvent2_Conc, WA5_Solvent2_Conc, WA6_Solvent2_Conc,\
           WA7_Solvent2_Conc, WA8_Solvent2_Conc, WA9_Solvent2_Conc, WA10_Solvent2_Conc, WA11_Solvent2_Conc, WA12_Solvent2_Conc,\
           WA13_Solvent2_Conc, WA14_Solvent2_Conc, WA15_Solvent2_Conc, WA16_Solvent2_Conc, WA17_Solvent2_Conc, WA18_Solvent2_Conc,\
           WA19_Solvent2_Conc, WA20_Solvent2_Conc, WA21_Solvent2_Conc, WA22_Solvent2_Conc, WA23_Solvent2_Conc, WA24_Solvent2_Conc,\
           WB1_Solvent2_Conc, WB2_Solvent2_Conc, WB3_Solvent2_Conc, WB4_Solvent2_Conc, WB5_Solvent2_Conc, WB6_Solvent2_Conc,\
           WB7_Solvent2_Conc, WB8_Solvent2_Conc, WB9_Solvent2_Conc, WB10_Solvent2_Conc, WB11_Solvent2_Conc, WB12_Solvent2_Conc,\
           WB13_Solvent2_Conc, WB14_Solvent2_Conc, WB15_Solvent2_Conc, WB16_Solvent2_Conc, WB17_Solvent2_Conc, WB18_Solvent2_Conc,\
           WB19_Solvent2_Conc, WB20_Solvent2_Conc, WB21_Solvent2_Conc, WB22_Solvent2_Conc, WB23_Solvent2_Conc, WB24_Solvent2_Conc,\
           WC1_Solvent2_Conc, WC2_Solvent2_Conc, WC3_Solvent2_Conc, WC4_Solvent2_Conc, WC5_Solvent2_Conc, WC6_Solvent2_Conc,\
           WC7_Solvent2_Conc, WC8_Solvent2_Conc, WC9_Solvent2_Conc, WC10_Solvent2_Conc, WC11_Solvent2_Conc, WC12_Solvent2_Conc,\
           WC13_Solvent2_Conc, WC14_Solvent2_Conc, WC15_Solvent2_Conc, WC16_Solvent2_Conc, WC17_Solvent2_Conc, WC18_Solvent2_Conc,\
           WC19_Solvent2_Conc, WC20_Solvent2_Conc, WC21_Solvent2_Conc, WC22_Solvent2_Conc, WC23_Solvent2_Conc, WC24_Solvent2_Conc,\
           WD1_Solvent2_Conc, WD2_Solvent2_Conc, WD3_Solvent2_Conc, WD4_Solvent2_Conc, WD5_Solvent2_Conc, WD6_Solvent2_Conc,\
           WD7_Solvent2_Conc, WD8_Solvent2_Conc, WD9_Solvent2_Conc, WD10_Solvent2_Conc, WD11_Solvent2_Conc, WD12_Solvent2_Conc,\
           WD13_Solvent2_Conc, WD14_Solvent2_Conc, WD15_Solvent2_Conc, WD16_Solvent2_Conc, WD17_Solvent2_Conc, WD18_Solvent2_Conc,\
           WD19_Solvent2_Conc, WD20_Solvent2_Conc, WD21_Solvent2_Conc, WD22_Solvent2_Conc, WD23_Solvent2_Conc, WD24_Solvent2_Conc,\
           WE1_Solvent2_Conc, WE2_Solvent2_Conc, WE3_Solvent2_Conc, WE4_Solvent2_Conc, WE5_Solvent2_Conc, WE6_Solvent2_Conc,\
           WE7_Solvent2_Conc, WE8_Solvent2_Conc, WE9_Solvent2_Conc, WE10_Solvent2_Conc, WE11_Solvent2_Conc, WE12_Solvent2_Conc,\
           WE13_Solvent2_Conc, WE14_Solvent2_Conc, WE15_Solvent2_Conc, WE16_Solvent2_Conc, WE17_Solvent2_Conc, WE18_Solvent2_Conc,\
           WE19_Solvent2_Conc, WE20_Solvent2_Conc, WE21_Solvent2_Conc, WE22_Solvent2_Conc, WE23_Solvent2_Conc, WE24_Solvent2_Conc,\
           WF1_Solvent2_Conc, WF2_Solvent2_Conc, WF3_Solvent2_Conc, WF4_Solvent2_Conc, WF5_Solvent2_Conc, WF6_Solvent2_Conc,\
           WF7_Solvent2_Conc, WF8_Solvent2_Conc, WF9_Solvent2_Conc, WF10_Solvent2_Conc, WF11_Solvent2_Conc, WF12_Solvent2_Conc,\
           WF13_Solvent2_Conc, WF14_Solvent2_Conc, WF15_Solvent2_Conc, WF16_Solvent2_Conc, WF17_Solvent2_Conc, WF18_Solvent2_Conc,\
           WF19_Solvent2_Conc, WF20_Solvent2_Conc, WF21_Solvent2_Conc, WF22_Solvent2_Conc, WF23_Solvent2_Conc, WF24_Solvent2_Conc,\
           WG1_Solvent2_Conc, WG2_Solvent2_Conc, WG3_Solvent2_Conc, WG4_Solvent2_Conc, WG5_Solvent2_Conc, WG6_Solvent2_Conc,\
           WG7_Solvent2_Conc, WG8_Solvent2_Conc, WG9_Solvent2_Conc, WG10_Solvent2_Conc, WG11_Solvent2_Conc, WG12_Solvent2_Conc,\
           WG13_Solvent2_Conc, WG14_Solvent2_Conc, WG15_Solvent2_Conc, WG16_Solvent2_Conc, WG17_Solvent2_Conc, WG18_Solvent2_Conc,\
           WG19_Solvent2_Conc, WG20_Solvent2_Conc, WG21_Solvent2_Conc, WG22_Solvent2_Conc, WG23_Solvent2_Conc, WG24_Solvent2_Conc,\
           WH1_Solvent2_Conc, WH2_Solvent2_Conc, WH3_Solvent2_Conc, WH4_Solvent2_Conc, WH5_Solvent2_Conc, WH6_Solvent2_Conc,\
           WH7_Solvent2_Conc, WH8_Solvent2_Conc, WH9_Solvent2_Conc, WH10_Solvent2_Conc, WH11_Solvent2_Conc, WH12_Solvent2_Conc,\
           WH13_Solvent2_Conc, WH14_Solvent2_Conc, WH15_Solvent2_Conc, WH16_Solvent2_Conc, WH17_Solvent2_Conc, WH18_Solvent2_Conc,\
           WH19_Solvent2_Conc, WH20_Solvent2_Conc, WH21_Solvent2_Conc, WH22_Solvent2_Conc, WH23_Solvent2_Conc, WH24_Solvent2_Conc,\
           WI1_Solvent2_Conc, WI2_Solvent2_Conc, WI3_Solvent2_Conc, WI4_Solvent2_Conc, WI5_Solvent2_Conc, WI6_Solvent2_Conc,\
           WI7_Solvent2_Conc, WI8_Solvent2_Conc, WI9_Solvent2_Conc, WI10_Solvent2_Conc, WI11_Solvent2_Conc, WI12_Solvent2_Conc,\
           WI13_Solvent2_Conc, WI14_Solvent2_Conc, WI15_Solvent2_Conc, WI16_Solvent2_Conc, WI17_Solvent2_Conc, WI18_Solvent2_Conc,\
           WI19_Solvent2_Conc, WI20_Solvent2_Conc, WI21_Solvent2_Conc, WI22_Solvent2_Conc, WI23_Solvent2_Conc, WI24_Solvent2_Conc,\
           WJ1_Solvent2_Conc, WJ2_Solvent2_Conc, WJ3_Solvent2_Conc, WJ4_Solvent2_Conc, WJ5_Solvent2_Conc, WJ6_Solvent2_Conc,\
           WJ7_Solvent2_Conc, WJ8_Solvent2_Conc, WJ9_Solvent2_Conc, WJ10_Solvent2_Conc, WJ11_Solvent2_Conc, WJ12_Solvent2_Conc,\
           WJ13_Solvent2_Conc, WJ14_Solvent2_Conc, WJ15_Solvent2_Conc, WJ16_Solvent2_Conc, WJ17_Solvent2_Conc, WJ18_Solvent2_Conc,\
           WJ19_Solvent2_Conc, WJ20_Solvent2_Conc, WJ21_Solvent2_Conc, WJ22_Solvent2_Conc, WJ23_Solvent2_Conc, WJ24_Solvent2_Conc,\
           WK1_Solvent2_Conc, WK2_Solvent2_Conc, WK3_Solvent2_Conc, WK4_Solvent2_Conc, WK5_Solvent2_Conc, WK6_Solvent2_Conc,\
           WK7_Solvent2_Conc, WK8_Solvent2_Conc, WK9_Solvent2_Conc, WK10_Solvent2_Conc, WK11_Solvent2_Conc, WK12_Solvent2_Conc,\
           WK13_Solvent2_Conc, WK14_Solvent2_Conc, WK15_Solvent2_Conc, WK16_Solvent2_Conc, WK17_Solvent2_Conc, WK18_Solvent2_Conc,\
           WK19_Solvent2_Conc, WK20_Solvent2_Conc, WK21_Solvent2_Conc, WK22_Solvent2_Conc, WK23_Solvent2_Conc, WK24_Solvent2_Conc,\
           WL1_Solvent2_Conc, WL2_Solvent2_Conc, WL3_Solvent2_Conc, WL4_Solvent2_Conc, WL5_Solvent2_Conc, WL6_Solvent2_Conc,\
           WL7_Solvent2_Conc, WL8_Solvent2_Conc, WL9_Solvent2_Conc, WL10_Solvent2_Conc, WL11_Solvent2_Conc, WL12_Solvent2_Conc,\
           WL13_Solvent2_Conc, WL14_Solvent2_Conc, WL15_Solvent2_Conc, WL16_Solvent2_Conc, WL17_Solvent2_Conc, WL18_Solvent2_Conc,\
           WL19_Solvent2_Conc, WL20_Solvent2_Conc, WL21_Solvent2_Conc, WL22_Solvent2_Conc, WL23_Solvent2_Conc, WL24_Solvent2_Conc,\
           WM1_Solvent2_Conc, WM2_Solvent2_Conc, WM3_Solvent2_Conc, WM4_Solvent2_Conc, WM5_Solvent2_Conc, WM6_Solvent2_Conc,\
           WM7_Solvent2_Conc, WM8_Solvent2_Conc, WM9_Solvent2_Conc, WM10_Solvent2_Conc, WM11_Solvent2_Conc, WM12_Solvent2_Conc,\
           WM13_Solvent2_Conc, WM14_Solvent2_Conc, WM15_Solvent2_Conc, WM16_Solvent2_Conc, WM17_Solvent2_Conc, WM18_Solvent2_Conc,\
           WM19_Solvent2_Conc, WM20_Solvent2_Conc, WM21_Solvent2_Conc, WM22_Solvent2_Conc, WM23_Solvent2_Conc, WM24_Solvent2_Conc,\
           WN1_Solvent2_Conc, WN2_Solvent2_Conc, WN3_Solvent2_Conc, WN4_Solvent2_Conc, WN5_Solvent2_Conc, WN6_Solvent2_Conc,\
           WN7_Solvent2_Conc, WN8_Solvent2_Conc, WN9_Solvent2_Conc, WN10_Solvent2_Conc, WN11_Solvent2_Conc, WN12_Solvent2_Conc,\
           WN13_Solvent2_Conc, WN14_Solvent2_Conc, WN15_Solvent2_Conc, WN16_Solvent2_Conc, WN17_Solvent2_Conc, WN18_Solvent2_Conc,\
           WN19_Solvent2_Conc, WN20_Solvent2_Conc, WN21_Solvent2_Conc, WN22_Solvent2_Conc, WN23_Solvent2_Conc, WN24_Solvent2_Conc,\
           WO1_Solvent2_Conc, WO2_Solvent2_Conc, WO3_Solvent2_Conc, WO4_Solvent2_Conc, WO5_Solvent2_Conc, WO6_Solvent2_Conc,\
           WO7_Solvent2_Conc, WO8_Solvent2_Conc, WO9_Solvent2_Conc, WO10_Solvent2_Conc, WO11_Solvent2_Conc, WO12_Solvent2_Conc,\
           WO13_Solvent2_Conc, WO14_Solvent2_Conc, WO15_Solvent2_Conc, WO16_Solvent2_Conc, WO17_Solvent2_Conc, WO18_Solvent2_Conc,\
           WO19_Solvent2_Conc, WO20_Solvent2_Conc, WO21_Solvent2_Conc, WO22_Solvent2_Conc, WO23_Solvent2_Conc, WO24_Solvent2_Conc,\
           WP1_Solvent2_Conc, WP2_Solvent2_Conc, WP3_Solvent2_Conc, WP4_Solvent2_Conc, WP5_Solvent2_Conc, WP6_Solvent2_Conc,\
           WP7_Solvent2_Conc, WP8_Solvent2_Conc, WP9_Solvent2_Conc, WP10_Solvent2_Conc, WP11_Solvent2_Conc, WP12_Solvent2_Conc,\
           WP13_Solvent2_Conc, WP14_Solvent2_Conc, WP15_Solvent2_Conc, WP16_Solvent2_Conc, WP17_Solvent2_Conc, WP18_Solvent2_Conc,\
           WP19_Solvent2_Conc, WP20_Solvent2_Conc, WP21_Solvent2_Conc, WP22_Solvent2_Conc, WP23_Solvent2_Conc, WP24_Solvent2_Conc,\
           WA1_SS_Conc, WA2_SS_Conc, WA3_SS_Conc, WA4_SS_Conc, WA5_SS_Conc, WA6_SS_Conc,\
           WA7_SS_Conc, WA8_SS_Conc, WA9_SS_Conc, WA10_SS_Conc, WA11_SS_Conc, WA12_SS_Conc,\
           WA13_SS_Conc, WA14_SS_Conc, WA15_SS_Conc, WA16_SS_Conc, WA17_SS_Conc, WA18_SS_Conc,\
           WA19_SS_Conc, WA20_SS_Conc, WA21_SS_Conc, WA22_SS_Conc, WA23_SS_Conc, WA24_SS_Conc,\
           WB1_SS_Conc, WB2_SS_Conc, WB3_SS_Conc, WB4_SS_Conc, WB5_SS_Conc, WB6_SS_Conc,\
           WB7_SS_Conc, WB8_SS_Conc, WB9_SS_Conc, WB10_SS_Conc, WB11_SS_Conc, WB12_SS_Conc,\
           WB13_SS_Conc, WB14_SS_Conc, WB15_SS_Conc, WB16_SS_Conc, WB17_SS_Conc, WB18_SS_Conc,\
           WB19_SS_Conc, WB20_SS_Conc, WB21_SS_Conc, WB22_SS_Conc, WB23_SS_Conc, WB24_SS_Conc,\
           WC1_SS_Conc, WC2_SS_Conc, WC3_SS_Conc, WC4_SS_Conc, WC5_SS_Conc, WC6_SS_Conc,\
           WC7_SS_Conc, WC8_SS_Conc, WC9_SS_Conc, WC10_SS_Conc, WC11_SS_Conc, WC12_SS_Conc,\
           WC13_SS_Conc, WC14_SS_Conc, WC15_SS_Conc, WC16_SS_Conc, WC17_SS_Conc, WC18_SS_Conc,\
           WC19_SS_Conc, WC20_SS_Conc, WC21_SS_Conc, WC22_SS_Conc, WC23_SS_Conc, WC24_SS_Conc,\
           WD1_SS_Conc, WD2_SS_Conc, WD3_SS_Conc, WD4_SS_Conc, WD5_SS_Conc, WD6_SS_Conc,\
           WD7_SS_Conc, WD8_SS_Conc, WD9_SS_Conc, WD10_SS_Conc, WD11_SS_Conc, WD12_SS_Conc,\
           WD13_SS_Conc, WD14_SS_Conc, WD15_SS_Conc, WD16_SS_Conc, WD17_SS_Conc, WD18_SS_Conc,\
           WD19_SS_Conc, WD20_SS_Conc, WD21_SS_Conc, WD22_SS_Conc, WD23_SS_Conc, WD24_SS_Conc,\
           WE1_SS_Conc, WE2_SS_Conc, WE3_SS_Conc, WE4_SS_Conc, WE5_SS_Conc, WE6_SS_Conc,\
           WE7_SS_Conc, WE8_SS_Conc, WE9_SS_Conc, WE10_SS_Conc, WE11_SS_Conc, WE12_SS_Conc,\
           WE13_SS_Conc, WE14_SS_Conc, WE15_SS_Conc, WE16_SS_Conc, WE17_SS_Conc, WE18_SS_Conc,\
           WE19_SS_Conc, WE20_SS_Conc, WE21_SS_Conc, WE22_SS_Conc, WE23_SS_Conc, WE24_SS_Conc,\
           WF1_SS_Conc, WF2_SS_Conc, WF3_SS_Conc, WF4_SS_Conc, WF5_SS_Conc, WF6_SS_Conc,\
           WF7_SS_Conc, WF8_SS_Conc, WF9_SS_Conc, WF10_SS_Conc, WF11_SS_Conc, WF12_SS_Conc,\
           WF13_SS_Conc, WF14_SS_Conc, WF15_SS_Conc, WF16_SS_Conc, WF17_SS_Conc, WF18_SS_Conc,\
           WF19_SS_Conc, WF20_SS_Conc, WF21_SS_Conc, WF22_SS_Conc, WF23_SS_Conc, WF24_SS_Conc,\
           WG1_SS_Conc, WG2_SS_Conc, WG3_SS_Conc, WG4_SS_Conc, WG5_SS_Conc, WG6_SS_Conc,\
           WG7_SS_Conc, WG8_SS_Conc, WG9_SS_Conc, WG10_SS_Conc, WG11_SS_Conc, WG12_SS_Conc,\
           WG13_SS_Conc, WG14_SS_Conc, WG15_SS_Conc, WG16_SS_Conc, WG17_SS_Conc, WG18_SS_Conc,\
           WG19_SS_Conc, WG20_SS_Conc, WG21_SS_Conc, WG22_SS_Conc, WG23_SS_Conc, WG24_SS_Conc,\
           WH1_SS_Conc, WH2_SS_Conc, WH3_SS_Conc, WH4_SS_Conc, WH5_SS_Conc, WH6_SS_Conc,\
           WH7_SS_Conc, WH8_SS_Conc, WH9_SS_Conc, WH10_SS_Conc, WH11_SS_Conc, WH12_SS_Conc,\
           WH13_SS_Conc, WH14_SS_Conc, WH15_SS_Conc, WH16_SS_Conc, WH17_SS_Conc, WH18_SS_Conc,\
           WH19_SS_Conc, WH20_SS_Conc, WH21_SS_Conc, WH22_SS_Conc, WH23_SS_Conc, WH24_SS_Conc,\
           WI1_SS_Conc, WI2_SS_Conc, WI3_SS_Conc, WI4_SS_Conc, WI5_SS_Conc, WI6_SS_Conc,\
           WI7_SS_Conc, WI8_SS_Conc, WI9_SS_Conc, WI10_SS_Conc, WI11_SS_Conc, WI12_SS_Conc,\
           WI13_SS_Conc, WI14_SS_Conc, WI15_SS_Conc, WI16_SS_Conc, WI17_SS_Conc, WI18_SS_Conc,\
           WI19_SS_Conc, WI20_SS_Conc, WI21_SS_Conc, WI22_SS_Conc, WI23_SS_Conc, WI24_SS_Conc,\
           WJ1_SS_Conc, WJ2_SS_Conc, WJ3_SS_Conc, WJ4_SS_Conc, WJ5_SS_Conc, WJ6_SS_Conc,\
           WJ7_SS_Conc, WJ8_SS_Conc, WJ9_SS_Conc, WJ10_SS_Conc, WJ11_SS_Conc, WJ12_SS_Conc,\
           WJ13_SS_Conc, WJ14_SS_Conc, WJ15_SS_Conc, WJ16_SS_Conc, WJ17_SS_Conc, WJ18_SS_Conc,\
           WJ19_SS_Conc, WJ20_SS_Conc, WJ21_SS_Conc, WJ22_SS_Conc, WJ23_SS_Conc, WJ24_SS_Conc,\
           WK1_SS_Conc, WK2_SS_Conc, WK3_SS_Conc, WK4_SS_Conc, WK5_SS_Conc, WK6_SS_Conc,\
           WK7_SS_Conc, WK8_SS_Conc, WK9_SS_Conc, WK10_SS_Conc, WK11_SS_Conc, WK12_SS_Conc,\
           WK13_SS_Conc, WK14_SS_Conc, WK15_SS_Conc, WK16_SS_Conc, WK17_SS_Conc, WK18_SS_Conc,\
           WK19_SS_Conc, WK20_SS_Conc, WK21_SS_Conc, WK22_SS_Conc, WK23_SS_Conc, WK24_SS_Conc,\
           WL1_SS_Conc, WL2_SS_Conc, WL3_SS_Conc, WL4_SS_Conc, WL5_SS_Conc, WL6_SS_Conc,\
           WL7_SS_Conc, WL8_SS_Conc, WL9_SS_Conc, WL10_SS_Conc, WL11_SS_Conc, WL12_SS_Conc,\
           WL13_SS_Conc, WL14_SS_Conc, WL15_SS_Conc, WL16_SS_Conc, WL17_SS_Conc, WL18_SS_Conc,\
           WL19_SS_Conc, WL20_SS_Conc, WL21_SS_Conc, WL22_SS_Conc, WL23_SS_Conc, WL24_SS_Conc,\
           WM1_SS_Conc, WM2_SS_Conc, WM3_SS_Conc, WM4_SS_Conc, WM5_SS_Conc, WM6_SS_Conc,\
           WM7_SS_Conc, WM8_SS_Conc, WM9_SS_Conc, WM10_SS_Conc, WM11_SS_Conc, WM12_SS_Conc,\
           WM13_SS_Conc, WM14_SS_Conc, WM15_SS_Conc, WM16_SS_Conc, WM17_SS_Conc, WM18_SS_Conc,\
           WM19_SS_Conc, WM20_SS_Conc, WM21_SS_Conc, WM22_SS_Conc, WM23_SS_Conc, WM24_SS_Conc,\
           WN1_SS_Conc, WN2_SS_Conc, WN3_SS_Conc, WN4_SS_Conc, WN5_SS_Conc, WN6_SS_Conc,\
           WN7_SS_Conc, WN8_SS_Conc, WN9_SS_Conc, WN10_SS_Conc, WN11_SS_Conc, WN12_SS_Conc,\
           WN13_SS_Conc, WN14_SS_Conc, WN15_SS_Conc, WN16_SS_Conc, WN17_SS_Conc, WN18_SS_Conc,\
           WN19_SS_Conc, WN20_SS_Conc, WN21_SS_Conc, WN22_SS_Conc, WN23_SS_Conc, WN24_SS_Conc,\
           WO1_SS_Conc, WO2_SS_Conc, WO3_SS_Conc, WO4_SS_Conc, WO5_SS_Conc, WO6_SS_Conc,\
           WO7_SS_Conc, WO8_SS_Conc, WO9_SS_Conc, WO10_SS_Conc, WO11_SS_Conc, WO12_SS_Conc,\
           WO13_SS_Conc, WO14_SS_Conc, WO15_SS_Conc, WO16_SS_Conc, WO17_SS_Conc, WO18_SS_Conc,\
           WO19_SS_Conc, WO20_SS_Conc, WO21_SS_Conc, WO22_SS_Conc, WO23_SS_Conc, WO24_SS_Conc,\
           WP1_SS_Conc, WP2_SS_Conc, WP3_SS_Conc, WP4_SS_Conc, WP5_SS_Conc, WP6_SS_Conc,\
           WP7_SS_Conc, WP8_SS_Conc, WP9_SS_Conc, WP10_SS_Conc, WP11_SS_Conc, WP12_SS_Conc,\
           WP13_SS_Conc, WP14_SS_Conc, WP15_SS_Conc, WP16_SS_Conc, WP17_SS_Conc, WP18_SS_Conc,\
           WP19_SS_Conc, WP20_SS_Conc, WP21_SS_Conc, WP22_SS_Conc, WP23_SS_Conc, WP24_SS_Conc,\
           WA1_Vol, WA2_Vol, WA3_Vol, WA4_Vol, WA5_Vol, WA6_Vol,\
           WA7_Vol, WA8_Vol, WA9_Vol, WA10_Vol, WA11_Vol, WA12_Vol,\
           WA13_Vol, WA14_Vol, WA15_Vol, WA16_Vol, WA17_Vol, WA18_Vol,\
           WA19_Vol, WA20_Vol, WA21_Vol, WA22_Vol, WA23_Vol, WA24_Vol,\
           WB1_Vol, WB2_Vol, WB3_Vol, WB4_Vol, WB5_Vol, WB6_Vol,\
           WB7_Vol, WB8_Vol, WB9_Vol, WB10_Vol, WB11_Vol, WB12_Vol,\
           WB13_Vol, WB14_Vol, WB15_Vol, WB16_Vol, WB17_Vol, WB18_Vol,\
           WB19_Vol, WB20_Vol, WB21_Vol, WB22_Vol, WB23_Vol, WB24_Vol,\
           WC1_Vol, WC2_Vol, WC3_Vol, WC4_Vol, WC5_Vol, WC6_Vol,\
           WC7_Vol, WC8_Vol, WC9_Vol, WC10_Vol, WC11_Vol, WC12_Vol,\
           WC13_Vol, WC14_Vol, WC15_Vol, WC16_Vol, WC17_Vol, WC18_Vol,\
           WC19_Vol, WC20_Vol, WC21_Vol, WC22_Vol, WC23_Vol, WC24_Vol,\
           WD1_Vol, WD2_Vol, WD3_Vol, WD4_Vol, WD5_Vol, WD6_Vol,\
           WD7_Vol, WD8_Vol, WD9_Vol, WD10_Vol, WD11_Vol, WD12_Vol,\
           WD13_Vol, WD14_Vol, WD15_Vol, WD16_Vol, WD17_Vol, WD18_Vol,\
           WD19_Vol, WD20_Vol, WD21_Vol, WD22_Vol, WD23_Vol, WD24_Vol,\
           WE1_Vol, WE2_Vol, WE3_Vol, WE4_Vol, WE5_Vol, WE6_Vol,\
           WE7_Vol, WE8_Vol, WE9_Vol, WE10_Vol, WE11_Vol, WE12_Vol,\
           WE13_Vol, WE14_Vol, WE15_Vol, WE16_Vol, WE17_Vol, WE18_Vol,\
           WE19_Vol, WE20_Vol, WE21_Vol, WE22_Vol, WE23_Vol, WE24_Vol,\
           WF1_Vol, WF2_Vol, WF3_Vol, WF4_Vol, WF5_Vol, WF6_Vol,\
           WF7_Vol, WF8_Vol, WF9_Vol, WF10_Vol, WF11_Vol, WF12_Vol,\
           WF13_Vol, WF14_Vol, WF15_Vol, WF16_Vol, WF17_Vol, WF18_Vol,\
           WF19_Vol, WF20_Vol, WF21_Vol, WF22_Vol, WF23_Vol, WF24_Vol,\
           WG1_Vol, WG2_Vol, WG3_Vol, WG4_Vol, WG5_Vol, WG6_Vol,\
           WG7_Vol, WG8_Vol, WG9_Vol, WG10_Vol, WG11_Vol, WG12_Vol,\
           WG13_Vol, WG14_Vol, WG15_Vol, WG16_Vol, WG17_Vol, WG18_Vol,\
           WG19_Vol, WG20_Vol, WG21_Vol, WG22_Vol, WG23_Vol, WG24_Vol,\
           WH1_Vol, WH2_Vol, WH3_Vol, WH4_Vol, WH5_Vol, WH6_Vol,\
           WH7_Vol, WH8_Vol, WH9_Vol, WH10_Vol, WH11_Vol, WH12_Vol,\
           WH13_Vol, WH14_Vol, WH15_Vol, WH16_Vol, WH17_Vol, WH18_Vol,\
           WH19_Vol, WH20_Vol, WH21_Vol, WH22_Vol, WH23_Vol, WH24_Vol,\
           WI1_Vol, WI2_Vol, WI3_Vol, WI4_Vol, WI5_Vol, WI6_Vol,\
           WI7_Vol, WI8_Vol, WI9_Vol, WI10_Vol, WI11_Vol, WI12_Vol,\
           WI13_Vol, WI14_Vol, WI15_Vol, WI16_Vol, WI17_Vol, WI18_Vol,\
           WI19_Vol, WI20_Vol, WI21_Vol, WI22_Vol, WI23_Vol, WI24_Vol,\
           WJ1_Vol, WJ2_Vol, WJ3_Vol, WJ4_Vol, WJ5_Vol, WJ6_Vol,\
           WJ7_Vol, WJ8_Vol, WJ9_Vol, WJ10_Vol, WJ11_Vol, WJ12_Vol,\
           WJ13_Vol, WJ14_Vol, WJ15_Vol, WJ16_Vol, WJ17_Vol, WJ18_Vol,\
           WJ19_Vol, WJ20_Vol, WJ21_Vol, WJ22_Vol, WJ23_Vol, WJ24_Vol,\
           WK1_Vol, WK2_Vol, WK3_Vol, WK4_Vol, WK5_Vol, WK6_Vol,\
           WK7_Vol, WK8_Vol, WK9_Vol, WK10_Vol, WK11_Vol, WK12_Vol,\
           WK13_Vol, WK14_Vol, WK15_Vol, WK16_Vol, WK17_Vol, WK18_Vol,\
           WK19_Vol, WK20_Vol, WK21_Vol, WK22_Vol, WK23_Vol, WK24_Vol,\
           WL1_Vol, WL2_Vol, WL3_Vol, WL4_Vol, WL5_Vol, WL6_Vol,\
           WL7_Vol, WL8_Vol, WL9_Vol, WL10_Vol, WL11_Vol, WL12_Vol,\
           WL13_Vol, WL14_Vol, WL15_Vol, WL16_Vol, WL17_Vol, WL18_Vol,\
           WL19_Vol, WL20_Vol, WL21_Vol, WL22_Vol, WL23_Vol, WL24_Vol,\
           WM1_Vol, WM2_Vol, WM3_Vol, WM4_Vol, WM5_Vol, WM6_Vol,\
           WM7_Vol, WM8_Vol, WM9_Vol, WM10_Vol, WM11_Vol, WM12_Vol,\
           WM13_Vol, WM14_Vol, WM15_Vol, WM16_Vol, WM17_Vol, WM18_Vol,\
           WM19_Vol, WM20_Vol, WM21_Vol, WM22_Vol, WM23_Vol, WM24_Vol,\
           WN1_Vol, WN2_Vol, WN3_Vol, WN4_Vol, WN5_Vol, WN6_Vol,\
           WN7_Vol, WN8_Vol, WN9_Vol, WN10_Vol, WN11_Vol, WN12_Vol,\
           WN13_Vol, WN14_Vol, WN15_Vol, WN16_Vol, WN17_Vol, WN18_Vol,\
           WN19_Vol, WN20_Vol, WN21_Vol, WN22_Vol, WN23_Vol, WN24_Vol,\
           WO1_Vol, WO2_Vol, WO3_Vol, WO4_Vol, WO5_Vol, WO6_Vol,\
           WO7_Vol, WO8_Vol, WO9_Vol, WO10_Vol, WO11_Vol, WO12_Vol,\
           WO13_Vol, WO14_Vol, WO15_Vol, WO16_Vol, WO17_Vol, WO18_Vol,\
           WO19_Vol, WO20_Vol, WO21_Vol, WO22_Vol, WO23_Vol, WO24_Vol,\
           WP1_Vol, WP2_Vol, WP3_Vol, WP4_Vol, WP5_Vol, WP6_Vol,\
           WP7_Vol, WP8_Vol, WP9_Vol, WP10_Vol, WP11_Vol, WP12_Vol,\
           WP13_Vol, WP14_Vol, WP15_Vol, WP16_Vol, WP17_Vol, WP18_Vol,\
           WP19_Vol, WP20_Vol, WP21_Vol, WP22_Vol, WP23_Vol, WP24_Vol,\
           WA1_IngrMenu, WA2_IngrMenu, WA3_IngrMenu, WA4_IngrMenu, WA5_IngrMenu, WA6_IngrMenu,\
           WA7_IngrMenu, WA8_IngrMenu, WA9_IngrMenu, WA10_IngrMenu, WA11_IngrMenu, WA12_IngrMenu,\
           WA13_IngrMenu, WA14_IngrMenu, WA15_IngrMenu, WA16_IngrMenu, WA17_IngrMenu, WA18_IngrMenu,\
           WA19_IngrMenu, WA20_IngrMenu, WA21_IngrMenu, WA22_IngrMenu, WA23_IngrMenu, WA24_IngrMenu,\
           WB1_IngrMenu, WB2_IngrMenu, WB3_IngrMenu, WB4_IngrMenu, WB5_IngrMenu, WB6_IngrMenu,\
           WB7_IngrMenu, WB8_IngrMenu, WB9_IngrMenu, WB10_IngrMenu, WB11_IngrMenu, WB12_IngrMenu,\
           WB13_IngrMenu, WB14_IngrMenu, WB15_IngrMenu, WB16_IngrMenu, WB17_IngrMenu, WB18_IngrMenu,\
           WB19_IngrMenu, WB20_IngrMenu, WB21_IngrMenu, WB22_IngrMenu, WB23_IngrMenu, WB24_IngrMenu,\
           WC1_IngrMenu, WC2_IngrMenu, WC3_IngrMenu, WC4_IngrMenu, WC5_IngrMenu, WC6_IngrMenu,\
           WC7_IngrMenu, WC8_IngrMenu, WC9_IngrMenu, WC10_IngrMenu, WC11_IngrMenu, WC12_IngrMenu,\
           WC13_IngrMenu, WC14_IngrMenu, WC15_IngrMenu, WC16_IngrMenu, WC17_IngrMenu, WC18_IngrMenu,\
           WC19_IngrMenu, WC20_IngrMenu, WC21_IngrMenu, WC22_IngrMenu, WC23_IngrMenu, WC24_IngrMenu,\
           WD1_IngrMenu, WD2_IngrMenu, WD3_IngrMenu, WD4_IngrMenu, WD5_IngrMenu, WD6_IngrMenu,\
           WD7_IngrMenu, WD8_IngrMenu, WD9_IngrMenu, WD10_IngrMenu, WD11_IngrMenu, WD12_IngrMenu,\
           WD13_IngrMenu, WD14_IngrMenu, WD15_IngrMenu, WD16_IngrMenu, WD17_IngrMenu, WD18_IngrMenu,\
           WD19_IngrMenu, WD20_IngrMenu, WD21_IngrMenu, WD22_IngrMenu, WD23_IngrMenu, WD24_IngrMenu,\
           WE1_IngrMenu, WE2_IngrMenu, WE3_IngrMenu, WE4_IngrMenu, WE5_IngrMenu, WE6_IngrMenu,\
           WE7_IngrMenu, WE8_IngrMenu, WE9_IngrMenu, WE10_IngrMenu, WE11_IngrMenu, WE12_IngrMenu,\
           WE13_IngrMenu, WE14_IngrMenu, WE15_IngrMenu, WE16_IngrMenu, WE17_IngrMenu, WE18_IngrMenu,\
           WE19_IngrMenu, WE20_IngrMenu, WE21_IngrMenu, WE22_IngrMenu, WE23_IngrMenu, WE24_IngrMenu,\
           WF1_IngrMenu, WF2_IngrMenu, WF3_IngrMenu, WF4_IngrMenu, WF5_IngrMenu, WF6_IngrMenu,\
           WF7_IngrMenu, WF8_IngrMenu, WF9_IngrMenu, WF10_IngrMenu, WF11_IngrMenu, WF12_IngrMenu,\
           WF13_IngrMenu, WF14_IngrMenu, WF15_IngrMenu, WF16_IngrMenu, WF17_IngrMenu, WF18_IngrMenu,\
           WF19_IngrMenu, WF20_IngrMenu, WF21_IngrMenu, WF22_IngrMenu, WF23_IngrMenu, WF24_IngrMenu,\
           WG1_IngrMenu, WG2_IngrMenu, WG3_IngrMenu, WG4_IngrMenu, WG5_IngrMenu, WG6_IngrMenu,\
           WG7_IngrMenu, WG8_IngrMenu, WG9_IngrMenu, WG10_IngrMenu, WG11_IngrMenu, WG12_IngrMenu,\
           WG13_IngrMenu, WG14_IngrMenu, WG15_IngrMenu, WG16_IngrMenu, WG17_IngrMenu, WG18_IngrMenu,\
           WG19_IngrMenu, WG20_IngrMenu, WG21_IngrMenu, WG22_IngrMenu, WG23_IngrMenu, WG24_IngrMenu,\
           WH1_IngrMenu, WH2_IngrMenu, WH3_IngrMenu, WH4_IngrMenu, WH5_IngrMenu, WH6_IngrMenu,\
           WH7_IngrMenu, WH8_IngrMenu, WH9_IngrMenu, WH10_IngrMenu, WH11_IngrMenu, WH12_IngrMenu,\
           WH13_IngrMenu, WH14_IngrMenu, WH15_IngrMenu, WH16_IngrMenu, WH17_IngrMenu, WH18_IngrMenu,\
           WH19_IngrMenu, WH20_IngrMenu, WH21_IngrMenu, WH22_IngrMenu, WH23_IngrMenu, WH24_IngrMenu,\
           WI1_IngrMenu, WI2_IngrMenu, WI3_IngrMenu, WI4_IngrMenu, WI5_IngrMenu, WI6_IngrMenu,\
           WI7_IngrMenu, WI8_IngrMenu, WI9_IngrMenu, WI10_IngrMenu, WI11_IngrMenu, WI12_IngrMenu,\
           WI13_IngrMenu, WI14_IngrMenu, WI15_IngrMenu, WI16_IngrMenu, WI17_IngrMenu, WI18_IngrMenu,\
           WI19_IngrMenu, WI20_IngrMenu, WI21_IngrMenu, WI22_IngrMenu, WI23_IngrMenu, WI24_IngrMenu,\
           WJ1_IngrMenu, WJ2_IngrMenu, WJ3_IngrMenu, WJ4_IngrMenu, WJ5_IngrMenu, WJ6_IngrMenu,\
           WJ7_IngrMenu, WJ8_IngrMenu, WJ9_IngrMenu, WJ10_IngrMenu, WJ11_IngrMenu, WJ12_IngrMenu,\
           WJ13_IngrMenu, WJ14_IngrMenu, WJ15_IngrMenu, WJ16_IngrMenu, WJ17_IngrMenu, WJ18_IngrMenu,\
           WJ19_IngrMenu, WJ20_IngrMenu, WJ21_IngrMenu, WJ22_IngrMenu, WJ23_IngrMenu, WJ24_IngrMenu,\
           WK1_IngrMenu, WK2_IngrMenu, WK3_IngrMenu, WK4_IngrMenu, WK5_IngrMenu, WK6_IngrMenu,\
           WK7_IngrMenu, WK8_IngrMenu, WK9_IngrMenu, WK10_IngrMenu, WK11_IngrMenu, WK12_IngrMenu,\
           WK13_IngrMenu, WK14_IngrMenu, WK15_IngrMenu, WK16_IngrMenu, WK17_IngrMenu, WK18_IngrMenu,\
           WK19_IngrMenu, WK20_IngrMenu, WK21_IngrMenu, WK22_IngrMenu, WK23_IngrMenu, WK24_IngrMenu,\
           WL1_IngrMenu, WL2_IngrMenu, WL3_IngrMenu, WL4_IngrMenu, WL5_IngrMenu, WL6_IngrMenu,\
           WL7_IngrMenu, WL8_IngrMenu, WL9_IngrMenu, WL10_IngrMenu, WL11_IngrMenu, WL12_IngrMenu,\
           WL13_IngrMenu, WL14_IngrMenu, WL15_IngrMenu, WL16_IngrMenu, WL17_IngrMenu, WL18_IngrMenu,\
           WL19_IngrMenu, WL20_IngrMenu, WL21_IngrMenu, WL22_IngrMenu, WL23_IngrMenu, WL24_IngrMenu,\
           WM1_IngrMenu, WM2_IngrMenu, WM3_IngrMenu, WM4_IngrMenu, WM5_IngrMenu, WM6_IngrMenu,\
           WM7_IngrMenu, WM8_IngrMenu, WM9_IngrMenu, WM10_IngrMenu, WM11_IngrMenu, WM12_IngrMenu,\
           WM13_IngrMenu, WM14_IngrMenu, WM15_IngrMenu, WM16_IngrMenu, WM17_IngrMenu, WM18_IngrMenu,\
           WM19_IngrMenu, WM20_IngrMenu, WM21_IngrMenu, WM22_IngrMenu, WM23_IngrMenu, WM24_IngrMenu,\
           WN1_IngrMenu, WN2_IngrMenu, WN3_IngrMenu, WN4_IngrMenu, WN5_IngrMenu, WN6_IngrMenu,\
           WN7_IngrMenu, WN8_IngrMenu, WN9_IngrMenu, WN10_IngrMenu, WN11_IngrMenu, WN12_IngrMenu,\
           WN13_IngrMenu, WN14_IngrMenu, WN15_IngrMenu, WN16_IngrMenu, WN17_IngrMenu, WN18_IngrMenu,\
           WN19_IngrMenu, WN20_IngrMenu, WN21_IngrMenu, WN22_IngrMenu, WN23_IngrMenu, WN24_IngrMenu,\
           WO1_IngrMenu, WO2_IngrMenu, WO3_IngrMenu, WO4_IngrMenu, WO5_IngrMenu, WO6_IngrMenu,\
           WO7_IngrMenu, WO8_IngrMenu, WO9_IngrMenu, WO10_IngrMenu, WO11_IngrMenu, WO12_IngrMenu,\
           WO13_IngrMenu, WO14_IngrMenu, WO15_IngrMenu, WO16_IngrMenu, WO17_IngrMenu, WO18_IngrMenu,\
           WO19_IngrMenu, WO20_IngrMenu, WO21_IngrMenu, WO22_IngrMenu, WO23_IngrMenu, WO24_IngrMenu,\
           WP1_IngrMenu, WP2_IngrMenu, WP3_IngrMenu, WP4_IngrMenu, WP5_IngrMenu, WP6_IngrMenu,\
           WP7_IngrMenu, WP8_IngrMenu, WP9_IngrMenu, WP10_IngrMenu, WP11_IngrMenu, WP12_IngrMenu,\
           WP13_IngrMenu, WP14_IngrMenu, WP15_IngrMenu, WP16_IngrMenu, WP17_IngrMenu, WP18_IngrMenu,\
           WP19_IngrMenu, WP20_IngrMenu, WP21_IngrMenu, WP22_IngrMenu, WP23_IngrMenu, WP24_IngrMenu,\
           WA1_SS, WA2_SS, WA3_SS, WA4_SS, WA5_SS, WA6_SS, WA7_SS, WA8_SS,\
           WA9_SS, WA10_SS, WA11_SS, WA12_SS, WA13_SS, WA14_SS, WA15_SS, WA16_SS,\
           WA17_SS, WA18_SS, WA19_SS, WA20_SS, WA21_SS, WA22_SS, WA23_SS, WA24_SS,\
           WB1_SS, WB2_SS, WB3_SS, WB4_SS, WB5_SS, WB6_SS, WB7_SS, WB8_SS,\
           WB9_SS, WB10_SS, WB11_SS, WB12_SS, WB13_SS, WB14_SS, WB15_SS, WB16_SS,\
           WB17_SS, WB18_SS, WB19_SS, WB20_SS, WB21_SS, WB22_SS, WB23_SS, WB24_SS,\
           WC1_SS, WC2_SS, WC3_SS, WC4_SS, WC5_SS, WC6_SS, WC7_SS, WC8_SS,\
           WC9_SS, WC10_SS, WC11_SS, WC12_SS, WC13_SS, WC14_SS, WC15_SS, WC16_SS,\
           WC17_SS, WC18_SS, WC19_SS, WC20_SS, WC21_SS, WC22_SS, WC23_SS, WC24_SS,\
           WD1_SS, WD2_SS, WD3_SS, WD4_SS, WD5_SS, WD6_SS, WD7_SS, WD8_SS,\
           WD9_SS, WD10_SS, WD11_SS, WD12_SS, WD13_SS, WD14_SS, WD15_SS, WD16_SS,\
           WD17_SS, WD18_SS, WD19_SS, WD20_SS, WD21_SS, WD22_SS, WD23_SS, WD24_SS,\
           WE1_SS, WE2_SS, WE3_SS, WE4_SS, WE5_SS, WE6_SS, WE7_SS, WE8_SS,\
           WE9_SS, WE10_SS, WE11_SS, WE12_SS, WE13_SS, WE14_SS, WE15_SS, WE16_SS,\
           WE17_SS, WE18_SS, WE19_SS, WE20_SS, WE21_SS, WE22_SS, WE23_SS, WE24_SS,\
           WF1_SS, WF2_SS, WF3_SS, WF4_SS, WF5_SS, WF6_SS, WF7_SS, WF8_SS,\
           WF9_SS, WF10_SS, WF11_SS, WF12_SS, WF13_SS, WF14_SS, WF15_SS, WF16_SS,\
           WF17_SS, WF18_SS, WF19_SS, WF20_SS, WF21_SS, WF22_SS, WF23_SS, WF24_SS,\
           WG1_SS, WG2_SS, WG3_SS, WG4_SS, WG5_SS, WG6_SS, WG7_SS, WG8_SS,\
           WG9_SS, WG10_SS, WG11_SS, WG12_SS, WG13_SS, WG14_SS, WG15_SS, WG16_SS,\
           WG17_SS, WG18_SS, WG19_SS, WG20_SS, WG21_SS, WG22_SS, WG23_SS, WG24_SS,\
           WH1_SS, WH2_SS, WH3_SS, WH4_SS, WH5_SS, WH6_SS, WH7_SS, WH8_SS,\
           WH9_SS, WH10_SS, WH11_SS, WH12_SS, WH13_SS, WH14_SS, WH15_SS, WH16_SS,\
           WH17_SS, WH18_SS, WH19_SS, WH20_SS, WH21_SS, WH22_SS, WH23_SS, WH24_SS,\
           WI1_SS, WI2_SS, WI3_SS, WI4_SS, WI5_SS, WI6_SS, WI7_SS, WI8_SS,\
           WI9_SS, WI10_SS, WI11_SS, WI12_SS, WI13_SS, WI14_SS, WI15_SS, WI16_SS,\
           WI17_SS, WI18_SS, WI19_SS, WI20_SS, WI21_SS, WI22_SS, WI23_SS, WI24_SS,\
           WJ1_SS, WJ2_SS, WJ3_SS, WJ4_SS, WJ5_SS, WJ6_SS, WJ7_SS, WJ8_SS,\
           WJ9_SS, WJ10_SS, WJ11_SS, WJ12_SS, WJ13_SS, WJ14_SS, WJ15_SS, WJ16_SS,\
           WJ17_SS, WJ18_SS, WJ19_SS, WJ20_SS, WJ21_SS, WJ22_SS, WJ23_SS, WJ24_SS,\
           WK1_SS, WK2_SS, WK3_SS, WK4_SS, WK5_SS, WK6_SS, WK7_SS, WK8_SS,\
           WK9_SS, WK10_SS, WK11_SS, WK12_SS, WK13_SS, WK14_SS, WK15_SS, WK16_SS,\
           WK17_SS, WK18_SS, WK19_SS, WK20_SS, WK21_SS, WK22_SS, WK23_SS, WK24_SS,\
           WL1_SS, WL2_SS, WL3_SS, WL4_SS, WL5_SS, WL6_SS, WL7_SS, WL8_SS,\
           WL9_SS, WL10_SS, WL11_SS, WL12_SS, WL13_SS, WL14_SS, WL15_SS, WL16_SS,\
           WL17_SS, WL18_SS, WL19_SS, WL20_SS, WL21_SS, WL22_SS, WL23_SS, WL24_SS,\
           WM1_SS, WM2_SS, WM3_SS, WM4_SS, WM5_SS, WM6_SS, WM7_SS, WM8_SS,\
           WM9_SS, WM10_SS, WM11_SS, WM12_SS, WM13_SS, WM14_SS, WM15_SS, WM16_SS,\
           WM17_SS, WM18_SS, WM19_SS, WM20_SS, WM21_SS, WM22_SS, WM23_SS, WM24_SS,\
           WN1_SS, WN2_SS, WN3_SS, WN4_SS, WN5_SS, WN6_SS, WN7_SS, WN8_SS,\
           WN9_SS, WN10_SS, WN11_SS, WN12_SS, WN13_SS, WN14_SS, WN15_SS, WN16_SS,\
           WN17_SS, WN18_SS, WN19_SS, WN20_SS, WN21_SS, WN22_SS, WN23_SS, WN24_SS,\
           WO1_SS, WO2_SS, WO3_SS, WO4_SS, WO5_SS, WO6_SS, WO7_SS, WO8_SS,\
           WO9_SS, WO10_SS, WO11_SS, WO12_SS, WO13_SS, WO14_SS, WO15_SS, WO16_SS,\
           WO17_SS, WO18_SS, WO19_SS, WO20_SS, WO21_SS, WO22_SS, WO23_SS, WO24_SS,\
           WP1_SS, WP2_SS, WP3_SS, WP4_SS, WP5_SS, WP6_SS, WP7_SS, WP8_SS,\
           WP9_SS, WP10_SS, WP11_SS, WP12_SS, WP13_SS, WP14_SS, WP15_SS, WP16_SS,\
           WP17_SS, WP18_SS, WP19_SS, WP20_SS, WP21_SS, WP22_SS, WP23_SS, WP24_SS,\
           WA1_SSMenu, WA2_SSMenu, WA3_SSMenu, WA4_SSMenu, WA5_SSMenu, WA6_SSMenu, WA7_SSMenu, WA8_SSMenu,\
           WA9_SSMenu, WA10_SSMenu, WA11_SSMenu, WA12_SSMenu, WA13_SSMenu, WA14_SSMenu, WA15_SSMenu, WA16_SSMenu,\
           WA17_SSMenu, WA18_SSMenu, WA19_SSMenu, WA20_SSMenu, WA21_SSMenu, WA22_SSMenu, WA23_SSMenu, WA24_SSMenu,\
           WB1_SSMenu, WB2_SSMenu, WB3_SSMenu, WB4_SSMenu, WB5_SSMenu, WB6_SSMenu, WB7_SSMenu, WB8_SSMenu,\
           WB9_SSMenu, WB10_SSMenu, WB11_SSMenu, WB12_SSMenu, WB13_SSMenu, WB14_SSMenu, WB15_SSMenu, WB16_SSMenu,\
           WB17_SSMenu, WB18_SSMenu, WB19_SSMenu, WB20_SSMenu, WB21_SSMenu, WB22_SSMenu, WB23_SSMenu, WB24_SSMenu,\
           WC1_SSMenu, WC2_SSMenu, WC3_SSMenu, WC4_SSMenu, WC5_SSMenu, WC6_SSMenu, WC7_SSMenu, WC8_SSMenu,\
           WC9_SSMenu, WC10_SSMenu, WC11_SSMenu, WC12_SSMenu, WC13_SSMenu, WC14_SSMenu, WC15_SSMenu, WC16_SSMenu,\
           WC17_SSMenu, WC18_SSMenu, WC19_SSMenu, WC20_SSMenu, WC21_SSMenu, WC22_SSMenu, WC23_SSMenu, WC24_SSMenu,\
           WD1_SSMenu, WD2_SSMenu, WD3_SSMenu, WD4_SSMenu, WD5_SSMenu, WD6_SSMenu, WD7_SSMenu, WD8_SSMenu,\
           WD9_SSMenu, WD10_SSMenu, WD11_SSMenu, WD12_SSMenu, WD13_SSMenu, WD14_SSMenu, WD15_SSMenu, WD16_SSMenu,\
           WD17_SSMenu, WD18_SSMenu, WD19_SSMenu, WD20_SSMenu, WD21_SSMenu, WD22_SSMenu, WD23_SSMenu, WD24_SSMenu,\
           WE1_SSMenu, WE2_SSMenu, WE3_SSMenu, WE4_SSMenu, WE5_SSMenu, WE6_SSMenu, WE7_SSMenu, WE8_SSMenu,\
           WE9_SSMenu, WE10_SSMenu, WE11_SSMenu, WE12_SSMenu, WE13_SSMenu, WE14_SSMenu, WE15_SSMenu, WE16_SSMenu,\
           WE17_SSMenu, WE18_SSMenu, WE19_SSMenu, WE20_SSMenu, WE21_SSMenu, WE22_SSMenu, WE23_SSMenu, WE24_SSMenu,\
           WF1_SSMenu, WF2_SSMenu, WF3_SSMenu, WF4_SSMenu, WF5_SSMenu, WF6_SSMenu, WF7_SSMenu, WF8_SSMenu,\
           WF9_SSMenu, WF10_SSMenu, WF11_SSMenu, WF12_SSMenu, WF13_SSMenu, WF14_SSMenu, WF15_SSMenu, WF16_SSMenu,\
           WF17_SSMenu, WF18_SSMenu, WF19_SSMenu, WF20_SSMenu, WF21_SSMenu, WF22_SSMenu, WF23_SSMenu, WF24_SSMenu,\
           WG1_SSMenu, WG2_SSMenu, WG3_SSMenu, WG4_SSMenu, WG5_SSMenu, WG6_SSMenu, WG7_SSMenu, WG8_SSMenu,\
           WG9_SSMenu, WG10_SSMenu, WG11_SSMenu, WG12_SSMenu, WG13_SSMenu, WG14_SSMenu, WG15_SSMenu, WG16_SSMenu,\
           WG17_SSMenu, WG18_SSMenu, WG19_SSMenu, WG20_SSMenu, WG21_SSMenu, WG22_SSMenu, WG23_SSMenu, WG24_SSMenu,\
           WH1_SSMenu, WH2_SSMenu, WH3_SSMenu, WH4_SSMenu, WH5_SSMenu, WH6_SSMenu, WH7_SSMenu, WH8_SSMenu,\
           WH9_SSMenu, WH10_SSMenu, WH11_SSMenu, WH12_SSMenu, WH13_SSMenu, WH14_SSMenu, WH15_SSMenu, WH16_SSMenu,\
           WH17_SSMenu, WH18_SSMenu, WH19_SSMenu, WH20_SSMenu, WH21_SSMenu, WH22_SSMenu, WH23_SSMenu, WH24_SSMenu,\
           WI1_SSMenu, WI2_SSMenu, WI3_SSMenu, WI4_SSMenu, WI5_SSMenu, WI6_SSMenu, WI7_SSMenu, WI8_SSMenu,\
           WI9_SSMenu, WI10_SSMenu, WI11_SSMenu, WI12_SSMenu, WI13_SSMenu, WI14_SSMenu, WI15_SSMenu, WI16_SSMenu,\
           WI17_SSMenu, WI18_SSMenu, WI19_SSMenu, WI20_SSMenu, WI21_SSMenu, WI22_SSMenu, WI23_SSMenu, WI24_SSMenu,\
           WJ1_SSMenu, WJ2_SSMenu, WJ3_SSMenu, WJ4_SSMenu, WJ5_SSMenu, WJ6_SSMenu, WJ7_SSMenu, WJ8_SSMenu,\
           WJ9_SSMenu, WJ10_SSMenu, WJ11_SSMenu, WJ12_SSMenu, WJ13_SSMenu, WJ14_SSMenu, WJ15_SSMenu, WJ16_SSMenu,\
           WJ17_SSMenu, WJ18_SSMenu, WJ19_SSMenu, WJ20_SSMenu, WJ21_SSMenu, WJ22_SSMenu, WJ23_SSMenu, WJ24_SSMenu,\
           WK1_SSMenu, WK2_SSMenu, WK3_SSMenu, WK4_SSMenu, WK5_SSMenu, WK6_SSMenu, WK7_SSMenu, WK8_SSMenu,\
           WK9_SSMenu, WK10_SSMenu, WK11_SSMenu, WK12_SSMenu, WK13_SSMenu, WK14_SSMenu, WK15_SSMenu, WK16_SSMenu,\
           WK17_SSMenu, WK18_SSMenu, WK19_SSMenu, WK20_SSMenu, WK21_SSMenu, WK22_SSMenu, WK23_SSMenu, WK24_SSMenu,\
           WL1_SSMenu, WL2_SSMenu, WL3_SSMenu, WL4_SSMenu, WL5_SSMenu, WL6_SSMenu, WL7_SSMenu, WL8_SSMenu,\
           WL9_SSMenu, WL10_SSMenu, WL11_SSMenu, WL12_SSMenu, WL13_SSMenu, WL14_SSMenu, WL15_SSMenu, WL16_SSMenu,\
           WL17_SSMenu, WL18_SSMenu, WL19_SSMenu, WL20_SSMenu, WL21_SSMenu, WL22_SSMenu, WL23_SSMenu, WL24_SSMenu,\
           WM1_SSMenu, WM2_SSMenu, WM3_SSMenu, WM4_SSMenu, WM5_SSMenu, WM6_SSMenu, WM7_SSMenu, WM8_SSMenu,\
           WM9_SSMenu, WM10_SSMenu, WM11_SSMenu, WM12_SSMenu, WM13_SSMenu, WM14_SSMenu, WM15_SSMenu, WM16_SSMenu,\
           WM17_SSMenu, WM18_SSMenu, WM19_SSMenu, WM20_SSMenu, WM21_SSMenu, WM22_SSMenu, WM23_SSMenu, WM24_SSMenu,\
           WN1_SSMenu, WN2_SSMenu, WN3_SSMenu, WN4_SSMenu, WN5_SSMenu, WN6_SSMenu, WN7_SSMenu, WN8_SSMenu,\
           WN9_SSMenu, WN10_SSMenu, WN11_SSMenu, WN12_SSMenu, WN13_SSMenu, WN14_SSMenu, WN15_SSMenu, WN16_SSMenu,\
           WN17_SSMenu, WN18_SSMenu, WN19_SSMenu, WN20_SSMenu, WN21_SSMenu, WN22_SSMenu, WN23_SSMenu, WN24_SSMenu,\
           WO1_SSMenu, WO2_SSMenu, WO3_SSMenu, WO4_SSMenu, WO5_SSMenu, WO6_SSMenu, WO7_SSMenu, WO8_SSMenu,\
           WO9_SSMenu, WO10_SSMenu, WO11_SSMenu, WO12_SSMenu, WO13_SSMenu, WO14_SSMenu, WO15_SSMenu, WO16_SSMenu,\
           WO17_SSMenu, WO18_SSMenu, WO19_SSMenu, WO20_SSMenu, WO21_SSMenu, WO22_SSMenu, WO23_SSMenu, WO24_SSMenu,\
           WP1_SSMenu, WP2_SSMenu, WP3_SSMenu, WP4_SSMenu, WP5_SSMenu, WP6_SSMenu, WP7_SSMenu, WP8_SSMenu,\
           WP9_SSMenu, WP10_SSMenu, WP11_SSMenu, WP12_SSMenu, WP13_SSMenu, WP14_SSMenu, WP15_SSMenu, WP16_SSMenu,\
           WP17_SSMenu, WP18_SSMenu, WP19_SSMenu, WP20_SSMenu, WP21_SSMenu, WP22_SSMenu, WP23_SSMenu, WP24_SSMenu,\
           WA1_Dilu, WA2_Dilu, WA3_Dilu, WA4_Dilu, WA5_Dilu, WA6_Dilu, WA7_Dilu, WA8_Dilu,\
           WA9_Dilu, WA10_Dilu, WA11_Dilu, WA12_Dilu, WA13_Dilu, WA14_Dilu, WA15_Dilu, WA16_Dilu,\
           WA17_Dilu, WA18_Dilu, WA19_Dilu, WA20_Dilu, WA21_Dilu, WA22_Dilu, WA23_Dilu, WA24_Dilu,\
           WB1_Dilu, WB2_Dilu, WB3_Dilu, WB4_Dilu, WB5_Dilu, WB6_Dilu, WB7_Dilu, WB8_Dilu,\
           WB9_Dilu, WB10_Dilu, WB11_Dilu, WB12_Dilu, WB13_Dilu, WB14_Dilu, WB15_Dilu, WB16_Dilu,\
           WB17_Dilu, WB18_Dilu, WB19_Dilu, WB20_Dilu, WB21_Dilu, WB22_Dilu, WB23_Dilu, WB24_Dilu,\
           WC1_Dilu, WC2_Dilu, WC3_Dilu, WC4_Dilu, WC5_Dilu, WC6_Dilu, WC7_Dilu, WC8_Dilu,\
           WC9_Dilu, WC10_Dilu, WC11_Dilu, WC12_Dilu, WC13_Dilu, WC14_Dilu, WC15_Dilu, WC16_Dilu,\
           WC17_Dilu, WC18_Dilu, WC19_Dilu, WC20_Dilu, WC21_Dilu, WC22_Dilu, WC23_Dilu, WC24_Dilu,\
           WD1_Dilu, WD2_Dilu, WD3_Dilu, WD4_Dilu, WD5_Dilu, WD6_Dilu, WD7_Dilu, WD8_Dilu,\
           WD9_Dilu, WD10_Dilu, WD11_Dilu, WD12_Dilu, WD13_Dilu, WD14_Dilu, WD15_Dilu, WD16_Dilu,\
           WD17_Dilu, WD18_Dilu, WD19_Dilu, WD20_Dilu, WD21_Dilu, WD22_Dilu, WD23_Dilu, WD24_Dilu,\
           WE1_Dilu, WE2_Dilu, WE3_Dilu, WE4_Dilu, WE5_Dilu, WE6_Dilu, WE7_Dilu, WE8_Dilu,\
           WE9_Dilu, WE10_Dilu, WE11_Dilu, WE12_Dilu, WE13_Dilu, WE14_Dilu, WE15_Dilu, WE16_Dilu,\
           WE17_Dilu, WE18_Dilu, WE19_Dilu, WE20_Dilu, WE21_Dilu, WE22_Dilu, WE23_Dilu, WE24_Dilu,\
           WF1_Dilu, WF2_Dilu, WF3_Dilu, WF4_Dilu, WF5_Dilu, WF6_Dilu, WF7_Dilu, WF8_Dilu,\
           WF9_Dilu, WF10_Dilu, WF11_Dilu, WF12_Dilu, WF13_Dilu, WF14_Dilu, WF15_Dilu, WF16_Dilu,\
           WF17_Dilu, WF18_Dilu, WF19_Dilu, WF20_Dilu, WF21_Dilu, WF22_Dilu, WF23_Dilu, WF24_Dilu,\
           WG1_Dilu, WG2_Dilu, WG3_Dilu, WG4_Dilu, WG5_Dilu, WG6_Dilu, WG7_Dilu, WG8_Dilu,\
           WG9_Dilu, WG10_Dilu, WG11_Dilu, WG12_Dilu, WG13_Dilu, WG14_Dilu, WG15_Dilu, WG16_Dilu,\
           WG17_Dilu, WG18_Dilu, WG19_Dilu, WG20_Dilu, WG21_Dilu, WG22_Dilu, WG23_Dilu, WG24_Dilu,\
           WH1_Dilu, WH2_Dilu, WH3_Dilu, WH4_Dilu, WH5_Dilu, WH6_Dilu, WH7_Dilu, WH8_Dilu,\
           WH9_Dilu, WH10_Dilu, WH11_Dilu, WH12_Dilu, WH13_Dilu, WH14_Dilu, WH15_Dilu, WH16_Dilu,\
           WH17_Dilu, WH18_Dilu, WH19_Dilu, WH20_Dilu, WH21_Dilu, WH22_Dilu, WH23_Dilu, WH24_Dilu,\
           WI1_Dilu, WI2_Dilu, WI3_Dilu, WI4_Dilu, WI5_Dilu, WI6_Dilu, WI7_Dilu, WI8_Dilu,\
           WI9_Dilu, WI10_Dilu, WI11_Dilu, WI12_Dilu, WI13_Dilu, WI14_Dilu, WI15_Dilu, WI16_Dilu,\
           WI17_Dilu, WI18_Dilu, WI19_Dilu, WI20_Dilu, WI21_Dilu, WI22_Dilu, WI23_Dilu, WI24_Dilu,\
           WJ1_Dilu, WJ2_Dilu, WJ3_Dilu, WJ4_Dilu, WJ5_Dilu, WJ6_Dilu, WJ7_Dilu, WJ8_Dilu,\
           WJ9_Dilu, WJ10_Dilu, WJ11_Dilu, WJ12_Dilu, WJ13_Dilu, WJ14_Dilu, WJ15_Dilu, WJ16_Dilu,\
           WJ17_Dilu, WJ18_Dilu, WJ19_Dilu, WJ20_Dilu, WJ21_Dilu, WJ22_Dilu, WJ23_Dilu, WJ24_Dilu,\
           WK1_Dilu, WK2_Dilu, WK3_Dilu, WK4_Dilu, WK5_Dilu, WK6_Dilu, WK7_Dilu, WK8_Dilu,\
           WK9_Dilu, WK10_Dilu, WK11_Dilu, WK12_Dilu, WK13_Dilu, WK14_Dilu, WK15_Dilu, WK16_Dilu,\
           WK17_Dilu, WK18_Dilu, WK19_Dilu, WK20_Dilu, WK21_Dilu, WK22_Dilu, WK23_Dilu, WK24_Dilu,\
           WL1_Dilu, WL2_Dilu, WL3_Dilu, WL4_Dilu, WL5_Dilu, WL6_Dilu, WL7_Dilu, WL8_Dilu,\
           WL9_Dilu, WL10_Dilu, WL11_Dilu, WL12_Dilu, WL13_Dilu, WL14_Dilu, WL15_Dilu, WL16_Dilu,\
           WL17_Dilu, WL18_Dilu, WL19_Dilu, WL20_Dilu, WL21_Dilu, WL22_Dilu, WL23_Dilu, WL24_Dilu,\
           WM1_Dilu, WM2_Dilu, WM3_Dilu, WM4_Dilu, WM5_Dilu, WM6_Dilu, WM7_Dilu, WM8_Dilu,\
           WM9_Dilu, WM10_Dilu, WM11_Dilu, WM12_Dilu, WM13_Dilu, WM14_Dilu, WM15_Dilu, WM16_Dilu,\
           WM17_Dilu, WM18_Dilu, WM19_Dilu, WM20_Dilu, WM21_Dilu, WM22_Dilu, WM23_Dilu, WM24_Dilu,\
           WN1_Dilu, WN2_Dilu, WN3_Dilu, WN4_Dilu, WN5_Dilu, WN6_Dilu, WN7_Dilu, WN8_Dilu,\
           WN9_Dilu, WN10_Dilu, WN11_Dilu, WN12_Dilu, WN13_Dilu, WN14_Dilu, WN15_Dilu, WN16_Dilu,\
           WN17_Dilu, WN18_Dilu, WN19_Dilu, WN20_Dilu, WN21_Dilu, WN22_Dilu, WN23_Dilu, WN24_Dilu,\
           WO1_Dilu, WO2_Dilu, WO3_Dilu, WO4_Dilu, WO5_Dilu, WO6_Dilu, WO7_Dilu, WO8_Dilu,\
           WO9_Dilu, WO10_Dilu, WO11_Dilu, WO12_Dilu, WO13_Dilu, WO14_Dilu, WO15_Dilu, WO16_Dilu,\
           WO17_Dilu, WO18_Dilu, WO19_Dilu, WO20_Dilu, WO21_Dilu, WO22_Dilu, WO23_Dilu, WO24_Dilu,\
           WP1_Dilu, WP2_Dilu, WP3_Dilu, WP4_Dilu, WP5_Dilu, WP6_Dilu, WP7_Dilu, WP8_Dilu,\
           WP9_Dilu, WP10_Dilu, WP11_Dilu, WP12_Dilu, WP13_Dilu, WP14_Dilu, WP15_Dilu, WP16_Dilu,\
           WP17_Dilu, WP18_Dilu, WP19_Dilu, WP20_Dilu, WP21_Dilu, WP22_Dilu, WP23_Dilu, WP24_Dilu,
           WA1_DiluMenu, WA2_DiluMenu, WA3_DiluMenu, WA4_DiluMenu, WA5_DiluMenu, WA6_DiluMenu, WA7_DiluMenu, WA8_DiluMenu,\
           WA9_DiluMenu, WA10_DiluMenu, WA11_DiluMenu, WA12_DiluMenu, WA13_DiluMenu, WA14_DiluMenu, WA15_DiluMenu, WA16_DiluMenu,\
           WA17_DiluMenu, WA18_DiluMenu, WA19_DiluMenu, WA20_DiluMenu, WA21_DiluMenu, WA22_DiluMenu, WA23_DiluMenu, WA24_DiluMenu,\
           WB1_DiluMenu, WB2_DiluMenu, WB3_DiluMenu, WB4_DiluMenu, WB5_DiluMenu, WB6_DiluMenu, WB7_DiluMenu, WB8_DiluMenu,\
           WB9_DiluMenu, WB10_DiluMenu, WB11_DiluMenu, WB12_DiluMenu, WB13_DiluMenu, WB14_DiluMenu, WB15_DiluMenu, WB16_DiluMenu,\
           WB17_DiluMenu, WB18_DiluMenu, WB19_DiluMenu, WB20_DiluMenu, WB21_DiluMenu, WB22_DiluMenu, WB23_DiluMenu, WB24_DiluMenu,\
           WC1_DiluMenu, WC2_DiluMenu, WC3_DiluMenu, WC4_DiluMenu, WC5_DiluMenu, WC6_DiluMenu, WC7_DiluMenu, WC8_DiluMenu,\
           WC9_DiluMenu, WC10_DiluMenu, WC11_DiluMenu, WC12_DiluMenu, WC13_DiluMenu, WC14_DiluMenu, WC15_DiluMenu, WC16_DiluMenu,\
           WC17_DiluMenu, WC18_DiluMenu, WC19_DiluMenu, WC20_DiluMenu, WC21_DiluMenu, WC22_DiluMenu, WC23_DiluMenu, WC24_DiluMenu,\
           WD1_DiluMenu, WD2_DiluMenu, WD3_DiluMenu, WD4_DiluMenu, WD5_DiluMenu, WD6_DiluMenu, WD7_DiluMenu, WD8_DiluMenu,\
           WD9_DiluMenu, WD10_DiluMenu, WD11_DiluMenu, WD12_DiluMenu, WD13_DiluMenu, WD14_DiluMenu, WD15_DiluMenu, WD16_DiluMenu,\
           WD17_DiluMenu, WD18_DiluMenu, WD19_DiluMenu, WD20_DiluMenu, WD21_DiluMenu, WD22_DiluMenu, WD23_DiluMenu, WD24_DiluMenu,\
           WE1_DiluMenu, WE2_DiluMenu, WE3_DiluMenu, WE4_DiluMenu, WE5_DiluMenu, WE6_DiluMenu, WE7_DiluMenu, WE8_DiluMenu,\
           WE9_DiluMenu, WE10_DiluMenu, WE11_DiluMenu, WE12_DiluMenu, WE13_DiluMenu, WE14_DiluMenu, WE15_DiluMenu, WE16_DiluMenu,\
           WE17_DiluMenu, WE18_DiluMenu, WE19_DiluMenu, WE20_DiluMenu, WE21_DiluMenu, WE22_DiluMenu, WE23_DiluMenu, WE24_DiluMenu,\
           WF1_DiluMenu, WF2_DiluMenu, WF3_DiluMenu, WF4_DiluMenu, WF5_DiluMenu, WF6_DiluMenu, WF7_DiluMenu, WF8_DiluMenu,\
           WF9_DiluMenu, WF10_DiluMenu, WF11_DiluMenu, WF12_DiluMenu, WF13_DiluMenu, WF14_DiluMenu, WF15_DiluMenu, WF16_DiluMenu,\
           WF17_DiluMenu, WF18_DiluMenu, WF19_DiluMenu, WF20_DiluMenu, WF21_DiluMenu, WF22_DiluMenu, WF23_DiluMenu, WF24_DiluMenu,\
           WG1_DiluMenu, WG2_DiluMenu, WG3_DiluMenu, WG4_DiluMenu, WG5_DiluMenu, WG6_DiluMenu, WG7_DiluMenu, WG8_DiluMenu,\
           WG9_DiluMenu, WG10_DiluMenu, WG11_DiluMenu, WG12_DiluMenu, WG13_DiluMenu, WG14_DiluMenu, WG15_DiluMenu, WG16_DiluMenu,\
           WG17_DiluMenu, WG18_DiluMenu, WG19_DiluMenu, WG20_DiluMenu, WG21_DiluMenu, WG22_DiluMenu, WG23_DiluMenu, WG24_DiluMenu,\
           WH1_DiluMenu, WH2_DiluMenu, WH3_DiluMenu, WH4_DiluMenu, WH5_DiluMenu, WH6_DiluMenu, WH7_DiluMenu, WH8_DiluMenu,\
           WH9_DiluMenu, WH10_DiluMenu, WH11_DiluMenu, WH12_DiluMenu, WH13_DiluMenu, WH14_DiluMenu, WH15_DiluMenu, WH16_DiluMenu,\
           WH17_DiluMenu, WH18_DiluMenu, WH19_DiluMenu, WH20_DiluMenu, WH21_DiluMenu, WH22_DiluMenu, WH23_DiluMenu, WH24_DiluMenu,\
           WI1_DiluMenu, WI2_DiluMenu, WI3_DiluMenu, WI4_DiluMenu, WI5_DiluMenu, WI6_DiluMenu, WI7_DiluMenu, WI8_DiluMenu,\
           WI9_DiluMenu, WI10_DiluMenu, WI11_DiluMenu, WI12_DiluMenu, WI13_DiluMenu, WI14_DiluMenu, WI15_DiluMenu, WI16_DiluMenu,\
           WI17_DiluMenu, WI18_DiluMenu, WI19_DiluMenu, WI20_DiluMenu, WI21_DiluMenu, WI22_DiluMenu, WI23_DiluMenu, WI24_DiluMenu,\
           WJ1_DiluMenu, WJ2_DiluMenu, WJ3_DiluMenu, WJ4_DiluMenu, WJ5_DiluMenu, WJ6_DiluMenu, WJ7_DiluMenu, WJ8_DiluMenu,\
           WJ9_DiluMenu, WJ10_DiluMenu, WJ11_DiluMenu, WJ12_DiluMenu, WJ13_DiluMenu, WJ14_DiluMenu, WJ15_DiluMenu, WJ16_DiluMenu,\
           WJ17_DiluMenu, WJ18_DiluMenu, WJ19_DiluMenu, WJ20_DiluMenu, WJ21_DiluMenu, WJ22_DiluMenu, WJ23_DiluMenu, WJ24_DiluMenu,\
           WK1_DiluMenu, WK2_DiluMenu, WK3_DiluMenu, WK4_DiluMenu, WK5_DiluMenu, WK6_DiluMenu, WK7_DiluMenu, WK8_DiluMenu,\
           WK9_DiluMenu, WK10_DiluMenu, WK11_DiluMenu, WK12_DiluMenu, WK13_DiluMenu, WK14_DiluMenu, WK15_DiluMenu, WK16_DiluMenu,\
           WK17_DiluMenu, WK18_DiluMenu, WK19_DiluMenu, WK20_DiluMenu, WK21_DiluMenu, WK22_DiluMenu, WK23_DiluMenu, WK24_DiluMenu,\
           WL1_DiluMenu, WL2_DiluMenu, WL3_DiluMenu, WL4_DiluMenu, WL5_DiluMenu, WL6_DiluMenu, WL7_DiluMenu, WL8_DiluMenu,\
           WL9_DiluMenu, WL10_DiluMenu, WL11_DiluMenu, WL12_DiluMenu, WL13_DiluMenu, WL14_DiluMenu, WL15_DiluMenu, WL16_DiluMenu,\
           WL17_DiluMenu, WL18_DiluMenu, WL19_DiluMenu, WL20_DiluMenu, WL21_DiluMenu, WL22_DiluMenu, WL23_DiluMenu, WL24_DiluMenu,\
           WM1_DiluMenu, WM2_DiluMenu, WM3_DiluMenu, WM4_DiluMenu, WM5_DiluMenu, WM6_DiluMenu, WM7_DiluMenu, WM8_DiluMenu,\
           WM9_DiluMenu, WM10_DiluMenu, WM11_DiluMenu, WM12_DiluMenu, WM13_DiluMenu, WM14_DiluMenu, WM15_DiluMenu, WM16_DiluMenu,\
           WM17_DiluMenu, WM18_DiluMenu, WM19_DiluMenu, WM20_DiluMenu, WM21_DiluMenu, WM22_DiluMenu, WM23_DiluMenu, WM24_DiluMenu,\
           WN1_DiluMenu, WN2_DiluMenu, WN3_DiluMenu, WN4_DiluMenu, WN5_DiluMenu, WN6_DiluMenu, WN7_DiluMenu, WN8_DiluMenu,\
           WN9_DiluMenu, WN10_DiluMenu, WN11_DiluMenu, WN12_DiluMenu, WN13_DiluMenu, WN14_DiluMenu, WN15_DiluMenu, WN16_DiluMenu,\
           WN17_DiluMenu, WN18_DiluMenu, WN19_DiluMenu, WN20_DiluMenu, WN21_DiluMenu, WN22_DiluMenu, WN23_DiluMenu, WN24_DiluMenu,\
           WO1_DiluMenu, WO2_DiluMenu, WO3_DiluMenu, WO4_DiluMenu, WO5_DiluMenu, WO6_DiluMenu, WO7_DiluMenu, WO8_DiluMenu,\
           WO9_DiluMenu, WO10_DiluMenu, WO11_DiluMenu, WO12_DiluMenu, WO13_DiluMenu, WO14_DiluMenu, WO15_DiluMenu, WO16_DiluMenu,\
           WO17_DiluMenu, WO18_DiluMenu, WO19_DiluMenu, WO20_DiluMenu, WO21_DiluMenu, WO22_DiluMenu, WO23_DiluMenu, WO24_DiluMenu,\
           WP1_DiluMenu, WP2_DiluMenu, WP3_DiluMenu, WP4_DiluMenu, WP5_DiluMenu, WP6_DiluMenu, WP7_DiluMenu, WP8_DiluMenu,\
           WP9_DiluMenu, WP10_DiluMenu, WP11_DiluMenu, WP12_DiluMenu, WP13_DiluMenu, WP14_DiluMenu, WP15_DiluMenu, WP16_DiluMenu,\
           WP17_DiluMenu, WP18_DiluMenu, WP19_DiluMenu, WP20_DiluMenu, WP21_DiluMenu, WP22_DiluMenu, WP23_DiluMenu, WP24_DiluMenu]

    Ingr_List = [WA1_Ingr, WA2_Ingr, WA3_Ingr, WA4_Ingr, WA5_Ingr, WA6_Ingr,\
           WA7_Ingr, WA8_Ingr, WA9_Ingr, WA10_Ingr, WA11_Ingr, WA12_Ingr,\
           WA13_Ingr, WA14_Ingr, WA15_Ingr, WA16_Ingr, WA17_Ingr, WA18_Ingr,\
           WA19_Ingr, WA20_Ingr, WA21_Ingr, WA22_Ingr, WA23_Ingr, WA24_Ingr,\
           WB1_Ingr, WB2_Ingr, WB3_Ingr, WB4_Ingr, WB5_Ingr, WB6_Ingr,\
           WB7_Ingr, WB8_Ingr, WB9_Ingr, WB10_Ingr, WB11_Ingr, WB12_Ingr,\
           WB13_Ingr, WB14_Ingr, WB15_Ingr, WB16_Ingr, WB17_Ingr, WB18_Ingr,\
           WB19_Ingr, WB20_Ingr, WB21_Ingr, WB22_Ingr, WB23_Ingr, WB24_Ingr,\
           WC1_Ingr, WC2_Ingr, WC3_Ingr, WC4_Ingr, WC5_Ingr, WC6_Ingr,\
           WC7_Ingr, WC8_Ingr, WC9_Ingr, WC10_Ingr, WC11_Ingr, WC12_Ingr,\
           WC13_Ingr, WC14_Ingr, WC15_Ingr, WC16_Ingr, WC17_Ingr, WC18_Ingr,\
           WC19_Ingr, WC20_Ingr, WC21_Ingr, WC22_Ingr, WC23_Ingr, WC24_Ingr,\
           WD1_Ingr, WD2_Ingr, WD3_Ingr, WD4_Ingr, WD5_Ingr, WD6_Ingr,\
           WD7_Ingr, WD8_Ingr, WD9_Ingr, WD10_Ingr, WD11_Ingr, WD12_Ingr,\
           WD13_Ingr, WD14_Ingr, WD15_Ingr, WD16_Ingr, WD17_Ingr, WD18_Ingr,\
           WD19_Ingr, WD20_Ingr, WD21_Ingr, WD22_Ingr, WD23_Ingr, WD24_Ingr,\
           WE1_Ingr, WE2_Ingr, WE3_Ingr, WE4_Ingr, WE5_Ingr, WE6_Ingr,\
           WE7_Ingr, WE8_Ingr, WE9_Ingr, WE10_Ingr, WE11_Ingr, WE12_Ingr,\
           WE13_Ingr, WE14_Ingr, WE15_Ingr, WE16_Ingr, WE17_Ingr, WE18_Ingr,\
           WE19_Ingr, WE20_Ingr, WE21_Ingr, WE22_Ingr, WE23_Ingr, WE24_Ingr,\
           WF1_Ingr, WF2_Ingr, WF3_Ingr, WF4_Ingr, WF5_Ingr, WF6_Ingr,\
           WF7_Ingr, WF8_Ingr, WF9_Ingr, WF10_Ingr, WF11_Ingr, WF12_Ingr,\
           WF13_Ingr, WF14_Ingr, WF15_Ingr, WF16_Ingr, WF17_Ingr, WF18_Ingr,\
           WF19_Ingr, WF20_Ingr, WF21_Ingr, WF22_Ingr, WF23_Ingr, WF24_Ingr,\
           WG1_Ingr, WG2_Ingr, WG3_Ingr, WG4_Ingr, WG5_Ingr, WG6_Ingr,\
           WG7_Ingr, WG8_Ingr, WG9_Ingr, WG10_Ingr, WG11_Ingr, WG12_Ingr,\
           WG13_Ingr, WG14_Ingr, WG15_Ingr, WG16_Ingr, WG17_Ingr, WG18_Ingr,\
           WG19_Ingr, WG20_Ingr, WG21_Ingr, WG22_Ingr, WG23_Ingr, WG24_Ingr,\
           WH1_Ingr, WH2_Ingr, WH3_Ingr, WH4_Ingr, WH5_Ingr, WH6_Ingr,\
           WH7_Ingr, WH8_Ingr, WH9_Ingr, WH10_Ingr, WH11_Ingr, WH12_Ingr,\
           WH13_Ingr, WH14_Ingr, WH15_Ingr, WH16_Ingr, WH17_Ingr, WH18_Ingr,\
           WH19_Ingr, WH20_Ingr, WH21_Ingr, WH22_Ingr, WH23_Ingr, WH24_Ingr,\
           WI1_Ingr, WI2_Ingr, WI3_Ingr, WI4_Ingr, WI5_Ingr, WI6_Ingr,\
           WI7_Ingr, WI8_Ingr, WI9_Ingr, WI10_Ingr, WI11_Ingr, WI12_Ingr,\
           WI13_Ingr, WI14_Ingr, WI15_Ingr, WI16_Ingr, WI17_Ingr, WI18_Ingr,\
           WI19_Ingr, WI20_Ingr, WI21_Ingr, WI22_Ingr, WI23_Ingr, WI24_Ingr,\
           WJ1_Ingr, WJ2_Ingr, WJ3_Ingr, WJ4_Ingr, WJ5_Ingr, WJ6_Ingr,\
           WJ7_Ingr, WJ8_Ingr, WJ9_Ingr, WJ10_Ingr, WJ11_Ingr, WJ12_Ingr,\
           WJ13_Ingr, WJ14_Ingr, WJ15_Ingr, WJ16_Ingr, WJ17_Ingr, WJ18_Ingr,\
           WJ19_Ingr, WJ20_Ingr, WJ21_Ingr, WJ22_Ingr, WJ23_Ingr, WJ24_Ingr,\
           WK1_Ingr, WK2_Ingr, WK3_Ingr, WK4_Ingr, WK5_Ingr, WK6_Ingr,\
           WK7_Ingr, WK8_Ingr, WK9_Ingr, WK10_Ingr, WK11_Ingr, WK12_Ingr,\
           WK13_Ingr, WK14_Ingr, WK15_Ingr, WK16_Ingr, WK17_Ingr, WK18_Ingr,\
           WK19_Ingr, WK20_Ingr, WK21_Ingr, WK22_Ingr, WK23_Ingr, WK24_Ingr,\
           WL1_Ingr, WL2_Ingr, WL3_Ingr, WL4_Ingr, WL5_Ingr, WL6_Ingr,\
           WL7_Ingr, WL8_Ingr, WL9_Ingr, WL10_Ingr, WL11_Ingr, WL12_Ingr,\
           WL13_Ingr, WL14_Ingr, WL15_Ingr, WL16_Ingr, WL17_Ingr, WL18_Ingr,\
           WL19_Ingr, WL20_Ingr, WL21_Ingr, WL22_Ingr, WL23_Ingr, WL24_Ingr,\
           WM1_Ingr, WM2_Ingr, WM3_Ingr, WM4_Ingr, WM5_Ingr, WM6_Ingr,\
           WM7_Ingr, WM8_Ingr, WM9_Ingr, WM10_Ingr, WM11_Ingr, WM12_Ingr,\
           WM13_Ingr, WM14_Ingr, WM15_Ingr, WM16_Ingr, WM17_Ingr, WM18_Ingr,\
           WM19_Ingr, WM20_Ingr, WM21_Ingr, WM22_Ingr, WM23_Ingr, WM24_Ingr,\
           WN1_Ingr, WN2_Ingr, WN3_Ingr, WN4_Ingr, WN5_Ingr, WN6_Ingr,\
           WN7_Ingr, WN8_Ingr, WN9_Ingr, WN10_Ingr, WN11_Ingr, WN12_Ingr,\
           WN13_Ingr, WN14_Ingr, WN15_Ingr, WN16_Ingr, WN17_Ingr, WN18_Ingr,\
           WN19_Ingr, WN20_Ingr, WN21_Ingr, WN22_Ingr, WN23_Ingr, WN24_Ingr,\
           WO1_Ingr, WO2_Ingr, WO3_Ingr, WO4_Ingr, WO5_Ingr, WO6_Ingr,\
           WO7_Ingr, WO8_Ingr, WO9_Ingr, WO10_Ingr, WO11_Ingr, WO12_Ingr,\
           WO13_Ingr, WO14_Ingr, WO15_Ingr, WO16_Ingr, WO17_Ingr, WO18_Ingr,\
           WO19_Ingr, WO20_Ingr, WO21_Ingr, WO22_Ingr, WO23_Ingr, WO24_Ingr,\
           WP1_Ingr, WP2_Ingr, WP3_Ingr, WP4_Ingr, WP5_Ingr, WP6_Ingr,\
           WP7_Ingr, WP8_Ingr, WP9_Ingr, WP10_Ingr, WP11_Ingr, WP12_Ingr,\
           WP13_Ingr, WP14_Ingr, WP15_Ingr, WP16_Ingr, WP17_Ingr, WP18_Ingr,\
           WP19_Ingr, WP20_Ingr, WP21_Ingr, WP22_Ingr, WP23_Ingr, WP24_Ingr]

    SS_List = [WA1_SS, WA2_SS, WA3_SS, WA4_SS, WA5_SS, WA6_SS, WA7_SS, WA8_SS,\
           WA9_SS, WA10_SS, WA11_SS, WA12_SS, WA13_SS, WA14_SS, WA15_SS, WA16_SS,\
           WA17_SS, WA18_SS, WA19_SS, WA20_SS, WA21_SS, WA22_SS, WA23_SS, WA24_SS,\
           WB1_SS, WB2_SS, WB3_SS, WB4_SS, WB5_SS, WB6_SS, WB7_SS, WB8_SS,\
           WB9_SS, WB10_SS, WB11_SS, WB12_SS, WB13_SS, WB14_SS, WB15_SS, WB16_SS,\
           WB17_SS, WB18_SS, WB19_SS, WB20_SS, WB21_SS, WB22_SS, WB23_SS, WB24_SS,\
           WC1_SS, WC2_SS, WC3_SS, WC4_SS, WC5_SS, WC6_SS, WC7_SS, WC8_SS,\
           WC9_SS, WC10_SS, WC11_SS, WC12_SS, WC13_SS, WC14_SS, WC15_SS, WC16_SS,\
           WC17_SS, WC18_SS, WC19_SS, WC20_SS, WC21_SS, WC22_SS, WC23_SS, WC24_SS,\
           WD1_SS, WD2_SS, WD3_SS, WD4_SS, WD5_SS, WD6_SS, WD7_SS, WD8_SS,\
           WD9_SS, WD10_SS, WD11_SS, WD12_SS, WD13_SS, WD14_SS, WD15_SS, WD16_SS,\
           WD17_SS, WD18_SS, WD19_SS, WD20_SS, WD21_SS, WD22_SS, WD23_SS, WD24_SS,\
           WE1_SS, WE2_SS, WE3_SS, WE4_SS, WE5_SS, WE6_SS, WE7_SS, WE8_SS,\
           WE9_SS, WE10_SS, WE11_SS, WE12_SS, WE13_SS, WE14_SS, WE15_SS, WE16_SS,\
           WE17_SS, WE18_SS, WE19_SS, WE20_SS, WE21_SS, WE22_SS, WE23_SS, WE24_SS,\
           WF1_SS, WF2_SS, WF3_SS, WF4_SS, WF5_SS, WF6_SS, WF7_SS, WF8_SS,\
           WF9_SS, WF10_SS, WF11_SS, WF12_SS, WF13_SS, WF14_SS, WF15_SS, WF16_SS,\
           WF17_SS, WF18_SS, WF19_SS, WF20_SS, WF21_SS, WF22_SS, WF23_SS, WF24_SS,\
           WG1_SS, WG2_SS, WG3_SS, WG4_SS, WG5_SS, WG6_SS, WG7_SS, WG8_SS,\
           WG9_SS, WG10_SS, WG11_SS, WG12_SS, WG13_SS, WG14_SS, WG15_SS, WG16_SS,\
           WG17_SS, WG18_SS, WG19_SS, WG20_SS, WG21_SS, WG22_SS, WG23_SS, WG24_SS,\
           WH1_SS, WH2_SS, WH3_SS, WH4_SS, WH5_SS, WH6_SS, WH7_SS, WH8_SS,\
           WH9_SS, WH10_SS, WH11_SS, WH12_SS, WH13_SS, WH14_SS, WH15_SS, WH16_SS,\
           WH17_SS, WH18_SS, WH19_SS, WH20_SS, WH21_SS, WH22_SS, WH23_SS, WH24_SS,\
           WI1_SS, WI2_SS, WI3_SS, WI4_SS, WI5_SS, WI6_SS, WI7_SS, WI8_SS,\
           WI9_SS, WI10_SS, WI11_SS, WI12_SS, WI13_SS, WI14_SS, WI15_SS, WI16_SS,\
           WI17_SS, WI18_SS, WI19_SS, WI20_SS, WI21_SS, WI22_SS, WI23_SS, WI24_SS,\
           WJ1_SS, WJ2_SS, WJ3_SS, WJ4_SS, WJ5_SS, WJ6_SS, WJ7_SS, WJ8_SS,\
           WJ9_SS, WJ10_SS, WJ11_SS, WJ12_SS, WJ13_SS, WJ14_SS, WJ15_SS, WJ16_SS,\
           WJ17_SS, WJ18_SS, WJ19_SS, WJ20_SS, WJ21_SS, WJ22_SS, WJ23_SS, WJ24_SS,\
           WK1_SS, WK2_SS, WK3_SS, WK4_SS, WK5_SS, WK6_SS, WK7_SS, WK8_SS,\
           WK9_SS, WK10_SS, WK11_SS, WK12_SS, WK13_SS, WK14_SS, WK15_SS, WK16_SS,\
           WK17_SS, WK18_SS, WK19_SS, WK20_SS, WK21_SS, WK22_SS, WK23_SS, WK24_SS,\
           WL1_SS, WL2_SS, WL3_SS, WL4_SS, WL5_SS, WL6_SS, WL7_SS, WL8_SS,\
           WL9_SS, WL10_SS, WL11_SS, WL12_SS, WL13_SS, WL14_SS, WL15_SS, WL16_SS,\
           WL17_SS, WL18_SS, WL19_SS, WL20_SS, WL21_SS, WL22_SS, WL23_SS, WL24_SS,\
           WM1_SS, WM2_SS, WM3_SS, WM4_SS, WM5_SS, WM6_SS, WM7_SS, WM8_SS,\
           WM9_SS, WM10_SS, WM11_SS, WM12_SS, WM13_SS, WM14_SS, WM15_SS, WM16_SS,\
           WM17_SS, WM18_SS, WM19_SS, WM20_SS, WM21_SS, WM22_SS, WM23_SS, WM24_SS,\
           WN1_SS, WN2_SS, WN3_SS, WN4_SS, WN5_SS, WN6_SS, WN7_SS, WN8_SS,\
           WN9_SS, WN10_SS, WN11_SS, WN12_SS, WN13_SS, WN14_SS, WN15_SS, WN16_SS,\
           WN17_SS, WN18_SS, WN19_SS, WN20_SS, WN21_SS, WN22_SS, WN23_SS, WN24_SS,\
           WO1_SS, WO2_SS, WO3_SS, WO4_SS, WO5_SS, WO6_SS, WO7_SS, WO8_SS,\
           WO9_SS, WO10_SS, WO11_SS, WO12_SS, WO13_SS, WO14_SS, WO15_SS, WO16_SS,\
           WO17_SS, WO18_SS, WO19_SS, WO20_SS, WO21_SS, WO22_SS, WO23_SS, WO24_SS,\
           WP1_SS, WP2_SS, WP3_SS, WP4_SS, WP5_SS, WP6_SS, WP7_SS, WP8_SS,\
           WP9_SS, WP10_SS, WP11_SS, WP12_SS, WP13_SS, WP14_SS, WP15_SS, WP16_SS,\
           WP17_SS, WP18_SS, WP19_SS, WP20_SS, WP21_SS, WP22_SS, WP23_SS, WP24_SS]
    
    Dilu_List = [WA1_Dilu, WA2_Dilu, WA3_Dilu, WA4_Dilu, WA5_Dilu, WA6_Dilu, WA7_Dilu, WA8_Dilu,\
               WA9_Dilu, WA10_Dilu, WA11_Dilu, WA12_Dilu, WA13_Dilu, WA14_Dilu, WA15_Dilu, WA16_Dilu,\
               WA17_Dilu, WA18_Dilu, WA19_Dilu, WA20_Dilu, WA21_Dilu, WA22_Dilu, WA23_Dilu, WA24_Dilu,\
               WB1_Dilu, WB2_Dilu, WB3_Dilu, WB4_Dilu, WB5_Dilu, WB6_Dilu, WB7_Dilu, WB8_Dilu,\
               WB9_Dilu, WB10_Dilu, WB11_Dilu, WB12_Dilu, WB13_Dilu, WB14_Dilu, WB15_Dilu, WB16_Dilu,\
               WB17_Dilu, WB18_Dilu, WB19_Dilu, WB20_Dilu, WB21_Dilu, WB22_Dilu, WB23_Dilu, WB24_Dilu,\
               WC1_Dilu, WC2_Dilu, WC3_Dilu, WC4_Dilu, WC5_Dilu, WC6_Dilu, WC7_Dilu, WC8_Dilu,\
               WC9_Dilu, WC10_Dilu, WC11_Dilu, WC12_Dilu, WC13_Dilu, WC14_Dilu, WC15_Dilu, WC16_Dilu,\
               WC17_Dilu, WC18_Dilu, WC19_Dilu, WC20_Dilu, WC21_Dilu, WC22_Dilu, WC23_Dilu, WC24_Dilu,\
               WD1_Dilu, WD2_Dilu, WD3_Dilu, WD4_Dilu, WD5_Dilu, WD6_Dilu, WD7_Dilu, WD8_Dilu,\
               WD9_Dilu, WD10_Dilu, WD11_Dilu, WD12_Dilu, WD13_Dilu, WD14_Dilu, WD15_Dilu, WD16_Dilu,\
               WD17_Dilu, WD18_Dilu, WD19_Dilu, WD20_Dilu, WD21_Dilu, WD22_Dilu, WD23_Dilu, WD24_Dilu,\
               WE1_Dilu, WE2_Dilu, WE3_Dilu, WE4_Dilu, WE5_Dilu, WE6_Dilu, WE7_Dilu, WE8_Dilu,\
               WE9_Dilu, WE10_Dilu, WE11_Dilu, WE12_Dilu, WE13_Dilu, WE14_Dilu, WE15_Dilu, WE16_Dilu,\
               WE17_Dilu, WE18_Dilu, WE19_Dilu, WE20_Dilu, WE21_Dilu, WE22_Dilu, WE23_Dilu, WE24_Dilu,\
               WF1_Dilu, WF2_Dilu, WF3_Dilu, WF4_Dilu, WF5_Dilu, WF6_Dilu, WF7_Dilu, WF8_Dilu,\
               WF9_Dilu, WF10_Dilu, WF11_Dilu, WF12_Dilu, WF13_Dilu, WF14_Dilu, WF15_Dilu, WF16_Dilu,\
               WF17_Dilu, WF18_Dilu, WF19_Dilu, WF20_Dilu, WF21_Dilu, WF22_Dilu, WF23_Dilu, WF24_Dilu,\
               WG1_Dilu, WG2_Dilu, WG3_Dilu, WG4_Dilu, WG5_Dilu, WG6_Dilu, WG7_Dilu, WG8_Dilu,\
               WG9_Dilu, WG10_Dilu, WG11_Dilu, WG12_Dilu, WG13_Dilu, WG14_Dilu, WG15_Dilu, WG16_Dilu,\
               WG17_Dilu, WG18_Dilu, WG19_Dilu, WG20_Dilu, WG21_Dilu, WG22_Dilu, WG23_Dilu, WG24_Dilu,\
               WH1_Dilu, WH2_Dilu, WH3_Dilu, WH4_Dilu, WH5_Dilu, WH6_Dilu, WH7_Dilu, WH8_Dilu,\
               WH9_Dilu, WH10_Dilu, WH11_Dilu, WH12_Dilu, WH13_Dilu, WH14_Dilu, WH15_Dilu, WH16_Dilu,\
               WH17_Dilu, WH18_Dilu, WH19_Dilu, WH20_Dilu, WH21_Dilu, WH22_Dilu, WH23_Dilu, WH24_Dilu,\
               WI1_Dilu, WI2_Dilu, WI3_Dilu, WI4_Dilu, WI5_Dilu, WI6_Dilu, WI7_Dilu, WI8_Dilu,\
               WI9_Dilu, WI10_Dilu, WI11_Dilu, WI12_Dilu, WI13_Dilu, WI14_Dilu, WI15_Dilu, WI16_Dilu,\
               WI17_Dilu, WI18_Dilu, WI19_Dilu, WI20_Dilu, WI21_Dilu, WI22_Dilu, WI23_Dilu, WI24_Dilu,\
               WJ1_Dilu, WJ2_Dilu, WJ3_Dilu, WJ4_Dilu, WJ5_Dilu, WJ6_Dilu, WJ7_Dilu, WJ8_Dilu,\
               WJ9_Dilu, WJ10_Dilu, WJ11_Dilu, WJ12_Dilu, WJ13_Dilu, WJ14_Dilu, WJ15_Dilu, WJ16_Dilu,\
               WJ17_Dilu, WJ18_Dilu, WJ19_Dilu, WJ20_Dilu, WJ21_Dilu, WJ22_Dilu, WJ23_Dilu, WJ24_Dilu,\
               WK1_Dilu, WK2_Dilu, WK3_Dilu, WK4_Dilu, WK5_Dilu, WK6_Dilu, WK7_Dilu, WK8_Dilu,\
               WK9_Dilu, WK10_Dilu, WK11_Dilu, WK12_Dilu, WK13_Dilu, WK14_Dilu, WK15_Dilu, WK16_Dilu,\
               WK17_Dilu, WK18_Dilu, WK19_Dilu, WK20_Dilu, WK21_Dilu, WK22_Dilu, WK23_Dilu, WK24_Dilu,\
               WL1_Dilu, WL2_Dilu, WL3_Dilu, WL4_Dilu, WL5_Dilu, WL6_Dilu, WL7_Dilu, WL8_Dilu,\
               WL9_Dilu, WL10_Dilu, WL11_Dilu, WL12_Dilu, WL13_Dilu, WL14_Dilu, WL15_Dilu, WL16_Dilu,\
               WL17_Dilu, WL18_Dilu, WL19_Dilu, WL20_Dilu, WL21_Dilu, WL22_Dilu, WL23_Dilu, WL24_Dilu,\
               WM1_Dilu, WM2_Dilu, WM3_Dilu, WM4_Dilu, WM5_Dilu, WM6_Dilu, WM7_Dilu, WM8_Dilu,\
               WM9_Dilu, WM10_Dilu, WM11_Dilu, WM12_Dilu, WM13_Dilu, WM14_Dilu, WM15_Dilu, WM16_Dilu,\
               WM17_Dilu, WM18_Dilu, WM19_Dilu, WM20_Dilu, WM21_Dilu, WM22_Dilu, WM23_Dilu, WM24_Dilu,\
               WN1_Dilu, WN2_Dilu, WN3_Dilu, WN4_Dilu, WN5_Dilu, WN6_Dilu, WN7_Dilu, WN8_Dilu,\
               WN9_Dilu, WN10_Dilu, WN11_Dilu, WN12_Dilu, WN13_Dilu, WN14_Dilu, WN15_Dilu, WN16_Dilu,\
               WN17_Dilu, WN18_Dilu, WN19_Dilu, WN20_Dilu, WN21_Dilu, WN22_Dilu, WN23_Dilu, WN24_Dilu,\
               WO1_Dilu, WO2_Dilu, WO3_Dilu, WO4_Dilu, WO5_Dilu, WO6_Dilu, WO7_Dilu, WO8_Dilu,\
               WO9_Dilu, WO10_Dilu, WO11_Dilu, WO12_Dilu, WO13_Dilu, WO14_Dilu, WO15_Dilu, WO16_Dilu,\
               WO17_Dilu, WO18_Dilu, WO19_Dilu, WO20_Dilu, WO21_Dilu, WO22_Dilu, WO23_Dilu, WO24_Dilu,\
               WP1_Dilu, WP2_Dilu, WP3_Dilu, WP4_Dilu, WP5_Dilu, WP6_Dilu, WP7_Dilu, WP8_Dilu,\
               WP9_Dilu, WP10_Dilu, WP11_Dilu, WP12_Dilu, WP13_Dilu, WP14_Dilu, WP15_Dilu, WP16_Dilu,\
               WP17_Dilu, WP18_Dilu, WP19_Dilu, WP20_Dilu, WP21_Dilu, WP22_Dilu, WP23_Dilu, WP24_Dilu]

    IngrMenu_List = [WA1_IngrMenu, WA2_IngrMenu, WA3_IngrMenu, WA4_IngrMenu, WA5_IngrMenu, WA6_IngrMenu,\
                   WA7_IngrMenu, WA8_IngrMenu, WA9_IngrMenu, WA10_IngrMenu, WA11_IngrMenu, WA12_IngrMenu,\
                   WA13_IngrMenu, WA14_IngrMenu, WA15_IngrMenu, WA16_IngrMenu, WA17_IngrMenu, WA18_IngrMenu,\
                   WA19_IngrMenu, WA20_IngrMenu, WA21_IngrMenu, WA22_IngrMenu, WA23_IngrMenu, WA24_IngrMenu,\
                   WB1_IngrMenu, WB2_IngrMenu, WB3_IngrMenu, WB4_IngrMenu, WB5_IngrMenu, WB6_IngrMenu,\
                   WB7_IngrMenu, WB8_IngrMenu, WB9_IngrMenu, WB10_IngrMenu, WB11_IngrMenu, WB12_IngrMenu,\
                   WB13_IngrMenu, WB14_IngrMenu, WB15_IngrMenu, WB16_IngrMenu, WB17_IngrMenu, WB18_IngrMenu,\
                   WB19_IngrMenu, WB20_IngrMenu, WB21_IngrMenu, WB22_IngrMenu, WB23_IngrMenu, WB24_IngrMenu,\
                   WC1_IngrMenu, WC2_IngrMenu, WC3_IngrMenu, WC4_IngrMenu, WC5_IngrMenu, WC6_IngrMenu,\
                   WC7_IngrMenu, WC8_IngrMenu, WC9_IngrMenu, WC10_IngrMenu, WC11_IngrMenu, WC12_IngrMenu,\
                   WC13_IngrMenu, WC14_IngrMenu, WC15_IngrMenu, WC16_IngrMenu, WC17_IngrMenu, WC18_IngrMenu,\
                   WC19_IngrMenu, WC20_IngrMenu, WC21_IngrMenu, WC22_IngrMenu, WC23_IngrMenu, WC24_IngrMenu,\
                   WD1_IngrMenu, WD2_IngrMenu, WD3_IngrMenu, WD4_IngrMenu, WD5_IngrMenu, WD6_IngrMenu,\
                   WD7_IngrMenu, WD8_IngrMenu, WD9_IngrMenu, WD10_IngrMenu, WD11_IngrMenu, WD12_IngrMenu,\
                   WD13_IngrMenu, WD14_IngrMenu, WD15_IngrMenu, WD16_IngrMenu, WD17_IngrMenu, WD18_IngrMenu,\
                   WD19_IngrMenu, WD20_IngrMenu, WD21_IngrMenu, WD22_IngrMenu, WD23_IngrMenu, WD24_IngrMenu,\
                   WE1_IngrMenu, WE2_IngrMenu, WE3_IngrMenu, WE4_IngrMenu, WE5_IngrMenu, WE6_IngrMenu,\
                   WE7_IngrMenu, WE8_IngrMenu, WE9_IngrMenu, WE10_IngrMenu, WE11_IngrMenu, WE12_IngrMenu,\
                   WE13_IngrMenu, WE14_IngrMenu, WE15_IngrMenu, WE16_IngrMenu, WE17_IngrMenu, WE18_IngrMenu,\
                   WE19_IngrMenu, WE20_IngrMenu, WE21_IngrMenu, WE22_IngrMenu, WE23_IngrMenu, WE24_IngrMenu,\
                   WF1_IngrMenu, WF2_IngrMenu, WF3_IngrMenu, WF4_IngrMenu, WF5_IngrMenu, WF6_IngrMenu,\
                   WF7_IngrMenu, WF8_IngrMenu, WF9_IngrMenu, WF10_IngrMenu, WF11_IngrMenu, WF12_IngrMenu,\
                   WF13_IngrMenu, WF14_IngrMenu, WF15_IngrMenu, WF16_IngrMenu, WF17_IngrMenu, WF18_IngrMenu,\
                   WF19_IngrMenu, WF20_IngrMenu, WF21_IngrMenu, WF22_IngrMenu, WF23_IngrMenu, WF24_IngrMenu,\
                   WG1_IngrMenu, WG2_IngrMenu, WG3_IngrMenu, WG4_IngrMenu, WG5_IngrMenu, WG6_IngrMenu,\
                   WG7_IngrMenu, WG8_IngrMenu, WG9_IngrMenu, WG10_IngrMenu, WG11_IngrMenu, WG12_IngrMenu,\
                   WG13_IngrMenu, WG14_IngrMenu, WG15_IngrMenu, WG16_IngrMenu, WG17_IngrMenu, WG18_IngrMenu,\
                   WG19_IngrMenu, WG20_IngrMenu, WG21_IngrMenu, WG22_IngrMenu, WG23_IngrMenu, WG24_IngrMenu,\
                   WH1_IngrMenu, WH2_IngrMenu, WH3_IngrMenu, WH4_IngrMenu, WH5_IngrMenu, WH6_IngrMenu,\
                   WH7_IngrMenu, WH8_IngrMenu, WH9_IngrMenu, WH10_IngrMenu, WH11_IngrMenu, WH12_IngrMenu,\
                   WH13_IngrMenu, WH14_IngrMenu, WH15_IngrMenu, WH16_IngrMenu, WH17_IngrMenu, WH18_IngrMenu,\
                   WH19_IngrMenu, WH20_IngrMenu, WH21_IngrMenu, WH22_IngrMenu, WH23_IngrMenu, WH24_IngrMenu,\
                   WI1_IngrMenu, WI2_IngrMenu, WI3_IngrMenu, WI4_IngrMenu, WI5_IngrMenu, WI6_IngrMenu,\
                   WI7_IngrMenu, WI8_IngrMenu, WI9_IngrMenu, WI10_IngrMenu, WI11_IngrMenu, WI12_IngrMenu,\
                   WI13_IngrMenu, WI14_IngrMenu, WI15_IngrMenu, WI16_IngrMenu, WI17_IngrMenu, WI18_IngrMenu,\
                   WI19_IngrMenu, WI20_IngrMenu, WI21_IngrMenu, WI22_IngrMenu, WI23_IngrMenu, WI24_IngrMenu,\
                   WJ1_IngrMenu, WJ2_IngrMenu, WJ3_IngrMenu, WJ4_IngrMenu, WJ5_IngrMenu, WJ6_IngrMenu,\
                   WJ7_IngrMenu, WJ8_IngrMenu, WJ9_IngrMenu, WJ10_IngrMenu, WJ11_IngrMenu, WJ12_IngrMenu,\
                   WJ13_IngrMenu, WJ14_IngrMenu, WJ15_IngrMenu, WJ16_IngrMenu, WJ17_IngrMenu, WJ18_IngrMenu,\
                   WJ19_IngrMenu, WJ20_IngrMenu, WJ21_IngrMenu, WJ22_IngrMenu, WJ23_IngrMenu, WJ24_IngrMenu,\
                   WK1_IngrMenu, WK2_IngrMenu, WK3_IngrMenu, WK4_IngrMenu, WK5_IngrMenu, WK6_IngrMenu,\
                   WK7_IngrMenu, WK8_IngrMenu, WK9_IngrMenu, WK10_IngrMenu, WK11_IngrMenu, WK12_IngrMenu,\
                   WK13_IngrMenu, WK14_IngrMenu, WK15_IngrMenu, WK16_IngrMenu, WK17_IngrMenu, WK18_IngrMenu,\
                   WK19_IngrMenu, WK20_IngrMenu, WK21_IngrMenu, WK22_IngrMenu, WK23_IngrMenu, WK24_IngrMenu,\
                   WL1_IngrMenu, WL2_IngrMenu, WL3_IngrMenu, WL4_IngrMenu, WL5_IngrMenu, WL6_IngrMenu,\
                   WL7_IngrMenu, WL8_IngrMenu, WL9_IngrMenu, WL10_IngrMenu, WL11_IngrMenu, WL12_IngrMenu,\
                   WL13_IngrMenu, WL14_IngrMenu, WL15_IngrMenu, WL16_IngrMenu, WL17_IngrMenu, WL18_IngrMenu,\
                   WL19_IngrMenu, WL20_IngrMenu, WL21_IngrMenu, WL22_IngrMenu, WL23_IngrMenu, WL24_IngrMenu,\
                   WM1_IngrMenu, WM2_IngrMenu, WM3_IngrMenu, WM4_IngrMenu, WM5_IngrMenu, WM6_IngrMenu,\
                   WM7_IngrMenu, WM8_IngrMenu, WM9_IngrMenu, WM10_IngrMenu, WM11_IngrMenu, WM12_IngrMenu,\
                   WM13_IngrMenu, WM14_IngrMenu, WM15_IngrMenu, WM16_IngrMenu, WM17_IngrMenu, WM18_IngrMenu,\
                   WM19_IngrMenu, WM20_IngrMenu, WM21_IngrMenu, WM22_IngrMenu, WM23_IngrMenu, WM24_IngrMenu,\
                   WN1_IngrMenu, WN2_IngrMenu, WN3_IngrMenu, WN4_IngrMenu, WN5_IngrMenu, WN6_IngrMenu,\
                   WN7_IngrMenu, WN8_IngrMenu, WN9_IngrMenu, WN10_IngrMenu, WN11_IngrMenu, WN12_IngrMenu,\
                   WN13_IngrMenu, WN14_IngrMenu, WN15_IngrMenu, WN16_IngrMenu, WN17_IngrMenu, WN18_IngrMenu,\
                   WN19_IngrMenu, WN20_IngrMenu, WN21_IngrMenu, WN22_IngrMenu, WN23_IngrMenu, WN24_IngrMenu,
                   WO1_IngrMenu, WO2_IngrMenu, WO3_IngrMenu, WO4_IngrMenu, WO5_IngrMenu, WO6_IngrMenu,\
                   WO7_IngrMenu, WO8_IngrMenu, WO9_IngrMenu, WO10_IngrMenu, WO11_IngrMenu, WO12_IngrMenu,\
                   WO13_IngrMenu, WO14_IngrMenu, WO15_IngrMenu, WO16_IngrMenu, WO17_IngrMenu, WO18_IngrMenu,\
                   WO19_IngrMenu, WO20_IngrMenu, WO21_IngrMenu, WO22_IngrMenu, WO23_IngrMenu, WO24_IngrMenu,\
                   WP1_IngrMenu, WP2_IngrMenu, WP3_IngrMenu, WP4_IngrMenu, WP5_IngrMenu, WP6_IngrMenu,\
                   WP7_IngrMenu, WP8_IngrMenu, WP9_IngrMenu, WP10_IngrMenu, WP11_IngrMenu, WP12_IngrMenu,\
                   WP13_IngrMenu, WP14_IngrMenu, WP15_IngrMenu, WP16_IngrMenu, WP17_IngrMenu, WP18_IngrMenu,\
                   WP19_IngrMenu, WP20_IngrMenu, WP21_IngrMenu, WP22_IngrMenu, WP23_IngrMenu, WP24_IngrMenu]

    SSMenu_List = [WA1_SSMenu, WA2_SSMenu, WA3_SSMenu, WA4_SSMenu, WA5_SSMenu, WA6_SSMenu, WA7_SSMenu, WA8_SSMenu,\
           WA9_SSMenu, WA10_SSMenu, WA11_SSMenu, WA12_SSMenu, WA13_SSMenu, WA14_SSMenu, WA15_SSMenu, WA16_SSMenu,\
           WA17_SSMenu, WA18_SSMenu, WA19_SSMenu, WA20_SSMenu, WA21_SSMenu, WA22_SSMenu, WA23_SSMenu, WA24_SSMenu,\
           WB1_SSMenu, WB2_SSMenu, WB3_SSMenu, WB4_SSMenu, WB5_SSMenu, WB6_SSMenu, WB7_SSMenu, WB8_SSMenu,\
           WB9_SSMenu, WB10_SSMenu, WB11_SSMenu, WB12_SSMenu, WB13_SSMenu, WB14_SSMenu, WB15_SSMenu, WB16_SSMenu,\
           WB17_SSMenu, WB18_SSMenu, WB19_SSMenu, WB20_SSMenu, WB21_SSMenu, WB22_SSMenu, WB23_SSMenu, WB24_SSMenu,\
           WC1_SSMenu, WC2_SSMenu, WC3_SSMenu, WC4_SSMenu, WC5_SSMenu, WC6_SSMenu, WC7_SSMenu, WC8_SSMenu,\
           WC9_SSMenu, WC10_SSMenu, WC11_SSMenu, WC12_SSMenu, WC13_SSMenu, WC14_SSMenu, WC15_SSMenu, WC16_SSMenu,\
           WC17_SSMenu, WC18_SSMenu, WC19_SSMenu, WC20_SSMenu, WC21_SSMenu, WC22_SSMenu, WC23_SSMenu, WC24_SSMenu,\
           WD1_SSMenu, WD2_SSMenu, WD3_SSMenu, WD4_SSMenu, WD5_SSMenu, WD6_SSMenu, WD7_SSMenu, WD8_SSMenu,\
           WD9_SSMenu, WD10_SSMenu, WD11_SSMenu, WD12_SSMenu, WD13_SSMenu, WD14_SSMenu, WD15_SSMenu, WD16_SSMenu,\
           WD17_SSMenu, WD18_SSMenu, WD19_SSMenu, WD20_SSMenu, WD21_SSMenu, WD22_SSMenu, WD23_SSMenu, WD24_SSMenu,\
           WE1_SSMenu, WE2_SSMenu, WE3_SSMenu, WE4_SSMenu, WE5_SSMenu, WE6_SSMenu, WE7_SSMenu, WE8_SSMenu,\
           WE9_SSMenu, WE10_SSMenu, WE11_SSMenu, WE12_SSMenu, WE13_SSMenu, WE14_SSMenu, WE15_SSMenu, WE16_SSMenu,\
           WE17_SSMenu, WE18_SSMenu, WE19_SSMenu, WE20_SSMenu, WE21_SSMenu, WE22_SSMenu, WE23_SSMenu, WE24_SSMenu,\
           WF1_SSMenu, WF2_SSMenu, WF3_SSMenu, WF4_SSMenu, WF5_SSMenu, WF6_SSMenu, WF7_SSMenu, WF8_SSMenu,\
           WF9_SSMenu, WF10_SSMenu, WF11_SSMenu, WF12_SSMenu, WF13_SSMenu, WF14_SSMenu, WF15_SSMenu, WF16_SSMenu,\
           WF17_SSMenu, WF18_SSMenu, WF19_SSMenu, WF20_SSMenu, WF21_SSMenu, WF22_SSMenu, WF23_SSMenu, WF24_SSMenu,\
           WG1_SSMenu, WG2_SSMenu, WG3_SSMenu, WG4_SSMenu, WG5_SSMenu, WG6_SSMenu, WG7_SSMenu, WG8_SSMenu,\
           WG9_SSMenu, WG10_SSMenu, WG11_SSMenu, WG12_SSMenu, WG13_SSMenu, WG14_SSMenu, WG15_SSMenu, WG16_SSMenu,\
           WG17_SSMenu, WG18_SSMenu, WG19_SSMenu, WG20_SSMenu, WG21_SSMenu, WG22_SSMenu, WG23_SSMenu, WG24_SSMenu,\
           WH1_SSMenu, WH2_SSMenu, WH3_SSMenu, WH4_SSMenu, WH5_SSMenu, WH6_SSMenu, WH7_SSMenu, WH8_SSMenu,\
           WH9_SSMenu, WH10_SSMenu, WH11_SSMenu, WH12_SSMenu, WH13_SSMenu, WH14_SSMenu, WH15_SSMenu, WH16_SSMenu,\
           WH17_SSMenu, WH18_SSMenu, WH19_SSMenu, WH20_SSMenu, WH21_SSMenu, WH22_SSMenu, WH23_SSMenu, WH24_SSMenu,\
           WI1_SSMenu, WI2_SSMenu, WI3_SSMenu, WI4_SSMenu, WI5_SSMenu, WI6_SSMenu, WI7_SSMenu, WI8_SSMenu,\
           WI9_SSMenu, WI10_SSMenu, WI11_SSMenu, WI12_SSMenu, WI13_SSMenu, WI14_SSMenu, WI15_SSMenu, WI16_SSMenu,\
           WI17_SSMenu, WI18_SSMenu, WI19_SSMenu, WI20_SSMenu, WI21_SSMenu, WI22_SSMenu, WI23_SSMenu, WI24_SSMenu,\
           WJ1_SSMenu, WJ2_SSMenu, WJ3_SSMenu, WJ4_SSMenu, WJ5_SSMenu, WJ6_SSMenu, WJ7_SSMenu, WJ8_SSMenu,\
           WJ9_SSMenu, WJ10_SSMenu, WJ11_SSMenu, WJ12_SSMenu, WJ13_SSMenu, WJ14_SSMenu, WJ15_SSMenu, WJ16_SSMenu,\
           WJ17_SSMenu, WJ18_SSMenu, WJ19_SSMenu, WJ20_SSMenu, WJ21_SSMenu, WJ22_SSMenu, WJ23_SSMenu, WJ24_SSMenu,\
           WK1_SSMenu, WK2_SSMenu, WK3_SSMenu, WK4_SSMenu, WK5_SSMenu, WK6_SSMenu, WK7_SSMenu, WK8_SSMenu,\
           WK9_SSMenu, WK10_SSMenu, WK11_SSMenu, WK12_SSMenu, WK13_SSMenu, WK14_SSMenu, WK15_SSMenu, WK16_SSMenu,\
           WK17_SSMenu, WK18_SSMenu, WK19_SSMenu, WK20_SSMenu, WK21_SSMenu, WK22_SSMenu, WK23_SSMenu, WK24_SSMenu,\
           WL1_SSMenu, WL2_SSMenu, WL3_SSMenu, WL4_SSMenu, WL5_SSMenu, WL6_SSMenu, WL7_SSMenu, WL8_SSMenu,\
           WL9_SSMenu, WL10_SSMenu, WL11_SSMenu, WL12_SSMenu, WL13_SSMenu, WL14_SSMenu, WL15_SSMenu, WL16_SSMenu,\
           WL17_SSMenu, WL18_SSMenu, WL19_SSMenu, WL20_SSMenu, WL21_SSMenu, WL22_SSMenu, WL23_SSMenu, WL24_SSMenu,\
           WM1_SSMenu, WM2_SSMenu, WM3_SSMenu, WM4_SSMenu, WM5_SSMenu, WM6_SSMenu, WM7_SSMenu, WM8_SSMenu,\
           WM9_SSMenu, WM10_SSMenu, WM11_SSMenu, WM12_SSMenu, WM13_SSMenu, WM14_SSMenu, WM15_SSMenu, WM16_SSMenu,\
           WM17_SSMenu, WM18_SSMenu, WM19_SSMenu, WM20_SSMenu, WM21_SSMenu, WM22_SSMenu, WM23_SSMenu, WM24_SSMenu,\
           WN1_SSMenu, WN2_SSMenu, WN3_SSMenu, WN4_SSMenu, WN5_SSMenu, WN6_SSMenu, WN7_SSMenu, WN8_SSMenu,\
           WN9_SSMenu, WN10_SSMenu, WN11_SSMenu, WN12_SSMenu, WN13_SSMenu, WN14_SSMenu, WN15_SSMenu, WN16_SSMenu,\
           WN17_SSMenu, WN18_SSMenu, WN19_SSMenu, WN20_SSMenu, WN21_SSMenu, WN22_SSMenu, WN23_SSMenu, WN24_SSMenu,\
           WO1_SSMenu, WO2_SSMenu, WO3_SSMenu, WO4_SSMenu, WO5_SSMenu, WO6_SSMenu, WO7_SSMenu, WO8_SSMenu,\
           WO9_SSMenu, WO10_SSMenu, WO11_SSMenu, WO12_SSMenu, WO13_SSMenu, WO14_SSMenu, WO15_SSMenu, WO16_SSMenu,\
           WO17_SSMenu, WO18_SSMenu, WO19_SSMenu, WO20_SSMenu, WO21_SSMenu, WO22_SSMenu, WO23_SSMenu, WO24_SSMenu,\
           WP1_SSMenu, WP2_SSMenu, WP3_SSMenu, WP4_SSMenu, WP5_SSMenu, WP6_SSMenu, WP7_SSMenu, WP8_SSMenu,\
           WP9_SSMenu, WP10_SSMenu, WP11_SSMenu, WP12_SSMenu, WP13_SSMenu, WP14_SSMenu, WP15_SSMenu, WP16_SSMenu,\
           WP17_SSMenu, WP18_SSMenu, WP19_SSMenu, WP20_SSMenu, WP21_SSMenu, WP22_SSMenu, WP23_SSMenu, WP24_SSMenu]

    DiluMenu_List = [WA1_DiluMenu, WA2_DiluMenu, WA3_DiluMenu, WA4_DiluMenu, WA5_DiluMenu, WA6_DiluMenu, WA7_DiluMenu, WA8_DiluMenu,\
           WA9_DiluMenu, WA10_DiluMenu, WA11_DiluMenu, WA12_DiluMenu, WA13_DiluMenu, WA14_DiluMenu, WA15_DiluMenu, WA16_DiluMenu,\
           WA17_DiluMenu, WA18_DiluMenu, WA19_DiluMenu, WA20_DiluMenu, WA21_DiluMenu, WA22_DiluMenu, WA23_DiluMenu, WA24_DiluMenu,\
           WB1_DiluMenu, WB2_DiluMenu, WB3_DiluMenu, WB4_DiluMenu, WB5_DiluMenu, WB6_DiluMenu, WB7_DiluMenu, WB8_DiluMenu,\
           WB9_DiluMenu, WB10_DiluMenu, WB11_DiluMenu, WB12_DiluMenu, WB13_DiluMenu, WB14_DiluMenu, WB15_DiluMenu, WB16_DiluMenu,\
           WB17_DiluMenu, WB18_DiluMenu, WB19_DiluMenu, WB20_DiluMenu, WB21_DiluMenu, WB22_DiluMenu, WB23_DiluMenu, WB24_DiluMenu,\
           WC1_DiluMenu, WC2_DiluMenu, WC3_DiluMenu, WC4_DiluMenu, WC5_DiluMenu, WC6_DiluMenu, WC7_DiluMenu, WC8_DiluMenu,\
           WC9_DiluMenu, WC10_DiluMenu, WC11_DiluMenu, WC12_DiluMenu, WC13_DiluMenu, WC14_DiluMenu, WC15_DiluMenu, WC16_DiluMenu,\
           WC17_DiluMenu, WC18_DiluMenu, WC19_DiluMenu, WC20_DiluMenu, WC21_DiluMenu, WC22_DiluMenu, WC23_DiluMenu, WC24_DiluMenu,\
           WD1_DiluMenu, WD2_DiluMenu, WD3_DiluMenu, WD4_DiluMenu, WD5_DiluMenu, WD6_DiluMenu, WD7_DiluMenu, WD8_DiluMenu,\
           WD9_DiluMenu, WD10_DiluMenu, WD11_DiluMenu, WD12_DiluMenu, WD13_DiluMenu, WD14_DiluMenu, WD15_DiluMenu, WD16_DiluMenu,\
           WD17_DiluMenu, WD18_DiluMenu, WD19_DiluMenu, WD20_DiluMenu, WD21_DiluMenu, WD22_DiluMenu, WD23_DiluMenu, WD24_DiluMenu,\
           WE1_DiluMenu, WE2_DiluMenu, WE3_DiluMenu, WE4_DiluMenu, WE5_DiluMenu, WE6_DiluMenu, WE7_DiluMenu, WE8_DiluMenu,\
           WE9_DiluMenu, WE10_DiluMenu, WE11_DiluMenu, WE12_DiluMenu, WE13_DiluMenu, WE14_DiluMenu, WE15_DiluMenu, WE16_DiluMenu,\
           WE17_DiluMenu, WE18_DiluMenu, WE19_DiluMenu, WE20_DiluMenu, WE21_DiluMenu, WE22_DiluMenu, WE23_DiluMenu, WE24_DiluMenu,\
           WF1_DiluMenu, WF2_DiluMenu, WF3_DiluMenu, WF4_DiluMenu, WF5_DiluMenu, WF6_DiluMenu, WF7_DiluMenu, WF8_DiluMenu,\
           WF9_DiluMenu, WF10_DiluMenu, WF11_DiluMenu, WF12_DiluMenu, WF13_DiluMenu, WF14_DiluMenu, WF15_DiluMenu, WF16_DiluMenu,\
           WF17_DiluMenu, WF18_DiluMenu, WF19_DiluMenu, WF20_DiluMenu, WF21_DiluMenu, WF22_DiluMenu, WF23_DiluMenu, WF24_DiluMenu,\
           WG1_DiluMenu, WG2_DiluMenu, WG3_DiluMenu, WG4_DiluMenu, WG5_DiluMenu, WG6_DiluMenu, WG7_DiluMenu, WG8_DiluMenu,\
           WG9_DiluMenu, WG10_DiluMenu, WG11_DiluMenu, WG12_DiluMenu, WG13_DiluMenu, WG14_DiluMenu, WG15_DiluMenu, WG16_DiluMenu,\
           WG17_DiluMenu, WG18_DiluMenu, WG19_DiluMenu, WG20_DiluMenu, WG21_DiluMenu, WG22_DiluMenu, WG23_DiluMenu, WG24_DiluMenu,\
           WH1_DiluMenu, WH2_DiluMenu, WH3_DiluMenu, WH4_DiluMenu, WH5_DiluMenu, WH6_DiluMenu, WH7_DiluMenu, WH8_DiluMenu,\
           WH9_DiluMenu, WH10_DiluMenu, WH11_DiluMenu, WH12_DiluMenu, WH13_DiluMenu, WH14_DiluMenu, WH15_DiluMenu, WH16_DiluMenu,\
           WH17_DiluMenu, WH18_DiluMenu, WH19_DiluMenu, WH20_DiluMenu, WH21_DiluMenu, WH22_DiluMenu, WH23_DiluMenu, WH24_DiluMenu,\
           WI1_DiluMenu, WI2_DiluMenu, WI3_DiluMenu, WI4_DiluMenu, WI5_DiluMenu, WI6_DiluMenu, WI7_DiluMenu, WI8_DiluMenu,\
           WI9_DiluMenu, WI10_DiluMenu, WI11_DiluMenu, WI12_DiluMenu, WI13_DiluMenu, WI14_DiluMenu, WI15_DiluMenu, WI16_DiluMenu,\
           WI17_DiluMenu, WI18_DiluMenu, WI19_DiluMenu, WI20_DiluMenu, WI21_DiluMenu, WI22_DiluMenu, WI23_DiluMenu, WI24_DiluMenu,\
           WJ1_DiluMenu, WJ2_DiluMenu, WJ3_DiluMenu, WJ4_DiluMenu, WJ5_DiluMenu, WJ6_DiluMenu, WJ7_DiluMenu, WJ8_DiluMenu,\
           WJ9_DiluMenu, WJ10_DiluMenu, WJ11_DiluMenu, WJ12_DiluMenu, WJ13_DiluMenu, WJ14_DiluMenu, WJ15_DiluMenu, WJ16_DiluMenu,\
           WJ17_DiluMenu, WJ18_DiluMenu, WJ19_DiluMenu, WJ20_DiluMenu, WJ21_DiluMenu, WJ22_DiluMenu, WJ23_DiluMenu, WJ24_DiluMenu,\
           WK1_DiluMenu, WK2_DiluMenu, WK3_DiluMenu, WK4_DiluMenu, WK5_DiluMenu, WK6_DiluMenu, WK7_DiluMenu, WK8_DiluMenu,\
           WK9_DiluMenu, WK10_DiluMenu, WK11_DiluMenu, WK12_DiluMenu, WK13_DiluMenu, WK14_DiluMenu, WK15_DiluMenu, WK16_DiluMenu,\
           WK17_DiluMenu, WK18_DiluMenu, WK19_DiluMenu, WK20_DiluMenu, WK21_DiluMenu, WK22_DiluMenu, WK23_DiluMenu, WK24_DiluMenu,\
           WL1_DiluMenu, WL2_DiluMenu, WL3_DiluMenu, WL4_DiluMenu, WL5_DiluMenu, WL6_DiluMenu, WL7_DiluMenu, WL8_DiluMenu,\
           WL9_DiluMenu, WL10_DiluMenu, WL11_DiluMenu, WL12_DiluMenu, WL13_DiluMenu, WL14_DiluMenu, WL15_DiluMenu, WL16_DiluMenu,\
           WL17_DiluMenu, WL18_DiluMenu, WL19_DiluMenu, WL20_DiluMenu, WL21_DiluMenu, WL22_DiluMenu, WL23_DiluMenu, WL24_DiluMenu,\
           WM1_DiluMenu, WM2_DiluMenu, WM3_DiluMenu, WM4_DiluMenu, WM5_DiluMenu, WM6_DiluMenu, WM7_DiluMenu, WM8_DiluMenu,\
           WM9_DiluMenu, WM10_DiluMenu, WM11_DiluMenu, WM12_DiluMenu, WM13_DiluMenu, WM14_DiluMenu, WM15_DiluMenu, WM16_DiluMenu,\
           WM17_DiluMenu, WM18_DiluMenu, WM19_DiluMenu, WM20_DiluMenu, WM21_DiluMenu, WM22_DiluMenu, WM23_DiluMenu, WM24_DiluMenu,\
           WN1_DiluMenu, WN2_DiluMenu, WN3_DiluMenu, WN4_DiluMenu, WN5_DiluMenu, WN6_DiluMenu, WN7_DiluMenu, WN8_DiluMenu,\
           WN9_DiluMenu, WN10_DiluMenu, WN11_DiluMenu, WN12_DiluMenu, WN13_DiluMenu, WN14_DiluMenu, WN15_DiluMenu, WN16_DiluMenu,\
           WN17_DiluMenu, WN18_DiluMenu, WN19_DiluMenu, WN20_DiluMenu, WN21_DiluMenu, WN22_DiluMenu, WN23_DiluMenu, WN24_DiluMenu,\
           WO1_DiluMenu, WO2_DiluMenu, WO3_DiluMenu, WO4_DiluMenu, WO5_DiluMenu, WO6_DiluMenu, WO7_DiluMenu, WO8_DiluMenu,\
           WO9_DiluMenu, WO10_DiluMenu, WO11_DiluMenu, WO12_DiluMenu, WO13_DiluMenu, WO14_DiluMenu, WO15_DiluMenu, WO16_DiluMenu,\
           WO17_DiluMenu, WO18_DiluMenu, WO19_DiluMenu, WO20_DiluMenu, WO21_DiluMenu, WO22_DiluMenu, WO23_DiluMenu, WO24_DiluMenu,\
           WP1_DiluMenu, WP2_DiluMenu, WP3_DiluMenu, WP4_DiluMenu, WP5_DiluMenu, WP6_DiluMenu, WP7_DiluMenu, WP8_DiluMenu,\
           WP9_DiluMenu, WP10_DiluMenu, WP11_DiluMenu, WP12_DiluMenu, WP13_DiluMenu, WP14_DiluMenu, WP15_DiluMenu, WP16_DiluMenu,\
           WP17_DiluMenu, WP18_DiluMenu, WP19_DiluMenu, WP20_DiluMenu, WP21_DiluMenu, WP22_DiluMenu, WP23_DiluMenu, WP24_DiluMenu]
    
    
    Solvent1_Conc_List = [WA1_Solvent1_Conc, WA2_Solvent1_Conc, WA3_Solvent1_Conc, WA4_Solvent1_Conc, WA5_Solvent1_Conc, WA6_Solvent1_Conc,\
                       WA7_Solvent1_Conc, WA8_Solvent1_Conc, WA9_Solvent1_Conc, WA10_Solvent1_Conc, WA11_Solvent1_Conc, WA12_Solvent1_Conc,\
                       WA13_Solvent1_Conc, WA14_Solvent1_Conc, WA15_Solvent1_Conc, WA16_Solvent1_Conc, WA17_Solvent1_Conc, WA18_Solvent1_Conc,\
                       WA19_Solvent1_Conc, WA20_Solvent1_Conc, WA21_Solvent1_Conc, WA22_Solvent1_Conc, WA23_Solvent1_Conc, WA24_Solvent1_Conc,\
                       WB1_Solvent1_Conc, WB2_Solvent1_Conc, WB3_Solvent1_Conc, WB4_Solvent1_Conc, WB5_Solvent1_Conc, WB6_Solvent1_Conc,\
                       WB7_Solvent1_Conc, WB8_Solvent1_Conc, WB9_Solvent1_Conc, WB10_Solvent1_Conc, WB11_Solvent1_Conc, WB12_Solvent1_Conc,\
                       WB13_Solvent1_Conc, WB14_Solvent1_Conc, WB15_Solvent1_Conc, WB16_Solvent1_Conc, WB17_Solvent1_Conc, WB18_Solvent1_Conc,\
                       WB19_Solvent1_Conc, WB20_Solvent1_Conc, WB21_Solvent1_Conc, WB22_Solvent1_Conc, WB23_Solvent1_Conc, WB24_Solvent1_Conc,\
                       WC1_Solvent1_Conc, WC2_Solvent1_Conc, WC3_Solvent1_Conc, WC4_Solvent1_Conc, WC5_Solvent1_Conc, WC6_Solvent1_Conc,\
                       WC7_Solvent1_Conc, WC8_Solvent1_Conc, WC9_Solvent1_Conc, WC10_Solvent1_Conc, WC11_Solvent1_Conc, WC12_Solvent1_Conc,\
                       WC13_Solvent1_Conc, WC14_Solvent1_Conc, WC15_Solvent1_Conc, WC16_Solvent1_Conc, WC17_Solvent1_Conc, WC18_Solvent1_Conc,\
                       WC19_Solvent1_Conc, WC20_Solvent1_Conc, WC21_Solvent1_Conc, WC22_Solvent1_Conc, WC23_Solvent1_Conc, WC24_Solvent1_Conc,\
                       WD1_Solvent1_Conc, WD2_Solvent1_Conc, WD3_Solvent1_Conc, WD4_Solvent1_Conc, WD5_Solvent1_Conc, WD6_Solvent1_Conc,\
                       WD7_Solvent1_Conc, WD8_Solvent1_Conc, WD9_Solvent1_Conc, WD10_Solvent1_Conc, WD11_Solvent1_Conc, WD12_Solvent1_Conc,\
                       WD13_Solvent1_Conc, WD14_Solvent1_Conc, WD15_Solvent1_Conc, WD16_Solvent1_Conc, WD17_Solvent1_Conc, WD18_Solvent1_Conc,\
                       WD19_Solvent1_Conc, WD20_Solvent1_Conc, WD21_Solvent1_Conc, WD22_Solvent1_Conc, WD23_Solvent1_Conc, WD24_Solvent1_Conc,\
                       WE1_Solvent1_Conc, WE2_Solvent1_Conc, WE3_Solvent1_Conc, WE4_Solvent1_Conc, WE5_Solvent1_Conc, WE6_Solvent1_Conc,\
                       WE7_Solvent1_Conc, WE8_Solvent1_Conc, WE9_Solvent1_Conc, WE10_Solvent1_Conc, WE11_Solvent1_Conc, WE12_Solvent1_Conc,\
                       WE13_Solvent1_Conc, WE14_Solvent1_Conc, WE15_Solvent1_Conc, WE16_Solvent1_Conc, WE17_Solvent1_Conc, WE18_Solvent1_Conc,\
                       WE19_Solvent1_Conc, WE20_Solvent1_Conc, WE21_Solvent1_Conc, WE22_Solvent1_Conc, WE23_Solvent1_Conc, WE24_Solvent1_Conc,\
                       WF1_Solvent1_Conc, WF2_Solvent1_Conc, WF3_Solvent1_Conc, WF4_Solvent1_Conc, WF5_Solvent1_Conc, WF6_Solvent1_Conc,\
                       WF7_Solvent1_Conc, WF8_Solvent1_Conc, WF9_Solvent1_Conc, WF10_Solvent1_Conc, WF11_Solvent1_Conc, WF12_Solvent1_Conc,\
                       WF13_Solvent1_Conc, WF14_Solvent1_Conc, WF15_Solvent1_Conc, WF16_Solvent1_Conc, WF17_Solvent1_Conc, WF18_Solvent1_Conc,\
                       WF19_Solvent1_Conc, WF20_Solvent1_Conc, WF21_Solvent1_Conc, WF22_Solvent1_Conc, WF23_Solvent1_Conc, WF24_Solvent1_Conc,\
                       WG1_Solvent1_Conc, WG2_Solvent1_Conc, WG3_Solvent1_Conc, WG4_Solvent1_Conc, WG5_Solvent1_Conc, WG6_Solvent1_Conc,\
                       WG7_Solvent1_Conc, WG8_Solvent1_Conc, WG9_Solvent1_Conc, WG10_Solvent1_Conc, WG11_Solvent1_Conc, WG12_Solvent1_Conc,\
                       WG13_Solvent1_Conc, WG14_Solvent1_Conc, WG15_Solvent1_Conc, WG16_Solvent1_Conc, WG17_Solvent1_Conc, WG18_Solvent1_Conc,\
                       WG19_Solvent1_Conc, WG20_Solvent1_Conc, WG21_Solvent1_Conc, WG22_Solvent1_Conc, WG23_Solvent1_Conc, WG24_Solvent1_Conc,\
                       WH1_Solvent1_Conc, WH2_Solvent1_Conc, WH3_Solvent1_Conc, WH4_Solvent1_Conc, WH5_Solvent1_Conc, WH6_Solvent1_Conc,\
                       WH7_Solvent1_Conc, WH8_Solvent1_Conc, WH9_Solvent1_Conc, WH10_Solvent1_Conc, WH11_Solvent1_Conc, WH12_Solvent1_Conc,\
                       WH13_Solvent1_Conc, WH14_Solvent1_Conc, WH15_Solvent1_Conc, WH16_Solvent1_Conc, WH17_Solvent1_Conc, WH18_Solvent1_Conc,\
                       WH19_Solvent1_Conc, WH20_Solvent1_Conc, WH21_Solvent1_Conc, WH22_Solvent1_Conc, WH23_Solvent1_Conc, WH24_Solvent1_Conc,\
                       WI1_Solvent1_Conc, WI2_Solvent1_Conc, WI3_Solvent1_Conc, WI4_Solvent1_Conc, WI5_Solvent1_Conc, WI6_Solvent1_Conc,\
                       WI7_Solvent1_Conc, WI8_Solvent1_Conc, WI9_Solvent1_Conc, WI10_Solvent1_Conc, WI11_Solvent1_Conc, WI12_Solvent1_Conc,\
                       WI13_Solvent1_Conc, WI14_Solvent1_Conc, WI15_Solvent1_Conc, WI16_Solvent1_Conc, WI17_Solvent1_Conc, WI18_Solvent1_Conc,\
                       WI19_Solvent1_Conc, WI20_Solvent1_Conc, WI21_Solvent1_Conc, WI22_Solvent1_Conc, WI23_Solvent1_Conc, WI24_Solvent1_Conc,\
                       WJ1_Solvent1_Conc, WJ2_Solvent1_Conc, WJ3_Solvent1_Conc, WJ4_Solvent1_Conc, WJ5_Solvent1_Conc, WJ6_Solvent1_Conc,\
                       WJ7_Solvent1_Conc, WJ8_Solvent1_Conc, WJ9_Solvent1_Conc, WJ10_Solvent1_Conc, WJ11_Solvent1_Conc, WJ12_Solvent1_Conc,\
                       WJ13_Solvent1_Conc, WJ14_Solvent1_Conc, WJ15_Solvent1_Conc, WJ16_Solvent1_Conc, WJ17_Solvent1_Conc, WJ18_Solvent1_Conc,\
                       WJ19_Solvent1_Conc, WJ20_Solvent1_Conc, WJ21_Solvent1_Conc, WJ22_Solvent1_Conc, WJ23_Solvent1_Conc, WJ24_Solvent1_Conc,\
                       WK1_Solvent1_Conc, WK2_Solvent1_Conc, WK3_Solvent1_Conc, WK4_Solvent1_Conc, WK5_Solvent1_Conc, WK6_Solvent1_Conc,\
                       WK7_Solvent1_Conc, WK8_Solvent1_Conc, WK9_Solvent1_Conc, WK10_Solvent1_Conc, WK11_Solvent1_Conc, WK12_Solvent1_Conc,\
                       WK13_Solvent1_Conc, WK14_Solvent1_Conc, WK15_Solvent1_Conc, WK16_Solvent1_Conc, WK17_Solvent1_Conc, WK18_Solvent1_Conc,\
                       WK19_Solvent1_Conc, WK20_Solvent1_Conc, WK21_Solvent1_Conc, WK22_Solvent1_Conc, WK23_Solvent1_Conc, WK24_Solvent1_Conc,\
                       WL1_Solvent1_Conc, WL2_Solvent1_Conc, WL3_Solvent1_Conc, WL4_Solvent1_Conc, WL5_Solvent1_Conc, WL6_Solvent1_Conc,\
                       WL7_Solvent1_Conc, WL8_Solvent1_Conc, WL9_Solvent1_Conc, WL10_Solvent1_Conc, WL11_Solvent1_Conc, WL12_Solvent1_Conc,\
                       WL13_Solvent1_Conc, WL14_Solvent1_Conc, WL15_Solvent1_Conc, WL16_Solvent1_Conc, WL17_Solvent1_Conc, WL18_Solvent1_Conc,\
                       WL19_Solvent1_Conc, WL20_Solvent1_Conc, WL21_Solvent1_Conc, WL22_Solvent1_Conc, WL23_Solvent1_Conc, WL24_Solvent1_Conc,\
                       WM1_Solvent1_Conc, WM2_Solvent1_Conc, WM3_Solvent1_Conc, WM4_Solvent1_Conc, WM5_Solvent1_Conc, WM6_Solvent1_Conc,\
                       WM7_Solvent1_Conc, WM8_Solvent1_Conc, WM9_Solvent1_Conc, WM10_Solvent1_Conc, WM11_Solvent1_Conc, WM12_Solvent1_Conc,\
                       WM13_Solvent1_Conc, WM14_Solvent1_Conc, WM15_Solvent1_Conc, WM16_Solvent1_Conc, WM17_Solvent1_Conc, WM18_Solvent1_Conc,\
                       WM19_Solvent1_Conc, WM20_Solvent1_Conc, WM21_Solvent1_Conc, WM22_Solvent1_Conc, WM23_Solvent1_Conc, WM24_Solvent1_Conc,\
                       WN1_Solvent1_Conc, WN2_Solvent1_Conc, WN3_Solvent1_Conc, WN4_Solvent1_Conc, WN5_Solvent1_Conc, WN6_Solvent1_Conc,\
                       WN7_Solvent1_Conc, WN8_Solvent1_Conc, WN9_Solvent1_Conc, WN10_Solvent1_Conc, WN11_Solvent1_Conc, WN12_Solvent1_Conc,\
                       WN13_Solvent1_Conc, WN14_Solvent1_Conc, WN15_Solvent1_Conc, WN16_Solvent1_Conc, WN17_Solvent1_Conc, WN18_Solvent1_Conc,\
                       WN19_Solvent1_Conc, WN20_Solvent1_Conc, WN21_Solvent1_Conc, WN22_Solvent1_Conc, WN23_Solvent1_Conc, WN24_Solvent1_Conc,\
                       WO1_Solvent1_Conc, WO2_Solvent1_Conc, WO3_Solvent1_Conc, WO4_Solvent1_Conc, WO5_Solvent1_Conc, WO6_Solvent1_Conc,\
                       WO7_Solvent1_Conc, WO8_Solvent1_Conc, WO9_Solvent1_Conc, WO10_Solvent1_Conc, WO11_Solvent1_Conc, WO12_Solvent1_Conc,\
                       WO13_Solvent1_Conc, WO14_Solvent1_Conc, WO15_Solvent1_Conc, WO16_Solvent1_Conc, WO17_Solvent1_Conc, WO18_Solvent1_Conc,\
                       WO19_Solvent1_Conc, WO20_Solvent1_Conc, WO21_Solvent1_Conc, WO22_Solvent1_Conc, WO23_Solvent1_Conc, WO24_Solvent1_Conc,\
                       WP1_Solvent1_Conc, WP2_Solvent1_Conc, WP3_Solvent1_Conc, WP4_Solvent1_Conc, WP5_Solvent1_Conc, WP6_Solvent1_Conc,\
                       WP7_Solvent1_Conc, WP8_Solvent1_Conc, WP9_Solvent1_Conc, WP10_Solvent1_Conc, WP11_Solvent1_Conc, WP12_Solvent1_Conc,\
                       WP13_Solvent1_Conc, WP14_Solvent1_Conc, WP15_Solvent1_Conc, WP16_Solvent1_Conc, WP17_Solvent1_Conc, WP18_Solvent1_Conc,\
                       WP19_Solvent1_Conc, WP20_Solvent1_Conc, WP21_Solvent1_Conc, WP22_Solvent1_Conc, WP23_Solvent1_Conc, WP24_Solvent1_Conc]
    

    Solvent2_Conc_List = [WA1_Solvent2_Conc, WA2_Solvent2_Conc, WA3_Solvent2_Conc, WA4_Solvent2_Conc, WA5_Solvent2_Conc, WA6_Solvent2_Conc,\
                       WA7_Solvent2_Conc, WA8_Solvent2_Conc, WA9_Solvent2_Conc, WA10_Solvent2_Conc, WA11_Solvent2_Conc, WA12_Solvent2_Conc,\
                       WA13_Solvent2_Conc, WA14_Solvent2_Conc, WA15_Solvent2_Conc, WA16_Solvent2_Conc, WA17_Solvent2_Conc, WA18_Solvent2_Conc,\
                       WA19_Solvent2_Conc, WA20_Solvent2_Conc, WA21_Solvent2_Conc, WA22_Solvent2_Conc, WA23_Solvent2_Conc, WA24_Solvent2_Conc,\
                       WB1_Solvent2_Conc, WB2_Solvent2_Conc, WB3_Solvent2_Conc, WB4_Solvent2_Conc, WB5_Solvent2_Conc, WB6_Solvent2_Conc,\
                       WB7_Solvent2_Conc, WB8_Solvent2_Conc, WB9_Solvent2_Conc, WB10_Solvent2_Conc, WB11_Solvent2_Conc, WB12_Solvent2_Conc,\
                       WB13_Solvent2_Conc, WB14_Solvent2_Conc, WB15_Solvent2_Conc, WB16_Solvent2_Conc, WB17_Solvent2_Conc, WB18_Solvent2_Conc,\
                       WB19_Solvent2_Conc, WB20_Solvent2_Conc, WB21_Solvent2_Conc, WB22_Solvent2_Conc, WB23_Solvent2_Conc, WB24_Solvent2_Conc,\
                       WC1_Solvent2_Conc, WC2_Solvent2_Conc, WC3_Solvent2_Conc, WC4_Solvent2_Conc, WC5_Solvent2_Conc, WC6_Solvent2_Conc,\
                       WC7_Solvent2_Conc, WC8_Solvent2_Conc, WC9_Solvent2_Conc, WC10_Solvent2_Conc, WC11_Solvent2_Conc, WC12_Solvent2_Conc,\
                       WC13_Solvent2_Conc, WC14_Solvent2_Conc, WC15_Solvent2_Conc, WC16_Solvent2_Conc, WC17_Solvent2_Conc, WC18_Solvent2_Conc,\
                       WC19_Solvent2_Conc, WC20_Solvent2_Conc, WC21_Solvent2_Conc, WC22_Solvent2_Conc, WC23_Solvent2_Conc, WC24_Solvent2_Conc,\
                       WD1_Solvent2_Conc, WD2_Solvent2_Conc, WD3_Solvent2_Conc, WD4_Solvent2_Conc, WD5_Solvent2_Conc, WD6_Solvent2_Conc,\
                       WD7_Solvent2_Conc, WD8_Solvent2_Conc, WD9_Solvent2_Conc, WD10_Solvent2_Conc, WD11_Solvent2_Conc, WD12_Solvent2_Conc,\
                       WD13_Solvent2_Conc, WD14_Solvent2_Conc, WD15_Solvent2_Conc, WD16_Solvent2_Conc, WD17_Solvent2_Conc, WD18_Solvent2_Conc,\
                       WD19_Solvent2_Conc, WD20_Solvent2_Conc, WD21_Solvent2_Conc, WD22_Solvent2_Conc, WD23_Solvent2_Conc, WD24_Solvent2_Conc,\
                       WE1_Solvent2_Conc, WE2_Solvent2_Conc, WE3_Solvent2_Conc, WE4_Solvent2_Conc, WE5_Solvent2_Conc, WE6_Solvent2_Conc,\
                       WE7_Solvent2_Conc, WE8_Solvent2_Conc, WE9_Solvent2_Conc, WE10_Solvent2_Conc, WE11_Solvent2_Conc, WE12_Solvent2_Conc,\
                       WE13_Solvent2_Conc, WE14_Solvent2_Conc, WE15_Solvent2_Conc, WE16_Solvent2_Conc, WE17_Solvent2_Conc, WE18_Solvent2_Conc,\
                       WE19_Solvent2_Conc, WE20_Solvent2_Conc, WE21_Solvent2_Conc, WE22_Solvent2_Conc, WE23_Solvent2_Conc, WE24_Solvent2_Conc,\
                       WF1_Solvent2_Conc, WF2_Solvent2_Conc, WF3_Solvent2_Conc, WF4_Solvent2_Conc, WF5_Solvent2_Conc, WF6_Solvent2_Conc,\
                       WF7_Solvent2_Conc, WF8_Solvent2_Conc, WF9_Solvent2_Conc, WF10_Solvent2_Conc, WF11_Solvent2_Conc, WF12_Solvent2_Conc,\
                       WF13_Solvent2_Conc, WF14_Solvent2_Conc, WF15_Solvent2_Conc, WF16_Solvent2_Conc, WF17_Solvent2_Conc, WF18_Solvent2_Conc,\
                       WF19_Solvent2_Conc, WF20_Solvent2_Conc, WF21_Solvent2_Conc, WF22_Solvent2_Conc, WF23_Solvent2_Conc, WF24_Solvent2_Conc,\
                       WG1_Solvent2_Conc, WG2_Solvent2_Conc, WG3_Solvent2_Conc, WG4_Solvent2_Conc, WG5_Solvent2_Conc, WG6_Solvent2_Conc,\
                       WG7_Solvent2_Conc, WG8_Solvent2_Conc, WG9_Solvent2_Conc, WG10_Solvent2_Conc, WG11_Solvent2_Conc, WG12_Solvent2_Conc,\
                       WG13_Solvent2_Conc, WG14_Solvent2_Conc, WG15_Solvent2_Conc, WG16_Solvent2_Conc, WG17_Solvent2_Conc, WG18_Solvent2_Conc,\
                       WG19_Solvent2_Conc, WG20_Solvent2_Conc, WG21_Solvent2_Conc, WG22_Solvent2_Conc, WG23_Solvent2_Conc, WG24_Solvent2_Conc,\
                       WH1_Solvent2_Conc, WH2_Solvent2_Conc, WH3_Solvent2_Conc, WH4_Solvent2_Conc, WH5_Solvent2_Conc, WH6_Solvent2_Conc,\
                       WH7_Solvent2_Conc, WH8_Solvent2_Conc, WH9_Solvent2_Conc, WH10_Solvent2_Conc, WH11_Solvent2_Conc, WH12_Solvent2_Conc,\
                       WH13_Solvent2_Conc, WH14_Solvent2_Conc, WH15_Solvent2_Conc, WH16_Solvent2_Conc, WH17_Solvent2_Conc, WH18_Solvent2_Conc,\
                       WH19_Solvent2_Conc, WH20_Solvent2_Conc, WH21_Solvent2_Conc, WH22_Solvent2_Conc, WH23_Solvent2_Conc, WH24_Solvent2_Conc,\
                       WI1_Solvent2_Conc, WI2_Solvent2_Conc, WI3_Solvent2_Conc, WI4_Solvent2_Conc, WI5_Solvent2_Conc, WI6_Solvent2_Conc,\
                       WI7_Solvent2_Conc, WI8_Solvent2_Conc, WI9_Solvent2_Conc, WI10_Solvent2_Conc, WI11_Solvent2_Conc, WI12_Solvent2_Conc,\
                       WI13_Solvent2_Conc, WI14_Solvent2_Conc, WI15_Solvent2_Conc, WI16_Solvent2_Conc, WI17_Solvent2_Conc, WI18_Solvent2_Conc,\
                       WI19_Solvent2_Conc, WI20_Solvent2_Conc, WI21_Solvent2_Conc, WI22_Solvent2_Conc, WI23_Solvent2_Conc, WI24_Solvent2_Conc,\
                       WJ1_Solvent2_Conc, WJ2_Solvent2_Conc, WJ3_Solvent2_Conc, WJ4_Solvent2_Conc, WJ5_Solvent2_Conc, WJ6_Solvent2_Conc,\
                       WJ7_Solvent2_Conc, WJ8_Solvent2_Conc, WJ9_Solvent2_Conc, WJ10_Solvent2_Conc, WJ11_Solvent2_Conc, WJ12_Solvent2_Conc,\
                       WJ13_Solvent2_Conc, WJ14_Solvent2_Conc, WJ15_Solvent2_Conc, WJ16_Solvent2_Conc, WJ17_Solvent2_Conc, WJ18_Solvent2_Conc,\
                       WJ19_Solvent2_Conc, WJ20_Solvent2_Conc, WJ21_Solvent2_Conc, WJ22_Solvent2_Conc, WJ23_Solvent2_Conc, WJ24_Solvent2_Conc,\
                       WK1_Solvent2_Conc, WK2_Solvent2_Conc, WK3_Solvent2_Conc, WK4_Solvent2_Conc, WK5_Solvent2_Conc, WK6_Solvent2_Conc,\
                       WK7_Solvent2_Conc, WK8_Solvent2_Conc, WK9_Solvent2_Conc, WK10_Solvent2_Conc, WK11_Solvent2_Conc, WK12_Solvent2_Conc,\
                       WK13_Solvent2_Conc, WK14_Solvent2_Conc, WK15_Solvent2_Conc, WK16_Solvent2_Conc, WK17_Solvent2_Conc, WK18_Solvent2_Conc,\
                       WK19_Solvent2_Conc, WK20_Solvent2_Conc, WK21_Solvent2_Conc, WK22_Solvent2_Conc, WK23_Solvent2_Conc, WK24_Solvent2_Conc,\
                       WL1_Solvent2_Conc, WL2_Solvent2_Conc, WL3_Solvent2_Conc, WL4_Solvent2_Conc, WL5_Solvent2_Conc, WL6_Solvent2_Conc,\
                       WL7_Solvent2_Conc, WL8_Solvent2_Conc, WL9_Solvent2_Conc, WL10_Solvent2_Conc, WL11_Solvent2_Conc, WL12_Solvent2_Conc,\
                       WL13_Solvent2_Conc, WL14_Solvent2_Conc, WL15_Solvent2_Conc, WL16_Solvent2_Conc, WL17_Solvent2_Conc, WL18_Solvent2_Conc,\
                       WL19_Solvent2_Conc, WL20_Solvent2_Conc, WL21_Solvent2_Conc, WL22_Solvent2_Conc, WL23_Solvent2_Conc, WL24_Solvent2_Conc,\
                       WM1_Solvent2_Conc, WM2_Solvent2_Conc, WM3_Solvent2_Conc, WM4_Solvent2_Conc, WM5_Solvent2_Conc, WM6_Solvent2_Conc,\
                       WM7_Solvent2_Conc, WM8_Solvent2_Conc, WM9_Solvent2_Conc, WM10_Solvent2_Conc, WM11_Solvent2_Conc, WM12_Solvent2_Conc,\
                       WM13_Solvent2_Conc, WM14_Solvent2_Conc, WM15_Solvent2_Conc, WM16_Solvent2_Conc, WM17_Solvent2_Conc, WM18_Solvent2_Conc,\
                       WM19_Solvent2_Conc, WM20_Solvent2_Conc, WM21_Solvent2_Conc, WM22_Solvent2_Conc, WM23_Solvent2_Conc, WM24_Solvent2_Conc,\
                       WN1_Solvent2_Conc, WN2_Solvent2_Conc, WN3_Solvent2_Conc, WN4_Solvent2_Conc, WN5_Solvent2_Conc, WN6_Solvent2_Conc,\
                       WN7_Solvent2_Conc, WN8_Solvent2_Conc, WN9_Solvent2_Conc, WN10_Solvent2_Conc, WN11_Solvent2_Conc, WN12_Solvent2_Conc,\
                       WN13_Solvent2_Conc, WN14_Solvent2_Conc, WN15_Solvent2_Conc, WN16_Solvent2_Conc, WN17_Solvent2_Conc, WN18_Solvent2_Conc,\
                       WN19_Solvent2_Conc, WN20_Solvent2_Conc, WN21_Solvent2_Conc, WN22_Solvent2_Conc, WN23_Solvent2_Conc, WN24_Solvent2_Conc,\
                       WO1_Solvent2_Conc, WO2_Solvent2_Conc, WO3_Solvent2_Conc, WO4_Solvent2_Conc, WO5_Solvent2_Conc, WO6_Solvent2_Conc,\
                       WO7_Solvent2_Conc, WO8_Solvent2_Conc, WO9_Solvent2_Conc, WO10_Solvent2_Conc, WO11_Solvent2_Conc, WO12_Solvent2_Conc,\
                       WO13_Solvent2_Conc, WO14_Solvent2_Conc, WO15_Solvent2_Conc, WO16_Solvent2_Conc, WO17_Solvent2_Conc, WO18_Solvent2_Conc,\
                       WO19_Solvent2_Conc, WO20_Solvent2_Conc, WO21_Solvent2_Conc, WO22_Solvent2_Conc, WO23_Solvent2_Conc, WO24_Solvent2_Conc,\
                       WP1_Solvent2_Conc, WP2_Solvent2_Conc, WP3_Solvent2_Conc, WP4_Solvent2_Conc, WP5_Solvent2_Conc, WP6_Solvent2_Conc,\
                       WP7_Solvent2_Conc, WP8_Solvent2_Conc, WP9_Solvent2_Conc, WP10_Solvent2_Conc, WP11_Solvent2_Conc, WP12_Solvent2_Conc,\
                       WP13_Solvent2_Conc, WP14_Solvent2_Conc, WP15_Solvent2_Conc, WP16_Solvent2_Conc, WP17_Solvent2_Conc, WP18_Solvent2_Conc,\
                       WP19_Solvent2_Conc, WP20_Solvent2_Conc, WP21_Solvent2_Conc, WP22_Solvent2_Conc, WP23_Solvent2_Conc, WP24_Solvent2_Conc]
    

    SS_Conc_List = [WA1_SS_Conc, WA2_SS_Conc, WA3_SS_Conc, WA4_SS_Conc, WA5_SS_Conc, WA6_SS_Conc,\
                   WA7_SS_Conc, WA8_SS_Conc, WA9_SS_Conc, WA10_SS_Conc, WA11_SS_Conc, WA12_SS_Conc,\
                   WA13_SS_Conc, WA14_SS_Conc, WA15_SS_Conc, WA16_SS_Conc, WA17_SS_Conc, WA18_SS_Conc,\
                   WA19_SS_Conc, WA20_SS_Conc, WA21_SS_Conc, WA22_SS_Conc, WA23_SS_Conc, WA24_SS_Conc,\
                   WB1_SS_Conc, WB2_SS_Conc, WB3_SS_Conc, WB4_SS_Conc, WB5_SS_Conc, WB6_SS_Conc,\
                   WB7_SS_Conc, WB8_SS_Conc, WB9_SS_Conc, WB10_SS_Conc, WB11_SS_Conc, WB12_SS_Conc,\
                   WB13_SS_Conc, WB14_SS_Conc, WB15_SS_Conc, WB16_SS_Conc, WB17_SS_Conc, WB18_SS_Conc,\
                   WB19_SS_Conc, WB20_SS_Conc, WB21_SS_Conc, WB22_SS_Conc, WB23_SS_Conc, WB24_SS_Conc,\
                   WC1_SS_Conc, WC2_SS_Conc, WC3_SS_Conc, WC4_SS_Conc, WC5_SS_Conc, WC6_SS_Conc,\
                   WC7_SS_Conc, WC8_SS_Conc, WC9_SS_Conc, WC10_SS_Conc, WC11_SS_Conc, WC12_SS_Conc,\
                   WC13_SS_Conc, WC14_SS_Conc, WC15_SS_Conc, WC16_SS_Conc, WC17_SS_Conc, WC18_SS_Conc,\
                   WC19_SS_Conc, WC20_SS_Conc, WC21_SS_Conc, WC22_SS_Conc, WC23_SS_Conc, WC24_SS_Conc,\
                   WD1_SS_Conc, WD2_SS_Conc, WD3_SS_Conc, WD4_SS_Conc, WD5_SS_Conc, WD6_SS_Conc,\
                   WD7_SS_Conc, WD8_SS_Conc, WD9_SS_Conc, WD10_SS_Conc, WD11_SS_Conc, WD12_SS_Conc,\
                   WD13_SS_Conc, WD14_SS_Conc, WD15_SS_Conc, WD16_SS_Conc, WD17_SS_Conc, WD18_SS_Conc,\
                   WD19_SS_Conc, WD20_SS_Conc, WD21_SS_Conc, WD22_SS_Conc, WD23_SS_Conc, WD24_SS_Conc,\
                   WE1_SS_Conc, WE2_SS_Conc, WE3_SS_Conc, WE4_SS_Conc, WE5_SS_Conc, WE6_SS_Conc,\
                   WE7_SS_Conc, WE8_SS_Conc, WE9_SS_Conc, WE10_SS_Conc, WE11_SS_Conc, WE12_SS_Conc,\
                   WE13_SS_Conc, WE14_SS_Conc, WE15_SS_Conc, WE16_SS_Conc, WE17_SS_Conc, WE18_SS_Conc,\
                   WE19_SS_Conc, WE20_SS_Conc, WE21_SS_Conc, WE22_SS_Conc, WE23_SS_Conc, WE24_SS_Conc,\
                   WF1_SS_Conc, WF2_SS_Conc, WF3_SS_Conc, WF4_SS_Conc, WF5_SS_Conc, WF6_SS_Conc,\
                   WF7_SS_Conc, WF8_SS_Conc, WF9_SS_Conc, WF10_SS_Conc, WF11_SS_Conc, WF12_SS_Conc,\
                   WF13_SS_Conc, WF14_SS_Conc, WF15_SS_Conc, WF16_SS_Conc, WF17_SS_Conc, WF18_SS_Conc,\
                   WF19_SS_Conc, WF20_SS_Conc, WF21_SS_Conc, WF22_SS_Conc, WF23_SS_Conc, WF24_SS_Conc,\
                   WG1_SS_Conc, WG2_SS_Conc, WG3_SS_Conc, WG4_SS_Conc, WG5_SS_Conc, WG6_SS_Conc,\
                   WG7_SS_Conc, WG8_SS_Conc, WG9_SS_Conc, WG10_SS_Conc, WG11_SS_Conc, WG12_SS_Conc,\
                   WG13_SS_Conc, WG14_SS_Conc, WG15_SS_Conc, WG16_SS_Conc, WG17_SS_Conc, WG18_SS_Conc,\
                   WG19_SS_Conc, WG20_SS_Conc, WG21_SS_Conc, WG22_SS_Conc, WG23_SS_Conc, WG24_SS_Conc,\
                   WH1_SS_Conc, WH2_SS_Conc, WH3_SS_Conc, WH4_SS_Conc, WH5_SS_Conc, WH6_SS_Conc,\
                   WH7_SS_Conc, WH8_SS_Conc, WH9_SS_Conc, WH10_SS_Conc, WH11_SS_Conc, WH12_SS_Conc,\
                   WH13_SS_Conc, WH14_SS_Conc, WH15_SS_Conc, WH16_SS_Conc, WH17_SS_Conc, WH18_SS_Conc,\
                   WH19_SS_Conc, WH20_SS_Conc, WH21_SS_Conc, WH22_SS_Conc, WH23_SS_Conc, WH24_SS_Conc,\
                   WI1_SS_Conc, WI2_SS_Conc, WI3_SS_Conc, WI4_SS_Conc, WI5_SS_Conc, WI6_SS_Conc,\
                   WI7_SS_Conc, WI8_SS_Conc, WI9_SS_Conc, WI10_SS_Conc, WI11_SS_Conc, WI12_SS_Conc,\
                   WI13_SS_Conc, WI14_SS_Conc, WI15_SS_Conc, WI16_SS_Conc, WI17_SS_Conc, WI18_SS_Conc,\
                   WI19_SS_Conc, WI20_SS_Conc, WI21_SS_Conc, WI22_SS_Conc, WI23_SS_Conc, WI24_SS_Conc,\
                   WJ1_SS_Conc, WJ2_SS_Conc, WJ3_SS_Conc, WJ4_SS_Conc, WJ5_SS_Conc, WJ6_SS_Conc,\
                   WJ7_SS_Conc, WJ8_SS_Conc, WJ9_SS_Conc, WJ10_SS_Conc, WJ11_SS_Conc, WJ12_SS_Conc,\
                   WJ13_SS_Conc, WJ14_SS_Conc, WJ15_SS_Conc, WJ16_SS_Conc, WJ17_SS_Conc, WJ18_SS_Conc,\
                   WJ19_SS_Conc, WJ20_SS_Conc, WJ21_SS_Conc, WJ22_SS_Conc, WJ23_SS_Conc, WJ24_SS_Conc,\
                   WK1_SS_Conc, WK2_SS_Conc, WK3_SS_Conc, WK4_SS_Conc, WK5_SS_Conc, WK6_SS_Conc,\
                   WK7_SS_Conc, WK8_SS_Conc, WK9_SS_Conc, WK10_SS_Conc, WK11_SS_Conc, WK12_SS_Conc,\
                   WK13_SS_Conc, WK14_SS_Conc, WK15_SS_Conc, WK16_SS_Conc, WK17_SS_Conc, WK18_SS_Conc,\
                   WK19_SS_Conc, WK20_SS_Conc, WK21_SS_Conc, WK22_SS_Conc, WK23_SS_Conc, WK24_SS_Conc,\
                   WL1_SS_Conc, WL2_SS_Conc, WL3_SS_Conc, WL4_SS_Conc, WL5_SS_Conc, WL6_SS_Conc,\
                   WL7_SS_Conc, WL8_SS_Conc, WL9_SS_Conc, WL10_SS_Conc, WL11_SS_Conc, WL12_SS_Conc,\
                   WL13_SS_Conc, WL14_SS_Conc, WL15_SS_Conc, WL16_SS_Conc, WL17_SS_Conc, WL18_SS_Conc,\
                   WL19_SS_Conc, WL20_SS_Conc, WL21_SS_Conc, WL22_SS_Conc, WL23_SS_Conc, WL24_SS_Conc,\
                   WM1_SS_Conc, WM2_SS_Conc, WM3_SS_Conc, WM4_SS_Conc, WM5_SS_Conc, WM6_SS_Conc,\
                   WM7_SS_Conc, WM8_SS_Conc, WM9_SS_Conc, WM10_SS_Conc, WM11_SS_Conc, WM12_SS_Conc,\
                   WM13_SS_Conc, WM14_SS_Conc, WM15_SS_Conc, WM16_SS_Conc, WM17_SS_Conc, WM18_SS_Conc,\
                   WM19_SS_Conc, WM20_SS_Conc, WM21_SS_Conc, WM22_SS_Conc, WM23_SS_Conc, WM24_SS_Conc,\
                   WN1_SS_Conc, WN2_SS_Conc, WN3_SS_Conc, WN4_SS_Conc, WN5_SS_Conc, WN6_SS_Conc,\
                   WN7_SS_Conc, WN8_SS_Conc, WN9_SS_Conc, WN10_SS_Conc, WN11_SS_Conc, WN12_SS_Conc,\
                   WN13_SS_Conc, WN14_SS_Conc, WN15_SS_Conc, WN16_SS_Conc, WN17_SS_Conc, WN18_SS_Conc,\
                   WN19_SS_Conc, WN20_SS_Conc, WN21_SS_Conc, WN22_SS_Conc, WN23_SS_Conc, WN24_SS_Conc,\
                   WO1_SS_Conc, WO2_SS_Conc, WO3_SS_Conc, WO4_SS_Conc, WO5_SS_Conc, WO6_SS_Conc,\
                   WO7_SS_Conc, WO8_SS_Conc, WO9_SS_Conc, WO10_SS_Conc, WO11_SS_Conc, WO12_SS_Conc,\
                   WO13_SS_Conc, WO14_SS_Conc, WO15_SS_Conc, WO16_SS_Conc, WO17_SS_Conc, WO18_SS_Conc,\
                   WO19_SS_Conc, WO20_SS_Conc, WO21_SS_Conc, WO22_SS_Conc, WO23_SS_Conc, WO24_SS_Conc,\
                   WP1_SS_Conc, WP2_SS_Conc, WP3_SS_Conc, WP4_SS_Conc, WP5_SS_Conc, WP6_SS_Conc,\
                   WP7_SS_Conc, WP8_SS_Conc, WP9_SS_Conc, WP10_SS_Conc, WP11_SS_Conc, WP12_SS_Conc,\
                   WP13_SS_Conc, WP14_SS_Conc, WP15_SS_Conc, WP16_SS_Conc, WP17_SS_Conc, WP18_SS_Conc,\
                   WP19_SS_Conc, WP20_SS_Conc, WP21_SS_Conc, WP22_SS_Conc, WP23_SS_Conc, WP24_SS_Conc]
    
    Vol_List = [WA1_Vol, WA2_Vol, WA3_Vol, WA4_Vol, WA5_Vol, WA6_Vol,\
               WA7_Vol, WA8_Vol, WA9_Vol, WA10_Vol, WA11_Vol, WA12_Vol,\
               WA13_Vol, WA14_Vol, WA15_Vol, WA16_Vol, WA17_Vol, WA18_Vol,\
               WA19_Vol, WA20_Vol, WA21_Vol, WA22_Vol, WA23_Vol, WA24_Vol,\
               WB1_Vol, WB2_Vol, WB3_Vol, WB4_Vol, WB5_Vol, WB6_Vol,\
               WB7_Vol, WB8_Vol, WB9_Vol, WB10_Vol, WB11_Vol, WB12_Vol,\
               WB13_Vol, WB14_Vol, WB15_Vol, WB16_Vol, WB17_Vol, WB18_Vol,\
               WB19_Vol, WB20_Vol, WB21_Vol, WB22_Vol, WB23_Vol, WB24_Vol,\
               WC1_Vol, WC2_Vol, WC3_Vol, WC4_Vol, WC5_Vol, WC6_Vol,\
               WC7_Vol, WC8_Vol, WC9_Vol, WC10_Vol, WC11_Vol, WC12_Vol,\
               WC13_Vol, WC14_Vol, WC15_Vol, WC16_Vol, WC17_Vol, WC18_Vol,\
               WC19_Vol, WC20_Vol, WC21_Vol, WC22_Vol, WC23_Vol, WC24_Vol,\
               WD1_Vol, WD2_Vol, WD3_Vol, WD4_Vol, WD5_Vol, WD6_Vol,\
               WD7_Vol, WD8_Vol, WD9_Vol, WD10_Vol, WD11_Vol, WD12_Vol,\
               WD13_Vol, WD14_Vol, WD15_Vol, WD16_Vol, WD17_Vol, WD18_Vol,\
               WD19_Vol, WD20_Vol, WD21_Vol, WD22_Vol, WD23_Vol, WD24_Vol,\
               WE1_Vol, WE2_Vol, WE3_Vol, WE4_Vol, WE5_Vol, WE6_Vol,\
               WE7_Vol, WE8_Vol, WE9_Vol, WE10_Vol, WE11_Vol, WE12_Vol,\
               WE13_Vol, WE14_Vol, WE15_Vol, WE16_Vol, WE17_Vol, WE18_Vol,\
               WE19_Vol, WE20_Vol, WE21_Vol, WE22_Vol, WE23_Vol, WE24_Vol,\
               WF1_Vol, WF2_Vol, WF3_Vol, WF4_Vol, WF5_Vol, WF6_Vol,\
               WF7_Vol, WF8_Vol, WF9_Vol, WF10_Vol, WF11_Vol, WF12_Vol,\
               WF13_Vol, WF14_Vol, WF15_Vol, WF16_Vol, WF17_Vol, WF18_Vol,\
               WF19_Vol, WF20_Vol, WF21_Vol, WF22_Vol, WF23_Vol, WF24_Vol,\
               WG1_Vol, WG2_Vol, WG3_Vol, WG4_Vol, WG5_Vol, WG6_Vol,\
               WG7_Vol, WG8_Vol, WG9_Vol, WG10_Vol, WG11_Vol, WG12_Vol,\
               WG13_Vol, WG14_Vol, WG15_Vol, WG16_Vol, WG17_Vol, WG18_Vol,\
               WG19_Vol, WG20_Vol, WG21_Vol, WG22_Vol, WG23_Vol, WG24_Vol,\
               WH1_Vol, WH2_Vol, WH3_Vol, WH4_Vol, WH5_Vol, WH6_Vol,\
               WH7_Vol, WH8_Vol, WH9_Vol, WH10_Vol, WH11_Vol, WH12_Vol,\
               WH13_Vol, WH14_Vol, WH15_Vol, WH16_Vol, WH17_Vol, WH18_Vol,\
               WH19_Vol, WH20_Vol, WH21_Vol, WH22_Vol, WH23_Vol, WH24_Vol,\
               WI1_Vol, WI2_Vol, WI3_Vol, WI4_Vol, WI5_Vol, WI6_Vol,\
               WI7_Vol, WI8_Vol, WI9_Vol, WI10_Vol, WI11_Vol, WI12_Vol,\
               WI13_Vol, WI14_Vol, WI15_Vol, WI16_Vol, WI17_Vol, WI18_Vol,\
               WI19_Vol, WI20_Vol, WI21_Vol, WI22_Vol, WI23_Vol, WI24_Vol,\
               WJ1_Vol, WJ2_Vol, WJ3_Vol, WJ4_Vol, WJ5_Vol, WJ6_Vol,\
               WJ7_Vol, WJ8_Vol, WJ9_Vol, WJ10_Vol, WJ11_Vol, WJ12_Vol,\
               WJ13_Vol, WJ14_Vol, WJ15_Vol, WJ16_Vol, WJ17_Vol, WJ18_Vol,\
               WJ19_Vol, WJ20_Vol, WJ21_Vol, WJ22_Vol, WJ23_Vol, WJ24_Vol,\
               WK1_Vol, WK2_Vol, WK3_Vol, WK4_Vol, WK5_Vol, WK6_Vol,\
               WK7_Vol, WK8_Vol, WK9_Vol, WK10_Vol, WK11_Vol, WK12_Vol,\
               WK13_Vol, WK14_Vol, WK15_Vol, WK16_Vol, WK17_Vol, WK18_Vol,\
               WK19_Vol, WK20_Vol, WK21_Vol, WK22_Vol, WK23_Vol, WK24_Vol,\
               WL1_Vol, WL2_Vol, WL3_Vol, WL4_Vol, WL5_Vol, WL6_Vol,\
               WL7_Vol, WL8_Vol, WL9_Vol, WL10_Vol, WL11_Vol, WL12_Vol,\
               WL13_Vol, WL14_Vol, WL15_Vol, WL16_Vol, WL17_Vol, WL18_Vol,\
               WL19_Vol, WL20_Vol, WL21_Vol, WL22_Vol, WL23_Vol, WL24_Vol,\
               WM1_Vol, WM2_Vol, WM3_Vol, WM4_Vol, WM5_Vol, WM6_Vol,\
               WM7_Vol, WM8_Vol, WM9_Vol, WM10_Vol, WM11_Vol, WM12_Vol,\
               WM13_Vol, WM14_Vol, WM15_Vol, WM16_Vol, WM17_Vol, WM18_Vol,\
               WM19_Vol, WM20_Vol, WM21_Vol, WM22_Vol, WM23_Vol, WM24_Vol,\
               WN1_Vol, WN2_Vol, WN3_Vol, WN4_Vol, WN5_Vol, WN6_Vol,\
               WN7_Vol, WN8_Vol, WN9_Vol, WN10_Vol, WN11_Vol, WN12_Vol,\
               WN13_Vol, WN14_Vol, WN15_Vol, WN16_Vol, WN17_Vol, WN18_Vol,\
               WN19_Vol, WN20_Vol, WN21_Vol, WN22_Vol, WN23_Vol, WN24_Vol,\
               WO1_Vol, WO2_Vol, WO3_Vol, WO4_Vol, WO5_Vol, WO6_Vol,\
               WO7_Vol, WO8_Vol, WO9_Vol, WO10_Vol, WO11_Vol, WO12_Vol,\
               WO13_Vol, WO14_Vol, WO15_Vol, WO16_Vol, WO17_Vol, WO18_Vol,\
               WO19_Vol, WO20_Vol, WO21_Vol, WO22_Vol, WO23_Vol, WO24_Vol,\
               WP1_Vol, WP2_Vol, WP3_Vol, WP4_Vol, WP5_Vol, WP6_Vol,\
               WP7_Vol, WP8_Vol, WP9_Vol, WP10_Vol, WP11_Vol, WP12_Vol,\
               WP13_Vol, WP14_Vol, WP15_Vol, WP16_Vol, WP17_Vol, WP18_Vol,\
               WP19_Vol, WP20_Vol, WP21_Vol, WP22_Vol, WP23_Vol, WP24_Vol]
    

    Vol_Label_List = [Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                      Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label,\
                       Row1_Vol_Label,Row2_Vol_Label,Row3_Vol_Label,Row4_Vol_Label,Row5_Vol_Label,Row6_Vol_Label,\
                       Row7_Vol_Label,Row8_Vol_Label,Row9_Vol_Label,Row10_Vol_Label,Row11_Vol_Label,Row12_Vol_Label]

    Solvent1_Conc_Label_List = [Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label,\
                            Row1_Solvent1_Conc_Label,Row2_Solvent1_Conc_Label,Row3_Solvent1_Conc_Label,Row4_Solvent1_Conc_Label,Row5_Solvent1_Conc_Label,Row6_Solvent1_Conc_Label,\
                            Row7_Solvent1_Conc_Label,Row8_Solvent1_Conc_Label,Row9_Solvent1_Conc_Label,Row10_Solvent1_Conc_Label,Row11_Solvent1_Conc_Label,Row12_Solvent1_Conc_Label]

    Solvent2_Conc_Label_List = [Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label,\
                            Row1_Solvent2_Conc_Label,Row2_Solvent2_Conc_Label,Row3_Solvent2_Conc_Label,Row4_Solvent2_Conc_Label,Row5_Solvent2_Conc_Label,Row6_Solvent2_Conc_Label,\
                            Row7_Solvent2_Conc_Label,Row8_Solvent2_Conc_Label,Row9_Solvent2_Conc_Label,Row10_Solvent2_Conc_Label,Row11_Solvent2_Conc_Label,Row12_Solvent2_Conc_Label]



    SS_Conc_Label_List = [Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label,\
                           Row1_SS_Conc_Label, Row2_SS_Conc_Label, Row3_SS_Conc_Label, Row4_SS_Conc_Label,\
                           Row5_SS_Conc_Label, Row6_SS_Conc_Label, Row7_SS_Conc_Label, Row8_SS_Conc_Label,\
                           Row9_SS_Conc_Label, Row10_SS_Conc_Label, Row11_SS_Conc_Label, Row12_SS_Conc_Label]

    Ingr_Label_List = [Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label,\
                        Row1_Ingr_Label,Row2_Ingr_Label,Row3_Ingr_Label,Row4_Ingr_Label,Row5_Ingr_Label,Row6_Ingr_Label,\
                        Row7_Ingr_Label,Row8_Ingr_Label,Row9_Ingr_Label,Row10_Ingr_Label,Row11_Ingr_Label,Row12_Ingr_Label]

    SS_Label_List = [Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label,\
                        Row1_SS_Label,Row2_SS_Label,Row3_SS_Label,Row4_SS_Label,Row5_SS_Label,Row6_SS_Label,\
                        Row7_SS_Label,Row8_SS_Label,Row9_SS_Label,Row10_SS_Label,Row11_SS_Label,Row12_SS_Label]
    
    Dilu_Label_List = [Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label,\
                        Row1_Dilu_Label,Row2_Dilu_Label,Row3_Dilu_Label,Row4_Dilu_Label,Row5_Dilu_Label,Row6_Dilu_Label,\
                        Row7_Dilu_Label,Row8_Dilu_Label,Row9_Dilu_Label,Row10_Dilu_Label,Row11_Dilu_Label,Row12_Dilu_Label]

    
    # "Sub" how is many columns away from the rows labelling column the "ingredients,vols,concs" labels are
    global Sub
    Sub = 10
    
    #Heading_Label.grid(row=Tray_Label_row,column=Tray_Label_column-1, columnspan = 3,sticky=N+S+E+W)

    
    ##### TRAY SETUP OT ##### ##### TRAY SETUP OT ##### ##### TRAY SETUP OT ##### ##### TRAY SETUP OT #####
        # GLOBAL DECLARATIONS

    return Inputs(0)

    
Restart()
