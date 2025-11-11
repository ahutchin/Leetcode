from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(curr: List[int], remaining: List[int]) -> None:
            nonlocal res
            res.append(curr)

            for i in range(len(remaining)):
                backtracking(curr + [remaining[i]], remaining[i + 1:])
            
            return

        backtracking([], nums)
        return res
    

# Intuition:
# Store results in result array
# Define Backtracking algorithm that takes the current list, and the available numbers to add

# Time Complexity: O(n * 2^n) there are 2^n subsets, and we do n/2 (on average) operations per subset
# Space complexity: O(n * 2^n) where n is number of subsets -- n recursion stack depth