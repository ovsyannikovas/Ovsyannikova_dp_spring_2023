import unittest

from lrucache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)

    def test_attrs(self):
        self.assertTrue(isinstance(self.cache.dic, dict))
        self.assertTrue(self.cache.dic == {})
        ...
        self.assertTrue(isinstance(self.cache.limit, int))
        self.assertTrue(self.cache.limit == 2)

    def test_cache_get(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")

        self.assertTrue(self.cache.get("k3") is None)
        self.assertTrue(self.cache.get("k2") == "val2")
        self.assertTrue(self.cache.get("k1") == "val1")

        self.cache.set("k3", "val3")

        self.assertTrue(self.cache.get("k3") == "val3")
        self.assertTrue(self.cache.get("k2") is None)
        self.assertTrue(self.cache.get("k1") == "val1")

    def test_new_value(self):
        self.test_cache_get()
        self.cache.set("k3", "test")
        self.assertTrue(self.cache.get("k3") == "test")

    def test_not_setting_because_size(self):
        cache = LRUCache(1)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertTrue(cache.get("k2") == "val2")
        self.assertTrue(cache.get("k1") is None)

    def test_replace(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k3", "val3")
        self.cache.set("k4", "val4")

        self.assertTrue(self.cache.get("k1") is None)
        self.assertTrue(self.cache.get("k2") is None)
        self.assertTrue(self.cache.get("k3") == "val3")
        self.assertTrue(self.cache.get("k4") == "val4")

    def test_change_val_of_existent_and_displacement(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k1", "new_val1")
        self.cache.set("k3", "val3")

        self.assertTrue(self.cache.get("k1") == "new_val1")
        self.assertTrue(self.cache.get("k2") is None)
        self.assertTrue(self.cache.get("k3") == "val3")
