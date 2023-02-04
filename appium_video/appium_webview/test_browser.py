#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time
import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains, TouchActions
from time import sleep

class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'browserName': 'Browser',
            # 'browserName':'Chrome',
            'noReset': True,
            'deviceName':'192.168.56.101:5555',
            # 'deviceName': 'emulator-5554',
            'chromedriverExecutable': '/Users/juanxu/Documents/chromedriver'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        sleep(10)
        self.driver.quit()
    # @pytest.mark.skip
    def test_browser(self):
        sleep(5)
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        e = self.driver.find_element_by_id("index-bn")
        e.click()
        self.driver.find_element_by_xpath('//*[@id="page-hd"]/div/div[4]/div[1]/div[1]/div/a[3]/span').click()







