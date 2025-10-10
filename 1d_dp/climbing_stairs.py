# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# Overall intuition:
# 1. At each step, you can either climb 1 or 2 stairs — this forms a Fibonacci-like pattern.
# 2. The total ways to reach step `n` = ways to reach (n-1) + ways to reach (n-2).

# Solution 1: Recursion (Brute Force)
# Try all possible paths — from each step, move either 1 or 2 steps ahead recursively.
# This explores every possible way to reach the top.
# It's simple to understand but inefficient due to repeated subproblems.
# Time Complexity: O(2^n)
# Space Complexity: O(n) (recursion stack)

class Solution1:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            # Base case: if we've gone beyond step n
            if i >= n:
                # Return 1 if we exactly reached n, otherwise 0
                return i == n
            
            # Recursive case: move by 1 or 2 steps
            return dfs(i + 1) + dfs(i + 2)
        
        # Start climbing from step 0
        return dfs(0)


# Solution 2: Dynamic Programming (Top-down / Memoization)
# This is recursion + memory optimization.
# Store already computed results in a cache so we don’t recalculate the same subproblems.
# This reduces time complexity from exponential to linear.
# Time Complexity: O(n)
# Space Complexity: O(n) (recursion + cache)

class Solution2:
    def climbStairs(self, n: int) -> int:
        # Cache to store already computed results
        cache = [-1] * n
        
        def dfs(i):
            # Base case: same as before
            if i >= n:
                return i == n

            # If not cached, compute and store result
            if cache[i] == -1:
                cache[i] = dfs(i + 1) + dfs(i + 2)
            
            # Return cached result to avoid recomputation
            return cache[i]
        
        # Start from step 0
        return dfs(0)


# Solution 3: Dynamic Programming (Bottom-up / Tabulation)
# Build the solution iteratively from the base cases up to n.
# Each dp[i] stores the number of ways to reach step i using results from i-1 and i-2.
# This eliminates recursion entirely and uses a simple loop.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution3:
    def climbStairs(self, n: int) -> int:
        # Handle small inputs directly
        if n <= 2:
            return n
        
        # dp[i] represents number of ways to reach step i
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # Build the table iteratively from step 3 to n
        for i in range(3, n + 1):
            # The total ways to reach step i = sum of previous two steps
            dp[i] = dp[i - 1] + dp[i - 2]
        
        
        # Return the result for step n
        return dp[n]


# Solution 4: Dynamic Programming (Space Optimized)
# Notice only the last two computed values are needed at each step.
# Replace the dp array with two variables that roll forward as we iterate.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution4:
    def climbStairs(self, n: int) -> int:
        # Base cases: directly return n for first two stairs
        if n <= 2:
            return n

        # Initialize the last two computed results
        one = 2  # ways to reach step 2
        two = 1  # ways to reach step 1

        # Iteratively compute next steps using only two variables
        for _ in range(n - 2):
            # Shift forward: new value = sum of previous two
            one, two = one + two, one
        
        # 'one' now holds the total ways to reach step n
        return one
