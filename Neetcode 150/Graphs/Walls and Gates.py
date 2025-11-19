from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Treasure Chests
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(rows): # O(n * m)
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
        
        # Queue
        while q: # O(n * m) because we visit each index at most once
            for _ in range(len(q)):
                row, col, distance = q.popleft()
                for dr, dc, in directions:
                    newRow = row + dr
                    newCol = col + dc
                    if (newRow < 0 or newCol < 0 or
                        newRow >= rows or newCol >= cols or
                        grid[newRow][newCol] != 2147483647): 
                        continue
                    grid[newRow][newCol] = distance + 1
                    q.append((newRow, newCol, distance + 1))
        

            

            
            
# Intuition:
# Similar to rotten oranges
# 2 Pass
#   locate each treasure chest
#   BFS outwards from each treasure chest, updating the value to currDistance + 1 

# Space Complexity: O(n * m)
# Time Complexity: O(n * m) -- q will store all indices worst case