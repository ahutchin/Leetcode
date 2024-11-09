from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currHeight = 0
        maxHeight = 0

        for height in gain:
            currHeight += height
            if currHeight > maxHeight:
                maxHeight = currHeight

        return maxHeight