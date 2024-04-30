from typing import List

class Solution:
    @staticmethod
    def twoSumIterative(nums: List[int], target: int) -> List[int]:

        # Iterate through nums using indices
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start j from i + 1 to avoid duplicate pairs
                if nums[i] + nums[j] == target:  # Use == for comparison
                    return [i, j]
    
    @staticmethod
    def twoSumHash(nums: List[int], target: int) -> List[int]:
    
        # Define hashmap
        numsHash = {}

        # iterate through nums
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in numsHash:
                return [numsHash[compliment], i]
            numsHash[nums[i]] = i

# Example test case
nums = [2, 11, 23, 15, 7]
target = 9

# Call the twoSum method
result = Solution.twoSumHash(nums, target)
print(result)  # Output: [0, 1]