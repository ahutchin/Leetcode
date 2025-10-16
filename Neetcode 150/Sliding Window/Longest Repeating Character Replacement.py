from collections import Counter, defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int: ### FAILED APPROACH FUNDAMENTALLY ###
        curChar = Counter(s).most_common(1)[0][0] # O(2n) time
        maxCount = 1
        
        start = 0
        end = 0
        count = 0
        while end < len(s):
            if s[end] == curChar:
                count += 1
                end += 1
            elif s[end] != curChar and k > 0:
                k -= 1
                count += 1
                end += 1
            elif s[end] != curChar and k == 0:
                while s[start] == curChar:
                    start += 1
                    count -= 1
                start += 1
                end += 1
            if count > maxCount:
                maxCount = count

        return maxCount
    
    def characterReplacement2(self, s: str, k: int) -> int:
        count = defaultdict(lambda: 0)
        maxCount = 1
        maxLength = 1

        start = 0
        for end in range(len(s)):
            count[s[end]] += 1

            maxCount = max(maxCount, count[s[end]])

            windowSize = end - start + 1

            if windowSize - maxCount > k:
                count[s[start]] -= 1
                start += 1
            
            maxLength = max(end - start + 1, maxLength)
        
        return maxLength

            

# Intuition
# traverse along the string, when running into a non-current char, decrement k and shift over 1
# if hyou hit a situation where k is zero, move the left pointer until you hit the non char letter and increment continue shifting

# Optimal Sol:
# fundamental strat is this: windowSize - maxFrequency <= k
# as long as that holds true, the window is valid

test = Solution()
print(test.characterReplacement2("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 2))