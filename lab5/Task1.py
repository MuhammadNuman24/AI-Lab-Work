# Graph representation: {City: {Neighbor: Distance, ...}, ...}
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

start_city = 'Arad'
goal_city = 'Bucharest'

def depth_first_search(graph, start, goal):
    """
    Implements a standard Depth First Search to find a path.
    This finds the first path it explores, not necessarily the shortest.
    """
    # Stack stores (current_city, current_path, current_distance)
    stack = [(start, [start], 0)]
    visited = set()

    print(f"Starting DFS from {start} to {goal}...")

    while stack:
        # LIFO (Last-In, First-Out) behavior for DFS
        current_city, path, distance = stack.pop()

        if current_city == goal:
            return path, distance
        
        if current_city not in visited:
            visited.add(current_city)
            
            # Explore neighbors
            # The order in which neighbors are added to the stack determines 
            # the specific path found first. Here we iterate based on the map's definition.
            for neighbor, weight in graph.get(current_city, {}).items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_distance = distance + weight
                    stack.append((neighbor, new_path, new_distance))

    return "Path not found", 0

# --- Execution ---
dfs_path, dfs_distance = depth_first_search(romania_map, start_city, goal_city)

print("\n--- DFS Result ---")
print(f"Path Found: {dfs_path}")
print(f"Total Distance: {dfs_distance}")