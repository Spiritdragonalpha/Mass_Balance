from scipy.optimize import fsolve
from classes import Stream
import os

class Plant():
    def __init__(self,name):
        self.name = name
        self.nodes = {}
        self.streams = {}
        self.list_recycle_streams = []
        self.solved_nodes = set()

    def __repr__(self):
        return f"<Plant {self.name}>"

    def view(self,show_all=False):

        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
        print(f"Plant: {self.name}")
        print("Nodes:")
        for node in self.nodes.values():
            node.view_node(show_all)

    def add_node(self,node):
        self.nodes[node.name] = node
        return node

    #Create a stream, and set its connections
    def add_stream(self, name, flow=None, source=None, destination=None):
        stream = Stream(name,flow)
        self.streams[name]=stream
        if source:
            stream.source = source
        if destination:
            stream.destination = destination
        return stream

    #Inititalize the plant by storing all stream inputs/outputs into the nodes
    def initialize(self):
        for stream in self.streams.values():
                if stream.source is not None:
                    stream.source.outputs[stream.name] = stream

                if stream.destination is not None:
                    stream.destination.inputs[stream.name] = stream


    def solve_plant(self, max_iter=100):
        solved_nodes = set()

        for i in range(max_iter):
            progress = False

            for node in self.nodes.values():
                if node in solved_nodes:
                    continue
                if all(
                    stream is not None and stream.flow is not None
                    for stream in node.inputs.values()
                ):
                    node.solve()
                    solved_nodes.add(node)
                    progress = True
                    print(f"Solved node: {node.name}")

            if not progress:
                print("No further progress possible")
                break
        else:
            print("Reached max iterations")


    

    
