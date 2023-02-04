import urllib3
import json

# GET/HEAD/DELETE 请求
def test_querystr_get():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"
    # todo 定义查询字符串
    fields = {'school': 'hogwarts'}
    # todo 发送请求
    resp = pm.request('GET', url, fields=fields)
    # todo 查看响应信息
    content = json.loads(resp.data.decode('utf-8'))
    print(content)

# POST/PUT 请求
def test_querystr_post():

    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"

    # todo 从内置库urllib的parse模块导入编码方法
    from urllib.parse import urlencode

    # todo urlencode编码
    encoded_str = urlencode({'school': 'hogwarts'})
    # todo 拼接到URL中，发送请求
    resp = pm.request('POST',url=url + '?' + encoded_str)
    # todo 查看响应信息
    content = json.loads(resp.data.decode('utf-8'))
    print(content)