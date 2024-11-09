from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Var definition
        sumLeft = [0]
        sumRight = [0]

        # Iterate through nums
        currSum = 0
        for i in range(0, len(nums) - 1):
            currSum += nums[i]
            sumLeft.append(currSum)

        currSum = 0
        for i in range(len(nums) - 1, 0, -1):
            currSum += nums[i]
            sumRight.insert(0, currSum)

        # Find point where sumLeft & Right are equal
        for i in range(len(nums)):
            if sumLeft[i] == sumRight[i]: return i

        return -1
    
# TEST
nums = [1,7,3,6,5,6]

test = Solution()
result = test.pivotIndex(nums)
print(result)