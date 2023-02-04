import requests

# 定义一个代理的 配置信息, key值为协议，value 为代理工具的配置,
proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

# 通过proxies 传递代理配置
data = {"a":1}
requests.post(url="https://httpbin.testing-studio.com/post", proxies=proxy,json=data,  verify = False)