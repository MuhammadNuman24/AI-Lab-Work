from collections import deque
import matplotlib.pyplot as plt
import numpy as np

def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    q = deque([(start, [start])])  # (current_cell, path)
    visited = set([start])

    while q:
        (r, c), path = q.popleft()
        if (r, c) == goal:
            return path

        # Possible moves (down, up, right, left)
        #for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        # Prefer Right, Up, Down, Left
        for dr, dc in [(0,1), (-1,0), (1,0), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append(((nr, nc), path + [(nr, nc)]))
    return None

# --- Maze from your input ---
maze = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,0,1],
    [1,0,1,0,1,1,0,1],
    [1,0,1,2,1,0,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,2,1,1]
]

start = (4,3)   # given start
goal  = (7,5)   # given goal

path = bfs_maze(maze, start, goal)
print("Shortest BFS Path:", path)

# --- Visualization ---
maze_np = np.array(maze)

plt.figure(figsize=(6,6))
plt.imshow(maze_np, cmap="Blues")

if path:
    pr, pc = zip(*path)
    plt.plot(pc, pr, color="Orange", linewidth=2, marker="o")

# Mark start & goal
plt.text(start[1], start[0], "Start", color="green", ha="center", va="center", fontsize=12, fontweight="bold")
plt.text(goal[1], goal[0], "Goal", color="blue", ha="center", va="center", fontsize=12, fontweight="bold")

plt.title("BFS Path in Maze")
plt.gca().invert_yaxis()
plt.show()
