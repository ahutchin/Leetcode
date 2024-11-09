class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        wordList.reverse()
        return " ".join(wordList)

# Time complexity: O(n) because each operation is O(n) time