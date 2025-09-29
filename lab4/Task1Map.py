import networkx as nx
import matplotlib.pyplot as plt

# Province adjacency data
adjacent_provinces = {
    "Punjab": ["Sindh", "Khyber Pakhtunkhwa", "Islamabad", "Azad Kashmir"],
    "Sindh": ["Punjab", "Balochistan"],
    "Khyber Pakhtunkhwa": ["Punjab", "Islamabad", "Gilgit-Baltistan", "Afghanistan"],
    "Balochistan": ["Sindh", "Punjab", "Iran", "Afghanistan"],
    "Islamabad": ["Punjab", "Khyber Pakhtunkhwa"],
    "Gilgit-Baltistan": ["Khyber Pakhtunkhwa", "Azad Kashmir"],
    "Azad Kashmir": ["Punjab", "Khyber Pakhtunkhwa", "Gilgit-Baltistan", "India"]
}

# Coastal provinces
coastal_provinces = ["Sindh", "Balochistan"]

# Create a graph
G = nx.Graph()

# Add edges (adjacency relationships)
for province, neighbors in adjacent_provinces.items():
    for neighbor in neighbors:
        G.add_edge(province, neighbor)

# Define node colors: coastal provinces = blue, others = green
node_colors = []
for node in G.nodes():
    if node in coastal_provinces:
        node_colors.append("skyblue")
    else:
        node_colors.append("lightgreen")

# Plot the graph
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)  # layout for positioning

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1500, edgecolors="black")
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

plt.title("Map of Pakistan's Provinces (Adjacency + Coastal Highlight)", fontsize=14)
plt.axis("off")
plt.show()
