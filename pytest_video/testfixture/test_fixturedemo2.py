"""
__author__ = 'hogwarts_xixi'
"""
# fixture 的作用域
import pytest
# 定义了登录的fixture，尽量避免以test_开头
"""
@pytest.fixture
def fixture_name():
    setup 操作
    yield 返回值
    teardown 操作
"""
# @pytest.fixture(scope="class")
# def login():
#     # setup 操作
#     print("完成登录操作")
#     token = "abcdafafadfafda"
#     username = 'hogwarts'
#     yield token,username # 相当于return
#     # teardown 操作
#     print("完成登出操作")


def test_search(login):
    token,username = login
    print(f"token：{token} , name : {username}")
    # login 返回 None
    print("搜索")


def test_cart(login):
    print("购物车")


def test_order(login):
    print("下单功能")

class TestDemo:
    def test_case1(self,login):
        print("case1")

    def test_case2(self,login):
        print("case2")