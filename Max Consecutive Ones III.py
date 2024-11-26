from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # var def
        p1 = 0
        p2 = 0
        curOnes = 0
        maxOnes = 0
        flipCount = k

        # Traverse nums
        while p2 < len(nums):
            if nums[p2] == 1:
                curOnes += 1
                p2 += 1
            elif nums[p2] == 0:
                if flipCount > 0:
                    curOnes += 1
                    flipCount -= 1
                    p2 += 1
                else:
                    while nums[p1] != 0:
                        curOnes -= 1
                        p1 += 1
                    curOnes -= 1
                    flipCount += 1
                    p1 += 1
            
            if curOnes > maxOnes:
                maxOnes = curOnes
        
        # return
        return maxOnes

# Time Complexity: O(n) worst case we visit every node twice (each pointer visits each node)
# Space complexity: O(1) no additional space used