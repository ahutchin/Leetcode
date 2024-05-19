from typing import List


class Solution:    
    # Time Complexity: O(n * m) because we only visit each element in the image atmost once, n is the number of rows and m is columns
    # Space Complexity: O(n * m) because worst case the recursion is called through every element of the image thus taking up memory for each index
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def colorFill(image: List[List[int]], sr: int, sc: int, oldColor: int, newColor: int):
            if sr < 0 or sc < 0 or sr > len(image) - 1 or sc > len(image[0]) - 1 or image[sr][sc] != oldColor: return

            image[sr][sc] = newColor

            colorFill(image, sr + 1, sc, oldColor, newColor)
            colorFill(image, sr - 1, sc, oldColor, newColor)
            colorFill(image, sr, sc + 1, oldColor, newColor)
            colorFill(image, sr, sc - 1, oldColor, newColor)

            return
        
        if color != image[sr][sc]: 
            colorFill(image, sr, sc, image[sr][sc], color)

        return image