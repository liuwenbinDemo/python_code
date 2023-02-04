#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time
import pytest
from time import sleep

class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'io.appium.android.apis.ApiDemos',
            # 'browserName':'Chrome',
            'deviceName':'192.168.56.101:5555',
            # 'deviceName': 'emulator-5554',
            'chromedriverExecutable': '/Users/juanxu/Documents/chromedriver'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.start_recording_screen()
        self.driver.find_element_by_accessibility_id("Views").click()
        webview = "WebView"
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}")'
                                                        '.instance(0));').click()
        contexts = self.driver.contexts
        print(contexts)
        # self.driver.switch_to.context(contexts[-1])
        sleep(2)
        self.driver.find_element_by_accessibility_id("i has no focus").send_keys("test webview")
        sleep(2)
        self.driver.find_element_by_accessibility_id("i am a link").click()
        sleep(2)
        print(self.driver.page_source)
        sleep(3)









