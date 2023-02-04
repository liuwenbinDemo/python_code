import requests


class TestReq:

    def setup_class(self):
        # 设置代理
        self.proxy = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

    def test_one(self):
        # 通过timeout 参数设置超时时间，timeout 对应的值通常是一个数字类型
        r = requests.post("https://httpbin.testing-studio.com/post")
        print(r.json())

    def test_two(self):
        # 通过timeout 参数设置超时时间，timeout 对应的值通常是一个数字类型
        r = requests.post("https://httpbin.testing-studio.com/post",
                          proxies=self.proxy, verify=False, timeout=3)
        print(r.json())

    def test_three(self):
        # 通过timeout 参数设置超时时间，timeout 对应的值通常是一个数字类型
        r = requests.post("https://httpbin.testing-studio.com/post")
        print(r.json())
