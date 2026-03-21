from classes import Node, Stream

class RO(Node):
    def __init__(self,name,recovery):
        super().__init__(name)
        self.add_input('feed')
        self.add_output('permeate')
        self.add_output('concentrate')

        self.recovery = recovery

    def get_parameters(self):
        return {
            'recovery': self.recovery
        }

    def solve(self):
        feed = sum(stream.flow for stream in self.inputs.values() if stream is not None)
        permeate = feed*self.recovery
        concentrate = feed-permeate
        
        self.outputs['permeate'] = permeate
        self.outputs['concentrate'] = concentrate



