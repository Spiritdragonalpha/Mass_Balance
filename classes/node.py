from .stream import Stream
import os

def draw_line():
    try: columns = os.get_terminal_size().columns
    except OSError:columns = 80 
    print("-" * columns)


class Node():
    def __init__(self,name):
        self.name = name
        self.inputs = []
        self.outputs = []


    def view_node(self):
        draw_line()
        print(f"Node: {self.name}")
        print("Input Streams:")
        for key, stream in self.inputs.items():
            print(f"  {key}: {stream.flow} gpm")
        print("Output Streams:")
        for key, stream in self.outputs.items():
            print(f"  {key}: {stream.flow} gpm")
        params = self.get_parameters()
        if params:
            print("Parameters:")
            for key, value in params.items():
                print(f"  {key}: {value}")

        def get_parameters(self):
            return {}







        
