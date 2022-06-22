class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.hashTable = collections.defaultdict(Node)

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        
        if self.hashTable[idx].value is None:
            self.hashTable[idx] = Node(key, value)
            return
        
        p = self.hashTable[idx]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = Node(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        
        if self.hashTable[idx].value is None:
            return -1
        
        p = self.hashTable[idx]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = key % self.size
        
        if self.hashTable[idx].value is None:
            return
        
        p = self.hashTable[idx]
        if p.key == key:
            self.hashTable[idx] = Node() if p.next is None else p.next
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)