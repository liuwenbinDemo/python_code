import requests

def test_req():
    # 如何定制请求方法
    # 第一个方式
    # r = requests.post(url)
    # print(r.json())
    # # 第二个方式
    # r = requests.request("post", url)
    # print("定制请求方法的第二个方式", r.json())
    # 如何定制请求头
    # header = {"User-Agent": "hogwarts"}
    # r = requests.get(url, headers=header)
    # print("请求头信息为",r.request.headers)
    url = "https://httpbin.ceshiren.com/get"
    # url = "https://httpbin.ceshiren.com/get?teacher=ad"
    # 定制请求url的参数
    param = {"teacher": "ad", "class": "interface"}

    r = requests.get(url, params=param)
    print(r.url)