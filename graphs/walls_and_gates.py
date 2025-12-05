# NOTE: This is a premium problem. We will use a similar problem from neetcode.io

# 286. Walls And Gates
# https://leetcode.com/problems/walls-and-gates/description/

# NeetCode - Islands and Treasure
# https://neetcode.io/problems/islands-and-treasure/question?list=neetcode150

# INTUITION:
# Use multi-source BFS starting from all treasure chests (0s) simultaneously.
# Each level of BFS represents cells at distance 1, 2, 3, etc. from nearest treasure.
# This ensures each land cell gets the shortest distance to ANY treasure chest.
# Time: O(m*n), Space: O(m*n) for queue and visited set

from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        # Step 1: Find all treasure chests (0s) and add them to queue as starting points
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        # Step 2: Perform level-order BFS from all treasures simultaneously
        dist = 0
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        while q:
            # Process all cells at current distance level
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist  # Update cell with distance to nearest treasure
                
                # Explore all 4 neighboring cells
                for dr, dc in DIRECTIONS:
                    nr = r+dr
                    nc = c+dc
                    # Add neighbor if: in bounds, not visited, and not a wall (-1)
                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and ((nr, nc) not in visit) and (grid[nr][nc] != -1):
                        q.append((nr, nc))
                        visit.add((nr, nc))
            
            # Move to next distance level
            dist+=1