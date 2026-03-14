from classes import Node, Stream


class Pond(Node):
    def __init__(self,name):
        super().__init__(name)
        self.inputs = {
            'feed': None
            }
        self.outputs = {
            'effluent': Stream(f'{name}_effluent')
        }
    def solve(self):
        feed = self.inputs['feed']
        effluent = self.outputs['effluent']
        effluent.flow = feed.flow