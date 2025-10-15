from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for k in range(1, len(prices)):
            curProfit = prices[k] - buy
            if curProfit > maxProfit:
                maxProfit = curProfit
            if prices[k] < buy:
                buy = prices[k]
            
        return maxProfit
