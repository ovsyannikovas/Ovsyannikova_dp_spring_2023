import io
import unittest
from filter_generator import filter_generator


class TestGenerator(unittest.TestCase):
    def test_found(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = filter_generator(['роза'], fileobject=file)
        self.assertEqual(list(gen), ['а Роза упала на лапу Азора'])

    def test_found_several(self):
        file = io.StringIO('а Роза упала на лапу Азора\nалая РОЗА\nАзор')
        gen = filter_generator(['РоЗа'], fileobject=file)
        self.assertEqual(list(gen), ['а Роза упала на лапу Азора\n',
                                     'алая РОЗА\n'])

    def test_not_found(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = filter_generator(['роз'], fileobject=file)
        self.assertEqual(list(gen), [])

    def test_empty_file(self):
        file = io.StringIO('')
        gen = filter_generator(['роза'], fileobject=file)
        self.assertEqual(list(gen), [])

    def test_empty_words_list(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = filter_generator([], fileobject=file)
        self.assertEqual(list(gen), [])

    def test_words_list_with_empty_string(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = filter_generator([''], fileobject=file)
        self.assertEqual(list(gen), [])
