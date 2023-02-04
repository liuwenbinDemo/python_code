import urllib3
import json

# POST/PUT 请求
def test_form():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"
    fields = {'school': 'hogwarts'}

    # todo: 使用field参数
    resp = pm.request('POST', url, fields=fields)
    # todo 解析响应信息
    content = json.loads(resp.data.decode('utf-8'))
    # print(content)
    print(content['form'])


