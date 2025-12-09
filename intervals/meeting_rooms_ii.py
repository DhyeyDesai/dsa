# NOTE: This is a premium problem. We will use a similar problem from neetcode.io

# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/description/

# NeetCode - https://neetcode.io/problems/meeting-schedule-ii/question?list=neetcode150

# INTUITION:
# The minimum number of meeting rooms needed equals the maximum number of meetings 
# happening at the same time. Instead of tracking individual rooms, we process all 
# start and end times chronologically. When a meeting starts, we need one more room. 
# When a meeting ends, we free up a room. The peak overlap tells us the answer.

# TIME COMPLEXITY: O(n log n) - Sorting both start and end arrays
# SPACE COMPLEXITY: O(n) - Storing start and end arrays separately

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Separate and sort all start times and end times independently
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = e = 0           # Pointers for start and end arrays
        res = count = 0     # res tracks max rooms, count tracks current rooms in use
        
        # Process all meetings by comparing earliest unprocessed start vs earliest unprocessed end
        while s < len(intervals):
            # If next meeting starts before earliest meeting ends
            if start[s] < end[e]:
                s += 1          # Process this start event
                count += 1      # Need one more room
            else:
                # A meeting has ended, freeing up a room
                e += 1          # Process this end event
                count -= 1      # One less room needed
            
            # Update maximum rooms needed at any point in time
            res = max(res, count)
        
        return res