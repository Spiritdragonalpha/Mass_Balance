from classes import Node, Stream


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