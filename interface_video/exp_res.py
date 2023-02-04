import requests

def test_res():
    r = requests.get("https://httpbin.ceshiren.com/get")
    # 断言请求是否发送成功
    assert r.status_code == 200
    # 断言业务逻辑是否正确
    #预期结果响应url为以下值

    assert r.json()["url"] == "https://httpbin.ceshiren.com/get"