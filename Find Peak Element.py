from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = (left + right) // 2
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return mid

# Utilize binary search
# Set left & right, calculate middle
# If middle is not a peak, set the new edge to the side that is greater than the middle

# Test
test = Solution()
result = test.findPeakElement([1])
print(result)