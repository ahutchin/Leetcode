from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Var definition
        numsLen = len(nums)
        index = 0

        # Iterate through nums
        for i in range(numsLen):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
    def moveZeroes2(self, nums: List[int]) -> None: # more efficient than using pop and append operations
        # var def
        curIndex = 0

        # Loop
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curIndex] = nums[i]
                curIndex += 1

        # Fill in remainder
        for i in range(curIndex, len(nums)):
            nums[i] = 0
                