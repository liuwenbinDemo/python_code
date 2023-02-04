import urllib3


def test_timeout_4s():
    pm = urllib3.PoolManager()
    # 访问这个地址，服务器会在3秒后响应
    url = "http://httpbin.org/delay/3"

    # todo 设置超时时间4秒
    resp = pm.request('GET',url, timeout=2.0)
    print(resp.status)


