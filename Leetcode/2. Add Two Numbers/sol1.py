# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:    
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            tmp, node.next =  node.next, prev
            prev, node = node, tmp
            
        return prev
    
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: Listnode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1 = self.toList(self.reverseList(l1))
        v2 = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in v1)) + \
                    int(''.join(str(e) for e in v2))
        
        return self.toReversedLinkedList(str(resultStr))