from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas, totalCost = sum(gas), sum(cost)
        if totalCost > totalGas:
            return -1

        curGas, res = 0, 0
        for i in range(len(gas)):
            curGas += gas[i]
            curGas -= cost[i]
            if curGas < 0:
                curGas = 0
                res = i + 1

        return res

# Intuition:
# Hint - Greedy Algorithm, Can be done with O(n) time & O(1) space
# Brute Force would be to see if we can complete the circular route starting from every index until we succeed or fail. This yields an O(n^2) time complexity.

# We are able to determine if the circuit can be completed based on the total available gas in the circuit.
# Iterate through the gas & cost lists while tracking the current gas by adding and subtracting gas & cost, if it is negative, reset the gas amount and mark the next index as the result index
