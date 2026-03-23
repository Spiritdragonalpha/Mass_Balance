from classes import Node
from utils import *


class MF(Node):
    def __init__(self,name, xr_percentage= None,):
        super().__init__(name)

        self.xr_percentage = xr_percentage

    def get_parameters(self):
      return {
            'xr_percentage': self.xr_percentage,}

       

    def solve(self):
        feed = sum(stream.flow for stream in self.inputs.values() if stream is not None)
        xr_flow = feed * self.xr_percentage
        filtrate_flow = feed - xr_flow

        self.outputs['filtrate'].flow = filtrate_flow
        self.outputs['xr'].flow = xr_flow