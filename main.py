from classes import Node, Stream, Plant, draw_line
import classes.equipment as eq



def main():
    Haile = Plant('Haile')
    
    Clarifier1 = eq.Clarifier('Clarifier1', wasting_ratio=0.1)
    RO1 = eq.RO('RO1', recovery=0.8)

    Haile.nodes['Clarifier1'] = Clarifier1
    Haile.nodes['RO1'] = RO1

    Main_Feed = Stream('Feed', flow=1000)

    Clarifier1.inputs['feed'] = Main_Feed
    Clarifier1.inputs['recycle'] = Clarifier1.outputs['sludge']
    Clarifier1.outputs['sludge'].destination = Clarifier1
    RO1.inputs['feed'] = Clarifier1.outputs['effluent']

    
    Haile.solve_plant()

    Clarifier1.view_node()
    RO1.view_node()






if __name__ == "__main__":
    main()