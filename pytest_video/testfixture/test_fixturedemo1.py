"""
__author__ = 'hogwarts_xixi'
"""
import pytest
# 定义了登录的fixture
# @pytest.fixture()
# def login():
#     print("完成登录操作")


def test_search(login):
    print("搜索")


def test_cart(login):
    print("购物车")


def test_order(login):
    print("下单功能")