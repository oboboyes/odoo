# coding=utf-8

# Python3.x

'''

利用有道翻译进行在线翻译

'''

import urllib.request

import urllib.parse

import json


def traslate(words):
    # 目标URL

    targetURL = "http://ai.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    # 用户自定义表单，words表示的是用户要翻译的内容。这里使用的是dict类型，也可以使用元组列表（已经试过的）。

    data = {'type': 'AUTO', 'i': words, 'doctype': 'json', 'xmlVersion': '1.8', 'keyfrom': 'fanyi.web', 'ue': 'UTF-8',
            'action': 'FY_BY_CLICKBUTTON', 'typoResult': 'true'}

    # 将自定义data转换成标准格式

    data = urllib.parse.urlencode(data).encode('utf-8')

    # 发送用户请求

    html = urllib.request.urlopen(targetURL, data)

    # 读取并解码内容

    rst = html.read().decode("utf-8")

    rst_dict = json.loads(rst)

    return rst_dict['translateResult'][0][0]['tgt']


if __name__ == "__main__":

    print("输入字母q表示退出")

    while True:

        words = input("请输入要查询的单词或句子:\n")

        if words == 'q':
            break

        result = traslate(words)

        print("翻译结果是：%s" % result)
