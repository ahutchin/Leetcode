from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            euclidianDistance = point[0]**2 + point[1]**2
            minHeap.append([euclidianDistance, point])
        heapq.heapify(minHeap)
        result = []
        while k > 0:
            euclidianDistance, point = heapq.heappop(minHeap)
            result.append(point)
            k -= 1
        return result
    
# Test
res = Solution()
res.kClosest([[3,3],[5,-1],[-2,4]], 2)