import matplotlib.pyplot as plt
import networkx as nx

# --- Romania Map (graph with distances) ---
romania_map = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# --- DFS Implementation ---
def depth_first_search(graph, start, goal):
    stack = [(start, [start], 0)]
    visited = set()

    while stack:
        current_city, path, distance = stack.pop()
        if current_city == goal:
            return path, distance
        if current_city not in visited:
            visited.add(current_city)
            for neighbor, weight in graph.get(current_city, {}).items():
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], distance + weight))
    return None, 0


# --- Run DFS ---
start_city = 'Arad'
goal_city = 'Bucharest'
dfs_path, dfs_distance = depth_first_search(romania_map, start_city, goal_city)

print("DFS Path:", dfs_path)
print("Total Distance:", dfs_distance)


# --- Visualization ---
G = nx.Graph()

# Add edges with distances
for city, neighbors in romania_map.items():
    for nb, dist in neighbors.items():
        G.add_edge(city, nb, weight=dist)

# Layout (spring_layout looks nice for maps)
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 8))

# Draw base graph
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=1000, edgecolors="black")
nx.draw_networkx_edges(G, pos, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Draw edge weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Highlight DFS path
if dfs_path:
    path_edges = list(zip(dfs_path, dfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color="red")
    nx.draw_networkx_nodes(G, pos, nodelist=dfs_path, node_color="orange", node_size=1000, edgecolors="black")

# Title
plt.title(f"DFS Path from {start_city} to {goal_city}\nPath: {' -> '.join(dfs_path)} (Distance: {dfs_distance})",
          fontsize=14, fontweight="bold")
plt.axis("off")
plt.show()
