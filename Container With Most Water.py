from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Var definition
        left = 0
        right = len(height) - 1
        maxArea = 0

        # Start Loop
        while left < right:
            currArea = min(height[left], height[right]) * (right - left)
            if currArea > maxArea: 
                maxArea = currArea
            
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        
        # return
        return maxArea