# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# Solution 1: Dynamic Programming (caching)
class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n
        def dfs(i):
            if i > n-1:
                return 0
            elif i == n-1:
                return cost[i]
            else:
                if dp[i] == -1:
                    left = dfs(i+1)
                    right = dfs(i+2)
                    dp[i] = min(left, right) + cost[i] 
                return dp[i]
            


        step1 = dfs(0)
        step2 = dfs(1)
        return min(step1, step2)


# Solution 2: Dynamic Programming (Bottom-up)
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]



# Solution 3: Dynamic Programming (Bottom-up and Space-Optimized)
class Solution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])