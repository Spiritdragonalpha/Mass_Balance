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

- water\_mass\_balance/

  - classes/

    - plant.py
    - node.py
    - stream.py
    - equipment/

      - ro.py
      - clarifier.py
      - mf.py
      - pond.py
  - core/
    - main.py
    
  - export/

    - excel\_export.py
  - ui/

    - streamlit\_app.py



\-import networkx as nx



## To Do



### Miscellaneous

\-Import data from Excel
-Export data to Excel
-Overspecify vs underspecify system
-Display formulas for data points

### Recycle

- Detect a recycle stream
-Able to detect recycle streams if recycling back to the same node
-Need to impliment further logic to detect recycle back to previous nodes upstream



### Equipment list

- MF rack

  - XR
  - AS/Backwash
  - EFM
  - Modules
  - Average vs Instantaneous
  - Flux
- UF rack

  - See MF
- **RO skid**

  - Monthly CIP
  - Daily perm Flush
  - Membrane swap
- **Clarifier**

  - Chemical addition
  - Partial sludge recirc
  - Residency time
- Sludge press
- Sludge thickener
- Chemical storage

  - Tank sizing
  - Dosing
  - TSS
- Reaction tank
- Forwarding tanks
- Sand filter
- Multimedia filter
- Mixing tank
- Oil/water separator
- DAF
- **Pond**
-Residency Time
- Finished water storage





## Completed

- Add stream to array of recycle streams
- Run iterative solver on recycle streams until convergence
- Connect streams to nodes
- Get basic flow data from nodes
-Display equipment data in a clean way

