from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

# Intuition:
# find largest increasing subsequence starting from each index in nums
# Use a cache of length n, where cache[i] = longest increasing subsequence starting at index i
# If we start from the end of nums,
# Time Complexity: O(n^2) for each num we visit the entire list


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
