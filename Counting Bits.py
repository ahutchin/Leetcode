from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            if i % 2 == 1:
                count = res[i // 2] + 1
            else:
                count = res[i // 2]
            res.append(count)

        return res

# 0: 0 -> 0
# 1: 1 -> 1
# 2: 10 -> 1
# 3: 11 -> 2
# 4: 100 -> 1
# 5: 101 -> 2
# 6: 110 -> 2
# 7: 111 -> 3
# 8: 1000 -> 1
# 9: 1001 -> 2
# 10: 1010 -> 2
# 11: 1011 -> 3
# 12: 1100 -> 2
# 13: 1101 -> 3
# 14: 1110 -> 3
# 15: 1111-> 4