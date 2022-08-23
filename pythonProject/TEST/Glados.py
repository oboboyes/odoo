import json
import requests

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = 'off'

# 填写server酱sendkey,不开启server酱则不用填（修改成你自己的）
sckey = 'SCT*******************************'

# 填入glados账号对应cookie（修改成你自己的）
cookie = 'koa:sess=eyJ1c2VySWQiOjE5MTI4NiwiX2V4cGlyZSI6MTY4NjM5MTc5MTc2NCwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=QOwnwZ5zIIG1TiRxNz8vmyzIsdM; Cookie=enabled; Cookie.sig=lbtpENsrE0x6riM8PFTvoh9nepc; _ga=GA1.2.961162871.1660473478; _gid=GA1.2.280648012.1660473478; __cf_bm=SZJrDw38XiRd9XcahjSAEMIUcJRR3Up_BhXVAIwp1dc-1660473877-0-AQKJV5dLHEYv4puTU9J/NOCh55GGXYYQVVLtvWkmUfYF5i4eUVEktsJCOGGw8g/oDfptSuPrUudaUrRz7zrdzp0rUlKhIbSoMWq/EKs0sHVzZyziX9Ce9yyZi6i//XqTKA=='


def start():
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    # checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    # state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 " \
                "Safari/537.36 "
    payload = {
        # 'token': 'glados_network'
        'token': 'glados.network'
    }
    checkin = requests.post(url,
                            headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent,
                                     'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
    state = requests.get(url2,
                         headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
    print(checkin.text)
    print(state.text)


    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print(mess)
        print(time)
        if sever == 'on':
            requests.get('https://sctapi.ftqq.com/' + sckey + '.send?title='+mess+'，you have '+time+' days left')

    else:
        requests.get('https://sctapi.ftqq.com/' + sckey + '.send?title=error')
        print("error")

    checkin.close()
    state.close()

def main_handler(event, context):
    start()


