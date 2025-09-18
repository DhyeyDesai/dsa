# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

# INTUITION:
# 1. Instead of checking if water can flow FROM each cell TO both oceans (which would be complex),
#    we reverse the problem: start FROM the ocean borders and see which cells water can flow TO
# 2. Water flows from higher to lower heights, so when going backwards from oceans,
#    we can only move to cells with equal or higher heights
# 3. Use DFS from all border cells (Pacific: top/left, Atlantic: bottom/right)
# 4. A cell can reach both oceans if it appears in both sets after our DFS traversals
# 5. This approach is more efficient because we only do 2 DFS traversals instead of checking every cell

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        # Sets to store cells that can reach each ocean
        pacific, atlantic = set(), set()
        
        # Directions for 4-directional movement (down, up, left, right)
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(row, col, visit, prevHeight):
            # Base cases: out of bounds, already visited, or can't flow (current height < previous)
            if (row, col) in visit or row < 0 or row == ROWS or col < 0 or col == COLS or heights[row][col] < prevHeight:
                return
            
            # Mark current cell as reachable from this ocean
            visit.add((row, col))

            # Explore all 4 directions with current cell's height as the new previous height
            for dr, dc in directions:
                dfs(row+dr, col+dc, visit, heights[row][col])

        # DFS from Pacific Ocean borders (top and left edges)
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])  # Top row -> Pacific
            dfs(ROWS - 1, c, atlantic, heights[ROWS-1][c])  # Bottom row -> Atlantic

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])  # Left column -> Pacific
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])  # Right column -> Atlantic

        # Find cells that can reach both oceans (intersection of both sets)
        result = []            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r,c])
        return result