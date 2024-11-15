from typing import List
import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # var definition
        minNum1 = minNum2 = math.inf

        # iterate through array
        for num in nums:
            if num < minNum1:
                minNum1 = num
            elif num > minNum1 and num < minNum2:
                minNum2 = num
            elif num > minNum1 and num > minNum2:
                return True
        
        # return
        return False