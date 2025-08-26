# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

"""
Intuition:
Floyd's Cycle Detection (Tortoise and Hare) algorithm:
The key insight is to treat the array as a linked list where nums[i] points to nums[nums[i]].
Since there's a duplicate number, multiple indices will point to the same value, creating
a cycle in this "linked list". 

The algorithm works in two phases:
1. Detect that a cycle exists using slow/fast pointers
2. Find the start of the cycle (which is our duplicate number) using Floyd's algorithm

Why this works: If value X appears multiple times, then multiple array positions will 
"point to" index X, creating a cycle when we follow the chain nums[0] → nums[nums[0]] → ...
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect cycle using Floyd's tortoise and hare
        slow = 0  # Tortoise moves 1 step at a time
        fast = 0  # Hare moves 2 steps at a time
        
        while True:
            # Move pointers: slow takes 1 step, fast takes 2 steps
            slow = nums[slow]           # Move 1 step
            fast = nums[nums[fast]]     # Move 2 steps
            
            # If they meet, we've detected a cycle
            if slow == fast:
                break

        # Phase 2: Find the start of the cycle (the duplicate number)
        # Start another slow pointer from the beginning
        slow2 = 0
        
        while True:
            # Move both pointers 1 step at a time
            slow = nums[slow]   # Continue from where we detected the cycle
            slow2 = nums[slow2] # Start fresh from index 0
            
            # When they meet, we've found the start of the cycle
            # This is guaranteed to be the duplicate number
            if slow == slow2:
                return slow