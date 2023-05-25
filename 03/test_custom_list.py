import unittest

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.custom1 = CustomList([1, 2, 3])
        self.custom2 = CustomList([1, 2, 3])

    def test_add_two_customs_with_common_len(self):
        result = self.custom1 + self.custom2
        self.assertEqual(list(result), [2, 4, 6])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(self.custom2), [1, 2, 3])

    def test_add_custom_with_list_with_common_len(self):
        lst = [1, 3, 2]
        result = self.custom1 + lst
        self.assertEqual(list(result), [2, 5, 5])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst, [1, 3, 2])

    def test_add_list_with_custom_with_common_len(self):
        lst = [1, 3, 2]
        result = lst + self.custom1
        self.assertEqual(list(result), [2, 5, 5])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst, [1, 3, 2])

    def test_add_two_customs_with_diff_len(self):
        custom_lst = CustomList([1, 2, 3, 4, 5])
        result = self.custom1 + custom_lst
        self.assertEqual(list(result), [2, 4, 6, 4, 5])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [1, 2, 3, 4, 5])

        result = custom_lst + self.custom1
        self.assertEqual(list(result), [2, 4, 6, 4, 5])
        self.assertEqual(self.custom1, CustomList([1, 2, 3]))
        self.assertEqual(custom_lst, CustomList([1, 2, 3, 4, 5]))

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [1, 2, 3, 4, 5])

    def test_add_custom_with_list_with_diff_len(self):
        lst1 = [1, 2, 3, 4, 5]
        lst2 = [1, 2]
        result = self.custom1 + lst1
        self.assertEqual(list(result), [2, 4, 6, 4, 5])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst1, [1, 2, 3, 4, 5])

        result = self.custom1 + lst2
        self.assertEqual(list(result), [2, 4, 3])
        self.assertEqual(self.custom1, CustomList([1, 2, 3]))

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst2, [1, 2])

    def test_add_list_with_custom_with_diff_len(self):
        lst1 = [1, 2, 3, 4, 5]
        lst2 = [1, 2]
        result = lst1 + self.custom1
        self.assertEqual(list(result), [2, 4, 6, 4, 5])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst1, [1, 2, 3, 4, 5])

        result = lst2 + self.custom1
        self.assertEqual(list(result), [2, 4, 3])
        self.assertEqual(self.custom1, CustomList([1, 2, 3]))
        self.assertEqual(lst2, [1, 2])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst2, [1, 2])

    def test_sub_two_customs_with_common_len(self):
        result = self.custom1 - self.custom2
        self.assertEqual(list(result), CustomList([0, 0, 0]))

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(self.custom2), [1, 2, 3])

    def test_sub_custom_with_list_with_common_len(self):
        lst = [1, 2, 3]
        result = self.custom1 - lst
        self.assertEqual(list(result), [0, 0, 0])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst, [1, 2, 3])

    def test_sub_list_with_custom_with_common_len(self):
        lst = [1, 2, 3]
        result = lst - self.custom1
        self.assertEqual(list(result), CustomList([0, 0, 0]))

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst, [1, 2, 3])

    def test_sub_two_customs_with_diff_len(self):
        custom_lst = CustomList([5, 1, 3, 7])
        result = custom_lst - self.custom1
        self.assertEqual(list(result), [4, -1, 0, 7])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [5, 1, 3, 7])

        result = self.custom1 - custom_lst
        self.assertEqual(list(result), [-4, 1, 0, -7])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [5, 1, 3, 7])

    def test_sub_custom_with_list_with_diff_len(self):
        custom_lst = CustomList([5, 1, 3, 7])
        lst1 = [1, 2, 3]
        lst2 = [1, 2, 3, 4, 5, 6]
        result = custom_lst - lst1
        self.assertEqual(list(result), [4, -1, 0, 7])

        self.assertEqual(lst1, [1, 2, 3])
        self.assertEqual(list(custom_lst), [5, 1, 3, 7])

        result = custom_lst - lst2
        self.assertEqual(list(result), [4, -1, 0, 3, -5, -6])

        self.assertEqual(lst2, [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(custom_lst), [5, 1, 3, 7])

    def test_sub_list_with_custom_with_diff_len(self):
        lst1 = [5, 1, 3, 7]
        lst2 = [5, 1]
        result = lst1 - self.custom1
        self.assertEqual(list(result), [4, -1, 0, 7])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst1, [5, 1, 3, 7])

        result = lst2 - self.custom1
        self.assertEqual(list(result), [4, -1, -3])

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst2, [5, 1])

    def test_equal_same_lists(self):
        self.assertTrue(self.custom1 == self.custom2)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(self.custom2), [1, 2, 3])

    def test_equal_diff_lists_with_same_sum(self):
        custom_lst = CustomList([2, 2, 2])
        self.assertTrue(self.custom1 == custom_lst)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [2, 2, 2])

    def test_not_equal(self):
        custom_lst = CustomList([2, 1, 2])
        self.assertTrue(self.custom1 != custom_lst)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [2, 1, 2])

    def test_not_equal_diff_lists_with_same_sum(self):
        custom_lst = CustomList([2, 2, 2])
        self.assertFalse(self.custom1 != custom_lst)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [2, 2, 2])

    def test_greater(self):
        custom_lst = CustomList([1, 2])
        self.assertTrue(self.custom1 > custom_lst)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [1, 2])

    def test_greater_or_equal_with_greater(self):
        custom_lst = CustomList([1, 2])
        self.assertTrue(self.custom1 > CustomList([1, 2]))

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [1, 2])

    def test_greater_or_equal_with_equal(self):
        self.assertTrue(self.custom1 >= self.custom2)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(self.custom2), [1, 2, 3])

    def test_lower(self):
        custom_lst = CustomList([1, 2])
        self.assertTrue(custom_lst < self.custom1)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(custom_lst), [1, 2])

    def test_lower_or_equal_with_lower(self):
        lst = CustomList([1, 2])
        self.assertTrue(lst <= self.custom1)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(lst, [1, 2])

    def test_lower_or_equal_with_equal(self):
        self.assertTrue(self.custom2 <= self.custom1)

        self.assertEqual(list(self.custom1), [1, 2, 3])
        self.assertEqual(list(self.custom2), [1, 2, 3])

    def test_str(self):
        message = f'[1, 2, 3] Сумма: {sum(self.custom1)}'
        self.assertEqual(str(self.custom1), message)
        self.assertEqual(list(self.custom1), [1, 2, 3])
