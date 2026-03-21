from classes import Node, Stream


class Clarifier (Node):
    def __init__(self,name,wasting_ratio=.15):
        super().__init__(name)

        self.add_input('feed')
        self.add_output('sludge')
        self.add_output('effluent')
        
        self.wasting_ratio = wasting_ratio

    def get_parameters(self):
                return {
            'wasting_ratio': self.wasting_ratio
        }

    def solve(self):
        feed = sum(stream.flow for stream in self.inputs.values() if stream is not None)
        sludge_flow = feed * self.wasting_ratio
        effluent_flow = feed - sludge_flow

        self.outputs['sludge'] = sludge_flow
        self.outputs['effluent'] = effluent_flow

    