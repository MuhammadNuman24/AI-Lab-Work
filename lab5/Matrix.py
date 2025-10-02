import sys
# Increase recursion limit for potentially long DFS paths, though 4x4 is small.
sys.setrecursionlimit(2000)

# --- 1. Data Setup ---

# The 4x4 Boggle Board from Figure 15
BOGGLE_BOARD = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

# The input dictionary of valid words (using a set for fast lookup)
DICTIONARY = {"START", "NOTE", "SAND", "STONED"}

# Dimensions of the board
ROWS = len(BOGGLE_BOARD)
COLS = len(BOGGLE_BOARD[0])

# Pre-calculate a set of all possible prefixes for efficient pruning during DFS.
# If a generated word is not a prefix of any dictionary word, we stop exploring that path.
ALL_PREFIXES = set()
for word in DICTIONARY:
    for i in range(1, len(word) + 1):
        ALL_PREFIXES.add(word[:i])

# 8 possible directions (row_change, col_change) including diagonals
DIRECTIONS = [
    (-1, 0), (1, 0), (0, -1), (0, 1),   # North, South, West, East
    (-1, 1), (-1, -1), (1, 1), (1, -1)  # NE, NW, SE, SW
]

# Set to store the unique valid words found during the search
found_words = set()


# --- 2. DFS/Backtracking Implementation ---

def dfs(r: int, c: int, current_word: str, visited: list[list[bool]], board: list[list[str]], dictionary: set[str], prefixes: set[str]):
    """
    Recursive helper function for Depth First Search (backtracking).

    It explores adjacent cells to form words, ensuring each cell is used only once
    per word, and prunes branches using the prefix set.

    Args:
        r (int): Current row index.
        c (int): Current column index.
        current_word (str): The word formed so far in the path.
        visited (list[list[bool]]): Tracks cells used in the current path.
        board (list[list[str]]): The Boggle board.
        dictionary (set[str]): Set of valid complete words.
        prefixes (set[str]): Set of all valid prefixes.
    """
    
    # Pruning Optimization: If the current word is not a prefix of ANY dictionary word, stop exploring.
    if current_word not in prefixes:
        return

    # Check for a complete valid word
    if current_word in dictionary:
        # Add the word to the result set. We continue searching in case a longer word 
        # (e.g., 'NOTE' followed by 'NOTED') is possible.
        found_words.add(current_word)

    # Explore Neighbors in all 8 Directions
    for dr, dc in DIRECTIONS:
        new_r, new_c = r + dr, c + dc
        
        # Check bounds and if the cell has not been visited in this path
        if 0 <= new_r < ROWS and 0 <= new_c < COLS and not visited[new_r][new_c]:
            
            # 1. Action: Mark the cell as visited for this path
            visited[new_r][new_c] = True
            
            # 2. Recurse: Call DFS with the new state (new position, longer word)
            next_char = board[new_r][new_c]
            dfs(
                new_r, 
                new_c, 
                current_word + next_char, 
                visited, 
                board, 
                dictionary, 
                prefixes
            )
            
            # 3. Backtrack: Unmark the cell when returning from the recursion 
            # (allowing it to be used for future, different word paths)
            visited[new_r][new_c] = False


def solve_boggle(board: list[list[str]], dictionary: set[str], prefixes: set[str]) -> set[str]:
    """
    Main function to initiate the Boggle search from every cell.
    """
    
    # Start DFS from every single cell on the board
    for r in range(ROWS):
        for c in range(COLS):
            # 1. Initialize a fresh visited matrix for each starting position
            visited = [[False] * COLS for _ in range(ROWS)]
            
            # 2. Set up the first step
            start_char = board[r][c]
            visited[r][c] = True
            
            # 3. Begin the search
            # We pass the global 'found_words' implicitly via the function scope
            dfs(r, c, start_char, visited, board, dictionary, prefixes)
            
            # 4. Cleanup (unmark the start cell, though the fresh visited matrix 
            # handles it, it's good practice)
            visited[r][c] = False 
            
    return found_words


# --- 3. Execution and Output ---

if __name__ == "__main__":
    print("--- Lab Task 2: Boggle Board Solver ---")
    print(f"Board Dimensions: {ROWS}x{COLS}")
    print(f"Input Dictionary: {list(DICTIONARY)}")
    
    # Run the solver
    valid_words_found = solve_boggle(BOGGLE_BOARD, DICTIONARY, ALL_PREFIXES)
    
    # Sort for consistent output display
    sorted_words = sorted(list(valid_words_found))

    print("\n--- Result ---")
    print(f"Found Words: {sorted_words}")
    
    # Expected output matches the problem description: ['NOTE', 'SAND', 'STONED']
    # 'START' is not on the board.