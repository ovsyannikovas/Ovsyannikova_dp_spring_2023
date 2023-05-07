class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove_node(n)
            self._add_node(n)
            return n.val
        return None

    def set(self, key, value):
        if key in self.dic:
            self._remove_node(self.dic[key])
        new_node = Node(key, value)
        self._add_node(new_node)
        self.dic[key] = new_node

        if len(self.dic) > self.limit:
            new_node = self.head.next
            self._remove_node(new_node)
            del self.dic[new_node.key]

    def _remove_node(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add_node(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
