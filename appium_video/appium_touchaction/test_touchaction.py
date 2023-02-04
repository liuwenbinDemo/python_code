#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_accessibility_id("Buttons").click()

        action = TouchAction(self.driver)
        action.tap(self.driver.find_element_by_accessibility_id("Toggle")).perform()

    def test_touchaction_swipe(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        action = TouchAction(self.driver)
        action.long_press(x=550,y=2200).wait(200).move_to(x=550,y=550).wait(200).release().perform()

    def test_touchaction_swipe(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        action = TouchAction(self.driver)
        action.long_press(x=550, y=2200).wait(200).move_to(x=550, y=550).wait(200).release().perform()

