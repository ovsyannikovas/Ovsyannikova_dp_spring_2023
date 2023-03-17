import io
import unittest
from filter_generator import filter_generator


class TestGenerator(unittest.TestCase):
    def test_found(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = filter_generator(file, ['роза'])
        self.assertEqual(next(gen), 'а Роза упала на лапу Азора')
        with self.assertRaises(Exception) as context:
            next(gen)
        self.assertTrue(isinstance(context.exception, StopIteration))

    def test_not_found(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = filter_generator(file, ['роз'])
        with self.assertRaises(Exception) as context:
            next(gen)
        self.assertTrue(isinstance(context.exception, StopIteration))

    def test_empty_file(self):
        file = io.StringIO('')
        gen = filter_generator(file, ['роза'])
        with self.assertRaises(Exception) as context:
            next(gen)
        self.assertTrue(isinstance(context.exception, StopIteration))

    def test_empty_words_list(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = filter_generator(file, [])
        with self.assertRaises(Exception) as context:
            next(gen)
        self.assertTrue(isinstance(context.exception, StopIteration))

    def test_words_list_with_empty_string(self):
        file = io.StringIO('а Роза упала на лапу Азора')
        gen = filter_generator(file, [''])
        with self.assertRaises(Exception) as context:
            next(gen)
        self.assertTrue(isinstance(context.exception, StopIteration))
