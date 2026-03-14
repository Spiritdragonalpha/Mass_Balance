from classes import Node, Stream

class RO(Node):
    def __init__(self,name,recovery):
        super().__init__(name)
        self.inputs = {
            'feed':None
            }
        self.outputs = {
            'permeate': Stream(f'{name}_permeate'),
            'concentrate': Stream(f'{name}_concentrate')
            }
        self.recovery = recovery

    def get_parameters(self):
        return {
            'recovery': self.recovery
        }

    def solve(self):
        feed = self.inputs['feed']
        permeate = self.outputs['permeate']
        concentrate = self.outputs['concentrate']
        
        permeate.flow = feed.flow * self.recovery
        concentrate.flow = feed.flow - permeate.flow



