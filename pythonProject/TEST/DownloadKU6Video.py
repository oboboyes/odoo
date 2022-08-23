import requests
import json

# 找到真实的网站地址
url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'
# 伪装成浏览器访问
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/95.0.4621.0 Safari/537.36'}
response = requests.get(url, headers=headers).text
# print(response)
# print(type(response))

# 转成字典类型，字典类型具有极快的查找速度
req = json.loads(response)
# print(type(req))
datas = req['data']
# print(datas) #列表  过滤方法：re lxml bs4 xpath
for data in datas:  # 遍历，去掉外层的【】
    data_title = data['title'] + '.mp4'
    data_link = data['playUrl']
    # print(data_title,data_link)

    # 下载视频，需要转换格式
    video_data = requests.get(url + data_link, headers=headers).content
    # print(type(video_data))
    with open('video\\' + data_title, mode='wb') as f:
        f.write(video_data)
        print('下载成功', data_title)
