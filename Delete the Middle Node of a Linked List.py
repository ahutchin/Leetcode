from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case:
        if head is None or head.next is None:
            return None

        # 2 ptrs
        ptr1 = ptr2 = head

        # 1st ptr moves by 1, 2nd ptr moves by 2, when the 2nd ptr is None or 2nd ptr.next is None, we are done and the first ptr is just before the middle Node
        while ptr2.next.next is not None and ptr2.next.next.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        
        # assignment
        prevNode = ptr1
        nextNode = ptr1.next.next
        ptr1 = None # set to None to save memory
        prevNode.next = nextNode
        
        # return
        return head
    
# Time Complexity: O(n) because we visit traverse the linked list 1 time
# Space Complexity: O(1) because we dont allocate any additional memory 