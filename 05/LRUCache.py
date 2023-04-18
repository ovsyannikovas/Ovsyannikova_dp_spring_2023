from collections import deque


class LRUCache:

    def __init__(self, limit=42):
        self.cache = {}
        self.keys_deque = deque()
        self.limit = limit

    def get(self, key):
        if key not in self.keys_deque:
            return None
        else:
            val = self.keys_deque[self.keys_deque.index(key)]
            self.keys_deque.remove(val)
            self.keys_deque.append(val)
            return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value
        self.keys_deque.append(key)
        if len(self.keys_deque) > self.limit:
            self.cache.pop(self.keys_deque[0])
            self.keys_deque.popleft()
