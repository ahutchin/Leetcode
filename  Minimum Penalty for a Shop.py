class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        counts = [0] * (n + 1)

        noCustomerPenalty = 0
        for i in range(n + 1):
            counts[i] += noCustomerPenalty
            if i < n and customers[i] == 'N':
                noCustomerPenalty += 1

        closedShopPenalty = 0
        res = [counts[n], n]
        for i in range(n, -1, -1):
            counts[i] += closedShopPenalty
            if counts[i] <= res[0]:
                res = [counts[i], i]
            if i > 0 and customers[i - 1] == 'Y':
                closedShopPenalty += 1

        return res[1]

# Intuition
# construct a list of length n where each index indicates the penalty of closing the store at index i
# Two pass, first pass in order to count the number of instances of no customers
# second pass to count number of instances of store open, going in reverse order
# storing minimum number and minimum index

# Time complexity: O(2n) for 2 pass
# Space complexity: O(n) for the list
