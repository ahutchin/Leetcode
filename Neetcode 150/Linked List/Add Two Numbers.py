from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            # Calculate sum
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # Update curr.val
            carry = sum // 10
            curr.val = sum % 10

            if l1 or l2 or carry:
                curr.next = ListNode(0)
                curr = curr.next
                
        return head


# Intuition:
# Add from left to right, keep track of carry, continue 