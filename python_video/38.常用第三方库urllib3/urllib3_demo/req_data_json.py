import urllib3
import json

def test_json():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/post"

    # todo 设定请求体数据类型
    headers = {'Content-Type': 'application/json'}
    # todo 格式化JSON文本数据
    json_str = json.dumps({'school': 'hogwarts'})
    # todo 发送请求
    resp = pm.request('POST', url, headers=headers, body=json_str)

    content = json.loads(resp.data.decode('utf-8'))
    print(content)


