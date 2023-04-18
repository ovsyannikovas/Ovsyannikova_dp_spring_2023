import unittest
from LRUCache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)

    def test_1(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")

        self.assertTrue(self.cache.get("k3") is None)
        self.assertTrue(self.cache.get("k2") == "val2")
        self.assertTrue(self.cache.get("k1") == "val1")

    def test_2(self):
        self.test_1()
        self.cache.set("k3", "val3")

        self.assertTrue(self.cache.get("k3") == "val3")
        self.assertTrue(self.cache.get("k2") is None)
        self.assertTrue(self.cache.get("k1") == "val1")
