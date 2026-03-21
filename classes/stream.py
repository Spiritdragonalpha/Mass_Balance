class Stream():
    def __init__(self,name,flow=None,source=None,destination=None):
        self.name = name
        self.flow = flow
        self.composition = {}
        self.source = source
        self.destination = destination
        self.is_recycle = False
    def __repr__(self):
        return f"<Stream {self.source}.{self.name} (Flow: {self.flow})(Destination: {self.destination})>"



