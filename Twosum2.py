from typing import List

# Intuition is to utilize the sorted array to reduce time complexity from O(n) to O(logn)
# We could solve this with a hashmap or 2 pointers


class Solution:
    # Time Complexity: O(n) 
    # Space Complexity: O(1)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Idea with 2 pointers is that we have a left and right pointer
        l, r = 0, len(numbers) - 1

        # Then we read through numbers and increment the left or right pointer depending on how close the sum of l and r is to the target value
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            else:
                r -= 1
            