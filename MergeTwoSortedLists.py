# Time Complexity: O(n + m)
# Space Complexity: O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Define pointers 
        currentNode = ListNode()
        dummyHeadNode = currentNode

        # Iterate
        while list1 and list2:
            if list1.val <= list2.val:
                currentNode.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                currentNode.next = list2
                list2 = list2.next
            currentNode = currentNode.next

        # Append remaining node to currentNode.next
        if list1 or list2:
            currentNode.next = list1 if list1 else list2

        # Return
        return dummyHeadNode.next