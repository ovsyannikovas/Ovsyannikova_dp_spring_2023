import unittest
from unittest import mock

from parse_json import parse_json


class TestParseJson(unittest.TestCase):
    def setUp(self):
        self.old_json = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        self.required_fields = ["key1"]
        self.keywords = ["word2"]

    def test_valid_key_field(self):
        with mock.patch("parse_json.func") as mock_func:
            mock_func.return_value = 'new_value'
            new_json = '{"key1": "Word1 new_value", "key2": "word2 word3"}'
            self.assertEqual(parse_json(self.old_json, mock_func, self.required_fields, self.keywords), new_json)

    def test_invalid_key(self):
        with mock.patch("parse_json.func") as mock_func:
            mock_func.return_value = 'new_value'
            self.required_fields = ['invalid_key']

            with self.assertRaises(KeyError) as context:
                parse_json(self.old_json, mock_func, self.required_fields, self.keywords)

            self.assertTrue(isinstance(context.exception, KeyError))

    def test_no_keywords(self):
        with mock.patch("parse_json.func") as mock_func:
            mock_func.return_value = 'new_value'
            self.keywords = ['invalid_keyword']
            new_json = self.old_json
            self.assertEqual(parse_json(self.old_json, mock_func, self.required_fields, self.keywords), new_json)

    def test_several_fields(self):
        with mock.patch("parse_json.func") as mock_func:
            mock_func.return_value = 'new_value'
            self.required_fields = ["key1", "key2"]
            new_json = '{"key1": "Word1 new_value", "key2": "new_value word3"}'
            self.assertEqual(parse_json(self.old_json, mock_func, self.required_fields, self.keywords), new_json)
