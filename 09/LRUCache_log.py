import argparse
import logging

CAPACITY = 5

logging.basicConfig(
    filename='cache.log',
    level=logging.INFO,
    format='%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s',
)

logger = logging.getLogger('LRUCache')


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
            logger.info('Was return element %s with key %s', n.val, key)
            return n.val
        logger.warning('Not existing key %s in cache', key)
        return None

    def set(self, key, value):
        if key in self.dic:
            logger.info('Key %s already exist in cache', key)
            logger.info('Deleting element %s with key %s in cache', self.dic[key].val, key)
            self._remove_node(self.dic[key])
        new_node = Node(key, value)
        logger.info('Adding new element %s with key %s in cache', value, key)
        self._add_node(new_node)
        self.dic[key] = new_node

        if len(self.dic) > self.limit:
            logger.warning('Cache is full')
            new_node = self.head.next
            logger.info('Deleting element %s with key %s in cache', new_node.val, new_node.key)
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


class SomeFilter(logging.Filter):
    def filter(self, record):
        return len(record.msg.split()) % 2 != 0


def set_logger_stdout(stdout, filter):
    handler = logging.StreamHandler()
    if stdout:
        stdout_log_format = logging.Formatter(
            '[%(asctime)s] [%(threadName)s] (%(name)s): %(message)s'
        )
        handler.setFormatter(stdout_log_format)

    if filter:
        handler.addFilter(SomeFilter())

    logger.addHandler(handler)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-f', action='store_true')
    args = parser.parse_args()

    set_logger_stdout(args.s, args.f)

    cache = LRUCache(limit=CAPACITY)

    for i in range(CAPACITY):
        cache.set(i, f'value{i}')

    for i in range(CAPACITY):
        cache.get(i)

    cache.set(0, 'newvalue0')
    cache.get(0)

    cache.set(CAPACITY, f'value{CAPACITY}')
    cache.get(1)
