# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(head: ListNode):
    if head is None:
        return ""
    return reverseList(head.next) + str(head.val)

class Solution:    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        
        retval = str(int(reverseList(l1)) + int(reverseList(l2)))
        
        next_ = None
        for ch in retval:
            node = ListNode(ch)
            node.next = next_
            next_ = node
        
        return node