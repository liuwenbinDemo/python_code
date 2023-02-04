#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains, TouchActions
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            # 'platformVersion': '8.0',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.common.MainActivity',
            'deviceName': '192.168.56.101:5555', #6.0
            "automationName": "uiautomator2",

            # 'deviceName': '192.168.56.102:5555',  # 8.0


            'noReset': 'true',
            # 'chromedriverExecutable': '/Users/juanxu/Documents/chromedriver'
            'chromedriverExecutableDir': '/Users/juanxu/Documents/mychromedriver/all/',
            'chromedriverChromeMappingFile': '/Users/juanxu/Documents/霍格沃兹培训/录播课程/appium/测试demo/appium_webview/mapping.json',
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    # def teardown(self):
    #     pass
        # self.driver.quit()


    def test_webview(self):

        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        sleep(2)
        print(self.driver.contexts)
        print(self.driver.current_context)
        self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        print("上下文")
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)

        ele = self.driver.find_element_by_xpath('//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')
        ele.click()
        # sleep(30)
        print(self.driver.contexts)
        print(self.driver.current_context)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        print(self.driver.current_window_handle)


        # self.driver.find_element_by_xpath('//*[@id="phone-number"]').send_keys("11111111111")
        input_locator = (By.ID,"phone-number")
        el = WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located(input_locator))
        el.send_keys("13810100202")
        self.driver.find_element_by_id("code").send_keys("1234")
        sleep(2)
        print(self.driver.page_source)
        self.driver.find_element_by_css_selector(".btn-submit").click()



        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        # self.driver.
        # time.sleep(10)
        # print("用户手机号：")
        # print(driver.find_element_by_id("phone-number").text)

        # input_locator = (MobileBy.ACCESSIBILITY_ID, "输入11位手机号")
        # WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable(input_locator))
        #
        # ele = self.driver.find_element(*input_locator)
        # contexts = self.driver.contexts
        # print(contexts)
        # self.driver.switch_to.context(contexts[-1])
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "输入验证码").send_keys("111")
        # sleep(20)
        # print(ele.is_enabled())
        # ele.click()
        # ele.send_keys("13811111111")

        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "输入验证码").send_keys("111")





