import urllib3
import json

def test_response():
    pm = urllib3.PoolManager()
    resp = pm.request(method='GET', url="http://httpbin.org/ip")

    # todo 获取二进制形式的响应内容
    raw = resp.data
    # print(type(raw), raw)
    # 解码成字符串
    content = raw.decode('utf-8')
    # print(type(content), content)
    # JSON解析成字典对象
    obj = json.loads(content)
    # print(type(obj), obj)
    print(obj['origin'])

