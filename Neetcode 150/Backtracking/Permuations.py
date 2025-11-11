from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picks = [False] * len(nums)

        def dfs(curr: List[int], nums: List[int], picks: List[bool]) -> None:
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if not picks[i]:
                    curr.append(nums[i])
                    picks[i] = True
                    dfs(curr, nums, picks)
                    curr.pop()
                    picks[i] = False
        
        dfs([], nums, picks)
        return res
                

# Intuition:
# DFS