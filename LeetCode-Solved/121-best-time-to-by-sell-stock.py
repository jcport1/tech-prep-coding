# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #time complexity = O(n)
        
        # buy low, sell high
        buy = 0

        # profit
        profit = 0

        for i in range(len(prices)-1):
            if prices[i+1] < prices[buy]:
                buy = i+1
            else:
                profit = max(profit, prices[i+1] - prices[buy])
        
        return profit
