from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # define result object
        resultNode = ListNode(0, None)
        currNode = resultNode
        carryOver = False

        # start addition
        while (l1 is not None and l2 is not None):
            currNode.val = l1.val + l2.val + 1 if carryOver else l1.val + l2.val
            if (currNode.val >= 10):
                currNode.val = currNode.val % 10
                carryOver = True
            else:
                carryOver = False

            l1 = l1.next
            l2 = l2.next
            if (l1 or l2):
                currNode.next = ListNode(0, None)
                currNode = currNode.next
        
        while (l1 is not None):
            if (carryOver):
                currNode.val = l1.val + 1
            else:
                currNode.val = l1.val
                currNode.next = l1.next
                break
            
            if (currNode.val >= 10):
                currNode.val = currNode.val % 10
                carryOver = True
            else:
                carryOver = False
            
            l1 = l1.next
            if (l1):
                currNode.next = ListNode(0, None)
                currNode = currNode.next

        while (l2 is not None):
            if (carryOver):
                currNode.val = l2.val + 1
            else:
                currNode.val = l2.val
                currNode.next = l2.next
                break
            
            if (currNode.val >= 10):
                currNode.val = currNode.val % 10
                carryOver = True
            else:
                carryOver = False

            l2 = l2.next
            if (l2):
                currNode.next = ListNode(0, None)
                currNode = currNode.next

        if (carryOver):
            currNode.next = ListNode(1, None)

        return resultNode

# Testing
l1 = ListNode(1, ListNode(8))
l2 = ListNode(0)

test = Solution()

result = test.addTwoNumbers(l1, l2)

while (result != None):
    print(result.val, " ")
    result = result.next