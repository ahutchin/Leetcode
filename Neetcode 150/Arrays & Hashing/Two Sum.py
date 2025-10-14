from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # copmlements dictionary
        complements = dict()

        # iterate through every value in nums
        for index in range(len(nums)):
            # Calculate complement
            complement = target - nums[index]

            if complement in complements:
                return [complements[complement], index]
            
            # Add num to complements dict
            complements[nums[index]] = index
        
        return []

# Intuition:
# use a dict: complement, index