from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        oddTail = head
        evenTail = evenHead = head.next
        oddNode = True
        curNode = evenHead.next

        while curNode:
            if oddNode:
                oddTail.next = curNode
                oddTail = curNode
                oddNode = False
            else: 
                evenTail.next = curNode
                evenTail = curNode
                oddNode = True

            curNode = curNode.next

        evenTail.next = None
        oddTail.next = evenHead
        return head

# O(n) time: just making linked list changes in place
# O(1) space: not using any additional memory