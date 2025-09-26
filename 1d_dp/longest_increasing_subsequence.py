# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/description/

# INTUITION:
# 1. Bottom-up DP working backwards from end of array
# 2. LIS[i] = length of longest increasing subsequence starting at index i
# 3. For each position i, look at all positions j > i and extend if nums[i] < nums[j]
# 4. Key insight: by working backwards, when we process i, all positions j > i are already computed

# ALGORITHM BREAKDOWN:
# - Initialize LIS[i] = 1 for all positions (each element forms subsequence of length 1)
# - Work backwards: for each i, check all j where j > i
# - If nums[i] < nums[j], we can extend: LIS[i] = max(LIS[i], 1 + LIS[j])
# - Answer is the maximum value in LIS array

# TODO: This is O(n²) solution. There's also O(n log n) solution using binary search + patience sorting.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i] = length of longest increasing subsequence starting at index i
        LIS = [1] * len(nums)  # Base case: each element forms subsequence of length 1
        
        # Work backwards through the array
        for i in range(len(nums) - 1, -1, -1):
            # Check all positions after current position
            for j in range(i + 1, len(nums)):
                # Can we extend subsequence starting at i by including position j?
                if nums[i] < nums[j]:
                    # Option 1: current LIS[i] 
                    # Option 2: start with nums[i], then take best subsequence from j
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        # The answer is the maximum LIS starting from any position
        return max(LIS)
