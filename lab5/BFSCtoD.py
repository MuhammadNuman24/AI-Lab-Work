from collections import deque

# --------- Graph (Activity 1 wala hi) ---------
graph = {
    'A': ['B', 'E', 'C'],
    'B': ['D', 'E', 'A'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}


# --------- BFS Implementation ---------
def bfs(initial, goal):
    queue = deque([initial])   # FIFO
    explored = []              # sequence of explored nodes
    parent = {initial: None}   # track path
    
    while queue:
        current = queue.popleft()
        explored.append(current)

        if current == goal:
            # build path from parent map
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], explored

        for child in graph[current]:
            if child not in parent:  # not visited yet
                parent[child] = current
                queue.append(child)

    return None, explored


# --------- Run BFS (D -> C) ---------
path, explored = bfs('D', 'C')
print("Final Path:", path)
print("Explored Sequence:", explored)
