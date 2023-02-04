#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import pytest
from hamcrest import *

class TestGetAttr:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipServerInstallation'] = True
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    @pytest.mark.skip
    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
        assert 'search' in search_ele.get_attribute("resource-id")

    @pytest.mark.skip
    def test_assert(self):
        a = 10
        b = 20
        # assert a > b
        assert 'h' in 'this'


    def test_hamrest(self):
        # assert_that( 10 , equal_to(9) , '这是一个提示')
        # assert_that( 13 , close_to( 10 , 2))
        assert_that( "contains some string", contains_string("string"))





