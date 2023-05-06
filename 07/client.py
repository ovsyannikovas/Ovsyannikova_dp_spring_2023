import asyncio
import json
import math
import socket

import click as click


class Client:
    def __init__(self, request_file=None, urls_list=None, host='127.0.0.1', port=5000, threads=5):
        self.host = host
        self.port = port
        self.request_file = request_file
        self.urls = urls_list
        self.threads = threads

    async def start(self):
        url_list = await self.get_url_list()

        for url in url_list:
            await self.worker_thread(url)

    async def worker_thread(self, url_list):
        for url in url_list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))

            sock.send(url.encode())
            data = sock.recv(1024)

            print(f'{url}: ', data.decode())

            sock.close()

    async def get_url_list(self):
        if not self.urls:
            with open(self.request_file, 'r', encoding='utf-8') as file:
                self.urls = json.load(file)

        step = math.ceil(len(self.urls) / self.threads)
        result = [self.urls[i:i + step] for i in range(0, len(self.urls), step)]

        return result


@click.argument('threads', default=5)
@click.argument('filename', default='urls.json')
async def main(threads=5, filename='urls.json'):
    client = Client(filename, threads=threads)
    task = asyncio.create_task(client.start())
    await task


if __name__ == '__main__':
    asyncio.run(main())
