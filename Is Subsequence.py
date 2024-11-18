class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        sIndex = 0
        tIndex = 0

        if sLen > tLen:
            return False
        if sLen == 0:
            return True

        while tIndex < tLen:
            if s[sIndex] == t[tIndex]:
                sIndex += 1
            tIndex += 1

            if sIndex == sLen:
                return True
            
        return False
