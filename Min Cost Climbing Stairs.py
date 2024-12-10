from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Base
        if len(cost) < 2:
            return min(cost[0], cost[1])
        
        # Setup
        dp = [0] * len(cost)
        dp[-1], dp[-2] = cost[-1], cost[-2]

        # Cost traversal
        for i in range(len(cost) - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])
# Is there a way to do this without having to explore every route
# Start from final floor and take eitehr 1 or 2 steps backwards until 
# DP?

# Test
test = Solution()
res = test.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
print(res)