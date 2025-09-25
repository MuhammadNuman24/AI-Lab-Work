from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs(graph, start, target):
    """
    Performs BFS to find the shortest path from start to target.
    
    Args:
        graph (dict): Adjacency list representation of the graph.
        start (str): Starting node.
        target (str): Target node.
    
    Returns:
        list: Shortest path from start to target if found, else None.
    """
    visited = set()
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == target:
            return path
        
        if node not in visited:
            visited.add(node)
            neighbors = graph.get(node, [])
            for neighbor, _ in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None

def visualize_graph(graph, path=None):
    """
    Visualizes the graph using NetworkX and matplotlib.
    Highlights the given path if provided.
    
    Args:
        graph (dict): The graph as adjacency list with weights.
        path (list): List of nodes representing the path to highlight.
    """
    G = nx.Graph()
    
    # Add edges with weights
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    
    # Position nodes with spring layout (force-directed)
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(12, 8))
    
    # Draw nodes and labels
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
    # Draw all edges in gray
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray')
    
    # Draw edge weights in red
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    # Highlight the path if provided
    if path:
        # Edges on the path
        path_edges = list(zip(path, path[1:]))
        
        # Highlight nodes in orange
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange', node_size=900)
        
        # Highlight path edges in green and wider lines
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3)
    
    plt.title("Romania Map Graph - BFS Path Highlighted")
    plt.axis('off')
    plt.show()

def main():
    # Define the graph with weighted edges
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
        'Urziceni': [('Bucharest', 85), ('Hirsova', 98)],
        'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
        'Eforie': [('Hirsova', 86)],
        'Neamt': [('Iasi', 87)],
        'Iasi': [('Neamt', 87), ('Vaslui', 92)],
        'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    }
    
    start = 'Arad'
    target = 'Bucharest'
    
    path = bfs(graph, start, target)
    
    if path:
        print(f"Shortest path from {start} to {target}: {' → '.join(path)}")
    else:
        print(f"No path found from {start} to {target}")
    
    visualize_graph(graph, path)

if __name__ == "__main__":
    main()