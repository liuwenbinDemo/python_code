import urllib3
import json


def test_HTTPS():
    url = "https://httpbin.ceshiren.com/get"

    # todo 创建不校验证书的连接池对象
    pm_https = urllib3.PoolManager(cert_reqs="CERT_NONE")
    # todo 发送HTTPS请求
    resp = pm_https.request('GET', url)

    content = json.loads(resp.data.decode('utf-8'))
    print(content)

