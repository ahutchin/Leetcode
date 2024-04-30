from typing import List

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # pointer priceDifference
        priceDifference = 0

        # iterate through prices array
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] < prices[i]: # if the difference between the indeces is negative
                    i = j
                    break
                elif (prices[j] - prices[i]) > priceDifference:
                    priceDifference = prices[j] - prices[i]
        
        # return
        return priceDifference
    
    def maxProfit2(self, prices: List[int]) -> int:
        # pointer priceDifference
        buy = prices[0]
        profit = 0

        for k in range(1, len(prices)):
            if prices[k] < buy:
                buy = prices[k]
            if profit < prices[k] - buy:
                profit = prices[k] - buy
        
        return profit
    
# Example test case
solution = Solution()

prices = [7,6,4,3,1]

result = solution.maxProfit2(prices)
print(result)