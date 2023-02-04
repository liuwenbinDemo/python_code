#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestSearch:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['app'] = '/Users/juanxu/Documents/霍格沃兹培训/录播课程/appium/测试demo/交互api/xueqiu.apk'
        # desired_caps['avd'] = 'Pixel_23_6'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        pass
        # self.driver.make_gsm_call('13812345678', GsmCallActions.CALL)
        # self.driver.send_sms('13812345671', 'hello appium api')
        # self.driver.set_network_connection(1)
        # self.driver.get_screenshot_as_file('./photos/img.png')
        # sleep(3)
        # self.driver.set_network_connection(4)
        # sleep(3)

