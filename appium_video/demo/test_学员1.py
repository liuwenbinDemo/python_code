#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testdw():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        #desired_caps['dontStopAppOnReset'] = 'true'
        #输入非英文之外的语言并在测试完成后重置输入法
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        time.sleep(15)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    #def teardown(self):
        #self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        time.sleep(20)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        time.sleep(20)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        time.sleep(20)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        time.sleep(20)
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 190

    @pytest.mark.skip
    def test_attr(self):
        element =self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)

        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            element22 = alibaba_element.get_attribute('displayed')
            if element22 == 'true':
                print("它是可见的，搜查成功")
            else:
                print("它不可见，搜查失败")

    @pytest.mark.skip
    def test_touchaction(self):
        action=TouchAction(self.driver)
        time.sleep(20)
        window_rect = self.driver.get_window_rect()
        #print(window_rect)
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height*4/5)
        y_end = int(height*1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

    def test_scroll(self):
        #self.driver.find_element_by_android_uiautomator('new UiSelector().text("热门")').click()
        # 显示等待
        # def wait(x):
        #     return len(self.driver.find_element_by_xpath("//*[@text='雪球热股']")) >= 1
        # WebDriverWait(self.driver, 80).until(wait)

        # locator = (MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/title_text' and @text='热门']")
        # WebDriverWait(self.driver,60).until(expected_conditions.element_to_be_clickable(locator))
        # time.sleep(120)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("雪球达人秀").'
                                                        'instance(0));').click()
if __name__=='__main__':
    pytest.main()