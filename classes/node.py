#from .stream import Stream
from utils import *

class Node():
    def __init__(self,name):
        self.name = name
        self.inputs = {}
        self.outputs = {}

    def __getattr__(self, name):
        if name in self.inputs:
            return self.inputs[name]
        if name in self.outputs:
            return self.outputs[name]
        raise AttributeError(f"{name} not found in inputs or outputs of {self.name}")

    def get_parameters(self):
        return {}

    def view_node(self,show_all=False):
        draw_line()
        print(f"Node: {self.name}")
        print("Input Streams:")
        for key, stream in self.inputs.items():
            print(f"  {key}: {stream.flow} gpm")
        print("Output Streams:")
        for key, stream in self.outputs.items():
            print(f"  {key}: {stream.flow} gpm")
        if show_all:
            params = self.get_parameters()
            if params:
                print("Parameters:")
                for key, value in params.items():
                    if value:
                        print(f"  {key}: {value}")
                    else: print(f"  {key}: {value}")








