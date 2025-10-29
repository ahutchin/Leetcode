from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif target < val:
                r = mid - 1
            elif target > val:
                l = mid + 1

        return -1

sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(sol.search(nums, target))