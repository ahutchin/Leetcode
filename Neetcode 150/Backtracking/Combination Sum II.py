from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(total, curr, i) -> None:
            if total == target:
                res.append(curr.copy())
                return None
            elif total > target or i == len(candidates):
                return None
            
            curr.append(candidates[i])
            dfs(total + candidates[i], curr, i + 1)
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(total, curr, i + 1)

        dfs(0, [], 0)
        return res            
        
    # OPTIMIZED
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)
    
        def dfs(total, curr, i) -> None:
            if total == target:
                res.append(curr[:])
                return
            if total > target or i >= n:
                return
            
            if candidates[i] > target - total:  # prune
                return
            
            # Include current element
            curr.append(candidates[i])
            dfs(total + candidates[i], curr, i + 1)
            curr.pop()
    
            # Skip duplicates and explore next
            j = i + 1
            while j < n and candidates[j] == candidates[i]:
                j += 1
            dfs(total, curr, j)
    
        dfs(0, [], 0)
        return res         
                
# Intuition:
# This seems identical to subsets

# Test
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30
