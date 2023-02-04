from flask import Flask, redirect, make_response

app = Flask(__name__)

@app.route("/demo")
def demo():
    res = redirect("https://httpbin.testing-studio.com/get")
    res2 = make_response(redirect("https://httpbin.testing-studio.com/get"))
    print(res2)
    return res2

if __name__ == '__main__':
    app.run()