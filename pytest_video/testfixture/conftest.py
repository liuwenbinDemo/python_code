"""
__author__ = 'hogwarts_xixi'
"""
# conftest.py 名字是固定的，不能改变
import pytest


@pytest.fixture(scope="function",autouse=True)
def login():
    # setup 操作
    print("完成登录操作")
    token = "abcdafafadfafda"
    username = 'hogwarts'
    yield token,username # 相当于return
    # teardown 操作
    print("完成登出操作")

@pytest.fixture()
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")