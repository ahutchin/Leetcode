from typing import Optional
from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        nodes = {}
        nodeToIndex = {}
        curr = head
        i = 0

        while curr:
            nodeToIndex[curr] = i
            nodes[i] = (Node(curr.val))
            i += 1
            curr = curr.next
        
        curr = head
        for j in range(i):
            if curr.next:
                nodes[j].next = nodes[j + 1]
            if curr.random:
                random_index = nodeToIndex[curr.random]
                nodes[j].random = nodes[random_index]
            curr = curr.next
        return nodes[0]

# Intuition:
# 2-pass solution, 
# 1st pass -> build each node (their value, their next) & Store each in a hashtable
# 2nd pass -> Assign each node's random according to the hashtable

# Time & Space Complexity: O(n) because we do 2 passes through n nodes, and store 2 hash tables of n nodes