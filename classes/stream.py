class Stream():
    def __init__(self,name,flow=None,source=None,destination=None):
        self.name = name
        self.flow = flow
        self.composition = {}
        self.source = source
        self.destination = destination
        self.is_recycle = False

    def connect(self,source,destination):
        self.source = source
        self.destination = destination



