from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        islands = 0
        rows, cols, = len(grid), len(grid[0])

        def bfs(r: int, c: int) -> None:
            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if (newRow < 0 or newCol < 0 or
                        newRow >= rows or newCol >= cols or
                        grid[newRow][newCol] == "0"):
                        continue
                    q.append((newRow, newCol))
                    grid[newRow][newCol] = "0"
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        
        return islands
                


# Intuition:
# Traverse every cell in grid
#   When land is found, BFS and update all the land to water, then increment island count by 1

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)