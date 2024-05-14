from typing import List


class Solution:
    # Time Complexity: O(logn) 
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while (low < high):
            mid = low + ((high - low + 1) // 2)
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid

        return low if nums[low] == target else -1
    
# Test
solution = Solution()

nums = [-1,0,3,5,9,12]
target = 9

result = solution.search(nums, target)
print(result)