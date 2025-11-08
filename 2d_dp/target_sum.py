# 494. Target Sum
# https://leetcode.com/problems/target-sum/

# Solution 1: DP recursion with memoization
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, curr_sum):
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            if i == len(nums):
                return 1 if curr_sum == target else 0
        
            dp[(i, curr_sum)] = backtrack(i + 1, curr_sum + nums[i]) + backtrack(i + 1, curr_sum - nums[i])
            return dp[(i, curr_sum)]
                

        return backtrack(0, 0)
    

# Solution 2: Bottom-Up DP
from collections import defaultdict
class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]

        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total+nums[i]] += count
                dp[i+1][total-nums[i]] += count
        
        return dp[n][target]
    
# Solution 3: Bottom-Up DP (Space-Optimized)
# INTUITION:
# 1. At each number, we have 2 choices: add (+) or subtract (-), creating a tree of possibilities
# 2. Instead of exploring all paths recursively (exponential), we track how many ways we can 
#     reach each possible sum at each step (dynamic programming)
# 3. We use a dictionary to store {current_sum: number_of_ways_to_reach_it}, building layer by layer
# 4. For each new number, we update all reachable sums by adding/subtracting the current number

# TIME COMPLEXITY: O(n * s) where n = len(nums), s = number of unique sums possible
#                     In worst case, s can be O(sum(nums)), so O(n * sum(nums))
# SPACE COMPLEXITY: O(s) for the dictionary storing reachable sums, worst case O(sum(nums))

from collections import defaultdict
class Solution3:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Initialize: we can reach sum=0 in exactly 1 way (by choosing nothing yet)
        dp = defaultdict(int)
        dp[0] = 1

        # Process each number in the array
        for i in range(len(nums)):
            next_dp = defaultdict(int)
            
            # For each currently reachable sum and its count of ways
            for total, count in dp.items():
                # Option 1: Add current number - propagate the count of ways
                next_dp[total+nums[i]] += count

                # Option 2: Subtract current number - propagate the count of ways
                next_dp[total-nums[i]] += count
            
            # Move to next layer: next_dp becomes our new state
            dp = next_dp
        
        # Return how many ways we can reach the target sum
        return dp[target]