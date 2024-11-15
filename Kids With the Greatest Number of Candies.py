from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Iterate through List to find largest count of candies
        maxCount = 0
        for candy in candies:
            if candy > maxCount: 
                maxCount = candy
        
        # Create result List using maxCount & extraCandies
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCount)

        # return
        return result
    
# Test
test = Solution()
result = test.kidsWithCandies([2,3,5,1,3], 3)

# O(n) time, O(n) space