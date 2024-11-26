from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # var definition
        numsLen = len(nums)
        curSum = 0
        curMax = 0
        p1 = 0
        p2 = 0

        # Case when k < numsLen
        if k > numsLen:
            return 0
        
        # Read through array
        while p2 < k:
            curSum += nums[p2]
            p2 += 1
        curMax = curSum / k

        while p2 < numsLen:
            curSum = curSum - nums[p1] + nums[p2]
            curMax = max(curMax, curSum / k)
            p1 += 1
            p2 += 1

        return curMax
    
# Test
testcase = Solution()
result = testcase.findMaxAverage([1,12,-5,-6,50,3], 4)

# Time Complexity: O(n) because we visit each element in the list once
# Space Complexity: O(1) because we do not utilize any notable amount of additiona memory