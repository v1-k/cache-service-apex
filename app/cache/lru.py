import time

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.timestamp = time.time()

class LRUCache:
    def __init__(self, capacity: int, ttl: int):
        self.capacity = capacity
        self.ttl = ttl
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def __remove(self,node):
        next = node.next
        prev = node.prev
        prev.next= next
        next.prev = prev

    def __insert_top(self,node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            if time.time() - node.timestamp > self.ttl:
                self.__remove(node)
                del self.cache[key]
                return None
            else:
                self.__remove(node)
                self.__insert_top(node)
                return node.val
        return None
    
    def put(self, key, value) -> None:
        if key in self.cache:
            self.__remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.__insert_top(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.__remove(lru)
            del self.cache[lru.key]