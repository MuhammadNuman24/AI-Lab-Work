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
        print("Visiting:", currentNode)

        explored.append(currentNode)
        currentChildren = 0

        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent = currentNode
                if graph[child].state == goalState:
                    print("Explored nodes:", explored)
                    return actionSequence(graph, initialState, goalState)

                currentChildren += 1
                frontier.append(child)

        if currentChildren == 0:
            explored.pop()  # backtracking

    return None


# Run DFS from D → C
solution = DFS('D', 'C')
print("Solution path:", solution)

