from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = -1
        start = 0
        end = len(height) - 1

        while start < end:
            curArea = min(height[start], height[end]) * (end - start)
            if curArea > maxArea:
                maxArea = curArea
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return maxArea