from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = defaultdict(int)

        for num in arr: # O(n) time
            occurences[num] += 1
        
        # grab values from occurences, and turn them into a set
        return len(set(occurences.values())) == len(occurences)

# O(n) time: because of list traversal
# O(n) space: because we store everything in a set