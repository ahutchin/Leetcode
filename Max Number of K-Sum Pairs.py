from typing import List
from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        compliments = defaultdict(int)
        operationCount = 0

        for num in nums:
            compliment = k - num
            if compliment in compliments and compliments[compliment] > 0:
                compliments[compliment] -= 1
                operationCount += 1
            else:
                compliments[num] += 1

        return operationCount
    
# Time Complexity: O(n) because we traverse nums once and do a set number of operations each time
# Space Complexity: O(n) worst case we store every num in our dictionary