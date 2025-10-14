from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums: 
            if num in seen:
                return True
            seen.add(num)
        return False


# Initial thought: 
# Use a hashmap to track presence of digits
# If digit is present -> return True
# Else return false at end of loop
# This solution takes O(n) time & O(n) space
# Can I cut the space to O(1)?

# Solution:
# Use a set instead, otherwise same idea
# Better to use a set when tracking existence, and dict when tracking count 

# O(n) Time and Space complexity