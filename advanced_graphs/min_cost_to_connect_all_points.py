# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/


# Solution 1: Prim's Algorithm Optimal
# TODO: understand this better
# Instead of building the entire adjacency list upfront (O(n^2) space),
# we can calculate distances on-the-fly. This is Prim's algorithm optimized:
# 1. Start from any point and track the minimum cost to connect each unvisited point
# 2. Greedily select the unvisited point with minimum connection cost
# 3. Update costs for remaining unvisited points from the newly added point
# 4. Repeat until all points are connected
#
# KEY OPTIMIZATION: We don't need to store all edges explicitly. Instead, we
# maintain an array tracking the minimum cost to connect each unvisited point.
#
# TIME COMPLEXITY: O(n^2)
# - We iterate through n points (outer loop)
# - For each point, we scan all n points to find minimum and update costs
# - Total: O(n * n) = O(n^2)
#
# SPACE COMPLEXITY: O(n)
# - minCost array: O(n)
# - visited array: O(n)
# - No adjacency list needed!

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # minCost[i] = minimum cost to connect point i to the growing MST
        # Initialize all to infinity except we'll start from point 0
        minCost = [float('inf')] * n
        minCost[0] = 0  # Start from point 0 with cost 0
        
        # Track which points are already in the MST
        visited = [False] * n
        
        totalCost = 0
        
        # We need to add n points to the MST
        for _ in range(n):
            # Find the unvisited point with minimum connection cost
            currPoint = -1
            currMinCost = float('inf')
            
            for i in range(n):
                if not visited[i] and minCost[i] < currMinCost:
                    currMinCost = minCost[i]
                    currPoint = i
            
            # Add this point to MST
            visited[currPoint] = True
            totalCost += currMinCost
            
            # Update minimum costs for all unvisited points
            # Check if connecting through currPoint gives a better cost
            x1, y1 = points[currPoint]
            for j in range(n):
                if not visited[j]:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    # Update if this path is cheaper than previous best
                    minCost[j] = min(minCost[j], dist)
        
        return totalCost


# Solution 2: Prim's Algorithm
# INTUITION:
# This is a Minimum Spanning Tree (MST) problem. We need to connect all points
# with minimum total cost where cost is the Manhattan distance between points.
# We use Prim's algorithm with a min-heap:
# 1. Build a graph where each point connects to all other points with their distances
# 2. Start from any point (point 0) and greedily add the minimum cost edge
# 3. Keep track of visited points to avoid cycles
# 4. Continue until all points are connected
#
# TIME COMPLEXITY: O(n^2 * log(n))
# - Building adjacency list: O(n^2) to calculate distances between all pairs
# - Prim's algorithm: O(n^2 * log(n)) where we potentially push n^2 edges to heap
#   and each heap operation takes O(log(n^2)) = O(2*log(n)) = O(log(n))
#
# SPACE COMPLEXITY: O(n^2)
# - Adjacency list stores all edges: O(n^2)
# - Min heap can grow up to O(n^2) in worst case
# - Visit set: O(n)

import heapq
class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Build adjacency list: map each point index to list of (distance, neighbor_index)
        adj = {i:[] for i in range(n)}       

        # Calculate Manhattan distance between every pair of points
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)  # Manhattan distance formula

                # Add bidirectional edges since graph is undirected
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        # Initialize result to accumulate total cost
        res = 0
        
        # Track visited points to avoid cycles
        visit = set()
        
        # Min heap to always get the minimum cost edge
        # Start with point 0 at cost 0
        minHeap = [[0, 0]]  # [cost, point_index]

        # Continue until all points are visited (MST is complete)
        while len(visit) < n:
            # Pop the edge with minimum cost
            cost, i = heapq.heappop(minHeap)
            
            # Skip if this point is already in MST (lazy deletion)
            if i in visit:
                continue
            
            # Add this edge's cost to total result
            res += cost
            
            # Mark current point as visited
            visit.add(i)
            
            # Add all edges from current point to unvisited neighbors
            for neiDist, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiDist, nei])

        return res