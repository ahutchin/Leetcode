from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]: # Initial Solution
        # Base Case
        if len(digits) == 0:
            return []
        
        # For each digit in digits we want to perform some operation
        res = [""]
        digitDict = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        for digit in digits: # O(n)
            new_res = []
            for combo in res: # O(3^n), worst case O(4^n)
                for char in digitDict[digit]: # O(3) or O(4) ~ O(1)
                    new_res.append(combo + char)
            res = new_res
        
        return res # Time Complexity: O(n(4^n))
    
    def letterCombinationsv2(self, digits: str) -> List[str]: # Backtracking implementation
        if digits == "":
            return []
        
        res = []
        digitDict = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

        def backtrack(i: int, curStr: str): # Key params are the current index and the current string (the object being operated on)
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for char in digitDict[digits[i]]:
                backtrack(i + 1, curStr + char)
        
        backtrack(0, "")
        return res
            


# Test
test = Solution()
result = test.letterCombinations("23")
print(result)