#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    # 测试用例前执行一次
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["platformVersion"] = "6.0.1"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "com.xueqiu.android"
        desire_caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
        desire_caps["noReset"] = "true"
        # 输入中文时调用unicode键盘，使用完成后重置键盘
        desire_caps["unicodeKeyBoard"] = "true"
        desire_caps["resetKeyBoard"] = "true"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touchAction(self):
        action = TouchAction(self.driver)
        # action.press(x=725, y=2229).wait(2000).move_to(x=725, y=350).release().perform()
        self.driver.swipe(725,2229, 725, 350)