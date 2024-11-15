from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # var definition
        curCount = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0: 
                return 1 >= n
            else:
                return 0 >= n

        # read through flowerbed, incrementing curCount when a flower can be placed
        # 1st element:
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            curCount += 1
            if curCount >= n:
                return True
        
        # Middle elements:
        for i in range(1, len(flowerbed) - 1):
            if (flowerbed[i] == 0) and (flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                curCount += 1
                if curCount >= n:
                    return True
        
        # Last element:
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            curCount += 1
            if curCount >= n:
                return True

        # return
        return curCount >= n
    
# Test
test = Solution()
result = test.canPlaceFlowers([0,0,0,0,1], 2)
print(result)

# O(n) time, O(1) space