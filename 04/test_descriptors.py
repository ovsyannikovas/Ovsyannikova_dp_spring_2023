import unittest
from descriptors import Data


class TestDescriptors(unittest.TestCase):

    def test_valid_values(self):
        inst = Data(-1, 'string', 999)

        self.assertEqual(inst.num, -1)
        self.assertEqual(inst.name, 'string')
        self.assertEqual(inst.price, 999)

    def test_valid_values_type(self):
        inst = Data(-1, 'string', 999)

        self.assertIsInstance(inst.num, int)
        self.assertIsInstance(inst.name, str)
        self.assertIsInstance(inst.price, int)

    def test_invalid_num_type(self):
        with self.assertRaises(Exception):
            inst = Data('', 'string', 999)

    def test_invalid_name_type(self):
        with self.assertRaises(Exception):
            inst = Data(-1, 2, 999)

    def test_invalid_price_value(self):
        with self.assertRaises(Exception):
            inst = Data(-1, 'string', -999)

    def test_invalid_price_type(self):
        with self.assertRaises(Exception):
            inst = Data(-1, 'string', '')

    def test_valid_change_num(self):
        inst = Data(-1, 'string', 999)
        inst.num = 2

        self.assertEqual(inst.num, 2)
        self.assertEqual(inst.name, 'string')
        self.assertEqual(inst.price, 999)

    def test_valid_change_name(self):
        inst = Data(-1, 'string', 999)
        inst.name = 'string2'

        self.assertEqual(inst.num, -1)
        self.assertEqual(inst.name, 'string2')
        self.assertEqual(inst.price, 999)

    def test_valid_change_price(self):
        inst = Data(-1, 'string', 999)
        inst.price = 1000

        self.assertEqual(inst.num, -1)
        self.assertEqual(inst.name, 'string')
        self.assertEqual(inst.price, 1000)

    def test_invalid_change_num(self):
        inst = Data(-1, 'string', 999)
        with self.assertRaises(Exception):
            inst.num = ''

        self.assertEqual(inst.num, -1)
        self.assertEqual(inst.name, 'string')
        self.assertEqual(inst.price, 999)

    def test_invalid_change_name(self):
        inst = Data(-1, 'string', 999)
        with self.assertRaises(Exception):
            inst.name = 2

        self.assertEqual(inst.num, -1)
        self.assertEqual(inst.name, 'string')
        self.assertEqual(inst.price, 999)

    def test_invalid_change_price(self):
        inst = Data(-1, 'string', 999)
        with self.assertRaises(Exception):
            inst.price = -2

        self.assertEqual(inst.num, -1)
        self.assertEqual(inst.name, 'string')
        self.assertEqual(inst.price, 999)
