from collections import deque

class RecentCounter:

    def __init__(self):
        self.pings = deque([])

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while len(self.pings) > 0 and self.pings[0] < t - 3000:
            self.pings.popleft()

        return len(self.pings)
    
# O(n) time complexity: worst case when popping elements we pop all elements in a single function call
# O(n) space complexity: worst case all elements that have been added to the queue are saved in memory