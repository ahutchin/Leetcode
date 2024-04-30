from collections import defaultdict
from typing import List


class Solution:
    # O(n) time
    # O(n) space
    def containsDuplicate(self, nums: List[int]) -> bool:
        # initialize Dictionary to store each value
        k = defaultdict(int)

        # iterate through nums
        for num in nums:
            k[num] += 1
            if k[num] > 1:
                return True
        
        # return
        return False
    
# test case
solution = Solution()

nums = [1,2,3,1]
result = solution.containsDuplicate(nums)
print(result)