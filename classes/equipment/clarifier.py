from classes import Node


class Clarifier (Node):
    def __init__(self,name,wasting_ratio=None):
        super().__init__(name)

        self.wasting_ratio = wasting_ratio

    def get_parameters(self):
                return {
            'wasting_ratio': self.wasting_ratio
        }

    def solve(self):
        #Calculations
        feed = sum(stream.flow for stream in self.inputs.values() if stream is not None)
        sludge_flow = feed * self.wasting_ratio
        effluent_flow = feed - sludge_flow

        #Assign to output streams
        self.outputs['sludge'].flow = sludge_flow
        self.outputs['effluent'].flow = effluent_flow

    