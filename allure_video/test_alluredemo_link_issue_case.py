#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure


@allure.link("http://www.baidu.com",name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用你还里面")
    pass


# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass










"""


# 给链接加个展示名
@allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='Click me')
def test_with_named_link():
    pass

'''
@allure.issue 提供一个链接带着bug图标
 --allure-link-pattern 执行的时候加上这个参数
$ pytest directory_with_tests/ --alluredir=/tmp/my_allure_report \
 --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
'''
@allure.issue('140', 'Pytest-flaky test retries shows like test steps')
def test_with_issue_link():
    pass

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    pass

"""