# NavisSpace3D
Indoor Navigation System for Large Buildings using Python, 3D Graphs, and Linear Algebra

Overview

PathMatrix 3D is a Python-based indoor navigation system designed for large multi-floor buildings such as hospitals, malls, universities, and airports.

Traditional GPS systems fail indoors, making navigation difficult. This project solves that problem by modeling the building as a 3D graph structure and computing the shortest route between two locations across multiple floors.

The system uses 3D coordinate mapping, graph theory, vectors, and matrix transformations to visualize paths in three-dimensional space.

🧩 Problem Statement

People often get lost inside large buildings because GPS signals are weak or unavailable indoors.

This becomes especially critical in:

Hospitals
Shopping malls
Corporate offices
Educational campuses
Airports

The objective is to create a smart navigation system that helps users move from a source location to a destination using the shortest and most efficient path.

💡 Core Concepts Used
1. 3D Coordinate System

Each location is represented as:

[
(x, y, z)
]

Where:

x → horizontal position
y → vertical position on floor map
z → floor number

Example:

Reception → (2, 4, 0)
ICU → (8, 3, 2)
2. Linear Algebra

This project heavily uses linear algebra concepts such as:

Vectors for movement direction
Matrices for floor transformations
Coordinate transformations
Distance calculations
Adjacency matrices

Example distance formula:

[
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}
]

3. Graph Theory

The building is modeled as a 3D weighted graph.

Each room, lift, staircase, and hallway intersection is a node.

Paths between them are edges.

Shortest path algorithms used:

Dijkstra’s Algorithm
A* Search Algorithm
⚙️ Features
Multi-floor indoor navigation
3D building representation
Stair/lift floor transitions
Shortest path computation
Real-time path visualization
Python-based implementation
Linear algebra driven coordinate transformation
🛠️ Tech Stack
Python
NumPy → matrix operations
NetworkX → graph pathfinding
Matplotlib (3D) → visualization
Plotly (optional for interactive 3D graphs)
📂 Project Structure
PathMatrix3D/
│
├── main.py
├── graph_builder.py
├── pathfinder.py
├── visualization.py
├── floor_mapper.py
├── requirements.txt
└── README.md
🚀 Working
User enters source and destination
System maps coordinates in 3D space
Graph nodes are generated
Shortest path is calculated
3D path is displayed
📊 Output

The output shows:

Start point
Destination
Floor transitions
3D route visualization

Example:

Start → Reception
Destination → ICU (2nd Floor)

Output path:

Reception → Lift → Floor 1 → Floor 2 → ICU

📈 Real World Impact

This project can be used in:

🏥 Hospitals

Critical for emergency navigation:

ICU
Operation theatres
Labs
Emergency wards
Shopping Malls
Store navigation
Parking guidance
Exit routing
->Universities
Classroom navigation
Department blocks
Lab access
-> Future Scope
Voice-guided navigation
AR route overlay
Mobile app integration
Real-time crowd avoidance
Emergency evacuation paths
-> Developed Using

Python + 3D Geometry + Linear Algebra + Graph Algorithms
