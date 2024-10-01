from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i: int, currVals: List[int], total: int) -> None:
            if total == target:
                result.append(currVals.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            currVals.append(candidates[i])
            dfs(i, currVals, total + candidates[i])
            currVals.pop()
            dfs(i + 1, currVals, total)

        dfs(0, [], 0)
        return result
    
test = Solution()
test.combinationSum([2,3,6,7], 7)