from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ptr1 = ptr2 = head
        twins = []

        while ptr2 is not None:
            twins.append(ptr1.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        
        index = len(twins) - 1
        while ptr1 is not None:
            twins[index] += ptr1.val
            ptr1 = ptr1.next
            index -= 1
        
        return max(twins)
    
# test
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

test = Solution()
result = test.pairSum(build_linked_list([5,4,2,1]))
print(result)