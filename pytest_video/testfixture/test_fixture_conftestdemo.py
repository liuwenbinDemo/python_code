"""
__author__ = 'hogwarts_xixi'
"""
def test_search(login):
    token,username = login
    print(f"token：{token} , name : {username}")
    # login 返回 None
    print("搜索")


def test_get_product(login,connectDB):
    print("验证 获取单品信息")

def test_cart(login):
    print("购物车")


def test_order(login):
    print("下单功能")

class TestDemo:
    def test_case1(self,login):
        print("case1")

    def test_case2(self,login):
        print("case2")