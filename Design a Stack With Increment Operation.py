class CustomStack: # The daily Challenge for 9/30/2024

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.currentSize = 0

    def push(self, x: int) -> None:
        if self.currentSize == self.maxSize:
            return
        self.stack.append(x)
        self.currentSize += 1
        return

    def pop(self) -> int:
        if self.currentSize == 0:
            return -1
        self.currentSize -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.currentSize)):
            self.stack[i] += val
        return


# Your CustomStack object will be instantiated and called as such:
stk = CustomStack(3) # Stack is Empty []
stk.push(1)                          # stack becomes [1]
stk.push(2)                          # stack becomes [1, 2]
stk.pop()                            # return 2 --> Return top of the stack 2, stack becomes [1]
stk.push(2)                          # stack becomes [1, 2]
stk.push(3)                          # stack becomes [1, 2, 3]
stk.push(4)                          # stack still [1, 2, 3], Do not add another elements as size is 4
stk.increment(5, 100)                # stack becomes [101, 102, 103]
stk.increment(2, 100)                # stack becomes [201, 202, 103]
stk.pop()                            # return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop()                            # return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop()                            # return 201 --> Return top of the stack 201, stack becomes []
stk.pop()                            # return -1 --> Stack is empty return -1.