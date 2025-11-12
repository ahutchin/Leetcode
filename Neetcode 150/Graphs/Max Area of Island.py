from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        Rows, Cols = len(grid), len(grid[0])

        def bfs(r: int, c: int) -> int:
            count = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if (newRow < 0 or newCol < 0 or
                        newRow >= Rows or newCol >= Cols or
                        grid[newRow][newCol] == 0):
                        continue
                    grid[newRow][newCol] = 0
                    count += 1
                    q.append((newRow, newCol))
            
            return count



        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 1:
                    area = max(area, bfs(i, j))
        
        return area

# Intuition:
# Same as Number of Islands, instead of tracking island count, we track size of island

# Time Complexity: O(n*m)
# Space Complexity: O(n*m)