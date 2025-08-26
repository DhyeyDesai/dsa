# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Intuition:
# The goal is to maximize profit from buying and selling a stock once.
# To do this, we need to track the lowest price so far (best day to buy)
# and calculate the potential profit if we sell at the current price.
# At each step, we update the maximum profit found so far.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize minimum price with the first day's price
        minYet = prices[0]
        
        # Keep track of maximum profit found so far
        profit = 0
        
        # Iterate over all prices
        for item in prices:
            # Update minimum price if we find a cheaper stock
            if item < minYet:
                minYet = item
            
            # Calculate profit if we sell today
            profitHere = item - minYet
            
            # Update max profit if today's profit is higher
            if profitHere > profit:
                profit = profitHere
        
        # Final maximum profit
        return profit

