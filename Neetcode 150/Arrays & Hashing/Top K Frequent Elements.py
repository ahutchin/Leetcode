from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        heap = [(-freq, num) for num, freq in frequency.items()]
        heapq.heapify(heap)
        # return [heapq.heappop(heap)[1] for _ in range(k)]

        res = []
        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
        
        return res
    
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num frequency count
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        arr = [(freq, num) for num, freq in frequency.items()]
        arr.sort(reverse=True)

        return [num for freq, num in arr[:k]]

# Intuition:
# 1:
#   1st pass counts frequency of each num in nums -- O(n)
#   Use a Heap of size k -- O(n)
#   return top k elements from the heap -- O(klogn)
# 2: 
#   1st pass counts frequency of each num in nums -- O(n)
#   Sort the frequency array -- worst case O(nlogn)
#   return top k entries -- O(1)