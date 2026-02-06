from typing import List
from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # O(1) time
        # If the length of hand is not divisible by groupSize, we return False
        n = len(hand)
        if n % groupSize != 0:
            return False

        # O(n) time
        # Counting the frequency of each number in hand using a dictinoary
        cards = defaultdict(int)
        for card in hand:
            cards[card] += 1

        # O(nlogn) time
        # Verify that all cards form sets of size groupSize
        for card in sorted(cards.keys()):
            if cards[card] > 0:
                count = cards[card]
                for i in range(groupSize):
                    cards[card + i] -= count
                    if cards[card + i] < 0:
                        return False

        return True


# Intuition:
# If the length of hand is not divisible by groupSize, we can return False
# Count the frequency of each number in hand using a dictionary
# Reach through the dictinoary, verifying that the groupSize sets exist and are valid
