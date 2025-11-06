from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            else:
                nums[abs(num) - 1] *= -1
        
        return -1

# Intuition:
# Iterate through nums
# For each num, check if the value at nums[num - 1] is negative -> if negative, return that number
# Else, multiply the number at that index by -1, continue

# Test
print(Solution().findDuplicate([1,3,4,2,2]))