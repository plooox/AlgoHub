class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.front = 0
        self.rear = 0
        self.length = k

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.length
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.length
            return True

    def Front(self) -> int:
        return self.q[self.front] if self.q[self.front] is not None else -1

    def Rear(self) -> int:
        return self.q[self.rear - 1] if self.q[self.rear - 1] is not None else -1

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
