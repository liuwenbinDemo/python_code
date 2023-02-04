import requests

r = requests.post("https://httpbin.ceshiren.com/post",
                  # files 参数用来解决文件上传接口
                  # value通过元组传递，实现指定filename的需求
                  files={"hogwarts_file": ("hogwarts.txt", open("1.text", "rb"))},
                  proxies = {"http": "http://127.0.0.1:8080",
                             "https": "http://127.0.0.1:8080"},
                  verify = False
                  )
print(r.json())



