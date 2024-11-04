from collections import Counter, defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Var definition
        word1Len = len(word1)
        word2Len = len(word2)
        word1Dict = defaultdict(int)
        word2Dict = defaultdict(int)

        # Case for different word lengths
        if word1Len != word2Len:
            return False
        
        # Check that words share same chars & that words share same counts of chars
        word1Values = []
        word2Values = []
        for i in range(word1Len):
            word1Dict[word1[i]] += 1
            word2Dict[word2[i]] += 1
        for key in word1Dict:
            word1Values.append(word1Dict[key])
            if key not in word2Dict:
                return False
        for key in word2Dict:
            word2Values.append(word2Dict[key])
            if key not in word1Dict:
                return False
        if Counter(word1Values) != Counter(word2Values):
            return False
        
        # ALTERNATIVE IMPLEMENTATION USING .keys() & .values() METHOD
        # if (word1Dict.keys() != word2Dict.keys()):
        #     return False
        # if set(word1Dict.values()) != set(word2Dict.values()):
        #     return False

        return True

        
        
# Requirements for word1 close to word2
# 1. word1 & word2 are same length
# 2. word1 & word2 have same letters present
# 3. word1 & word2 have same counts present

# Testing
word1 = "aaabbbbccddeeeeefffff"
word2 = "aaaaabbcccdddeeeeffff"

test = Solution()
result = test.closeStrings(word1, word2)
print(result)