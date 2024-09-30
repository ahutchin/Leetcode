class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        # declare length of deque, k
        self.maxLength = k
        # declare currentLength of deque, which will be necessary to track the number of elements in the deque
        self.currentLength = 0
        # declare head & tail
        self.head = listNode(0)
        self.tail = self.head

    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.head.val = value
            self.tail = self.head
            self.currentLength = 1
            return True
        elif self.isFull():
            return False
        else:
            self.head.prev = listNode(value)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.head.prev = self.tail
            self.tail.next = self.head
            self.currentLength += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.tail.val = value
            self.head = self.tail
            self.currentLength = 1
            return True
        elif self.isFull(): 
            return False
        else:
            self.tail.next = listNode(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.currentLength += 1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        elif self.currentLength == 1:
            self.head.val = 0
            self.currentLength -= 1
            return True
        else:
            self.head = self.head.next
            self.tail.next = self.head
            self.currentLength -= 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.currentLength == 1:
            self.head.val = 0
            self.currentLength -= 1
            return True
        else:
            self.tail = self.tail.prev
            self.head.prev = self.tail
            self.currentLength -= 1
            return True        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        if self.currentLength == 0:
            return True
        return False


    def isFull(self) -> bool:
        if self.currentLength == self.maxLength:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3);
print(obj.insertLast(1));  # return True
print(obj.insertLast(2));  # return True
print(obj.insertFront(3)); # return True
print(obj.insertFront(4)); # return False, the queue is full.
print(obj.getRear());      # return 2
print(obj.isFull());       # return True
print(obj.deleteLast());   # return True
print(obj.insertFront(4)); # return True
print(obj.getFront());     # return 4