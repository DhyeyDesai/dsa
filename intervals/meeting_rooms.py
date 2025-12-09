# NOTE: This is a premium problem. We will use a similar problem from neetcode.io

# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/description/

# NeetCode - https://neetcode.io/problems/meeting-schedule/question?list=neetcode150

# INTUITION:
# To attend all meetings, no two meetings should overlap. If we sort all meetings by 
# their start time, we only need to check if any meeting ends after the next meeting 
# starts. This is because after sorting, if meeting[i] doesn't overlap with meeting[i+1],
# and meeting[i+1] doesn't overlap with meeting[i+2], then meeting[i] won't overlap 
# with meeting[i+2] either (transitivity).

# TIME COMPLEXITY: O(n log n) - where n is the number of intervals
# - Sorting takes O(n log n)
# - Linear scan takes O(n)
# - Overall: O(n log n)

# SPACE COMPLEXITY: O(1) or O(n)
# - O(1) if we don't count the space used by sorting (in-place sorting)
# - O(n) if we count the space used by the sorting algorithm (Timsort in Python)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by their start time
        # This allows us to check overlaps sequentially
        intervals.sort(key = lambda x:x.start)

        # Iterate through sorted intervals starting from the second meeting
        for i in range(1, len(intervals)):
            prev = intervals[i-1]  # Previous meeting in sorted order
            curr = intervals[i]     # Current meeting
            
            # Check if previous meeting ends after current meeting starts
            # If prev.end > curr.start, there's an overlap
            # Example: prev=[1,5], curr=[3,7] → 5 > 3, so they overlap
            if prev.end > curr.start:
                return False
        
        # If we've checked all adjacent pairs without finding overlap,
        # all meetings can be attended
        return True