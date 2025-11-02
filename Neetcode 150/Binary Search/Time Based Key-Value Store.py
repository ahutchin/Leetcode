from collections import defaultdict
from typing import List

class TimeMap:

    # O(1) time
    def __init__(self): 
        self.dict = defaultdict(lambda: [])

    # O(1) time, appending to list is constant time
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    # O(logn) time, searching for target value uses binary search
    def get(self, key: str, timestamp: int) -> str:
        return self.binarySearch(self.dict[key], timestamp)

    def binarySearch(self, array: List[tuple], timestamp: int) -> str:
        if not array or timestamp < array[0][0]:
            return ""
        
        l = 0
        r = len(array) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if timestamp == array[mid][0]:
                return array[mid][1]
            
            if timestamp > array[mid][0]:
                l = mid
            elif timestamp < array[mid][0]:
                r = mid - 1
        
        return array[l][1]
            

# [(1, "foo"), (3, "foo"), (4, "foo"), (7, "foo"), (8, "foo"), (11, "foo"), ]
# [(10, "high"), (20, low)]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Intuition:
# When locating a value for key at time x, we will binary search for that time, and return the value at that time, or nearest time less than that time
# Use a dictionary for each key, value pair
# The value is a list of tuples (time, value)

# Time Complexity: constructor and setter are constant time, getter is O(logn) time
# Space Complexity: O(n * m)

# Test
timeMap = TimeMap()
timeMap.set("a","bar",1)
timeMap.set("x","b",3)
timeMap.get("b",3)
timeMap.set("foo","bar2",4)
timeMap.get("foo",4)
timeMap.get("foo",5)