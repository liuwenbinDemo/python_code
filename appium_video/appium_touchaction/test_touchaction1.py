#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class TestTouchAction():
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'io.appium.android.apis'
        caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        el1 = self.driver.find_element_by_accessibility_id(
            "Views")

        el2 = self.driver.find_element_by_accessibility_id(
            "Accessibility")

        action = TouchAction(self.driver)
        action.press(el1).wait(100).move_to(el2).wait(100).release().perform()

