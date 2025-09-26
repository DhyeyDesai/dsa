# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/

# INTUITION:
# 1. Classic bottom-up DP: build solution for amount 0, then 1, 2, ... up to target
# 2. dp[i] = minimum coins needed to make amount i
# 3. For each amount, try every coin and pick the option that uses fewest total coins
# 4. Key insight: dp[amount] = min(dp[amount - coin] + 1) for all valid coins

# ALGORITHM BREAKDOWN:
# - Initialize dp array with "impossible" values (amount+1 is larger than any valid answer)
# - Base case: dp[0] = 0 (0 coins needed to make amount 0)
# - For each amount, try each coin and take minimum
# - If final answer is still "impossible", return -1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = minimum coins needed to make amount i
        # Initialize with amount+1 (impossible value - max coins needed is 'amount')
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0
        
        # Build up solution for each amount from 1 to target
        for a in range(1, amount + 1):
            # Try each coin denomination
            for c in coins:
                # Check if this coin can be used (doesn't exceed current amount)
                if a - c >= 0:
                    # Option: use this coin + minimum coins for remaining amount
                    # dp[a-c] = min coins for remaining amount after using coin c
                    # +1 for the current coin we're using
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        # If dp[amount] is still impossible value, no solution exists
        return dp[amount] if dp[amount] != amount + 1 else -1