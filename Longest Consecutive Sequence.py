from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Find all 'starts' for sequences
        starts = set()
        lookups = set(nums) # O(n) time

        # find starts
        for num in nums: # O(n) time
            if (num - 1) not in lookups:
                starts.add(num)
        
        maxSequence = 0
        # find longest sequence
        for start in starts: # worst case O(n) time
            curSequence = 1
            curNum = start
            while curNum + 1 in lookups:
                curSequence += 1
                curNum += 1
            if curSequence > maxSequence:
                    maxSequence = curSequence
        
        return maxSequence
# Intuition:
# Must be a traversal method to stay in O(n)