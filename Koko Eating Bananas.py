from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper
        def canEatInTime(piles: List[int], k: int) -> bool:
            nonlocal h
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return True if hours <= h else False
        
        # BS setup
        left = 1
        right = max(piles)

        # BS
        while left <= right:
            mid = (left + right) // 2
            res = canEatInTime(piles, mid)
            if res:
                right = mid - 1
            else:
                left = mid + 1
        
        # return
        return left
# find the max size of a banana pile in piles
# start binary search, setting k equal to the middle of said difference
# check if such a k value completes the banana eating process in h hours

# Test
test = Solution()
result = test.minEatingSpeed([30,11,23,4,20], 6)
print(result)