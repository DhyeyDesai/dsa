# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

# TODO: Figure out O(1) space solution

# INTUITION
# 1. We need to maximize profit, but after selling a stock, we must wait one day (cooldown) before buying again.
# 2. At any given day, there are two possible states: 
#       - buying (we are allowed to buy)
#       - not buying (we are holding a stock and can sell)
# 3. We'll explore all choices recursively:
#       - If we are allowed to buy, we can either buy the stock or skip (cooldown).
#       - If we are holding a stock, we can either sell it (and skip next day) or skip (cooldown).
# 4. We memoize results (using dp) to avoid recomputing overlapping subproblems.
# 5. The recursive DFS explores all possibilities and returns the maximum achievable profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # Memoization dictionary to store (index, buying_state) -> max profit

        def dfs(i, buying):
            # Base case: if we've gone past the last day, no profit can be made
            if i >= len(prices):
                return 0

            # Return cached result if we've already computed this state
            if (i, buying) in dp:
                return dp[(i, buying)]

            # If we are in a "buying" state
            if buying:
                # Option 1: Buy stock today -> pay prices[i], switch to 'not buying' state
                buy = dfs(i + 1, not buying) - prices[i]
                # Option 2: Skip today (cooldown) -> remain in 'buying' state
                cooldown = dfs(i + 1, buying)
                # Take the max profit of the two options
                dp[(i, buying)] = max(buy, cooldown)
            
            # If we are in a "not buying" (holding) state
            else:
                # Option 1: Sell stock today -> gain prices[i], skip next day (i+2)
                sell = dfs(i + 2, not buying) + prices[i]
                # Option 2: Skip selling today (cooldown)
                cooldown = dfs(i + 1, buying)
                # Take the max profit of the two options
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        # Start recursion at day 0 with the ability to buy
        return dfs(0, True)