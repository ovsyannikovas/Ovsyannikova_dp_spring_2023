import unittest

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.custom1 = CustomList([1, 2, 3])
        self.custom2 = CustomList([1, 2, 3])

    def test_add_two_customs_with_common_len(self):
        result = self.custom1 + self.custom2
        self.assertEqual(result, CustomList([2, 4, 6]))

    def test_add_custom_with_list_with_common_len(self):
        result = self.custom1 + [1, 3, 2]
        self.assertEqual(result, CustomList([2, 5, 5]))

    def test_add_list_with_custom_with_common_len(self):
        result = [1, 3, 2] + self.custom1
        self.assertEqual(result, CustomList([2, 5, 5]))

    def test_add_two_customs_with_diff_len(self):
        result = self.custom1 + CustomList([1, 2, 3, 4, 5])
        self.assertEqual(result, CustomList([2, 4, 6, 4, 5]))

    def test_add_custom_with_list_with_diff_len(self):
        result = self.custom1 + [1, 2, 3, 4, 5]
        self.assertEqual(result, CustomList([2, 4, 6, 4, 5]))

    def test_add_list_with_custom_with_diff_len(self):
        result = [1, 2, 3, 4, 5] + self.custom1
        self.assertEqual(result, CustomList([2, 4, 6, 4, 5]))

    def test_sub_two_customs_with_common_len(self):
        result = self.custom1 - self.custom2
        self.assertEqual(result, CustomList([0, 0, 0]))

    def test_sub_custom_with_list_with_common_len(self):
        result = self.custom1 - [1, 2, 3]
        self.assertEqual(result, CustomList([0, 0, 0]))

    def test_sub_list_with_custom_with_common_len(self):
        result = [1, 2, 3] - self.custom1
        self.assertEqual(result, CustomList([0, 0, 0]))

    def test_sub_two_customs_with_diff_len(self):
        result = CustomList([5, 1, 3, 7]) - self.custom1
        self.assertEqual(result, CustomList([4, -1, 0, 7]))

    def test_sub_custom_with_list_with_diff_len(self):
        result = CustomList([5, 1, 3, 7]) - [1, 2, 3]
        self.assertEqual(result, CustomList([4, -1, 0, 7]))

    def test_sub_list_with_custom_with_diff_len(self):
        result = [5, 1, 3, 7] - self.custom1
        self.assertEqual(result, CustomList([4, -1, 0, 7]))

    def test_equal_same_lists(self):
        self.assertTrue(self.custom1 == self.custom2)

    def test_equal_diff_lists_with_same_sum(self):
        self.assertTrue(self.custom1 == CustomList([2, 2, 2]))

    def test_not_equal(self):
        self.assertTrue(self.custom1 != CustomList([2, 1, 2]))

    def test_not_equal_diff_lists_with_same_sum(self):
        self.assertFalse(self.custom1 != CustomList([2, 2, 2]))

    def test_greater(self):
        self.assertTrue(self.custom1 > CustomList([1, 2]))

    def test_greater_or_equal_with_greater(self):
        self.assertTrue(self.custom1 > CustomList([1, 2]))

    def test_greater_or_equal_with_equal(self):
        self.assertTrue(self.custom1 >= self.custom2)

    def test_lower(self):
        self.assertTrue(CustomList([1, 2]) < self.custom1)

    def test_lower_or_equal_with_lower(self):
        self.assertTrue(CustomList([1, 2]) <= self.custom1)

    def test_lower_or_equal_with_equal(self):
        self.assertTrue(self.custom2 <= self.custom1)

    def test_str(self):
        message = f'{self.custom1.lst} Сумма: {sum(self.custom1.lst)}'
        self.assertEqual(str(self.custom1), message)
