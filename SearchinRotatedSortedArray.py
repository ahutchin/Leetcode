from typing import List

# Intuition: somehow need to utilize that the array is sorted & rotated to produce log(n) search time
# We could split this problem into 2 parts: 
# 1. fix the rotated list
# 2. search for the target value
# Alternatively there may be a search algorithm that performs fine without needing the resort
# Step 1: Find the index where the nums[i] > nums[i+1]
# Step 2: rebuild array as newArray = nums[i+1:] + nums[0:i+1]
# Step 3: Search for target value using binary search (log(n) time)
class Solution:
    # Time complexity: O(log(n)) because its binary search
    # Space complexity: O(1) because we use no additional space
    def search(self, nums: List[int], target: int) -> int:
        # We do a binary search, but break down the cases much more particularly

        # Define left, right
        left, right = 0, len(nums) - 1

        # Iterate while left <= right to cover len(nums) = 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target: return mid

            # Determine which half of nums is sorted
            if nums[left] <= nums[mid]: # Left-half sorted
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[left]: # Right-half sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Return
        return -1
    
# Test Case
solution = Solution()

nums = [4,5,6,7,0,1,2]
target = 0

result = solution.search(nums, target)
print(result)