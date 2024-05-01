class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        output = ""

        for i in range(len(word)):
            output += word[i]
            if word[i] == ch:
                output = output[::-1] + word[i + 1:]
                break
        
        return output