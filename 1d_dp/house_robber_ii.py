# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/


# INTUITION:
# 1. Houses are arranged in a circle - first and last house are adjacent!
# 2. This means we can't rob both the first house AND the last house
# 3. Solution: solve two separate linear problems and take the maximum
# 4. Case 1: Rob houses 0 to n-2 (exclude last house, so first house is available)
# 5. Case 2: Rob houses 1 to n-1 (exclude first house, so last house is available)

# KEY INSIGHT:
# - If we rob first house, we can't rob last house → solve for nums[0:n-1]
# - If we rob last house, we can't rob first house → solve for nums[1:n]  
# - The optimal solution is one of these two scenarios


class Solution:
    def rob(self, nums: List[int]) -> int:
       
        def helper(nums):
            """Standard House Robber I algorithm for linear arrangement"""
            rob1, rob2 = 0, 0
            for num in nums:
                # Choice: skip current house (rob2) or rob it (rob1 + num)
                rob1, rob2 = rob2, max(num + rob1, rob2)
            return rob2
    
        n = len(nums)
        
        # Edge case: only one house
        if n == 1:
            return nums[0]
        
        # Case 1: Consider houses 0 to n-2 (can potentially rob first house)
        # Exclude last house to avoid adjacency with first house
        result1 = helper(nums[:n-1])  # nums[0] through nums[n-2]
        
        # Case 2: Consider houses 1 to n-1 (can potentially rob last house)  
        # Exclude first house to avoid adjacency with last house
        result2 = helper(nums[1:])    # nums[1] through nums[n-1]
        
        # Return the maximum of both scenarios
        return max(result1, result2)
