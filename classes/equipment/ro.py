from classes import Node, Stream

class RO(Node):
    def __init__(self,name,recovery=None):
        super().__init__(name)

        self.recovery = recovery

    def get_parameters(self):
        return {
            'recovery': self.recovery
        }

    def solve(self):
        feed = sum(stream.flow for stream in self.inputs.values() if stream is not None)
        permeate = feed*self.recovery
        concentrate = feed-permeate
        
        self.outputs['permeate'].flow = permeate
        self.outputs['concentrate'].flow = concentrate



