import bisect
from typing import List
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]: # Manual BS
        # var def
        res = []

        # setup
        potions.sort() # O(mlogm) sort in place
        
        # find the spell potion combo where the current combo fails, but the combo one after succeeds, if there are none, it means all succeed
        for spell in spells:
            minPotion = math.ceil(success/spell)

            # BS
            lower = 0
            upper = len(potions) - 1
            while lower <= upper:
                mid = (lower + upper) // 2
                if potions[mid] < minPotion:
                    lower = mid + 1
                else:
                    upper = mid - 1
            res.append(len(potions) - lower)
        
        # return
        return res
    

    def successfulPairsv2(self, spells: List[int], potions: List[int], success: int) -> List[int]: # GPT Revised using bisect
        res = []
        potions.sort()

        for spell in spells:
            minPotion = math.ceil(success/spell)
            index = bisect.bisect_left(potions, minPotion)
            res.append(len(potions) - index)
        
        return res
    
            
# Sort potions: O(mlogm)
# Use BS to find turning point for Spell potion combo for all potions: O(nlogn)

# Time Complexity: O(mlogm + nlogn)
# Space Complexity: O(1) we dont add anything to memory