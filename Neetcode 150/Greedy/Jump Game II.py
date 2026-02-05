from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     cache = [float("inf")] * n
    #     cache[n - 1] = 0

    #     for i in range(n - 2, -1, -1):
    #         jump = nums[i]
    #         for j in range(i + 1, min(i + jump + 1, n)):
    #             cache[i] = min(cache[i], 1 + cache[j])

    #     return cache[0]

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        count = 0

        while r < n - 1:
            next = 0
            for i in range(l, r + 1):
                next = max(next, i + nums[i])

            l = r + 1
            r = next
            count += 1

        return count

# Intuition:
# Work backwards from the final index, storing the minimum number of steps to reach the final index in a cache where
# cache[i] = minimum number of steps to reach final index
# O(n^2) Time worst case

# We use 2 pointers, these pointers define the range of reachable indices,
# We iterate through every num in the range to find the new max furthest reachable index
# then update the range to


test = Solution()
print(test.jump([2, 3, 0, 1, 4]))
