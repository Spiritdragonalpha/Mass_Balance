from classes import Stream, Plant
from classes.equipment import *


def test_basic(wtp_feed_flow=640):
    my_Plant = Plant('Plant')
    
    Clarifier1 = Clarifier('Clarifier1', wasting_ratio=0.25)
    MF1 = MF('MF1', XR_percentage=0.25)
    RO1 = RO('RO1', recovery=0.75)

    my_Plant.nodes['Clarifier1'] = Clarifier1
    my_Plant.nodes['MF1'] = MF1
    my_Plant.nodes['RO1'] = RO1

    wtp_feed = Stream('Feed', flow=wtp_feed_flow)

    Clarifier1.inputs['feed'] = wtp_feed
    MF1.inputs['feed'] = Clarifier1.outputs['effluent']
    RO1.inputs['feed'] = MF1.outputs['filtrate']

    my_Plant.solve_plant()
    solution = [
        480.0, #effluent
        160.0, #sludge
        360.0, #filtrate
        120.0, #XR
        270.0, #perm
        90.0]  #brine 
    
    results = [
            Clarifier1.outputs['effluent'].flow,
            Clarifier1.outputs['sludge'].flow,
            MF1.outputs['filtrate'].flow,
            MF1.outputs['XR'].flow,
            RO1.outputs['permeate'].flow,
            RO1.outputs['concentrate'].flow]
    assert results == solution


def test_recycle1():
    my_Plant = Plant('Haile')
    
    Clarifier1 = Clarifier('Clarifier1', wasting_ratio=0.5)
    MF1 = MF('MF1', XR_percentage=0.5)
    RO1 = RO('RO1', recovery=0.5)

    my_Plant.nodes['Clarifier1'] = Clarifier1
    my_Plant.nodes['MF1'] = MF1
    my_Plant.nodes['RO1'] = RO1

    wtp_feed = Stream('Feed', flow=640)

    Clarifier1.inputs['feed'] = wtp_feed
    Clarifier1.inputs['sludge_recycle'] = Clarifier1.outputs['sludge']
    Clarifier1.outputs['sludge'].destination = Clarifier1 #primitive logic to create recycle

    MF1.inputs['xr_recycle'] = MF1.outputs['XR']
    MF1.outputs['XR'].destination = MF1

    MF1.inputs['feed'] = Clarifier1.outputs['effluent']
    RO1.inputs['feed'] = MF1.outputs['filtrate']

    my_Plant.solve_plant()
    solution = [
        480.0, #effluent
        160.0, #sludge
        360.0, #filtrate
        120.0, #XR
        270.0, #perm
        90.0]  #brine 

    results = [
            Clarifier1.outputs['effluent'].flow,
            Clarifier1.outputs['sludge'].flow,
            MF1.outputs['filtrate'].flow,
            MF1.outputs['XR'].flow,
            RO1.outputs['permeate'].flow,
            RO1.outputs['concentrate'].flow]
    assert results == solution

def test_recycle2():
    my_Plant = Plant('Haile')
    
    Clarifier1 = Clarifier('Clarifier1', wasting_ratio=0.5)
    MF1 = MF('MF1', XR_percentage=0.5)
    RO1 = RO('RO1', recovery=0.5)

    my_Plant.nodes['Clarifier1'] = Clarifier1
    my_Plant.nodes['MF1'] = MF1
    my_Plant.nodes['RO1'] = RO1

    wtp_feed = Stream('Feed', flow=640)

    Clarifier1.inputs['feed'] = wtp_feed
    Clarifier1.inputs['sludge_recycle'] = Clarifier1.outputs['sludge']
    Clarifier1.outputs['sludge'].destination = Clarifier1 #primitive logic to create recycle

    Clarifier1.inputs['xr_recycle'] = MF1.outputs['XR']
    MF1.outputs['XR'].destination = Clarifier1

    MF1.inputs['feed'] = Clarifier1.outputs['effluent']
    RO1.inputs['feed'] = MF1.outputs['filtrate']

    my_Plant.solve_plant()
    solution = [
        480.0, #effluent
        160.0, #sludge
        360.0, #filtrate
        120.0, #XR
        270.0, #perm
        90.0]  #brine 

    results = [
            Clarifier1.outputs['effluent'].flow,
            Clarifier1.outputs['sludge'].flow,
            MF1.outputs['filtrate'].flow,
            MF1.outputs['XR'].flow,
            RO1.outputs['permeate'].flow,
            RO1.outputs['concentrate'].flow]

    assert results == solution