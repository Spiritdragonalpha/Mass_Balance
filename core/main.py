from classes import Stream, Plant
from classes.equipment import *
from utils import *


def Test1():
    plant = Plant('Haile')
   
    clarifier = plant.add_node(Clarifier('Clarifier1'))
    mf = plant.add_node(MF('MF1'))
    ro = plant.add_node(RO('RO1',recovery = .68))

    wtp_feed = Stream('wtp_feed',flow = 640)

    connect(wtp_feed,destination_port=clarifier.feed)
    connect(clarifier.effluent,destination_port=mf.feed)
    connect(mf.filtrate,destination_port=ro.feed)

    plant.solve_plant()
    plant.view()

def main():
    
    Test1()


if __name__ == "__main__":
    main()