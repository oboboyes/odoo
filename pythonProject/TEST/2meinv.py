import os
import threading
import time

import requests
from bs4 import BeautifulSoup
from queue import Queue
from loguru import logger as log

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36 ',
    'Connection': 'close'
}
q1 = Queue()
q2 = Queue()


def create_page_queue(num):
    for page in range(1, num):
        q1.put(page)
    log.info('创建页数队列成功')


class CreateURLQueueThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = 'thread_0' + name

    @log.catch()
    def run(self):
        log.info(self.name + '  开始啦!!!!!!')
        while True:
            index = q1.get()
            if index == 1:
                url = 'https://www.2meinv.com/'
            else:
                url = f'https://www.2meinv.com/index-{index}.html'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            a = soup.find('div', {'class': 'con-3-2 mt15'}).find_all('a')
            # 根据url规则处理url
            li = [j.attrs['href'][0:-5] for j in a]
            for j in set(li):
                q2.put(j)
            if q1.empty():
                log.info(self.name + '  结束啦!!!!!!')
                break


class DownloadThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = 'thread_0' + name

    @log.catch()
    def run(self):
        log.info(self.name + '  开始啦!!!!!!')
        while True:
            u = q2.get()
            for i in range(1, 100):
                if i == 1:
                    url = u + '.html'
                else:
                    url = u + f'-{i}.html'
                try:
                    response = requests.get(url, headers=headers)
                except requests.exceptions.ConnectionError:
                    log.error(f'{self.name} 下载 {url}  失败')
                    continue
                soup = BeautifulSoup(response.text, 'lxml')
                img = soup.find('div', {'class': 'pp hh'}).find('img')
                h1 = soup.find('div', {'class': 'des'}).find('h1')
                num1 = h1.get_text().split()[1].replace('(', '')
                num2 = h1.get_text().split()[3].replace(')', '')
                if not os.path.exists(rf'D:\www.2meinv.com\{img.attrs["alt"]}'):
                    os.makedirs(rf'D:\www.2meinv.com\{img.attrs["alt"]}')
                try:
                    response = requests.get(img.attrs['src'], headers=headers)
                except requests.exceptions.ConnectionError:
                    log.error(f'{self.name} 下载 {url}  失败')
                    continue
                with open(rf'D:\www.2meinv.com\{img.attrs["alt"]}\{img.attrs["src"][-18:]}', 'wb') as fp:
                    fp.write(response.content)
                    log.info(f'{self.name} 下载 {url} {h1.get_text()} 成功')
                time.sleep(1)  # 太快容易requests.exceptions.ConnectionError
                if num1 == num2:  # 根据标题显示的图片数量判断何时跳出循环
                    break
            if q2.empty():
                log.info(self.name + '  结束啦!!!!!!')
                break


if __name__ == '__main__':
    create_page_queue(100)
    threads = []
    for _ in range(10):
        thread = CreateURLQueueThread(str(_))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    threads = []
    for _ in range(10):
        thread = DownloadThread(str(_))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    log.info("退出主线程")