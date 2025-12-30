from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        r = 1

        curSum = nums[0]
        while r < n:
            if curSum < 0 and nums[r] > curSum:
                curSum = nums[r]
            else:
                curSum = curSum + nums[r]
            r += 1
            maxSum = max(maxSum, curSum)

        return maxSum


# Intuition:
# DP
# Time Complexity: O(n)
