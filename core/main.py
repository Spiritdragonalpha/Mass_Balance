from classes import Stream, Plant
from classes.equipment import *


def Test1(recycle_test):
    Haile = Plant('Haile')
    
    Clarifier1 = Clarifier('Clarifier1', wasting_ratio=0.25)
    MF1 = MF('MF1', XR_percentage=0.25)
    RO1 = RO('RO1', recovery=0.75)

    Haile.nodes['Clarifier1'] = Clarifier1
    Haile.nodes['MF1'] = MF1
    Haile.nodes['RO1'] = RO1

    wtp_feed = Stream('Feed', flow=640)

    Clarifier1.inputs['feed'] = wtp_feed
    if recycle_test == 1:
        Clarifier1.inputs['sludge_recycle'] = Clarifier1.outputs['sludge']
        Clarifier1.outputs['sludge'].destination = Clarifier1 #primitive logic to create recycle
    if recycle_test == 2:
        MF1.inputs['xr_recycle'] = MF1.outputs['XR']
        MF1.outputs['XR'].destination = MF1

    MF1.inputs['feed'] = Clarifier1.outputs['effluent']
    RO1.inputs['feed'] = MF1.outputs['filtrate']


    
    Haile.solve_plant()

    Haile.view_plant(show_all=True)
    #print(Haile.find_variable(var='Clarifier1.inputs.feed.flow', target='RO1.outputs.permeate.flow', target_value=500, guess=1000))
    #Haile.view_plant()

    print(RO1.outputs['permeate'].flow,
            RO1.outputs['concentrate'].flow,
            MF1.outputs['filtrate'].flow,
            MF1.outputs['XR'].flow,
            Clarifier1.outputs['effluent'].flow,
            Clarifier1.outputs['sludge'].flow)

def main():
    
    Test1(False)


if __name__ == "__main__":
    main()