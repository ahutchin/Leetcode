from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) Time Complexity
    # O(1) Space Complexity
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # Iterative Solution
        # Initialize 2 pointers
        currentNode = head
        previousNode = None

        # Iterate through linked list
        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        # Return
        return previousNode

