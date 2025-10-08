# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/

# INTUITION:
# 1. Sort intervals by start time to process them in order
# 2. Once sorted, overlapping intervals will be adjacent
# 3. Compare each interval with the last merged interval
# 4. If they overlap, extend the merged interval; otherwise, add as new interval

# KEY INSIGHT:
# - After sorting, we only need to check if current interval overlaps with the LAST merged one
# - Two intervals [a,b] and [c,d] overlap if c <= b (current start <= previous end)
# - When merging, take max of both ends to handle cases where one interval contains another

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time (first element)
        # This ensures overlapping intervals are adjacent
        intervals.sort(key=lambda x: x[0])
        
        # Initialize result with first interval
        result = [intervals[0]]
        
        # Process remaining intervals
        for i in range(1, len(intervals)):
            currentStart, currentEnd = intervals[i]
            prevStart, prevEnd = result[-1]  # Last interval in result

            # Check if current interval overlaps with previous merged interval
            if currentStart <= prevEnd:
                # Overlapping: merge by extending the end to maximum of both ends
                # Use max() to handle cases like [1,5] and [2,3] → [1,5]
                result[-1][1] = max(currentEnd, prevEnd)
            else:
                # No overlap: add current interval as separate interval
                result.append(intervals[i])
                
        return result