from typing import List
import collections

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # var def
        rows = len(maze)
        columns = len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # bfs
        queue = collections.deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set([(entrance[0], entrance[1])])
        while queue:
            row, column, steps = queue.popleft()

            # Check if we are at an exit
            if (row == 0 or row == rows - 1 or column == 0 or column == columns - 1) and (row != entrance[0] or column != entrance[1]):
                return steps

            for dr, dc in directions:
                new_row, new_col = row + dr, column + dc

                # confirms new row and column are within bounds of maze
                if 0 <= new_row < rows and 0 <= new_col < columns and maze[new_row][new_col] == "." and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, steps + 1))
                    visited.add((new_row, new_col))

        # If no exit is reachable
        return -1
    
# Time complexity: O(n * m) because we visit every node
# Space complexity: O(1) because we dont use additional space