from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Needs O(n) runtime
        s = set()

        # nums traversal
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        
        # return
        return list(s)[0]
    def singleNumberv2(self, nums: List[int]) -> int: # Better runtime & memory
        curNum = nums[0]
        for num in nums[1:]:
            curNum ^= num
        return curNum