from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def DFS(row: int, col: int) -> None:
            if (row < 0 or col < 0 or
                row >= rows or col >= cols or
                board[row][col] == "X" or
                board[row][col] == "#"):
                return
            board[row][col] = "#"

            for dr, dc in directions:
                DFS(row + dr, col + dc)

        for r in range(rows):
            DFS(r, 0)
            DFS(r, cols - 1)
        
        for c in range(1, cols - 1):
            DFS(0, c)
            DFS(rows - 1, c)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board [i][j] = "O"
        
# Intuition:
# For every 'O' on the edge of the board, DFS and remark as '#'
# Traverse board at the end, changing 'O' to 'X' and '#' to 'O'

# Time Complexity: O(n * m) We visit each index 2 times
# Space Complexity: O(n * m) Worst case our recursion stack covers the entire board