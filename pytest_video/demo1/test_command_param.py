"""
__author__ = 'hogwarts_xixi'
"""
import pytest


def double(a):
    return a * 2

# 测试数据：整型
@pytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)

# 测试数据：负数
@pytest.mark.minus
def test_double1_minus():
    print("test double minus")
    assert -2 == double(-1)

# 测试数据：浮点数
@pytest.mark.float
def test_double_float():
    assert 0.2 == double(0.1)

@pytest.mark.float
def test_double2_minus():
    assert -0.2 == double(-0.1)

@pytest.mark.zero
def test_double_0():
    assert 0 == double(0)

@pytest.mark.bignum
def test_double_bignum():
    assert 200 == double(100)


@pytest.mark.str
def test_double_str():
    assert 'aa' == double('a')

@pytest.mark.str
def test_double_str1():
    assert 'a$a$' == double('a$')

# if __name__ == '__main__':
#     # 1、运行当前目录下所有的 用例
#     # pytest.main()
#     # # 3、运行test_mark1.py::test_dkej模块中的某一条用例
#     # pytest.main(['test_param.py::test_something','-vs'])
#     # # 4、运行某个 标签
#     pytest.main(['test_command_param.py','-vs','-m','str'])