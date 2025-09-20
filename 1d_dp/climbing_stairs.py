# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

# Solution 1: Recursion
class Solution1:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i>=n:
                # Returns False(0) if we reached beyond the goal (i > n)
                # Returns True(1) if we reached the goal (i == n)
                return i == n
            return dfs(i+1) + dfs(i+2)
        return dfs(0)
    
# Solution 2: Dynamic Programming (Top-down)
class Solution2:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n
        def dfs(i):
            if i>=n:
                return i == n
            if cache[i] == -1:
                cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        
        return dfs(0)
    

# Solution 3: Dynamic Programming (Bottom-up)
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[n]

# Solution 4: Dynamic Programming (Space Optimized)
class Solution4:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
            
        one = 2
        two = 1

        for _ in range(n-2):
            one, two = one+two, one
        return one