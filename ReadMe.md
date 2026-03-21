# Overview Page

The purpose of this code is to create a mass balance tool capable of giving flow data for equipment typically used in designing water treatment plants.

## Outline

- The mass balance will be composed of various nodes, each with input(s) and output(s)
- Each node will be a piece of equipment
  - MF rack, RO skid, clarifier etc.
- The program should be able to easily add/remove nodes and be flexible enough to create new types of nodes for new projects
- The data should be displayed cleanly
- Each data point should have the option to see the formula of how that number was calculated
- Needs a way to "work backwards" from a desired output to find the necessary input
    -fsolve()
- Excel functionality
  -  Import data
   - Export data
- Nodes only take in input stream flows, calc internal variables, and output stream flows
- Streams are a data container
    -flow data
    -TDS
    -species



## Project Structure

`
Mass_Balance/                               #Main directory
│
├── core/
│   └── main.py                             #run this from terminal
│
├── classes/
│   ├── __init__.py
│   ├── node.py                             #parent node class
│   ├── stream.py                           #stream class
│   ├── plant.py                            #plant class
│   └── equipment/                          #child node class for specific equipment
│       ├── __init__.py
│       └── ... (Clarifier, MF, RO, etc.)
│
├── utils.py                                #helper functions
│
├── pytests/                                #pytesting
│   ├── test_1.py
│   └── ...
│
├── .venv/                                  #environment
├── ui/                                     #ui elements/code
│   └── streamlit.py
├── requirements.txt                        #environemnt requirements
├── README.md
└── ...
`



## To Do


### Miscellaneous

- Import data from Excel
- Export data to Excel
- Overspecify vs underspecify system
- Display formulas for data points
- fsolve function
- fsolve multiple variables

- Include instantaneous vs average auto calculated


### Recycle

- Detect a recycle stream
- Able to detect recycle streams if recycling back to the same node
- Need to impliment further logic to detect recycle back to previous nodes upstream



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
  - Residency Time
- Finished water storage





## Completed

- Add stream to array of recycle streams
- Run iterative solver on recycle streams until convergence
- Connect streams to nodes
- Get basic flow data from nodes
- Display equipment data in a clean way
-pytests

