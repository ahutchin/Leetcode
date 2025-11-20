from typing import List
from collections import defaultdict

class Solution:
    steps = defaultdict(int)
    steps[1] = 1
    steps[2] = 2

    def climbStairs(self, n: int) -> int:
        if n in Solution.steps:
            return Solution.steps[n]
        Solution.steps[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return Solution.steps[n]


# Intuition:
# When n = ...
# 1 -> 1 way
# 2 -> 2 way
# 3 -> 3 way
# 4 -> 5 way
# 5 -> 8 way
# The trick: climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)

print(Solution().climbStairs(4))

# Time Complexity: O(n)
# Space Complexity: O(n)