from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = max(nums)
        currMin = currMax = 1

        for num in nums:
            tmp = currMax * num
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp, currMin * num, num)
            globalMax = max(globalMax, currMax)

        return globalMax


# Intuition
# Given that this is a DP problem, probably want to use a cache where cache[i] is the largest product up to nums[i]
# The only information really to focus on is whether the num is positive, negative, or 0
# This also feels like 2 pointer

# Kadane's Algorithm:
# While traversing the array, track the following: (maximumSoFar, minimumSoFar), this way when we look at the next index, regardless of if that index is positive or negative, we can find what value it yields
# Additionally, track the global maximum

print(Solution().maxProduct([-2, 0, -1]))
