"""
__author__ = 'hogwarts_xixi'
"""
# 收集完测试用例 之后被调用的hook函数
from typing import List

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    # name 用例的名字
    # nodeid 就是测试用例路径
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    items.reverse()