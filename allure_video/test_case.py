#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK, '测试链接')
def test_with_testcase_link():
    pass