# 198. House Robber
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            rob1, rob2 = rob2, max(rob2, rob1+num)
        
        return rob2