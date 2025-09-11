# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/description/


# Intuition: Use BFS to simulate the rotting process level by level.
# Start with all initially rotten oranges in the queue, then spread rot
# to adjacent fresh oranges simultaneously. Each BFS level represents
# one minute passing. Return time taken if all oranges rot, else -1.


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Initialize queue with all initially rotten oranges and count fresh ones
        q = deque()
        fresh_count = 0

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # Fresh orange
                    fresh_count+=1
                elif grid[r][c] == 2: # Rotten orange
                    q.append((r,c))

        # If no fresh oranges initially, no time needed
        if fresh_count == 0:
            return 0        

        minutes = 0
        
        # BFS: process all oranges that rot at the same time (same minute)
        while q and fresh_count>0:
            # Process all oranges that are rotting in the current minute
            for _ in range(len(q)):
                row, col = q.popleft()

                # Check all 4 adjacent cells
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # Check bounds and if the orange is fresh
                    if (0 <= new_row < rows and 0 <= new_col < cols and 
                        grid[new_row][new_col] == 1):

                        # Rot the fresh orange
                        grid[new_row][new_col] = 2
                        fresh_count-=1
                        q.append((new_row, new_col))
            
            # One minute has passed
            minutes += 1    
        
        # Return minutes if all oranges are rotten, otherwise -1        
        return minutes if fresh_count == 0 else -1
        