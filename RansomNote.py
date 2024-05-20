from collections import defaultdict

class Solution:

    # Time Complexity: O(n+m) where n is the length of ransomNote and m is the lenght of magazine
    # Space Complexity: O(1) because there are a limited number of characters that ransomNote and magazine can use
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        # Intuition is to have a hashtable of all magazine and ransome note characters that increments the character by one when it appears in the
        # magazine, and decrement the character when it appears in the ransom note
        # if by the end of the magazine iteration any hashtable value is less than 0, return false

        magazineChars = defaultdict(lambda : 0)

        for i in range(max(len(magazine), len(ransomNote))):
            if i < len(magazine):
                magazineChars[magazine[i]] += 1
            if i < len(ransomNote):
                magazineChars[ransomNote[i]] -= 1

        # Check if magazineChars has any values less than 0
        return all(value >= 0 for value in magazineChars.values())
