from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        q = deque()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Check indices for rotten orange 
        for r in range(rows): # O(n * m)
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # If no fresh oranges, return 0
        if fresh_count == 0:
            return 0

        time = -1
        # Spread rotting
        while q: # O(n * m) worst case
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc
                    if (newRow < 0 or newCol < 0 or
                        newRow >= rows or newCol >= cols or
                        grid[newRow][newCol] != 1):
                        continue
                    grid[newRow][newCol] = 2
                    q.append((newRow, newCol))
            time += 1


        # Final pass
        for r in range(rows): # O(n * m)
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return time
        


# Intuition:
# Termination condition is: No rotton oranges next to fresh oranges
# for index in matrix, call BFS if its a rotten cell
# Return time
# Final pass, if there are still fresh ornages, return -1, otherwise return time

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)