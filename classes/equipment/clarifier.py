from classes import Node, Stream


class Clarifier (Node):
    def __init__(self,name,wasting_ratio):
        super().__init__(name)
        self.inputs = {
            'feed': None
            }
        self.outputs = {
            'effluent': Stream(f'{name}_effluent',source=self),
            'sludge': Stream(f'{name}_sludge',source=self)
            }
        self.wasting_ratio = wasting_ratio

    def get_parameters(self):
                return {
            'wasting_ratio': self.wasting_ratio
        }

    def solve(self):
        feedflow = sum(stream.flow for stream in self.inputs.values() if stream is not None)
        effluent = self.outputs['effluent']
        sludge = self.outputs['sludge']

        sludge.flow = feedflow * self.wasting_ratio
        effluent.flow = feedflow - sludge.flow

    