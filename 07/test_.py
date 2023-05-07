import asyncio
import json
import unittest
from unittest import mock
from unittest.mock import call

from server import Server
from client import Client


class TestClientAndServer(unittest.TestCase):

    async def test_server_and_client(self):
        with mock.patch('server.Server.get_top_words') as mock_model:
            mock_model.return_value = json.dumps({'good': 0}, ensure_ascii=False)

            urls = [
                'https://vk.com/',
                'https://mail.ru/',
            ]

            server = Server(top_words=5, port=10000)
            task_server = asyncio.create_task(server.start())

            client = Client(urls_list=urls, port=10000)
            task_client = asyncio.create_task(client.start())

            await asyncio.gather(*[task_server, task_client])
            await server.stop()

            self.assertEqual(mock_model.call_count, 2)
            self.assertEqual(mock_model.call_args_list, [call(5, 'https://vk.com/'), call(5, 'https://mail.ru/')])

    def test_get_top_words_method(self):
        url = 'https://vk.com/'
        with mock.patch('server.Server.get_top_words') as mock_model:
            mock_model.return_value = json.dumps({'good': 0}, ensure_ascii=False)
            res = asyncio.run(Server.get_top_words(5, url))
            expected_res = '{"good": 0}'

            self.assertEqual(res, expected_res)

    def test_get_top_words_method_with_invalid_url(self):
        url = 'https://vkontaktee.ru/'
        res = asyncio.run(Server.get_top_words(5, url))

        self.assertEqual(res, None)
