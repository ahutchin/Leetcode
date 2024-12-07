import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.heap = [1]
        heapq.heapify(self.heap)
        self.removed = set()

    def popSmallest(self) -> int:
        # If there is 1 item in the heap
        # perform heappushpop with the next smallest item
        # If there is more than 1 item in the heap
        # perform heappop
        if len(self.heap) == 1:
            smallest = self.heap[0]
            nextSmallest = smallest + 1
            while nextSmallest in self.removed:
                nextSmallest = nextSmallest + 1
            res = heapq.heappushpop(self.heap, nextSmallest)
        else:
            res = heapq.heappop(self.heap)
        # add the result of heappop to the removed set
        self.removed.add(res)
        return res

    def addBack(self, num: int) -> None:
        # perform heappush with the addedBack number
        # remove it from the removed set
        if num in self.removed:
            heapq.heappush(self.heap, num)
            self.removed.remove(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
smallestInfiniteSet = SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    
smallestInfiniteSet.popSmallest(); 
smallestInfiniteSet.popSmallest(); 
smallestInfiniteSet.popSmallest(); 
smallestInfiniteSet.addBack(1);    
smallestInfiniteSet.popSmallest(); 
smallestInfiniteSet.popSmallest(); 
smallestInfiniteSet.popSmallest(); 

# Time Complexity: contructor is O(1), popSmallest is O(logn) due to heappush, addBack is O(1)
# Space Complexity: O(m) where m is the number of elements added