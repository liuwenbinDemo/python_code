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

# class TestWebDriverWait:
#     def setup(self):
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '6.0'
#         desired_caps['deviceName'] = 'emulator-5554'
#         desired_caps['appPackage'] = 'com.xueqiu.android'
#         desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
#         desired_caps['noReset'] = True
#         desired_caps['dontStopAppOnReset'] = True
#         desired_caps['skipServerInstallation'] = True
#         desired_caps['unicodeKeyBoard'] = 'true'
#         desired_caps['resetKeyBoard'] = 'true'
#         self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     @pytest.mark.skip
#     def test_wait(self):
#         self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
#         sleep(2)
#         self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
#         sleep(2)
#         self.driver.find_element_by_xpath("//*[@text='阿里巴巴']").click()
#         sleep(2)
#         self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
#         sleep(2)
#         ele = self.driver.find_element_by_xpath(
#             "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
#         print(ele.text)
#         current_price = float(ele.text)
#         expect_price = 170
#         # 173
#         assert_that(current_price, close_to(expect_price, expect_price*0.1))
#
#     @pytest.mark.parametrize("searchkey, stocktype, expect_price", [('alibaba', 'BABA',170),
#                                                                     ('xiaomi','01810', 9.5)])
#     def test_hamrest(self, searchkey, stocktype, expect_price):
#         self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
#         sleep(2)
#         self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
#         sleep(2)
#         self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
#         actual_price = self.driver.find_element_by_xpath("//*[contains(@resource-id, 'stockCode') and "
#                                                          f"contains(@text,'{stocktype}')]"
#                                            "/../../..//*[contains(@resource-id,'current_price')]").text
#
#         assert_that(float(actual_price), close_to(expect_price,expect_price*0.1))


class TestWebDriverWait:
    def setup_class(self):
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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def setup(self):
        pass
    def teardown(self):
        print(" teardown")
        self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        sleep(3)

    def teardown_class(self):
        print("class teardown")
        self.driver.quit()

    @pytest.mark.skip
    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        sleep(2)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text='阿里巴巴']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
        sleep(2)
        ele = self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        print(ele.text)
        current_price = float(ele.text)
        expect_price = 170
        # 173
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))




    @pytest.mark.parametrize("searchkey, stocktype, expect_price", [('alibaba', 'BABA', 170),
                                                                    ('xiaomi', '01810', 9.5)])
    def test_hamrest(self, searchkey, stocktype, expect_price):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        sleep(2)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        sleep(2)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
        actual_price = self.driver.find_element_by_xpath("//*[contains(@resource-id, 'stockCode') and "
                                                         f"contains(@text,'{stocktype}')]"
                                                         "/../../..//*[contains(@resource-id,'current_price')]").text

        assert_that(float(actual_price), close_to(expect_price, expect_price * 0.1))
