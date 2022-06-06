# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        llA, llB = headA, headB

        while llA != llB:
            llA = llA.next if llA is not None else headB
            llB = llB.next if llB is not None else headA

        return llA
