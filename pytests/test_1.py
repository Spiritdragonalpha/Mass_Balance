from classes import Stream, Plant
from classes.equipment import *


def test_basic():
    plant = Plant('Haile')
   
    clarifier1 = plant.add_node(Clarifier('Clarifier1', wasting_ratio=.25))
    mf1 = plant.add_node(MF('MF1',xr_percentage=.25))
    ro1 = plant.add_node(RO('RO1',recovery = .75))

    plant.add_stream('feed', flow=640, destination=clarifier1)
    plant.add_stream('sludge', source=clarifier1)
    plant.add_stream('effluent', source=clarifier1, destination=mf1)
    plant.add_stream('xr', source=mf1)
    plant.add_stream('filtrate', source=mf1,destination=ro1)
    plant.add_stream('permeate',source=ro1)
    plant.add_stream('concentrate',source=ro1)


    plant.initialize()
    plant.solve_plant()

    solution = [
        480.0, #effluent
        160.0, #sludge
        360.0, #filtrate
        120.0, #XR
        270.0, #perm
        90.0]  #brine 
    
    results = [
            clarifier1.outputs['effluent'].flow,
            clarifier1.outputs['sludge'].flow,
            mf1.outputs['filtrate'].flow,
            mf1.outputs['xr'].flow,
            ro1.outputs['permeate'].flow,
            ro1.outputs['concentrate'].flow]
    assert results == solution