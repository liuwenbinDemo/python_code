"""
__author__ = 'hogwarts_xixi'
"""
class TestSearch():
    def test_case1(self):
        print("case1")

    def test_case2(self):
        print("case2")


class TestLogin():

    def test_login_success(self):
        print("打开应用")
        print("登录页面")
        print("输入用户名和密码")
        print("这是登录： 测试用例 ， 登录成功")

    def test_login_success_a(self):
        print("这是登录： 测试用例 ， 登录成功")

    def test_login_success_b(self):
        print("用户名缺失")

    def test_login_failure(self):
        print("输入用户名")
        print("输入密码")
        print("点击登录")
        assert '1' == 1
        print("登录失败 ")

    def test_login_failure_a(self):
        print("这是登录： 测试用例 ， 登录失败")
