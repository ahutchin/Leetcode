from typing import DefaultDict

class Solution:
    # Time Complexity: O(n) because we do 1 operation for each value of n
    # Space Complexity: O(n) beacuse each key value pair for n will have associated memory
    def climbStairs(self, n: int) -> int:
        # Intuition is that this is an math algorithm problem:
        # This feels like a one line solution
        # Lets write out the first few solutions for n and see if theres a pattern:
        # n = 1, result: 1 step: 1
        # n = 2, result: 2 step, 1 step + 1 step: 2
        # n = 3, result: 1 + 1 + 1, 1 + 2, 2 + 1: 3
        # n = 4, result: 1+1+1+1, 1+2+1, 1+1+2, 2+1+1, 2+2: 5
        # n = 5, result: 1+1+1+1+1, 1+1+1+2, 2+1+1+1, 1+2+2, 2+2+1, 2+1+2, 1+2+1+1, 1+1+2+1: 8
        # the pattern is s_n = s_(n-1) + s_(n-2)

        if n == 1: return 1
        elif n == 2: return 2

        hashtable = DefaultDict(lambda : 0)
        hashtable[1] = 1
        hashtable[2] = 2

        for i in range(3, n + 1):
            hashtable[i] = hashtable[i-1] + hashtable[i-2]

        return hashtable[n]