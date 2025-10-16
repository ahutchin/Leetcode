from collections import defaultdict
import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A count of each char in s1
        s1chars = set(s1)
        s1Count = defaultdict(lambda: 0)
        for char in s1:
            s1Count[char] += 1

        
        s2Count = copy.deepcopy(s1Count)
        start = 0
        end = 0
        while end < len(s2):
            # if the s2[end] is not in s1: 
            # move both end and start pointers over & reset the default dict counter
            if s2[end] not in s1chars:
                end += 1
                start = end
                s2Count = copy.deepcopy(s1Count)
                
            # if s2[end] is in s1:
                # increment the specified count in default dict
                # if it goes negative: 
                # we need to push the start pointer over until we can make that specific character no longer in the negative, while incrementing up the other ones
                # if not negative and the window size equals the len(s1): return true
            elif s2[end] in s1chars:
                s2Count[s2[end]] -= 1
                if s2Count[s2[end]] < 0:
                    while s2[start] != s2[end]:
                        s2Count[s2[start]] += 1
                        start += 1
                    s2Count[s2[start]] += 1
                    start += 1
                elif len(s1) == (end - start + 1):
                    return True
                end += 1        
        return False

        

    
# Intuition:
# Use a dictionary to store s1's characters & their counts
# We know we found a match when 'end - start + 1' == len(s1)

s1 = 'abbe'
s2 = 'oabbbea'

test = Solution()
print(test.checkInclusion("a", "ab"))

# Time complexity: O(n*m) where n is len s2, m is len s1
# Space complexity: O(m) storing s1