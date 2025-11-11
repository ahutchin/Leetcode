from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordLen = len(word)
        n = len(board)
        m = len(board[0])
        path = set()

        def dfs(wordIndex: int, i: int, j: int) -> bool:
            if wordIndex == wordLen:
                return True
            
            if (i < 0 or j < 0 or 
                i >= n or j >= m or
                board[i][j] != word[wordIndex] or 
                (i, j) in path):
                return False
            
            path.add((i, j))
            R = dfs(wordIndex + 1, i, j + 1) # Right neighbor
            L = dfs(wordIndex + 1, i , j - 1) # Left neighbor
            T = dfs(wordIndex + 1, i - 1, j) # Top neighbor
            B = dfs(wordIndex + 1, i + 1, j) # Bottom neighbor
            path.remove((i,j))

            return R or L or T or B
        
        for r in range(n):
            for c in range(m):
                if dfs(0, r, c): return True
        return False
            
            
# Intuition:
# Brute force 

# Time Complexity: O(n * m * 4^(w)) where n, m is rows, columns of board and w is word length
# Space Complexity: O(n * m)