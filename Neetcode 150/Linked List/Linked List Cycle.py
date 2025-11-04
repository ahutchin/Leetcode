from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = ptr2 = head

        while ptr2 != None and ptr2.next != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr2 == ptr1:
                return True
        
        return False
        

# Intuition:
# 2 ptr, one traverses 1 node at a time, other traverses at 2 nodes at a time
# If they ever equal each other, there is loop
# Only iterate for len(LinkedList) iterations