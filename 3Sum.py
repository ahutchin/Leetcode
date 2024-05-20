from typing import List

# Intuition is to brute force starting at index 0 and finding every combination of numbers that sum to 0
class Solution:
    # Time complexity: O(n) + O(n) + O(n^2) + O(n^2) = O(n^2)
    # Space complexity: O(n) because we use additional storage for each num in nums
    # I really like this solution because it breaks the problem down into several subproblems (cases) and handles each one independently
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        # Split nums into negative, zeros, and positives lists
        positives, zeros, negatives = [], [], []

        # Iterate through nums: 
        for num in nums: # O(n) run time
            if num > 0: 
                # Add to positive list
                positives.append(num)
            elif num < 0:
                # Add to negative list
                negatives.append(num)
            else: 
                # Add to zero list
                zeros.append(num)

        # Create sets for positive and negative lists for O(1) look-up
        positivesSet = set(positives)
        negativesSet = set(negatives)

        # Handle each case independently:
        # 3 Zeros Case
        if len(zeros) >= 3: # O(1) run time
            result.add((0, 0, 0))

        # 1 Zero Case
        if len(zeros) >= 1: # O(n) run time because O(1) look-up time for sets
            for num in positivesSet:
                if -1 * num in negativesSet:
                    result.add((-1 * num, 0, num))

        # Negative Pair complement Case
        for i in range(len(negatives)): # O(n^2) run time
            for j in range(i + 1, len(negatives)):
                target = -1 * (negatives[i] + negatives[j])
                if target in positivesSet:
                    result.add(tuple(sorted([negatives[i], negatives[j], target])))

        # Positive Pair complement Case
        for i in range(len(positives)): # O(n^2) run time
            for j in range(i + 1, len(positives)):
                target = -1 * (positives[i] + positives[j])
                if target in negativesSet:
                    result.add(tuple(sorted([positives[i], positives[j], target])))

        # Return
        return result