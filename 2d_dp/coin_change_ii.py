# 518. Coin Change II
# https://leetcode.com/problems/coin-change-ii/

# Solution 1: Reverse Order
# INTUITION:
# 1. We process coins in order (backwards here) to avoid counting duplicate combinations
# 2. dp[a] = number of ways to make amount 'a' using coins processed so far
# 3. For each coin, we update all amounts: "add ways by using this coin"
# 4. dp[a-coin] tells us ways to make the remaining amount after using current coin
# 5. Base case: dp[0] = 1 (one way to make 0 - use no coins)
#
# Time Complexity: O(n * amount) where n = len(coins)
# Space Complexity: O(amount) for the dp array

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] = number of ways to make amount 'a'
        dp = [0] * (amount + 1)
        
        # Base case: one way to make amount 0 (use no coins)
        dp[0] = 1

        # Process each coin (iterating backwards, but direction doesn't matter)
        for i in range(len(coins) - 1, -1, -1):
            
            # For each amount from 1 to target amount
            for a in range(1, amount + 1):
                # If we can use this coin (coin value <= current amount):
                # Add the number of ways to make the remaining amount (a - coins[i])
                # This represents choosing to use coins[i] in our combination
                #
                # Otherwise, add 0 (can't use a coin bigger than the amount)
                # This is a concise way to say: "only use the coin if it fits, otherwise add 0 (no new ways)"
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0

        # Return the number of ways to make the target amount
        return dp[amount]
    

# Solution 2: 1D DP (Space Optimized)

# INTUITION:
# 1. Process coins one at a time to avoid counting duplicate combinations ([1,2] vs [2,1])
# 2. dp[amount] = number of ways to make 'amount' using coins processed so far
# 3. For each coin, ask: "How does adding THIS coin create new ways to make each amount?"
# 4. dp[j] += dp[j-coin] means: "ways to make j-coin become NEW ways to make j"
# 5. Start inner loop from 'coin' value - automatically handles the "can we use this coin?" check
#
# Time Complexity: O(n * amount) where n = len(coins)
# Space Complexity: O(amount) - single 1D array

class Solution2:
    def change(self, amount, coins):
        # dp[j] = number of ways to make amount j using coins processed so far
        dp = [0] * (amount + 1)
        
        # Base case: exactly one way to make amount 0 (use no coins)
        dp[0] = 1
        
        # Process each coin sequentially (order matters to avoid duplicates!)
        for coin in coins:
            # Update all amounts where this coin can be used
            # Starting from 'coin' ensures coin <= j (no extra check needed)
            for j in range(coin, amount + 1):
                # Current ways to make j = old ways (without this coin)
                #                         + ways to make (j - coin) [using this coin]
                # dp[j-coin] represents: "after using this coin once, 
                # how many ways to make the leftover?"
                dp[j] += dp[j - coin]
        
        # Return total ways to make the target amount using all coins
        return dp[amount]