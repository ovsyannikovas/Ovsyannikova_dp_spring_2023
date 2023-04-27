import json
import socket
import threading
import time
import urllib.error
from collections import Counter
from urllib.request import urlopen

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
        self.lock_thread = threading.Lock()

    def start(self):
        server = threading.Thread(target=self.master_thread, daemon=True)
        server.start()

    def stop(self):
        self.socket.close()

    def is_running(self):
        return self.socket

    def master_thread(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1000)

        while self.is_running():
            if self.threads >= self.workers:
                continue

            client, _ = self.socket.accept()
            data = client.recv(1024)

            with self.lock_thread:
                self.threads += 1

            thread = threading.Thread(
                target=self.worker_thread,
                args=(data.decode(), self.top_words, client)
            )
            thread.start()
            time.sleep(0.5)

        self.stop()

    def worker_thread(self, url, top_words, client):
        response = self.get_top_words(top_words, url)

        if response:
            client.send(response.encode())
        else:
            client.send('Ошибка при открытии URL.'.encode())
        client.close()

        with self.lock_thread:
            self.threads -= 1
            self.parsed_urls += 1
            print(f'parsed urls: {self.parsed_urls}')

    @staticmethod
    def get_top_words(num, url):
        try:
            html = urlopen(url).read()
        except urllib.error.URLError:
            return

        counter_dict = Counter(html.split()).most_common(num)
        result = {}
        for key, value in counter_dict:
            result[key.decode()] = value

        return json.dumps(result, ensure_ascii=False)


@click.option('-w', default=5)
@click.option('-k', default=3)
def main(w=5, k=3):
    server = Server(w, k)
    server.start()

    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
