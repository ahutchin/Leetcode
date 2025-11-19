from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums) # O(n)
        starts = set()
        for num in nums: # O(n)
            if num - 1 not in lookup:
                starts.add(num)
        
        maxLength = 0
        for start in starts: # O(n)
            length = 1
            currNum = start
            while currNum + 1 in lookup:
                length += 1
                currNum += 1
            maxLength = max(maxLength, length)
    
        return maxLength

# Intuition:
# Use a set to have O(1) lookup time for nums
# Find all nums that can start a sequence

# Time Comlpexity: O(n)
# Space Complexity: O(n)