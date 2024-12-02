from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # var def
        curChar = chars[0]
        count = 1
        res = ""

        # traverse chars
        for char in chars[1:]:
            if char == curChar:
                count += 1
            else:
                if count == 1:
                    res += curChar
                else:
                    res += curChar + str(count)
                count = 1
                curChar = char
        
        # append ending count & char
        if count == 1:
            res += curChar
        else:
            res += curChar + str(count)

        # result
        for i in range(len(res)):
            chars[i] = res[i]
        
        return len(res)

# Time Complexity: O(n) because we traverse chars one time
# Space Complexity: O(n) because worst case we store every char from chars in res