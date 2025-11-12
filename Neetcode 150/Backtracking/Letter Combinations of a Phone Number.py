from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        n = len(digits)
        res = []

        def dfs(curr: str, i: int) -> None:
            if i == n:
                res.append(curr)
                return
            
            for letter in letters[digits[i]]:
                dfs(curr + letter, i + 1)
            
            return

        dfs("", 0)
        return res

# Intuition:
# Hashmap to store {numbers: letters} mapping
# DFS going through each digit

# Time Complexity: O(n * 4^n)
# Space Complexity: O(n)