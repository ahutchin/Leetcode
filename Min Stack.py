from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minTracker = deque()    

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minTracker) == 0 or self.minTracker[-1] >= val:
            self.minTracker.append(val)

    def pop(self) -> None:
        if (self.stack[-1] == self.minTracker[-1]):
            self.minTracker.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minTracker[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()