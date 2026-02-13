# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# INTUITION:
# We need to find the longest strictly increasing path in a matrix where we can move
# in 4 directions (up, down, left, right). The key insight is that this is a graph
# problem where each cell can be a starting point, and we explore all possible paths
# from that cell.

# We use DFS with memoization (top-down DP) because:
# 1. A cell's longest path only depends on its neighbors with greater values
# 2. Subproblems overlap - the same cell may be visited from multiple starting points
# 3. Memoization prevents recalculating the longest path from a cell we've already processed

# The "strictly increasing" constraint naturally prevents cycles, making DFS safe.

# TIME COMPLEXITY: O(ROWS * COLS)
# - We visit each cell once in the outer loops: O(ROWS * COLS)
# - Each cell's DFS is computed once and cached: O(ROWS * COLS)
# - Total: O(ROWS * COLS)

# SPACE COMPLEXITY: O(ROWS * COLS)
# - dp dictionary stores results for all cells: O(ROWS * COLS)
# - Recursion stack in worst case (snake pattern): O(ROWS * COLS)
# - Total: O(ROWS * COLS)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp={} # Memoization cache: (r, c) -> longest path from this cell

        def dfs(r, c, prevVal):
            # Returns the longest increasing path starting from cell (r, c).
            # prevVal: the value of the cell we came from (to enforce increasing constraint)

            # Base case: out of bounds or not strictly increasing
            if (r < 0 or r == ROWS or c<0 or c==COLS or matrix[r][c] <= prevVal):
                return 0
            currentVal = matrix[r][c]
            
            # If we've already computed the longest path from this cell, return cached result
            if (r, c) in dp:
                return dp[(r,c)]
            
            # Explore all 4 directions, only moving to cells with strictly greater values
            up = dfs(r-1, c, currentVal)
            down = dfs(r, c+1, currentVal)
            right = dfs(r+1, c, currentVal)
            left = dfs(r, c-1, currentVal)
            
            # The longest path from current cell is 1 (current cell) + max of all directions
            dp[(r,c)] = 1 + max(up, down, right, left)
            return dp[(r, c)]
        
        # Try every cell as a potential starting point
        maxPath = 0
        for r in range(ROWS):
            for c in range(COLS):
                # Start DFS with prevVal = -1 (smaller than any matrix value)
                # This allows the first cell to always be included
                res = dfs(r, c, -1)
                maxPath = max(maxPath, res)
        
        return maxPath

