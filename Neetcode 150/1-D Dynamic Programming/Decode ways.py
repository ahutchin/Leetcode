from collections import defaultdict


class Solution:
    def numDecodings(self, s: str) -> int:
        # # Check for validity:
        # n = len(s)
        # prev = s[0]
        # if prev == "0":
        #     return 0

        # for i in range(1, n):
        #     if prev == "0" and s[i] not in "12":
        #         return 0

        # # Determine Decoding ways
        # count = defaultdict(int)

        # for i in range(n - 1):
        #     if s[i] == "1" and s[i + 1] in "123456789":
        #         count["ones"] += 1
        #     elif s[i] == "2" and s[i + 1] in "123456":
        #         count["twos"] += 1

        # return 1 + count["ones"] + count["twos"]
        n = len(s)
        explored = [-1] * n

        def dfs(i):
            # If the character at index i is valid, continue dfs on index 'i + 1'
            nonlocal n

            if i >= n:
                return 1

            if explored[i] != -1:
                return explored[i]

            if s[i] == "0":
                explored[i] = 0
                return 0

            if (i + 1 < n and
                    (
                        s[i] == "1" and s[i + 1] in "0123456789" or
                        s[i] == "2" and s[i + 1] in "0123456")
                ):
                res = dfs(i + 1) + dfs(i + 2)
                explored[i] = res
                return res

            res = dfs(i + 1)
            explored[i] = res
            return res

        return dfs(0)


# Intuition:
# Not sure how this is DP
# What matters here is:
#   how many 1s followed by 0-9s there are
#   how many 2s followed by 0-6s there are
# As each instance of these will increase the ways we can interperent the code
# Things to look out for:
#   0s after any number 3-9
#   string starting with 0

# Approach problem as a Decision Tree - When traversing s, we can evaluate the current 'code' as either 1 or 2 digits
# if the 1 digit code is valid, continue down that branch, if the 2 digit code is valid, continue down that branch as well

# Time Complexity: O(n)
# Space Complexity: O(n)
