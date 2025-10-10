# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

# Overall Intuition:
# You can climb either 1 or 2 steps at a time, but each step has an associated cost.
# The goal is to reach the top of the floor (beyond the last index) with minimum total cost.
# The idea is similar to the Fibonacci pattern, but instead of counting ways, we minimize total cost.


# Solution 1: Dynamic Programming (Top-down with Caching)
# Intuition:
# We recursively calculate the minimum cost to reach the top starting from each step.
# To avoid redundant calculations, we store results in a cache (memoization).
class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n  # dp[i] = minimum cost to reach the top from step i

        def dfs(i):
            # Base case: if we go beyond the last step, no cost is added
            if i > n - 1:
                return 0
            # If we are on the last step, we must pay its cost
            elif i == n - 1:
                return cost[i]
            else:
                # If not cached, compute recursively
                if dp[i] == -1:
                    # Choose the cheaper option between 1-step and 2-step move
                    left = dfs(i + 1)
                    right = dfs(i + 2)
                    dp[i] = min(left, right) + cost[i]
                return dp[i]

        # We can start from step 0 or step 1, whichever is cheaper
        step1 = dfs(0)
        step2 = dfs(1)
        return min(step1, step2)


# Solution 2: Dynamic Programming (Bottom-up)
# Intuition:
# Build up the solution iteratively using a dp array.
# dp[i] represents the minimum cost required to reach step i.
# The cost to reach each step depends on the minimum cost of reaching the two previous steps.
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)  # dp[i] = min cost to reach step i

        # Start from step 2, since step 0 and 1 are free starting points
        for i in range(2, n + 1):
            # Choose the cheaper path: coming from one step behind or two steps behind
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        # dp[n] is the cost to reach beyond the last step
        return dp[n]


# Solution 3: Dynamic Programming (Bottom-up and Space-Optimized)
# Intuition:
# Instead of maintaining an extra dp array, we reuse the cost array itself.
# Starting from the end, we update each element to represent the minimum total cost from that step to the top.
# Finally, we choose the cheaper of the two starting positions (step 0 or step 1).
class Solution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Start from third last step and move backward
        for i in range(len(cost) - 3, -1, -1):
            # Each step's cost becomes its cost + min of next two steps
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        # Minimum cost to start from step 0 or step 1
        return min(cost[0], cost[1])
