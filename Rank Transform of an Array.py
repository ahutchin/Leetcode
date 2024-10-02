from typing import List

class Solution: # Daily for 10/2/2024
    def arrayRankTransform(self, arr: List[int]) -> List[int]: 
        sortedArr = sorted(arr)
        hashmap = {}
        rank = 1
        for el in sortedArr:
            if el not in hashmap:
                hashmap[el] = rank
                rank += 1
        
        for i in range(len(arr)):
            arr[i] = hashmap.get(arr[i])

        return arr