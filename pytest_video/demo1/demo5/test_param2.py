"""
__author__ = 'hogwarts_xixi'
"""
import pytest

# 1、参数化的名字，要与方法中的参数名，一一对应，
# 2、如果传递多个参数的话，要放在列表中，列表中嵌套列表 /元组
# 3、ids 的个数 == 传递的数据个数
@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),("2+5",7),("7+5",12)
],ids=["number1","number2","number3"])
def test_mark_more(test_input,expected):
    assert eval(test_input) == expected