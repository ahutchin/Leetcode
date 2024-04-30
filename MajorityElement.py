from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # initialize majority element
        majorityElement = nums[0]
        count = 1

        # iterate through the array
        for i in range(1, len(nums)):
            if nums[i] == majorityElement:
                count += 1
            else: 
                count -= 1
                if count == -1:
                    majorityElement = nums[i]
                    count = 1
        
        # return majorityElement
        return majorityElement
    
# Time complextiy: O(n)
# Space complexity: O(1)