"""
__author__ = 'hogwarts_xixi'
"""
import allure
import pytest


@pytest.fixture()
def login():
    print("登录")

@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    def test_case1(self):
        print("case1")

    @allure.story("搜索失败")
    def test_case2(self):
        print("case2")


@allure.feature("登录模块")
class TestLogin():

    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1: 打开应用"):
            print("打开应用")
        with allure.step("步骤2: 进入登录页面"):
            print("登录页面")
            allure.attach.file("/Users/juanxu/Downloads/logo帽子.jpg",
                               name = "截图",
            attachment_type=allure.attachment_type.JPG,
                               extension=".jpg")
        with allure.step("步骤3: 输入用户信息"):
            # assert 1 == 2
            allure.attach("这是一段文本信息",name="文本展示")
            print("输入用户名和密码")
        with allure.step("步骤4: 进入成功页面"):
            allure.attach('<li><a href="https://ceshiren.com/t/topic/7229" target="_blank"><img src="https://ceshiren.com/uploads/default/original/2X/c/c86874aad0434ab5148d840a48ff47f8a46a32e5.jpeg"></a></li>', name="html展示"
                          ,attachment_type=allure.attachment_type.HTML)
            print("这是登录： 测试用例 ， 登录成功")

    @allure.story("登录成功")
    def test_login_success_a(self):
        print("这是登录： 测试用例 ， 登录成功")

    @allure.story("登录成功")
    def test_login_success_b(self):
        print("用户名缺失")

    @allure.story("登录失败")
    def test_login_failure(self):
        print("输入用户名")
        print("输入密码")
        print("点击登录")
        assert '1' == 1
        print("登录失败 ")

    @allure.story("登录失败")
    def test_login_failure_a(self):
        print("这是登录： 测试用例 ， 登录失败")
