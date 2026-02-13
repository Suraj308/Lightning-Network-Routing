import numpy as np
import json

from phase2_circuit_model import (
    build_conductance_matrix,build_current_vector,build_lapicain_matrix
)
# Phase 3
# Solve LV=I 

with open("Synthetic_lightning_network_data.json") as f:
    edges = json.load(f)

nodes = set()
for edge in edges:
    nodes.add(edge["from"])
    nodes.add(edge["to"])

num_nodes = len(nodes)

# Build Matrix

G_matrix = build_conductance_matrix(edges,num_nodes)
L=build_lapicain_matrix(G_matrix)

# Define Payment

source = 0
destination = num_nodes-1
amount=1.0

I = build_current_vector(num_nodes,source,destination,amount)


# Ground One Node
#Handle Singularity

#Remove last row and column (it removes one variable)

L_reduced = L[:-1,:-1]
I_reduced = I[:-1]

V_reduced = np.linalg.solve(L_reduced,I_reduced)

V = np.append(V_reduced,0.0)

print(V)

# Commpute edge current

total_out=0.0

for edge in edges:
    i=edge["from"]
    j=edge["to"]
    R=edge["fee"]
    G=1.0/R

    current = G*(V[i]-V[j])

    print(f"{i}--{j} : {current: .6f}")

    if i == source :
        total_out+=current
print(total_out)


