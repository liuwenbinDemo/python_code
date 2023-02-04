"""
__author__ = 'hogwarts_xixi'
"""
import sys

import pytest

@pytest.mark.skip
def test_aaa():
    print("代码未开发完")
    assert True

@pytest.mark.skip(reason="存在bug")
def test_bbb():
    assert False


# if not sys.platform.startswith("darwin"):
#     pytest.skip("skipping windows-only tests", allow_module_level=True)

## 代码中添加 跳过代码块 pytest.skip(reason="")
def check_login():
    return False

def test_function():
    print("start")
    # 如果未登录，则跳过后续步骤
    if not check_login():
        pytest.skip("unsupported configuration")
    print("end")
