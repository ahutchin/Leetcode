class Solution:
    def reverseVowels(self, s: str) -> str:
        # Var definition
        s = list(s)
        p1, p2 = 0, len(s) - 1

        # 2ptr traversal
        while p1 < p2:
            if (s[p1] in "aeiouAIEOU") and (s[p2] in "aeiouAIEOU"):
                temp = s[p1]
                s[p1] = s[p2]
                s[p2] = temp
                p1 += 1
                p2 -= 1
            elif (s[p1] not in "aeiouAIEOU" and s[p2] not in "aeiouAIEOU"):
                p1 += 1
                p2 -= 1
            elif (s[p1] not in "aeiouAIEOU"):
                p1 += 1
            elif (s[p2] not in "aeiouAIEOU"):
                p2 -= 1
        
        # return
        return ''.join(s)