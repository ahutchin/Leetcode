from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = {}
        arr[0], arr[1] = cost[0], cost[1]
        n = len(cost)

        for i in range(2, n):
            arr[i] = cost[i] + min(arr[i - 1], arr[i - 2])
        
        return min(arr[n - 1], arr[n - 2])

# Intuition:
# We use a cache to store the minimum cost to get to step[n], where the minimum cost is cost[n] + min(cost[n-1], cost[n-2])

# Time Complexity: O(n) - We visit each step once
# Space Complexity: O(n) - We store the cost to reach every n step