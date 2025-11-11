from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(sum: int, curr: List[int], cand: List[int]) -> None:
            if sum > target:
                return
            elif sum == target:
                res.append(curr)
                return
            
            for i in range(len(cand)):
                dfs(sum + cand[i], curr + [cand[i]], cand[i:])
            
            return

        dfs(0, [], candidates)
        return res

# Intuition:
# Brute force backtracking
# Time Complexity: O(2t/m)
# Space Complexity: O(2t/m)