from typing import List
import heapq


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = [val * -1 for val in happiness]
        heapq.heapify(heap)
        turns, sum = 0, 0

        while (turns < k):
            val = (heapq.heappop(heap) * -1) - turns
            if val <= 0:
                break
            sum += val
            turns += 1

        return sum


# intuition:
# Max Heap
