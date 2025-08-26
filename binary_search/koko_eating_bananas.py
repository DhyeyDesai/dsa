# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/

# Intuition:
# This is a classic binary search on answer problem. We need to find the minimum eating 
# speed k such that Koko can finish all bananas within h hours. The key insight is that 
# if Koko can finish with speed k, she can also finish with any speed > k. This creates 
# a monotonic property perfect for binary search. We search between 1 (minimum possible 
# speed) and max(piles) (maximum needed speed), and for each candidate speed, calculate 
# if it's possible to finish within h hours.

# Time & Space Complexity
# Time complexity: O(n*logm)
# Space complexity: O(1)
# Where n is the length of the input array piles and m is the maximum number of bananas in a pile.

from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search bounds: minimum speed is 1, maximum needed is max(piles)
        l, r = 1, max(piles)
        result = r  # Initialize result to maximum possible (worst case)

        while l <= r:
            # Calculate middle eating speed to test
            m = l + (r - l) // 2  # Avoid potential overflow
            totalTime = 0

            # Calculate total time needed if eating at speed m
            for p in piles:
                # Time for each pile: ceil(pile_size / eating_speed)
                # If pile has 11 bananas and speed is 4, it takes ceil(11/4) = 3 hours
                totalTime += ceil(p / m)
            
            # Check if this eating speed allows finishing within h hours
            if totalTime <= h:
                # This speed works, but try to find a smaller one
                result = m  # Update our best result
                r = m - 1   # Search for smaller speeds in left half
            else:
                # This speed is too slow, need to eat faster
                l = m + 1   # Search for faster speeds in right half
        
        return result

                