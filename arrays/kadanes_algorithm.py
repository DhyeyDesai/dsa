# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        for num in nums:
            if curSum<0:
                curSum = 0
            curSum+=num
            maxSum = max(curSum, maxSum)

        return maxSum