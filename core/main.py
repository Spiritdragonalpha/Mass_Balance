from classes import Stream, Plant
from classes.equipment import *
from utils import *


def Test1():
    plant = Plant('Haile')
   
    clarifier1 = plant.add_node(Clarifier('Clarifier1', wasting_ratio=.25))
    mf1 = plant.add_node(MF('MF1',xr_percentage=.25))
    ro1 = plant.add_node(RO('RO1',recovery = .75))

    plant.add_stream('feed', destination=clarifier1)
    plant.add_stream('sludge', source=clarifier1)
    plant.add_stream('effluent', source=clarifier1, destination=mf1)
    plant.add_stream('xr', source=mf1)
    plant.add_stream('filtrate', source=mf1,destination=ro1)
    plant.add_stream('permeate', flow=270,source=ro1)
    plant.add_stream('concentrate',source=ro1)


    plant.initialize()
    plant.solve_plant()
    plant.view()

def main():
    
    Test1()


if __name__ == "__main__":
    main()