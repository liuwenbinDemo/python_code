import urllib3
import json

def test_headers():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"

    # todo 定制请求头
    headers = {'School': 'hogwarts'}
    # todo 发送请求
    resp = pm.request('GET', url, headers=headers)
    # todo 查看响应信息
    content = json.loads(resp.data.decode('utf-8'))
    # print(content)
    print(content['headers'])