from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        n = len(s)

        def dfs(i) -> None:
            if i >= n:
                res.append(part[:])
                return 
            
            for j in range(i, n):
                partition = s[i:j + 1]
                if self.palindrome(partition):
                    part.append(partition)
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res
        


    def palindrome(self, s: str) -> bool: # O(n) time complexity
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

# Intuition:
# s = "racecar"
# Before every index, we have the choice to partition there or not
# Brute force -> Check every possible split

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)