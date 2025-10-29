from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search along y axis: find the row
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            val = matrix[mid][0]
            if val == target:
                return True
            elif val < target:
                top = mid + 1
            elif val > target:
                bottom = mid - 1
        
        l = 0
        r = len(matrix[0]) - 1
        targetRow = bottom
        while l <= r:
            mid = (l + r) // 2
            val = matrix[targetRow][mid]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1

        return False

# Intuition:
# Binary Search along the y-axis, then Binary Search along the x-axis

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol = Solution()
print(sol.searchMatrix(matrix, target))