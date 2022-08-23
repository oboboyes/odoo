import random
import time

import requests as requests

headers = {
    "Host": "google-api.zhaoyizhe.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}


def scrapy(date):
    print('开始爬取%s' % date)
    url = 'https://google-api.zhaoyizhe.com/google-api/index/mon/sec?date=%s' % date
    try:
        time.sleep(random.randint(1, 3))
        res = requests.get(url, headers=headers).json()
        result = res['data']
        return result
    except Exception as err:
        print(err)
        return None
