# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

# INTUITION:
# We can only move right or down, so we work backwards from bottom-right to top-left.
# At each cell, the minimum path sum = current cell value + min(path from right, path from down).
# By processing bottom-up, we ensure subproblems are solved before we need them.

# APPROACH 1: In-place DP (Modify Input Grid)
# Time: O(m*n) - visit each cell once
# Space: O(1) - modify grid in place, no extra data structures
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Process from bottom-right to top-left
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r == rows - 1 and c == cols - 1:
                    # Base case: bottom-right corner stays as is
                    continue
                elif c == cols - 1:
                    # Right edge: can only come from below
                    grid[r][c] += grid[r+1][c]
                elif r == rows - 1:
                    # Bottom edge: can only come from right
                    grid[r][c] += grid[r][c+1]
                else:
                    # Interior cell: take minimum of right or down
                    grid[r][c] += min(grid[r+1][c], grid[r][c+1])
        
        # Top-left now contains the minimum path sum
        return grid[0][0]


# APPROACH 2: 1D DP with tracking variable (Preserve Input)
# Time: O(m*n) - visit each cell once
# Space: O(n) - single row DP array
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # dp[c] represents min path sum from grid[r][c] to bottom-right
        # Initialize with inf, except dp[-1] = 0 (starting point for bottom-right)
        dp = [float("inf")] * cols
        dp[-1] = 0 
        
        nxt = 0  # Tracks dp[c] from previous iteration (becomes dp[c+1] for current)
        
        # Process from bottom-right to top-left
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if c == cols - 1:
                    # Right edge: can only add value from below (stored in dp[c])
                    dp[c] = dp[c] + grid[r][c]
                else:
                    # Interior/left cells: min of right (nxt) or down (dp[c])
                    dp[c] = grid[r][c] + min(nxt, dp[c])
                
                # Store current dp[c] as nxt for next iteration (it becomes dp[c+1])
                nxt = dp[c]
        
        # dp[0] contains min path from top-left to bottom-right
        return dp[0]