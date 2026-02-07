from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # O(n) time
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1

        # O(n) time
        res = []
        chars = set(s[0])
        count = 0
        for char in s:
            if char not in chars:
                chars.add(char)

            count += 1
            counts[char] -= 1
            if counts[char] == 0:
                chars.remove(char)

            if len(chars) == 0:
                res.append(count)
                count = 0

        return res

# Intuition:
# Count occurances of each char in s
# O(n) Time Complexity
