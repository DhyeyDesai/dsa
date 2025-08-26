# 79. Word Search
# https://leetcode.com/problems/word-search/description/

"""
Intuition:
This problem is a classic backtracking/DFS problem. The idea is to:
1. Try starting the word search from every cell in the grid
2. For each starting position, use DFS to explore all 4 directions
3. Mark visited cells temporarily to avoid revisiting them in the current path
4. Backtrack by unmarking the cell when returning from recursion
5. Return True as soon as we find a complete word match

The key insight is using a temporary marker ("#") to mark visited cells during 
the current path exploration, then restoring the original character when backtracking.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            # Base case: if we've matched all characters in the word
            if i == len(word):
                return True
            
            # Check boundary conditions and character match
            # Also check if current cell is already visited (marked with "#")
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or board[r][c] == "#"):
                return False
            
            # Mark current cell as visited by temporarily changing it to "#"
            # This prevents us from using the same cell twice in one path
            board[r][c] = "#"

            # Explore all 4 directions: down, up, right, left
            # Move to next character (i+1) in each recursive call
            res = (dfs(r + 1, c, i + 1) or  # down
                   dfs(r - 1, c, i + 1) or  # up
                   dfs(r, c + 1, i + 1) or  # right
                   dfs(r, c - 1, i + 1))    # left
            
            # Backtrack: restore the original character
            # This allows other paths to use this cell
            board[r][c] = word[i]
            
            return res
        
        # Try starting the word search from every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If we find the word starting from position (r, c)
                if dfs(r, c, 0):
                    return True
        
        # Word not found starting from any position
        return False