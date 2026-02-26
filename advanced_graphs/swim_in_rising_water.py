# 778. Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/

# INTUITION:
# This is a modified Dijkstra's algorithm problem. Instead of finding the shortest path,
# we're finding the path where the MAXIMUM elevation encountered is minimized.

# Think of it as: "What's the minimum water level needed to swim from top-left to bottom-right?"

# We use a minHeap to always explore the path with the lowest "max elevation so far" first.
# When we reach the destination, we're guaranteed to have found the optimal path because:
# 1. MinHeap ensures we process cells in order of increasing time/elevation
# 2. First time we pop the destination = minimum possible max-elevation path
# 3. Any other path would have a higher or equal max-elevation (still in heap)

# TIME COMPLEXITY: O(N² log N²) = O(N² log N)
# - We process each cell once: O(N²)
# - Each heap operation (push/pop) takes O(log N²) = O(log N)
# - Total: O(N² log N)

# SPACE COMPLEXITY: O(N²)
# - Heap can contain up to O(N²) cells in worst case
# - Visited set stores up to O(N²) coordinates

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()

        # MinHeap: (max_elevation_so_far, row, col)
        # Start at top-left corner with its elevation as initial time
        minH = [[grid[0][0], 0, 0]]
        visit.add((0, 0))  # Mark starting position as visited

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # Right, Down, Left, Up

        while minH:
            # Pop cell with minimum max-elevation encountered so far
            t, r, c = heapq.heappop(minH)

            # If we've reached bottom-right, return the time
            # This is guaranteed to be optimal due to minHeap property
            if r == N - 1 and c == N - 1:
                return t
            
            # Explore all 4 neighboring cells
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                
                # Skip if out of bounds or already visited
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or 
                    (neiR, neiC) in visit):
                    continue

                # Mark neighbor as visited before adding to heap
                # This prevents processing the same cell multiple times
                visit.add((neiR, neiC))
                
                # The time to reach neighbor is the MAX of:
                # - Current time (max elevation on path so far)
                # - Neighbor's elevation (might be higher, forcing us to wait)
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
        

