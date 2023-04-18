import unittest
from LRUCache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)

    def test_cache_get(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")

        self.assertTrue(self.cache.get("k3") is None)
        self.assertTrue(self.cache.get("k2") == "val2")
        self.assertTrue(self.cache.get("k1") == "val1")

    def test_lru_mechanism(self):
        self.test_cache_get()
        self.cache.set("k3", "val3")

        self.assertTrue(self.cache.get("k3") == "val3")
        self.assertTrue(self.cache.get("k2") is None)

    def test_new_value(self):
        self.test_cache_get()
        self.cache.set("k3", "test")
        self.assertTrue(self.cache.get("k3") == "test")
