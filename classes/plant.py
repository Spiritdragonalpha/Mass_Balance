from .node import Node
from .stream import Stream

class Plant():
    def __init__(self,name):
        self.name = name
        self.nodes = {}
        self.streams = {}
        self.list_recycle_streams = []
        self.solved_nodes = set()

    def solve_plant(self):
        list_recycle_streams = self.check_recycle_streams()
        print(f'solve_plant: Found {len(list_recycle_streams)} recycle stream(s)')
        for stream in list_recycle_streams:
            print(f'solve_plant: Recycle Stream: {stream.name} from {stream.source.name} to {stream.destination.name}')
            if list_recycle_streams:
                self.solve_recycles(list_recycle_streams)
            else:
                self.solve_once()


    def check_recycle_streams(self):
        for node in self.nodes.values():
            #print(f'check_recycle_streams: Checking node {node.name} for recycle streams')
            for stream in node.inputs.values():
                print(f'check_recycle_streams: Checking input stream {node.name}: {stream.name if stream else "None"}')
                if stream is not None and stream.source is not None:
                    if stream.source == node:
                        self.list_recycle_streams.append(stream)
                        print(f'check_recycle_streams: Detected recycle stream {stream.name} in node {node.name}')
        return self.list_recycle_streams


    def solve_once(self):
        for node in self.nodes.values():
            if all(stream is not None and stream.flow is not None for stream in node.inputs.values()):
                node.solve()
                print(f"solve_once: Solved node {node.name}")
            else:
                print(f"solve_once: Skipping node {node.name}, inputs not ready")

    def solve_recycles(self, list_recycle_streams, tolerance=1e-6):
        print(f'solve_recycles: Solving plant with {len(list_recycle_streams)} recycle stream(s)')
        for stream in list_recycle_streams:
            if stream.flow is None:
                stream.flow = 1.0
            if not hasattr(stream, "_guess") or stream._guess is None:
                stream._guess = stream.flow

        for i in range(100):
            self.solve_once()
            converged = True
            for stream in list_recycle_streams:
                new = stream.flow
                print(f'solve_recycles: Iteration {i}, Stream {stream.name}: flow={stream.flow}')  #Debug: Recycle iterations
                if abs(new - stream._guess) > tolerance:
                    converged = False
                    stream._guess = new
                    stream.flow = new
                    print(f'solve_recycles: Stream {stream.name} not converged: new={new}, guess={stream._guess}')
            if converged:
                print(f"All recycle streams converged in {i} iterations")
                return
        raise RuntimeError("Recycle solver did not converge")