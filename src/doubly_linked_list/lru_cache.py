class LRUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
    
    def _add_to_front(self, node):
        node.prev = None
        node.next = self.head

        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node

    def _remove_node(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = npde.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

    def _move_to_front(self, node):
        if node is self.head:
            return

        self._remove_node(node)
        self._add_to_front(node)

    def _remove_tail(self):
        if self.tail is None:
            return None

        old_tail = self.tail
        self._remove_node(old_tail)

        return old_tail

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        self._move_to_front(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.cache[key] = value
            self._move_to_front(self, key)
            return

        new_node = LRUNode(key, value)

        self.cache[key] = value
        self._add_to_front(key,value)

        if len(self.cache) > self.capacity:
            removed_node = self._remove_tail()    
            del self.cache[removed_node.key]

    
            



