import sys
import matplotlib.pyplot as plt

# Increase recursion limit for potentially long DFS paths
sys.setrecursionlimit(2000)

# --- 1. Data Setup ---
BOGGLE_BOARD = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

DICTIONARY = {"START", "NOTE", "SAND", "STONED"}

ROWS = len(BOGGLE_BOARD)
COLS = len(BOGGLE_BOARD[0])

# Precompute prefixes
ALL_PREFIXES = set()
for word in DICTIONARY:
    for i in range(1, len(word) + 1):
        ALL_PREFIXES.add(word[:i])

DIRECTIONS = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, 1), (-1, -1), (1, 1), (1, -1)
]

found_words = set()
word_paths = {}  # store coordinates for visualization


# --- 2. DFS Implementation ---
def dfs(r, c, current_word, visited, board, dictionary, prefixes, path):
    if current_word not in prefixes:
        return

    if current_word in dictionary:
        found_words.add(current_word)
        word_paths[current_word] = path[:]  # save path

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, current_word + board[nr][nc],
                visited, board, dictionary, prefixes, path + [(nr, nc)])
            visited[nr][nc] = False


def solve_boggle(board, dictionary, prefixes):
    for r in range(ROWS):
        for c in range(COLS):
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] = True
            dfs(r, c, board[r][c], visited, board, dictionary, prefixes, [(r, c)])
            visited[r][c] = False
    return found_words


# --- 3. Visualization ---
def visualize_board(board, word_paths):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Draw grid and letters
    for r in range(ROWS):
        for c in range(COLS):
            ax.add_patch(plt.Rectangle((c, ROWS - 1 - r), 1, 1, fill=False))
            ax.text(c + 0.5, ROWS - 1 - r + 0.5, board[r][c],
                    ha='center', va='center', fontsize=16, fontweight='bold')

    # Highlight each word path
    colors = ["red", "blue", "green", "purple", "orange"]
    for i, (word, path) in enumerate(word_paths.items()):
        color = colors[i % len(colors)]
        coords = [(c + 0.5, ROWS - 1 - r + 0.5) for r, c in path]

        xs, ys = zip(*coords)
        ax.plot(xs, ys, marker='o', color=color, linewidth=2, label=word)

    ax.set_xlim(0, COLS)
    ax.set_ylim(0, ROWS)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    ax.legend()
    plt.title("Boggle Board Solution")
    plt.show()


# --- 4. Run Solver ---
if __name__ == "__main__":
    print("--- Lab Task 2: Boggle Board Solver ---")
    print(f"Board Dimensions: {ROWS}x{COLS}")
    print(f"Input Dictionary: {list(DICTIONARY)}")

    valid_words_found = solve_boggle(BOGGLE_BOARD, DICTIONARY, ALL_PREFIXES)
    sorted_words = sorted(list(valid_words_found))

    print("\n--- Result ---")
    print(f"Found Words: {sorted_words}")

    # Visualize
    visualize_board(BOGGLE_BOARD, word_paths)
