# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

# PROBLEM INTUITION:
# ==================
# You're at the top-left of an m*n grid and want to reach bottom-right.
# You can only move RIGHT or DOWN.

# Key insight: To reach any cell, you must come from either:
# - The cell above it, OR
# - The cell to the left of it

# So: paths[i][j] = paths[i+1][j] + paths[i][j+1]

# APPROACH:
# =========
# We use Dynamic Programming, building from the bottom-right (destination) 
# backwards to top-left (start).

# Base case: Bottom row and rightmost column all have exactly 1 path
# (you can only go straight right or straight down).

# Why build backwards? It's easier to reason about: "If I'm at position (i,j),
# I can reach the end by going right OR going down."


# SOLUTION 1: Two-Row DP (More Explicit)
# ======================================
# Space: O(n) - we keep TWO rows at a time
# Time: O(m*n) - visit each cell once

# This version is more explicit about maintaining the "current row" 
# and "row below" separately, making the logic clearer.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Start with bottom row - all cells have 1 path (go straight right to end)
        row = [1] * n
        
        # Process each row from bottom to top (excluding the last row we initialized)
        for i in range(m - 1):
            # Create a new row, initialize rightmost column to 1
            # (rightmost column always has 1 path: go straight down)
            newRow = [1] * n
            
            # Fill this row from right to left (excluding rightmost which is already 1)
            for j in range(n - 2, -1, -1):
                # Paths to (i,j) = paths from going right + paths from going down
                # newRow[j+1] = paths if we go RIGHT from here
                # row[j] = paths if we go DOWN from here (from the row below)
                newRow[j] = newRow[j + 1] + row[j]
            
            # Move to next row up (this row becomes the "row below" for next iteration)
            row = newRow
        
        # After processing all rows, row[0] contains paths from top-left
        return row[0]


# SOLUTION 2: Single-Row DP (Space Optimized)
# ===========================================
# Space: O(n) - we only keep ONE row and update it in place
# Time: O(m*n) - visit each cell once

# This is more space-efficient. Instead of creating newRow each time,
# we cleverly update the same array in place.

# The trick: When we update dp[j], we use:
# - dp[j+1]: already updated (represents going RIGHT)
# - dp[j]: not yet updated (still holds value from row below, represents going DOWN)
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize with bottom row - all 1s
        dp = [1] * n
        
        # Process rows from second-to-last up to first row
        for i in range(m - 2, -1, -1):
            # Process columns from right to left (rightmost stays 1, so skip it)
            for j in range(n - 2, -1, -1):
                # Update in place:
                # dp[j+1] was just updated - it's the "go RIGHT" path count
                # dp[j] is still old value from row below - it's the "go DOWN" path count
                dp[j] += dp[j + 1]
                # Now dp[j] = paths from going right + paths from going down
        
        # dp[0] now holds the answer: paths from (0,0) to (m-1, n-1)
        return dp[0]

