import json
import math
import socket
import threading

import click as click


class Client:
    def __init__(self, request_file, host='127.0.0.1', port=5000, threads=5):
        self.host = host
        self.port = port
        self.request_file = request_file
        self.threads = threads

    def start(self):
        url_list = self.get_url_list()

        threads = [
            threading.Thread(target=self.worker_thread, args=(url,))
            for url in url_list
        ]

        for thread in threads:
            thread.start()
            thread.join()

    def worker_thread(self, url_list):
        for url in url_list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))

            sock.send(url.encode())
            data = sock.recv(1024)

            print(f'{url}: ', data.decode())

            sock.close()

    def get_url_list(self):
        with open(self.request_file, 'r', encoding='utf-8') as file:
            urls = json.load(file)

        step = math.ceil(len(urls) / self.threads)
        result = [urls[i:i + step] for i in range(0, len(urls), step)]

        return result


@click.argument('threads', default=5)
@click.argument('filename', default='urls.json')
def main(threads=5, filename='urls.json'):
    client = Client(filename, threads=threads)
    client.start()


if __name__ == '__main__':
    main()
