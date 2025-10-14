from typing import List
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Define result List
        result = []

        # Create a Counter for each string in strs
        while strs:
            current = strs[0]
            res = [] # store anagrams for this iteration

            res.append(current)
            strs.remove(current)

            for i in range(len(strs) - 1, -1, -1):  # Go backwards
                if Counter(current) == Counter(strs[i]):
                    res.append(strs[i])
                    strs.remove(strs[i])
            
            # Add to result
            result.append(res)

        # return
        return result
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # dict to keep count of anagrams
        anagrams = defaultdict(list)
        
        for word in strs: # O(n) runtime
            word_to_list = sorted(word) # O(klogk) runtime where in is the length of the word
            key = ''.join(word_to_list) # Create key for anagrams dict
            anagrams[key].append(word) # append the word to the anagram key
        
        return list(anagrams.values())


    
# Initial Thoughts:
# Compare strs[0] to all remaining str, 
# pop all of those that match out of strs and add them to a List inside the result list
# Continue this with the remaining strings in strs
# How do we want to store their data
# Complexity: O(n^2 * k), where n is num of strings, k is longest string -> Time limit exceeded

test = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
# result = test.groupAnagrams(strs)


for word in strs:
    print(word, 'join sorted: ', ''.join(sorted(word)))

