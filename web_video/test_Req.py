import requests


def test_Req():
    url = "http://127.0.0.1:5000/demo"
    r = requests.get(url)
    print(r.text)