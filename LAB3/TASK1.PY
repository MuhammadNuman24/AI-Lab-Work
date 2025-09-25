from collections import deque

def bfs(graph, start, target):
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

def main():
    # Define the graph as an adjacency list
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
        print(f"Path from {start} to {target}: {path}")
    else:
        print(f"No path found from {start} to {target}")

if __name__ == "__main__":
    main()