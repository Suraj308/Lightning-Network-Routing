import json
import numpy as np
# Check JSON 

with open("Synthetic_lightning_network_data.json","r") as f:
    edges = json.load(f)
#print("Loaded Edges:")
#for edge in edges:
#    print(edge)

#Node Count

nodes=set()
for edge in edges:
    nodes.add(edge["from"])
    nodes.add(edge["to"])
num_nodes=len(nodes)

#print("Number of nodes-",num_nodes)

# Create Resitance( Covert fees to Resistance)

for edge in edges:
    edge["Resistance"]=edge["fee"]

# Initialise Condductance Matrix
G_matrix=np.zeros((num_nodes,num_nodes))
for edge in edges:
    i=edge["from"]
    j=edge["to"]
    R = edge["Resistance"]
    G=1.0/R

    G_matrix[i][j]+=G
    G_matrix[j][i]+=G

print("Conductance Matrix-")
print(G_matrix)

# Lets create Lapacian Matrix

L = np.zeros((num_nodes,num_nodes))
for i in range(num_nodes):
    for j in range(num_nodes):
        if i==j:
            L[i][i]=np.sum(G_matrix[i])
        else:
            L[i][j]=-G_matrix[i][j]

print("Lapcian Matrix-")
print(L)