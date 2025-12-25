from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n, m = len(mat), len(mat[0])

        # Identify 0s:
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))

        # Update mat
        while queue:
            for _ in range(len(queue)):
                row, col, distance = queue.popleft()
                if (row, col) in visited:
                    continue

                mat[row][col] = distance
                visited.add((row, col))
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if (newRow < 0 or newRow >= n or
                        newCol < 0 or newCol >= m or
                            (newRow, newCol) in visited):
                        continue
                    queue.append((newRow, newCol, distance + 1))

        return mat

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        queue = deque()

        # Identify 0s and mark 1s as unvisited (-1)
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < n and 0 <= newCol < m and mat[newRow][newCol] == -1:
                    mat[newRow][newCol] = mat[row][col] + 1
                    queue.append((newRow, newCol))

        return mat

# Intuition:
# This problem is very similar to rotton oranges
# Method:
# Use BFS starting from every 0 node, expanding outward to determine distance from 0s
# Modify in place, use a set to track visited indices in the matrix
# use a queue to contain
# Time Complexity: O(n * m) we visit each node twice
# Space Complexity: O(n * m) worst case, our queue stores every single value in mat
