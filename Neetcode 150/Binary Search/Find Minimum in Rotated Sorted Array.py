from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
        
        return nums[l]

# Intuition
# Compare left, right, and mid pointers for nums
# If midpoint is less than right, left side has the cut array -> set right to mid
# If midpoint is greater than right, right side has the split -> set left to mid

# Example:
# Input: nums = [7,0,1,2,3,4,5,6]
# Input: nums = [2,3,4,5,6,7,0,1]
# Input: nums = [4,5,6,7,0,1,2,3]
# Input: nums = [7,0,1,2,3,4,5]
# Input: nums = [2,3,4,5,6,7,0]
# Input: nums = [4,5,6,7,0,1,2]