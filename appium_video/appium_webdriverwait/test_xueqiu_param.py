#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import assert_that, close_to
import pytest
import logging
logging.getLogger()
class TestWebDriverWait:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['deviceName'] = 'RFCMC00LKZH'
        # desired_caps['udid'] = 'RFCMC00LKZH'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = True
        desired_caps['skipServerInstallation'] = True
        desired_caps['skipDeviceInitialization'] = True
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # desired_caps['autoLaunch'] = False
        desired_caps['avd'] = 'Pixel_3a_XL_API_23'
        # desired_caps['app'] = '/Users/juanxu/Documents/霍格沃兹培训/录播课程/appium/测试demo-apk/ContactManager.apk'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
        pass
        # self.driver.quit()

    def test_get_performance(self):
        sleep(5)
        types = self.driver.get_performance_data_types()
        print(types)
        for i in types:
            print(f"当前 {i}")
            print(self.driver.get_performance_data('com.xueqiu.android', i, 10))
        # print(self.driver.get_performance_data('com.xueqiu.android', 'cpuinfo', 5))


    @pytest.mark.parametrize('searchkey, type, expect_price', [
        ('alibaba', 'BABA', 180),
        ('xiaomi', '01810',10),
    ])
    def test_search(self, searchkey, type, expect_price):
        self.driver.start_recording_screen()
        """
        1. 打开雪球 应用
        2. 点击 搜索框
        3. 输入 搜索词 'alibaba' or 'xiaomi'...
        4. 点击第一个搜索结果
        5. 判断 股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        price_element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(price_element.text)
        # expect_price = 180
        print(f"当前的价格{current_price}")
        assert_that(current_price, close_to(expect_price, expect_price*0.1))
        self.driver.stop_recording_screen()
