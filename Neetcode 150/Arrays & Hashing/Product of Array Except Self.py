from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize left & right arrays
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)

        # compute left array
        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1]
        
        # compute right array
        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1]
        
        # compute productExceptSelf array
        res = []
        for i in range(len(nums)):
            res.append(leftProduct[i] * rightProduct[i])
        
        # return
        return res

# Initial Thought:
# 2nd time solving this, remember to build 2 arrays, 1 that contains the product of all elements before itself, the other being all products after itself
# multiply by left and right index of respective lists to get result array
# Ex: Input: nums = [1,2,3,4], Output: [24,12,8,6]
# leftProduct = [1, 1, 2, 6]
# rightProduct = [24, 12, 4, 1]

test = Solution()
print(test.productExceptSelf([1,2,3,4]))