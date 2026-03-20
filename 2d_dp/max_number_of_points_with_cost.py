# 1937. Maximum Number of Points with Cost
# https://leetcode.com/problems/maximum-number-of-points-with-cost/description/

# ============================================================================
# Solution 1: DFS with Memoization (Top-Down DP)
# ============================================================================
# Intuition:
# - Use recursion to explore all possible paths from top to bottom
# - At each cell, try moving to ALL columns in the next row
# - Apply penalty of abs(col - nextCol) for horizontal movement
# - Cache results to avoid recomputing the same (row, col) state
# 
# Time Complexity: O(m × n²)
#   - m × n unique states (cells)
#   - Each state checks n possible next columns
#   - Total: m × n × n = O(m × n²)
#
# Space Complexity: O(m × n)
#   - Cache stores m × n entries
#   - Recursion stack depth: O(m)
#   - Total: O(m × n)
#
# Note: This solution gets TLE (Time Limit Exceeded) for large inputs
# ============================================================================

class Solution1:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = [0] * len(points[0])    
        cache = {}  # Memoization: (row, col) -> max points from this cell
        
        def dfs(row, col):
            # Base case: reached the last row, return its value
            if row == len(points) - 1:
                return points[row][col]
            
            # Return cached result if already computed
            if (row, col) in cache:
                return cache[(row, col)]
            
            res = 0
            # Try moving to every column in the next row
            for nextCol in range(len(points[0])):
                # Calculate: points from next row - movement penalty + current cell
                val = dfs(row + 1, nextCol) + points[row][col] - abs(col - nextCol)
                res = max(res, val)
            
            # Cache and return the result
            cache[(row, col)] = res
            return res
        
        # Try starting from each column in the first row
        for col in range(len(points[0])):
            result[col] = dfs(0, col)
        
        return max(result)


# ============================================================================
# Solution 2: Left-Right DP Optimization (Bottom-Up DP)
# ============================================================================
# Intuition:
# - Process row by row from top to bottom
# - For each row, instead of checking all n columns for each cell (O(n²)),
#   precompute the best values coming from left and right directions
# - Left[j]: best value reaching column j from left side (cols 0 to j)
# - Right[j]: best value reaching column j from right side (cols j to n-1)
# - For each cell, take max(left[j], right[j]) to get best from ANY column
#
# Time Complexity: O(m × n)
#   - Process m rows
#   - For each row: 3 passes of n columns (left scan, right scan, combine)
#   - Total: m × 3n = O(m × n)
#
# Space Complexity: O(n)
#   - prev, left, right, curr arrays each store n elements
#   - No recursion stack needed
#   - Total: 4n = O(n)
# ============================================================================

class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        # Initialize with first row (base case)
        prev = points[0][:]  # prev[j] = max points achievable at column j of current row

        # Process each row starting from row 1
        for row in range(1, m):
            # LEFT SCAN: Calculate best value coming from left or same column
            left = [0] * n
            left[0] = prev[0]  # First column can only come from itself
            
            for col in range(1, n):
                # Either come from previous column (with penalty -1) or stay at current column
                left[col] = max(left[col - 1] - 1, prev[col])
            
            # RIGHT SCAN: Calculate best value coming from right or same column
            right = [0] * n
            right[n - 1] = prev[n - 1]  # Last column can only come from itself
            
            for col in range(n - 2, -1, -1):
                # Either come from next column (with penalty -1) or stay at current column
                right[col] = max(right[col + 1] - 1, prev[col])

            # COMBINE: For each column, take best from left or right, add current cell value
            curr = [0] * n
            for col in range(n):
                # max(left[col], right[col]) gives us the best value from ANY column in prev row
                curr[col] = points[row][col] + max(left[col], right[col])

            # Move to next row
            prev = curr

        # Return maximum value in the last row
        return max(prev)