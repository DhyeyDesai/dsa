# 198. House Robber
# https://leetcode.com/problems/house-robber/

# INTUITION:
# 1. Classic DP problem: at each house, decide whether to rob it or skip it
# 2. Can't rob adjacent houses, so we need to track two states
# 3. Key insight: only need to remember last two decisions, not entire history
# 4. Space optimization: instead of dp array, just use two variables

# ALGORITHM BREAKDOWN:
# - rob1 = max money we could have robbed up to house i-2
# - rob2 = max money we could have robbed up to house i-1  
# - At each house: either skip it (keep rob2) or rob it (rob1 + current house)
# - Update variables for next iteration using simultaneous assignment

class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 = max money robbed up to house i-2 (two houses ago)
        # rob2 = max money robbed up to house i-1 (previous house)
        rob1, rob2 = 0, 0

        for num in nums:
            # At current house, we have two choices:
            # Choice 1: Don't rob current house, keep previous max (rob2)
            # Choice 2: Rob current house, add to max from two houses ago (rob1 + num)
            
            # Simultaneous assignment to update both variables:
            # new_rob1 = old_rob2 (previous house becomes "two houses ago")
            # new_rob2 = max(old_rob2, old_rob1 + num) (best choice for current position)
            rob1, rob2 = rob2, max(rob2, rob1 + num)
        
        # rob2 now contains the maximum money we can rob from all houses
        return rob2