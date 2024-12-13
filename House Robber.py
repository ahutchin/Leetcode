from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Case for len(nums) < 3
        if len(nums) < 3:
            return max(nums)

        # var def
        dp = [-1] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        # Traversal
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        # Return
        return dp[-1]

# Start from beginning of array
# first two values in dp are the corresponding values from nums
# starting from 3rd item (index 2) we compare i-1 and i-2 + cur and take the bigger, and that defines the curr max

# Test
test = Solution()
res = test.rob([1,2,3,1])
print(res)