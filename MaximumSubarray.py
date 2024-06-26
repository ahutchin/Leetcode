from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        largest_sum = nums[0] # Default the largest_sum to the first value in the array (this covers arrays of length 1)

        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > largest_sum: largest_sum = current_sum
            if current_sum < 0: current_sum = 0
        return largest_sum 
            