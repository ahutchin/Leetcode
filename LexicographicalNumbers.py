from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        for i in range(1, 10): # range is inclusive, exclusive
            self.lexicalDFS(i, n, result)

        return result

    def lexicalDFS(self, currentNum: int, limit: int, result: List[int]) -> None:
        if currentNum > limit: return

        result.append(currentNum)

        for i in range(0, 10):
            nextNum = int(str(currentNum) + str(i))
            if nextNum > limit:
                break
            self.lexicalDFS(nextNum, limit, result)

# Test
sol = Solution()
result = sol.lexicalOrder(13)
print(result)

# Ideation:
# 137
# 1, 10, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
#    11, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
#    12, 120

# Work backwards?
# 137, 136, 135, 134, 133, 132, 131, 130, 13, 129, 128 