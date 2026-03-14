import NodeClass, StreamClass, PlantClass


def main():
    Haile = PlantClass.Plant('Haile')
    
    Clarifier1 = NodeClass.Clarifier('Clarifier1', wasting_ratio=0.1)
    RO1 = NodeClass.RO('RO1', recovery=0.8)

    Haile.nodes['Clarifier1'] = Clarifier1
    Haile.nodes['RO1'] = RO1

    Main_Feed = StreamClass.Stream('Feed', flow=1000)

    Clarifier1.inputs['feed'] = Main_Feed
    Clarifier1.inputs['recycle'] = Clarifier1.outputs['sludge']
    Clarifier1.outputs['sludge'].destination = Clarifier1
    RO1.inputs['feed'] = Clarifier1.outputs['effluent']

    
    Haile.solve_plant()

    print("Main Feed:", Main_Feed.flow)
    print("Effluent:", Clarifier1.outputs['effluent'].flow)
    print("Sludge:", Clarifier1.outputs['sludge'].flow)
    print("Permeate:", RO1.outputs['permeate'].flow)
    print("Concentrate:", RO1.outputs['concentrate'].flow)




if __name__ == "__main__":
    main()