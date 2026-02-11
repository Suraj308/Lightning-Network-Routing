# Phase 1 : Build a Synthetic Netwok


import random
import json
import networkx as nx
import matplotlib.pyplot as plt

# Values

num_nodes = 10
num_channels=21
min_fee = 1
max_fee = 10
min_capacity = 6
max_capacity = 27

random.seed(42)

# Create Graph

nodes= list(range(num_nodes))

G= nx.Graph()
G.add_nodes_from(nodes)

channels = set()

def add_channel(a,b):
    if a==b:
        return False
    edge = tuple(sorted((a,b)))
    if edge in channels:
        return False
    fee = random.randint(min_fee,max_fee)
    capacity = random.randint(min_capacity,max_capacity)

    G.add_edge(a,b,fee=fee,capacity=capacity)
    channels.add(edge)
    return True


# Create HUBS
    
hubs = random.sample(nodes,2)
for hub in hubs:
    others = [n for n in nodes if n!=hub]
    random.shuffle(others)
    for target in others[:4]:
        add_channel(hub,target)

# Add Channels
while len(channels)<num_channels:
    a=random.choice(nodes)
    b=random.choice(nodes)
    add_channel(a,b)

# Minimum Degree>=2

for node in nodes:
    while G.degree[node]<2:
        target = random.choice([n for n in nodes if n!=node])
        add_channel(node,target)

# Print Network Data
print("\n--Nodes--")
print(nodes)

print("\n--Channels--")
for (u,v,data) in G.edges(data=True):
    print(f"{u}--{v} | Fee ={data['fee']} | Capacity={data['capacity']}")

#Visualise the Synthetic Network
pos = nx.spring_layout(G,seed=42)

edge_width = [G[u][v]['capacity']*0.1 for u,v in G.edges()]
edge_colour = [G[u][v]['fee'] for u,v in G.edges()]

plt.figure(figsize=(8,6))
nx.draw(
    G,pos,with_labels=True,node_size=600,node_color='lightblue',
    edge_color=edge_colour,width=edge_width,edge_cmap=plt.cm.viridis
)

sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis)
sm.set_array(edge_colour)
plt.colorbar(sm, ax=plt.gca(),label="Fee (Phase 1)")

plt.title("Phase 1: Synthetic Lightning Network Data")
plt.savefig("Result/Phase1_Lightning_network_Data_Visualisation",dpi=300)
plt.show()

network_data =[]

for (u,v,data) in G.edges(data=True):
    network_data.append({
        'from':u,'to':v, "fee": data["fee"],"capacity":data['capacity']
    })

with open("Synthetic_lightning_network_data.json","w") as f:
    json.dump(network_data,f,indent=4)

print("\nNetwork saved to Json")

