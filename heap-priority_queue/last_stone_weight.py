# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/description/

# INTUITION:
# - We need to repeatedly pick the two HEAVIEST stones and smash them together
# - A max heap is perfect for this since it gives us the largest elements efficiently
# - Python only has min heap (heapq), so we use a trick: negate all values to simulate max heap
# - Keep smashing until 0 or 1 stone remains

# TIME: O(n log n) - heapify is O(n), then we do O(n) operations of O(log n) each
# SPACE: O(1) - we modify the input array in place (or O(n) if we count the heap)

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative values to simulate max heap
        # (Python's heapq is a min heap, so -8 becomes "smaller" than -5)
        heap = [-s for s in stones]
        heapq.heapify(stones) # Convert list to heap structure in O(n)
        
        # Keep smashing stones until 0 or 1 stone remains
        while len(heap)>1:
            # Pop two heaviest stones (most negative values = largest actual values)
            # eg., -8 and -5
            diff = heapq.heappop(stones)-heapq.heappop(stones) # heaviest - second_heaviest
            
            # If stones have different weights, the difference remains
            # Since both are negative: (-8) - (-5) = -8 + 5 = -3
            if diff:
                heapq.heappush(stones, diff)
            # If equal, both are destroyed (do nothing)

        # Return the last remaining stone's weight after turning back to positive,
        # or 0 if all destroyed
        return -heap[0] if heap else 0

