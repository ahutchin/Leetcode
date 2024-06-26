from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(1 + dp[a-c], dp[a])
        return dp[amount] if dp[amount] != amount + 1 else -1

    def coinChangev1(self, coins: List[int], amount: int) -> int:
        coins.sort()
        totalCount = 0
        for i in range(len(coins) - 1, -1, -1):
            coinCount = amount // coins[i]
            totalCount += coinCount
            amount -= coinCount * coins[i]
            if amount == 0:
                return totalCount
        return -1

# Test Case
solution = Solution()

coins = [186,419,83,408]
amount = 6249

result = solution.coinChange(coins, amount)
print(result)