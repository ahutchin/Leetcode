class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pointer priceDifference
        priceDifference = 0

        # iterate through prices array
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                if prices[j] < prices[i]: # if the difference between the indeces is negative
                    i = j
                    break
                elif (prices[j] - prices[i]) > priceDifference:
                    priceDifference = prices[j] - prices[i]
        
        # return
        return priceDifference