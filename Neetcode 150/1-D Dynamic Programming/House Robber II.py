from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        cost1 = [0] * (n)
        cost2 = [0] * (n)
        cost1[0] = nums[0]
        cost1[1] = cost2[1] = nums[1]
        cost2[2] = nums[2]

        for i in range(2, n - 1):
            cost1[i] = nums[i] + max(cost1[i - 2], cost1[i - 3])
            cost2[i + 1] = nums[i + 1] + max(cost2[i - 1], cost2[i - 2])
        
        return max(cost1[n - 2], cost1[n - 3], cost2[n - 1], cost2[n - 2])

# Intuition:
# Same as House Robber 1, but leave last index out of traversal

# Test:
print(Solution().rob([200,3,140,20,10]))

# Time & Space Complexity: O(n)