from typing import List
import heapq

class Solution:
    # O(n + n + klogn + n + n + n(logn + logn + logn)) ~ O(nlogn)
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int: 
        # var def
        curSum = 0
        curRes = 0
        curMax = 0
        nums1Max = {}

        # Build nums1 max heap
        nums1 = [[-x, i] for i, x in enumerate(nums1)] # O(n)
        heapq.heapify(nums1) # O(n)
        for _ in range(k): # O(klogn)
            val, i = heapq.heappop(nums1)
            curSum += val * -1
            nums1Max[i] = val * -1

        # Build nums2 minheap
        nums2heap = [[nums2[key], key] for key in nums1Max] # O(n)
        heapq.heapify(nums2heap) # O(n)

        curMax = curSum * nums2heap[0][0]

        # Test every item in nums1
        while nums1: # O(n)
            _, index = heapq.heappop(nums2heap) # O(logn)
            curSum -= nums1Max[index]
            val, index = heapq.heappop(nums1) # O(logn)
            nums1Max[index] = val * -1
            curSum += val * -1
            heapq.heappush(nums2heap, [nums2[index], index]) # O(logn)

            curRes = curSum * nums2heap[0][0]
            if curRes > curMax:
                curMax = curRes

        return curMax
    
    def maxScorev2(self, nums1: List[int], nums2: List[int], k: int) -> int: # Chatgpt optimized
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1]) # O(nlogn)

        curSum = 0
        maxSum = 0
        minHeap = []

        for num1, num2 in pairs: # O(n(logn + logn))
            heapq.heappush(minHeap, num1)
            curSum += num1

            if len(minHeap) > k:
                curSum -= heapq.heappop(minHeap)

            if len(minHeap) == k:
                maxSum = max(maxSum, curSum * num2)

        return maxSum