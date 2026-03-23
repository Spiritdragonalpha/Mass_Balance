from utils import *

class Node():
    def __init__(self,name):
        self.name = name
        self.inputs = {}
        self.outputs = {}

    def __repr__(self):
        return f"<Node: {self.name}>"


    def get_parameters(self):
        return {}

    def view_node(self,show_all=False):
        draw_line()
        print(f'Node: {self.name}')
        print("Input Streams:")
        for key, stream in self.inputs.items():
            if stream.flow is not None: print(f"  {key}: {stream.flow} gpm")
            else: print(f'  {key}:')
        print("Output Streams:")
        for key, stream in self.outputs.items():
            if stream.flow is not None: print(f"  {key}: {stream.flow} gpm")
            else: print(f'  {key}:')
        if show_all:
            params = self.get_parameters()
            if params:
                print("Parameters:")
                for key, value in params.items():
                    if value:
                        print(f"  {key}: {value}")


    






