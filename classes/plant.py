from scipy.optimize import fsolve

class Plant():
    def __init__(self,name):
        self.name = name
        self.nodes = {}
        self.streams = {}
        self.list_recycle_streams = []
        self.solved_nodes = set()

    def __repr__(self):
        return f"<Plant {self.name}>"

    def add_node(self,node):
        self.nodes[node.name] = node
        return node

    def add_stream(self,stream):
        self.streams[stream.name] = stream
        return stream


    def assign_streams(self):
        for node in self.nodes:
            for stream in self.streams:
                if stream.destination == node.name:
                    node.inputs[stream.name] = stream            


    def check_recycle_streams(self):
        for node in self.nodes.values():
            #print(f'check_recycle_streams: Checking node {node.name} for recycle streams')
            for stream in node.inputs.values():
                #print(f'check_recycle_streams: Checking input stream {node.name}: {stream.name if stream else "None"}')
                if stream is not None and stream.source is not None:
                    if stream.source == node:
                        self.list_recycle_streams.append(stream)
                        print(f'check_recycle_streams: Detected recycle stream {stream.name} in node {node.name}')
        return self.list_recycle_streams


    def solve_plant(self, max_iter=100):
        for i in range(max_iter):
            progress = False

            for node in self.nodes.values():
                if node in self.solved_nodes:
                    continue

                if all(
                    port.connected_stream is not None and port.connected_stream.flow is not None
                    for port in node.inputs.values()
                ):
                    node.solve()
                    self.solved_nodes.add(node)
                    progress = True
                    print(f"solve_plant: Solved node {node.name}")

            if not progress:
                print("solve_plant: No further progress possible")
                break

        else:
            print("solve_plant: Reached max iterations")

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
                #print(f'solve_recycles: Iteration {i}, Stream {stream.name}: flow={stream.flow}')  #Debug: Recycle iterations
                if abs(new - stream._guess) > tolerance:
                    converged = False
                    stream._guess = new
                    stream.flow = new
                    #print(f'solve_recycles: Stream {stream.name} not converged: new={new}, guess={stream._guess}')
            if converged:
                print(f"All recycle streams converged in {i} iterations")
                return
        raise RuntimeError("Recycle solver did not converge")


    def view(self,show_all=False):
        print(f"Plant: {self.name}")
        print("Nodes:")
        for node in self.nodes.values():
            node.view_node(show_all)

    

    def find_variable(self, var, target, target_value, guess):
        def get_value(path):          #"MF.outputs.filtrate.flow"    MF.avg_flux
            parts = path.split(".")
    
            obj = self.nodes[parts[0]]  # start at node

            for part in parts[1:]:
                if isinstance(obj, dict):
                    obj = obj[part]
                else:
                    obj = getattr(obj, part)

            return obj

        def set_variable(path, value):
            parts = path.split(".")
            obj = self.nodes[parts[0]]

            for part in parts[1:-1]:
                if isinstance(obj, dict):
                    obj = obj[part]
                else:
                    obj = getattr(obj, part)
            last = parts[-1]
            if isinstance(obj, dict):
                obj[last] = value
            else:
                setattr(obj, last, value)
            print(f'solve: Set variable {path} to {value}')

        def func(x):
            set_variable(var,x)
            self.solve_plant()
            result = get_value(target)
            return result - target_value
        solution = fsolve(func, guess)
        return solution[0]