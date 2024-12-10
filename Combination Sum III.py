from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(build: List[int], cur_num: int, sum_so_far: int):
            # Base Case
            if len(build) == k:
                if sum_so_far == n:
                    res.append(build)
                return
            
            # Recursion
            for i in range(cur_num, 9 + 1):
                if sum_so_far + i > n: break
                backtrack(build + [i], i + 1, sum_so_far + i)

            return
                    
        backtrack([], 1, 0)
        return res


        
# Start from n, and work downwards by trying to achieve zero via subtraction?
# Track the 'used' numbers and number of numbers used