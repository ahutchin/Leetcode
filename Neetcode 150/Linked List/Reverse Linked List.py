from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        prevNode = None

        while curNode != None:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        
        return prevNode

# Intuition:
# This should take O(n) time
# 3 pointers: 
#   1, currentNode -> set nextNode to its current neighbor, update its current neighbor to its new neighbor (prevNode)
#   2, prevNode -> set this to currentNode, set currentNode to nextNode
#   3, nextNode -> repeat the process

# head = [1,2,3,4,5]