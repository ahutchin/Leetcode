from typing import List
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSubArray = sys.maxsize
        l, r = 0, 0

        sum = 0
        while l < len(nums) and r < len(nums):
            sum += nums[r]
            if sum < target:
                r += 1
            elif sum >= target:
                while sum >= target:
                    sum -= nums[l]
                    l += 1
                minSubArray = min(r - l + 2, minSubArray)
                r += 1
        
        return 0 if minSubArray == sys.maxsize else minSubArray




# Intuition:
# Left & right pointers, 
# Starting at 0, add current right pointer val to total sum
# if sum is greater than or equal to target, calculate window size and compare it to current smallest subarray,
# increment left pointer by 1, if still greater than target, compare window size with smallest subarray
# if less than target, increment right pointer and repeat
target = 7
nums = [2,3,1,2,4,3]
test = Solution()
print(test.minSubArrayLen(target, nums))

# Time complexity: O(n)
# Space complexity: O(1)