#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestSearch:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipServerInstallation'] = True
        # desired_caps['noReset'] = True
        desired_caps['UiAutomator'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        self.driver.make_gsm_call("13801010101",GsmCallActions.CALL)
        self.driver.send_sms('555-123-4567', 'Hey lol')
        self.driver.set_clipboard_text()
        self.driver.get_clipboard_text()

    def test_network(self):
        print(self.driver.network_connection)
        self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        print(self.driver.network_connection)
        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

    def test_other(self):
        # self.driver.start_recording_screen()

        print("back")
        self.driver.keyevent(4)
        sleep(3)
        print("home")
        self.driver.keyevent(3)
        sleep(2)
        print("lock")
        self.driver.lock(4)
        sleep(3)
        # self.driver.orientation
        # self.driver.stop_recording_screen()
        # self.driver.get_log()
    def test_log(self):
        # print(self.driver.log_types)
        # print(self.driver.get_log("logcat"))
        types = self.driver.get_performance_data_types()
        print(types)
        sleep(10)
        print(self.driver.get_performance_data("com.xueqiu.android", 'cpuinfo', 10))
        # for i in types:
        #     self.driver.get_performance_data("com.xueqiu.android", i, 10)



