# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minYet = prices[0]
        profit = 0
        
        for item in prices:
            if item<minYet:
                minYet = item
            profitHere = item-minYet
            if profitHere>profit:
                profit = profitHere
        return profit

        return profit
