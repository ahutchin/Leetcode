class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        wordArray = sentence.split(maxsplit=-1)
        for i in range(len(wordArray) - 1):
            if wordArray[i][-1] != wordArray[i + 1][0]: return False

        if wordArray[0][0] != wordArray[-1][-1]: return False

        return True 