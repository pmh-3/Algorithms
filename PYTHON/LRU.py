from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

'''
class Node:
def __init__(self, k, v):
    self.key = k
    self.val = v
    self.prev = None
    self.next = None

class LRUCache:
def __init__(self, capacity):
    self.capacity = capacity
    self.dic = dict()
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head

def get(self, key):
    if key in self.dic:
        n = self.dic[key]
        self._remove(n)
        self._add(n)
        return n.val
    return -1

def set(self, key, value):
    if key in self.dic:
        self._remove(self.dic[key])
    n = Node(key, value)
    self._add(n)
    self.dic[key] = n
    if len(self.dic) > self.capacity:
        n = self.head.next
        self._remove(n)
        del self.dic[n.key]

def _remove(self, node):
    p = node.prev
    n = node.next
    p.next = n
    n.prev = p

def _add(self, node):
    p = self.tail.prev
    p.next = node
    self.tail.prev = node
    node.prev = p
    node.next = self.tail


from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        # dict to store kv
        # list of keys to store LRU
        self.cache = {}
        self.LRU = deque([])
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.LRU.remove(key)
            self.LRU.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # if over capacity, remove begining of LRU Q
        # add to Q
        
                #updaate key in Q
        if key in self.cache:
            self.LRU.remove(key)

        else:
            if len(self.LRU) == self.cap:
                del self.cache[self.LRU.popleft()]

        self.cache[key] = value
        self.LRU.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''