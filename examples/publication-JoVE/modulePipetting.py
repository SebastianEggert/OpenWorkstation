from opentrons import robot, containers, instruments

def getEquipment():
      equipment={}
      containers.create('heating-block-3x4', grid=(3, 4), spacing=(22.3, 22.3), diameter=17, depth=45)
      equipment['InputsC1'] = containers.load('heating-block-3x4','C1')
      containers.create('heating-block-3x4', grid=(3, 4), spacing=(22.3, 22.3), diameter=17, depth=45)
      equipment['MixingD1'] = containers.load('heating-block-3x4','D1')
      equipment['OutputD2'] = containers.load('96-flat','D2')
      equipment['TouchC2'] = containers.load('96-flat','C2')
      containers.create('1000tiprack2', grid=(7, 5), spacing=(10.3, 18.6), diameter=9, depth=56)
      equipment['1000tiprack'] = containers.load('1000tiprack2', 'B2')
      equipment['100TiprackB1'] = containers.load('tiprack-1000ul', 'B1')
      equipment['TrashA1'] = containers.load('trash-box','A1')
      equipment['pd1000'] = instruments.Pipette(
         name='pd1000',
         axis='b',
         max_volume=1000,
         min_volume=100,
         channels=1,
         aspirate_speed=800,
         dispense_speed=1200,
         trash_container=equipment['TrashA1'])
      equipment['pd100'] = instruments.Pipette(
         name='pd100',
         axis='a',
         max_volume=100,
         min_volume=10,
         channels=1,
         aspirate_speed=600,
         dispense_speed=1000,
         trash_container=equipment['TrashA1'])
      return(equipment)



