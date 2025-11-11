from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def dfs(curr: List[int], index: int) -> None:
            if index >= n:
                res.append(curr[:])
                return

            curr.append(nums[index])
            dfs(curr, index + 1)
            curr.pop()

            j = index + 1
            while j < n and nums[j] == nums[index]:
                j += 1
            dfs(curr, j)    
                
        dfs([], 0)
        return res

# Intuition:
# Similar to Combination Sum II, when deciding to skip a integer in forming a subset, we must make sure we skip all instances of that integer
# First sort nums
# Run DFS, if we go skipping route, we must make sure to skip all instances of that integer

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)