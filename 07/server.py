import asyncio
import json
import socket
import time
from collections import Counter

import aiohttp
import click as click


class Server:
    def __init__(self, workers, top_words, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.workers = workers
        self.threads = 0
        self.top_words = top_words
        self.socket = None
        self.parsed_urls = 0

    async def start(self):
        await self.master_thread()

    async def stop(self):
        self.socket.close()

    async def is_running(self):
        return self.socket

    async def master_thread(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1000)

        while await self.is_running():
            if self.threads >= self.workers:
                continue

            client, _ = self.socket.accept()
            data = client.recv(1024)

            await self.worker_thread(data.decode(), self.top_words, client)

        await self.stop()

    async def worker_thread(self, url, top_words, client):
        response = await self.get_top_words(top_words, url)

        if response:
            client.send(response.encode())
        else:
            client.send('Ошибка при открытии URL.'.encode())
        client.close()

        print(f'parsed urls: {self.parsed_urls}')

    @staticmethod
    async def get_top_words(num, url):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    html = await resp.read()
        except aiohttp.ClientError:
            return

        counter_dict = Counter(html.split()).most_common(num)
        result = {}
        for key, value in counter_dict:
            result[key.decode()] = value

        return json.dumps(result, ensure_ascii=False)


@click.option('-w', default=5)
@click.option('-k', default=3)
async def main(w=5, k=3):
    server = Server(w, k)
    task = asyncio.create_task(server.start())
    await task

    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
