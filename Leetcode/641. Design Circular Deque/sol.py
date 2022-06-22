class ListNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.maxlen, self.curlen = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            newNode = ListNode(value)
            curhead = self.head.right
            self.head.right, curhead.left = newNode, newNode
            newNode.left, newNode.right = self.head, curhead
            self.curlen += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            newNode = ListNode(value)
            curtail = self.tail.left
            self.tail.left, curtail.right = newNode, newNode
            newNode.left, newNode.right = curtail, self.tail
            self.curlen += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            newHead = self.head.right.right
            newHead.left, self.head.right = self.head, newHead
            self.curlen -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            newTail = self.tail.left.left
            newTail.right, self.tail.left = self.tail, newTail
            self.curlen -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.right.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.left.value

    def isEmpty(self) -> bool:
        return self.curlen == 0

    def isFull(self) -> bool:
        return self.curlen == self.maxlen


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
