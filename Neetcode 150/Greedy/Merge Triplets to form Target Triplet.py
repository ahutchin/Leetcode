from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]
        for triplet in triplets:
            if (triplet[0] <= target[0] and
                triplet[1] <= target[1] and
                    triplet[2] <= target[2]):
                if triplet[0] == target[0]:
                    res[0] = True
                if triplet[1] == target[1]:
                    res[1] = True
                if triplet[2] == target[2]:
                    res[2] = True

        return all(res)


# Intuition:
# Each digit in target (a, b, c) need to be present in atleast one triplet in triplets
# Additionally, for each triplet with a target value, the other two values need to be less than their respective targets
# O(n) Time Complexity
