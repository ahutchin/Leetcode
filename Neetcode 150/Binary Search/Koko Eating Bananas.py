from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l < r:
            mid = (l + r) // 2
            if self.validK(piles, h, mid):
                l = mid + 1
            else:
                r = mid
        
        return r

    def validK(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0
        for pile in piles: # O(n) time
            hours += math.ceil(pile / k)
        
        return hours > h

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

# Intuition:
# Define a method to check if koko can eat bananas in the hours
# Use binary search with range(1, max(piles)) to find the largest value that completes the task

# Time Complexity: O(n*log(m))
# Space complexity: O(1)