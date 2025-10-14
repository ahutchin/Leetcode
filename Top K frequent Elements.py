from typing import List
from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        frequency = Counter(nums)

        return [num for num, count in frequency.most_common(k)] # nlogn

# Initial Thoughts:
# This problem sounds like I could use some built in data stucture like 'Counter' and grab the most items with highest counts
# Time: O(nlogn)

    def bucketSort(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda: 0)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        for key, value in count.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: 
                    return res


nums = [3,0,1,0]
k = 1
test = Solution()
print(test.topKFrequent(nums, k))