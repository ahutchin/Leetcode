from typing import List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # cache = [-1] * (amount + 1)
        # n = len(coins)

        # def DFS(i: int, sum: int, depth: int) -> int:
        #     # We've exceeded the target
        #     if sum > amount:
        #         return

        #     # Pruning branches we have already explored more optimally
        #     if 0 < cache[sum] < depth:
        #         return

        #     # Update cache
        #     cache[sum] = depth

        #     # We've reached the target amount
        #     if sum == amount:
        #         return

        #     # Explore remaining branches
        #     for j in range(len(coins[i:])):
        #         DFS(i + j, sum + coins[i + j], depth + 1)

        # DFS(0, 0, 0)
        # return cache[amount]

        visited = set()
        q = deque([(0, 0, 0)])
        while q:
            for _ in range(len(q)):
                idx, sum, depth = q.popleft()
                if (sum > amount or
                        sum in visited):
                    continue
                if sum == amount:
                    return depth
                visited.add(sum)
                for j in range(len(coins[idx:])):
                    q.append((idx + j, sum + coins[idx + j], depth + 1))

        return -1


# Intuition:
# Use cache of length amount where amount[i] equals the minimum number of coins it takes to make i
# Potentially work backwards from the amount

# BFS with a cache

# Time Complexity: O(amount * len(coins)) the depth of our graph is worst case equal to amount, and for each ;eve; we iterate through all coins giving us len(coins) * amount
# Space Complexity: O(amount) worst case our set can store every value from 0 to amount
