from opentrons import robot, robot2, containers, instruments


def getTransportposition():
        transportposition={}

        # module positions
        transportposition['modulePipetting']  = 'G0 X481 Y5 Z5 A4 B5 F2000'
        transportposition['moduleCrosslinker']  = 'G0 X170 Y5 Z5 A4 B5 F2000'
        transportposition['moduleStorage']  = 'G0 X21.3 Y5 Z5 A4 B5 F2000'


        return(transportposition)
