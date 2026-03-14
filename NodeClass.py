from StreamClass import Stream

class Node():
    def __init__(self,name):
        self.name = name
        self.inputs = []
        self.outputs = []


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

    #def setRecovery(self, recovery):
    #   self.recovery = recovery

    def solve(self):
        feed = self.inputs['feed']
        permeate = self.outputs['permeate']
        concentrate = self.outputs['concentrate']
        
        permeate.flow = feed.flow * self.recovery
        concentrate.flow = feed.flow - permeate.flow



class Clarifier(Node):
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

    def solve(self):
        feed = sum(stream.flow for stream in self.inputs.values() if stream is not None)
        effluent = self.outputs['effluent']
        sludge = self.outputs['sludge']

        sludge.flow = feed * self.wasting_ratio
        effluent.flow = feed - sludge.flow



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



class MF(Node):
        def __init__(self,name,XR_percentage):
            super().__init__(name)
            self.inputs = {
                'feed':None
                }
            self.outputs = {
                'filtrate': Stream(f'{name}_filtrate'),
                'xrflow': Stream(f'{name}_xrflow')
                }
            self.XR_percentage = XR_percentage

        def solve(self):
            feed = self.inputs['feed']
            filtrate = self.outputs['filtrate']
            XR_percentage = self.outputs['xrflow']
        
