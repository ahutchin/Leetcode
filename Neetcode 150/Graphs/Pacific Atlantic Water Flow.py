from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        atlantic, pacific = set(), set()
        rows, cols = len(heights), len(heights[0])

        def DFS(row: int, col: int, visited: set, prevHeight: int): # O(n * m)
            if (row < 0 or col < 0 or
                row >= rows or col >= cols or
                heights[row][col] < prevHeight or
                (row, col) in visited):
                return
            visited.add((row, col))
            for dr, dc in directions:
                DFS(row + dr, col + dc, visited, heights[row][col])

        for c in range(cols): # O(n + m)
            DFS(0, c, pacific, heights[0][c])
            DFS(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows): # O(n + m)
            DFS(r, 0, pacific, heights[r][0])
            DFS(r, cols - 1, atlantic, heights[r][cols - 1])
        
        res = []
        for r in range(rows): # O(n * m)
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res


        
            


                
            

# Intuition:
# Brute Force: for every matrix entry, check its neighbors to see both Atlantic & Pacific Oceans are reached O(n^2 * m^2)
# Could I store information in a similar grid to prevent repeated operations 

# Use a set to store all indices that can reach pacific, and a 2nd set to store all indices that can reach atlantic
# Any overlapping values can reach both

# Time Complexity: O(n * m)