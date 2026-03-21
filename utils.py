import os

def draw_line():
    try: columns = os.get_terminal_size().columns
    except OSError:columns = 80 
    print("-" * columns)

def gpm_to_gpd(gpm):
    return gpm * 1440
def gpd_to_gpm(gpd):
    return gpd / 1440



def connect(stream, source_port = None, destination_port = None):
    if source_port:
        if source_port.kind != 'output':
            raise ValueError("Source must be an output port")
        node = source_port.node
        node.outputs[source_port.name] = stream
        stream.source = (node, source_port.name)
    if destination_port:
        if destination_port.kind != 'input':
            raise ValueError("Destination must be an input port")
        node = destination_port.node
        node.inputs[destination_port.name] = stream
        stream.destination = (node, destination_port.name)

