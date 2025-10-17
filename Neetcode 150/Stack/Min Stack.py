from collections import deque

class MinStack:

    def __init__(self):
        # valStack, minStack
        self.valStack = deque([])
        self.minStack = deque([])

    def push(self, val: int) -> None:
        self.valStack.append(val)
        if not self.minStack: # If minStack is empty
            self.minStack.append(val)
        else: # minStack is not empty, therefore we compare the current min with the incoming value
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.valStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.valStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()