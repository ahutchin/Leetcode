from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Traversal
        for i in range(len(numbers) - 1):
            curNum = numbers[i]
            complement = target - curNum
            # Binary search for complement
            j = self.binarySearch(numbers[i + 1:], complement)
            if j != -1:
                return [i + 1, (i + 1) + j + 1]

    def binarySearch(self, arr: List[int], target: int) -> int:
        start = 0
        stop = len(arr) - 1

        while start <= stop:
            mid = start + ((stop - start) // 2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                stop = mid - 1
        
        return -1
    
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            elif numbers[start] + numbers[end] > target:
                end -= 1
        
        return []


# Intuition:
# Left to right traversal, for each number, search for its complement
# Time complexity: O(nlogn) logn operations (binary search) for each element in numbers (n)
# Space complexity: O(1) does not use up additional space

# Optimal Sol:
# Use two pointers starting from either end, check if their sum exceeds or is less than the target, increment the appropriate pointer based on this