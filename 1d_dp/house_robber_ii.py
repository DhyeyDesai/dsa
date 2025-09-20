# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
       
        def helper(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                rob1, rob2 = rob2, max(num+rob1, rob2)
            return rob2
    
        n = len(nums)
        result1, result2 = helper(nums[:n-1]), helper(nums[1:])
        return max(result1, result2, nums[0])
