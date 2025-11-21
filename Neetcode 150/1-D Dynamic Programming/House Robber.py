from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n > 3:
            money = [0] * n
            money[0] = nums[0]
            money[1] = nums[1]
            money[2] = nums[2] + money[0]

            for i in range(3, n):
                money[i] = nums[i] + max(money[i - 2], money[i - 3])

            return max(money[n - 1], money[n - 2])
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            return max(nums[0] + nums[2], nums[1])
        

# Intuition:
# house[n] compares house[n - 2] and house[n - 3]
# We have an array that stores the money made up to house[n]

# Test
nums = [1,2,3,1]
print(Solution().rob(nums))

# Time Complexity: O(n) visit each index once
# Space Complexity: O(n) store cost in length n arr