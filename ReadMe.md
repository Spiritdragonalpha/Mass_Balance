# Overview Page

The purpose of this code is to create a mass balance tool capable of giving flow data for equipment typically used by Linkan in designing water treatment plants.

## Outline

- The mass balance will be composed of various nodes, each with input(s) and output(s)
- Each node will be a piece of equipment 
	- MF rack, RO skid, clarifier etc.
- The program should be able to easily add/remove nodes and be flexible enough to create new types of nodes for new projects
- The data should be displayed cleanly
- Each data point should have the option to see the formula of how that number was calculated
- Needs a way to "work backwards" from a desired output to find the necessary input
- Include a way to show in Excel


## Project Structure

water_mass_balance/

equipment/
    base_node.py
    ro.py
    clarifier.py
    filter.py

core/
    stream.py
    plant.py
    solver.py

export/
    excel_export.py

ui/
    streamlit_app.py


-import networkx as nx

### Node classes

class Node:
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def calculate(self):
        pass

class ROSkid(Node):

    def __init__(self, name, recovery):
        super().__init__(name)
        self.recovery = recovery

    def calculate(self):
        feed = self.inputs[0]

        permeate_flow = feed.flow * self.recovery
        brine_flow = feed.flow - permeate_flow

        self.outputs[0].flow = permeate_flow
        self.outputs[1].flow = brine_flow





### Equipment list

- MF rack
- UF rack
- RO skid
- Clarifier
- Sludge press
- Sludge thickener
- Chemical storage
- Reaction tank
- Forwarding tanks
- Sand filter
- Multimedia filter
- Mixing tank
- Oil/water separator
- DAF
- Pond
- Finished water storage
