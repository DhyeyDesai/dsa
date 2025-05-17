# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/description/

# This problem builds on the "Number of Islands" concept but requires tracking the area
# of each island, not just counting them. We need to find the island with the maximum area.        

# Solution 1 - BFS Approach

# Intuition:
# Here we use Breadth-First Search (BFS) which explores all neighbors at the current depth
# before moving to nodes at the next depth level.
# BFS uses a queue to track cells to visit. We start at a land cell (1), mark it as visited,
# and then explore outward layer by layer, marking connected land cells as visited, while counting the area of the current island.
# Each time we initiate a new BFS, we've found a new island.
# We keep track of the maximum area seen so far.

# Time Complexity: O(m×n) where m is rows and n is columns
# Space Complexity: O(min(m,n)) for the queue in worst case

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        # Edge case check
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        # Four possible directions: right, left, down, up
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]
        maxArea = 0 # Counter for number of cells in an island

        def bfs(r, c):
            # Initialize the area as 1
            area = 1 

            # Initialize queue for BFS
            q = deque()
            
            # Mark starting cell as visited and add to queue
            grid[r][c] = 0 # Mark as visited by changing to water
            q.append((r,c))

            # Process cells in the queue
            while q:
                row, col = q.popleft() # Get the next cell to process

                # Check all four adjacent directions
                for dr, dc in directions:
                    nr = row+dr # new row 
                    nc = col+dc # new column
                    
                    # Skip if out of bounds or water/already visited
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc] == 0:
                        continue
                    
                    # Add adjacent land to queue and mark as visited
                    q.append((nr, nc))
                    area+=1 # Increment the area of current island.
                    grid[nr][nc] = 0 # Mark as visited
            return area
        
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # Found an unvisited land cell
                    area = 1
                    newArea = bfs(r, c) # Start BFS to explore the entire island
                    maxArea = max(newArea, maxArea)
        
        return maxArea


# Solution 2 - DFS Approach
# Intuition:

# We use Depth-First Search (DFS) to explore and "sink" each island (change '1's to '0's) 
# as we find it. Each time we start a new DFS, we've found a new island.
# While  searching inside DFS, we keep incrementing the area as we find new pieces of land.        
# Time Complexity: O(m×n) where m is rows and n is columns
# Space Complexity: O(m×n) in worst case for the recursive call stack

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        # Edge case check
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        # Define the four possible directions to move (right, left, down, up)
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]
        maxArea = 0 # Counter for the number of islands found

        def dfs(r, c):
            # Base cases: out of bounds or water (0)
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 0
            
            # Mark current land as visited by changing it to water (sink the island)
            grid[r][c] = 0
            area=1

            # Recursively explore all adjacent cells in all four directions
            for dr, dc in directions:
                area += dfs(r+dr, c+dc)
            return area

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # Found a new piece of land
                    newArea = dfs(r,c) # Start DFS to explore and mark the entire island
                    maxArea = max(newArea, maxArea) # After DFS completes, we've finished exploring one island
        
        return maxArea

