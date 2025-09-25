from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, target):
    """
    Dijkstra's algorithm to find the shortest path by cost.
    
    Args:
        graph (dict): Adjacency list with (neighbor, weight).
        start (str): Starting node.
        target (str): Target node.
    
    Returns:
        tuple: (path as list, total cost)
    """
    # Priority queue: (cost, path)
    queue = [(0, [start])]
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == target:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (cost + weight, new_path))

    return None, float("inf")

def visualize_graph(graph, path=None, total_cost=None):
    """
    Visualizes the graph using NetworkX and matplotlib.
    Highlights the given path if provided.
    
    Args:
        graph (dict): The graph as adjacency list with weights.
        path (list): Path to highlight.
        total_cost (int): Total cost of the path.
    """
    G = nx.Graph()
    
    # Add edges with weights
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))
    
    # Draw base graph
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    
    # Edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    # Highlight path if available
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange', node_size=900)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3)
    
    title = "Romania Map Graph - Shortest Path (by Cost)"
    if total_cost is not None:
        title += f"\nTotal Cost = {total_cost}"
    
    plt.title(title)
    plt.axis('off')
    plt.show()

def main():
    # Romania map graph with weights
    graph = {
        'Oradea': [('Zerind', 71), ('Sibiu', 151)],
        'Zerind': [('Oradea', 71), ('Arad', 75)],
        'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
        'Timisoara': [('Arad', 118), ('Lugoj', 111)],
        'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
        'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
        'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
        'Sibiu': [('Oradea', 151), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
        'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
        'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
        'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
        'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
        'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
        'Giurgiu': [('Bucharest', 90)],
        'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
        'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
        'Eforie': [('Hirsova', 86)],
        'Neamt': [('Iasi', 87)],
        'Iasi': [('Neamt', 87), ('Vaslui', 92)],
        'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    }
    
    start = 'Arad'
    target = 'Bucharest'
    
    path, total_cost = dijkstra(graph, start, target)
    
    if path:
        print(f"Shortest path from {start} to {target}: {' → '.join(path)}")
        print(f"Total cost: {total_cost}")
    else:
        print(f"No path found from {start} to {target}")
    
    visualize_graph(graph, path, total_cost)

if __name__ == "__main__":
    main()
