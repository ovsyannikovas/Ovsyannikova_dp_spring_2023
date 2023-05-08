import json
import unittest
import time
from unittest import mock
from unittest.mock import call

from server import Server
from client import Client


class TestClientAndServer(unittest.TestCase):

    def test_server_and_client(self):
        with mock.patch('server.Server.get_top_words') as mock_model:
            mock_model.return_value = json.dumps(
                {'good': 0}, ensure_ascii=False)

            urls = [
                'https://vk.com/',
                'https://mail.ru/',
            ]

            server = Server(7, 5)
            server.start()
            time.sleep(1)

            client = Client(urls_list=urls)
            client.start()

            time.sleep(1)
            server.stop()

            self.assertEqual(mock_model.call_count, 2)
            self.assertEqual(mock_model.call_args_list,
                             [call(5, 'https://vk.com/'),
                              call(5, 'https://mail.ru/')])

    def test_get_top_words_method(self):
        url = 'https://vk.com/'
        res = Server.get_top_words(5, url)
        expected_res = '{"0": 60, "@keyframes": 59, ' \
                       '"<div": 34, "=": 24, "</div>": 22}'

        self.assertEqual(res, expected_res)

    def test_get_top_words_method_with_invalid_url(self):
        url = 'https://vkontaktee.ru/'
        res = Server.get_top_words(5, url)

        self.assertEqual(res, None)
