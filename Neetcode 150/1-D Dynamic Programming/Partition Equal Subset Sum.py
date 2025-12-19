from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2

        memo = {}

        def DFS(sum: int, i: int):
            if sum == target:
                return True
            if sum > target:
                return

            state = (sum, i)
            if state in memo:
                return memo[state]

            nonlocal n
            for j in range(i, n):
                if DFS(sum + nums[j], j + 1):
                    return True

        return True if DFS(0, 0) else False

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False


# Intuition:
# This problem can be visualized with a tree in which for every element we have the option to add or not add it to the outcome list
# Time Complexity: O(2^n)

print(Solution().canPartition([1, 2, 5]))
