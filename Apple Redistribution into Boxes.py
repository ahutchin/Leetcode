from typing import List
import heapq


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApples = sum(apple)
        heap = [val * -1 for val in capacity]
        heapq.heapify(heap)
        total, count = 0, 0
        while total < totalApples:
            total -= heapq.heappop(heap)
            count += 1
        return count

# Intuition:
# Assume: that the sum of the apples will fit into the sum of the capacity
# Method:
# We want to count the total number of apples - as the distinct package values do not matter because we can split them
# Then we want to max-heapify capacity, and pop from the heap until the sum of the pops equals/exceeds the total number of apples
# Time Complexity: O(m + n) - building the heap (m) & summing apple (n)
# Space Complexity: O(m) - storing the values of capacity in the heap


apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
Solution().minimumBoxes(apple, capacity)
