class Node:
    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node):
        prev, next = self.right.prev, self.right
        node.next = next
        node.prev = prev
        prev.next = next.prev = node

    def remove(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.insert(self.dict[key])
            return self.dict[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        self.dict[key] = Node(key, value)
        self.insert(self.dict[key])

        if len(self.dict) > self.capacity:
            lru = self.left.next
            del self.dict[lru.key]
            self.remove(lru)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Intuition
# Store key & value in dictionary
# Track LRU & MRU in doubly linked list

# Test
test = LRUCache(2)
test.put(2, 1)
test.get(2)