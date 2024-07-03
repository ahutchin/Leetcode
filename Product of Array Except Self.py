from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [0] * len(nums)
        prefix_array[0] = 1
        for i in range(1, len(nums)):
            prefix_array[i] = prefix_array[i - 1] * nums[i - 1]

        suffix_array = [0] * len(nums)
        suffix_array[- 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix_array[i] = suffix_array[i + 1] * nums[i + 1]


        for i in range(len(nums)):
            nums[i] = prefix_array[i] * suffix_array[i]

        return nums
    
# Test Case:
nums = [4, 3, 7, 11, -4] # nums
# [1, 4, 12, 84, 924] # prefix array
# [-924 ,-308, -44, -4, 1] # suffix array

solution = Solution()
result = solution.productExceptSelf(nums)
print(result)