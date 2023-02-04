import urllib3

def test_HTTP():
    # 创建线程池对象
    pm = urllib3.PoolManager()
    resp = pm.request(method='GET', url="http://httpbin.org/get")
    print(type(resp))
    print(resp.status)
    print(resp.headers)
    print(resp.data)

