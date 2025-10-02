import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

# Graph representation
graph = {
    'A': Node('A', None, ['B', 'E', 'C'], None),
    'B': Node('B', None, ['D', 'E', 'A'], None),
    'C': Node('C', None, ['A', 'F', 'G'], None),
    'D': Node('D', None, ['B', 'E'], None),
    'E': Node('E', None, ['A', 'B', 'D'], None),
    'F': Node('F', None, ['C'], None),
    'G': Node('G', None, ['C'], None)
}

def actionSequence(graph, initialState, goalState):
    """ Returns path from initialState to goalState by following parents """
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

def DFS(initialState, goalState):
    frontier = [initialState]
    explored = []

    while frontier:
        currentNode = frontier.pop()
        explored.append(currentNode)
        currentChildren = 0

        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if graph[child].state == goalState:
                    return actionSequence(graph, initialState, goalState)
                currentChildren += 1
                frontier.append(child)
        if currentChildren == 0:
            explored.pop()  # backtracking
    return None

# Run DFS from D → C
solution_path = DFS('D', 'C')

# Build graph for visualization
G = nx.Graph()
for node, node_obj in graph.items():
    for neighbor in node_obj.actions:
        G.add_edge(node, neighbor)

pos = nx.spring_layout(G, seed=42)  # Layout for consistent plotting

plt.figure(figsize=(8, 6))

# Draw all nodes and edges
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1000)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Highlight solution path
if solution_path:
    path_edges = list(zip(solution_path, solution_path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=solution_path, node_color='lightgreen', node_size=1000)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

plt.title(f"DFS Path from D to C: {' → '.join(solution_path)}", fontsize=14)
plt.axis('off')
plt.show()
