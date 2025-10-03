# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

# TODO Figure out how to use Boolean Array Instead of Set with early termination

# Intuition:
# 1. The goal is to split the array into two subsets with equal sum → total sum must be even.
# 2. If we can form a subset with sum = totalSum // 2, then the rest of the numbers automatically form the other subset.
# 3. Instead of traditional DP table, we use a set to track all possible subset sums we can build so far.
# 4. For each number, we either include it or exclude it → for every existing sum in dp, we generate two sums.
# 5. If at any point we hit the target sum, we can short-circuit and return True immediately.

class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        # If total sum is odd, we can never split it into two equal integers
        if sum(nums) % 2 != 0:
            return False
        
        dp = set()          # dp stores all achievable subset sums so far
        dp.add(0)           # Base case: sum of 0 is always possible using no elements
        target = sum(nums) // 2

        # Iterate numbers in reverse (forward also works, just a choice)
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                # If adding the current number reaches the target, return early
                if t + nums[i] == target:
                    return True
                
                # Option 1: Include nums[i] in subset sum
                nextDP.add(t + nums[i])
                # Option 2: Exclude nums[i] and carry forward existing sum
                nextDP.add(t)
            
            dp = nextDP  # Move to the next layer of DP

        # After checking all elements, see if target sum is achievable
        return target in dp





