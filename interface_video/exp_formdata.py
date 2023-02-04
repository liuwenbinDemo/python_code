import requests


class TestReq:

    def setup_class(self):
        # 设置代理
        self.proxy = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

    def test_data(self):
        data = {"howarts": "school"}
        # 通过data参数传入请求体信息
        r = requests.post("https://httpbin.testing-studio.com/post", data=data,
                      proxies = self.proxy, verify=False)
        print(r.json())

    def test_json(self):
        data = {"howarts": "school"}
        # 通过json参数传入请求体信息
        r = requests.post("https://httpbin.testing-studio.com/post", json=data, proxies=self.proxy, verify=False)
        print(r.json())

