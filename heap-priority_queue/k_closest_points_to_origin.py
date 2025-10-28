# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/

# INTUITION:
# We need the k closest points, not ALL points sorted by distance.
# Strategy: Maintain a max heap of size k containing the k closest points seen so far.
# - As we scan through points, we keep the k smallest distances in our heap
# - The heap root is the FARTHEST of our k closest points (max heap property)
# - If we find a closer point, we evict the farthest and add the new one
# - After processing all points, our heap contains exactly the k closest

# Why max heap? So we can quickly identify and remove the farthest point among our k candidates.
# Time: O(n log k) - we do n insertions/replacements, each taking log k time
# Space: O(k) - only store k points instead of all n points

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max heap to store k closest points
        # Python's heapq is a min heap, so negate distances to simulate max heap
        max_heap = []
        
        for x,y in points:
            # Calculate squared distance (no need for sqrt since we're just comparing)
            dist = -(x**2 + y**2) # Negative because we want a max heap
            if len(max_heap) < k:
                # Haven't found k points yet, just add this one
                heapq.heappush(max_heap, (dist, x, y))
            elif dist > max_heap[0][0]:
                # Current point is closer than the farthest point in our heap
                # Replace the farthest with this closer point
                heapq.heapreplace(max_heap, (dist, x, y))
                # heapreplace = pop + push in one operation (more efficient)
        
        # Extract just the coordinates (x, y) from our heap, discard distances
        return [(x,y) for _,x,y in max_heap]
            
