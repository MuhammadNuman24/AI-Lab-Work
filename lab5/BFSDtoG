import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

graph = {
    'A': ['B', 'E', 'C'],
    'B': ['D', 'E', 'A'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C'],
}

def bfs(graph, start, goal):
    queue = deque([start])
    explored = []
    parent = {start: None}

    while queue:
        node = queue.popleft()
        explored.append(node)

        if node == goal:
            # backtrack path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, explored

        for neighbor in graph[node]:
            if neighbor not in parent:  # not visited
                parent[neighbor] = node
                queue.append(neighbor)

    return None, explored


# --------- Run BFS (D -> G) ---------
path, explored = bfs(graph, 'D', 'G')
print("BFS Path:", path)
print("Explored Sequence:", explored)

# --------- Visualization ---------
G = nx.Graph()
for node, neighbors in graph.items():
    for nb in neighbors:
        G.add_edge(node, nb)

pos = nx.spring_layout(G, seed=42)  # layout
plt.figure(figsize=(6, 6))

# draw all nodes/edges
nx.draw(G, pos, with_labels=True, node_size=1200,
        node_color="lightblue", font_size=12, edge_color="gray")

# highlight explored nodes (lightgreen)
nx.draw_networkx_nodes(G, pos, nodelist=explored,
                       node_color="lightgreen", node_size=1200)

# highlight final path (red edges + orange nodes)
if path:
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color="red")
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange", node_size=1200)

plt.title(f"BFS from D to G\nPath: {' -> '.join(path)}", fontsize=14)
plt.show()
