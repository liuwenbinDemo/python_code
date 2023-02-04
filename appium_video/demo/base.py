#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver import webdriver


class Base:
    def __init__(self,driver):
        self._driver = driver

    def setup(self):
        _appPackage = "com.dangdang.buy2"
        _appActivity = ".activity.ActivityMainTab"
        if self._driver == None:
            print("_driver is None")
            desire = {
                'platformName' : 'android',
                'platformVersion' : '6.0',
                'deviceName' : 'emulator-5554',
                'appPackage' : _appPackage,
                'appActivity' : _appActivity,
                'noReset' : 'true'
            }
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire)
        else:
            print("_driver is not None")
            self._driver.start_activity(_appPackage, _appActivity)
        self._driver.implicitly_wait(5)

    def teardown(self):
        pass
        # self._driver.quit()
