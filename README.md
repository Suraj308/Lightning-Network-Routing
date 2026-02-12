# Lightning Network Routing via Electrical Circuit Modeling
What if Payment Routing wasn't a search problem...
but a physics problem?

Instead of forcing the algorithms to find the path,
what if we let nature decide?

This project reimagines the Bitcoin Lightning Network as a living electrical circuit -
where fees becomes resistance,
channels becomes wires,
and payment flow like current through a network of energy.

Nature always finds the path of least resistance.
So why shouldn't routing?

-----

# The Vision
The Lightning Network is a graph of nodes and channels.
In this project we see them as:-

Lightning Network - Electrical Circuit
Nodes - Electrical Junction
Channel - Resistor (Wire)
Fee - Resistance
Capacity - Maximum Current
Payment - Injected Current

Instead of running Dijkstra's algorithum,
we solve Kirchoff's laws.

Instead of searching paths,
we solve linear systems.

Routing becoomes physics.

-----

# Phase 1 - Building the Electrical World

Before current can flow, the circuit must exist.

Phase 1 constructs a synthetic Lightning-Network-Data that mirrors real-world structure:

- 10 interconnected nodes
- Hub-based topology (simulating routing hubs)
- Randomized channel fees
- Randomized channel capacities
- Minimum degree>= 2 (No isolated islands)
- Visualized network structure
- JSON export for reproducibility
- Saves a png image of Generated Network Data

This is the foundation.
The world before Electricity Flows.

# Network Visualisation

Below is the Image of Synthetic Lightning Network Data-

<p align="center"><img src="Result/Phase1_Lightning_network_Data_Visualisation.png" width="650"/></p>

# Visual Encoding

The Visualisations isn't just aesthetic - it's preparation for Next.

- Edge Thickness is proportional to Channel Capacity
- Edge Colour is proportional to Channel Fee

Next phase of the project will make:-
- Fee - Resistance
- Capacity - Maximum Current 

----

# Output

Running Phase 1 Generates:
Synthetic_lightning_network_data.json
Saved Visualistion of the Synthetic Lightning Network Data Graph.

This file stores structured channel data (nodes,fees,capacities) and will be used in Phase 2 for Electrical Modeling.

# Phase 2
It is where the network stops being a graph 
and starts behaving like physics.

The synthetic Lightning Network Data built in Phase 1 is transformed into a resistive circuital system.

Path search is abandoned.
Current is allowed to flow.

# From Graph to Physics
- Load the Synthetic Lightning Network Data from JSON.
- Interprets every channel fee as electrical resistance.
- Conversts Resistance into Conductance(G).
- Builds the Conductance Matrix.
- Builds the Laplacian Matrix.
- Encodes Kirchoff's Current Law for every node.
- Prepares the system for solving the equation LV=I.

At this stage , routing is no longer a search equation.
It becomes a system of equations.

# Mathematical Interpretation

Every nodes in the Network obeys a Conservative Law.
Total Outgoing Current = Injected Current
This balance is written as:

LV=I

L= Lapcian Matrix , V = Voltage of Node , I = Injected Current

Instead of ecploring paths manually, the network is converted into a linear system.

Routing is no longer guessed.
It is solved.

# Why Lapcian Matrix

The Lapcian Matrix is the heart of the model.

It
- Has Positive Diagonal Entries representing the Total Connection strength of each node.
- Has Negative Off-Diagonal Entries representing interaction between neighbouring nodes.
- Has rows the sum of zero, enforcing conservation of current.
- Encodes the entire routing topology mathematically.

The single Matrix contains the full Physics of the Lightning Network Routing.

# Output

Running Phase 2 constructs:-

- The Conductance Matrix.
- The Lapcian Matrix.
- Current Injection Vector(Sturucture only)

These Matrices define the electrical model of Lightning Network Routing.