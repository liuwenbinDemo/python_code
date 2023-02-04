#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome("../chromedriver")
    def teardown(self):
        self.driver.quit()
    def test_alert(self):
        """Alert弹窗获取文本与确认操作"""
        self.driver.get("http://sahitest.com/demo/alertTest.htm")
        self.driver.find_element_by_name("b1").click()
        WebDriverWait(self.driver, 5, 0.5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        time.sleep(1)
        print(alert.text)
        # alert.accept()
        alert.dismiss()
        time.sleep(5)
    def test_alert_1(self):
        """Alert弹窗获取文本与确认操作"""
        self.driver.get("http://sahitest.com/demo/alertTest.htm")
        self.driver.find_element_by_name("b1").click()
        from selenium.webdriver.common.alert import Alert
        alert = Alert(self.driver)
        time.sleep(1)
        print(alert.text)
        # alert.accept()
        alert.dismiss()
        time.sleep(5)

    def test_prompt(self):
        """Prompt 弹窗获取文本、输入内容、确认操作"""
        self.driver.get("http://sahitest.com/demo/promptTest.htm")
        self.driver.find_element_by_name("b1").click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.send_keys('Selenium Alert弹出窗口输入信息')
        time.sleep(2)
        alert.accept()

        time.sleep(5)

    def test_confirm(self):
        """Comfirm弹窗获取文本、确认、取消操作"""
        self.driver.get("http://sahitest.com/demo/confirmTest.htm")
        self.driver.find_element_by_name("b1").click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())  # 等待弹出窗口出现
        alert = self.driver.switch_to.alert
        print(alert.text)
        time.sleep(2)
        alert.accept()
        # alert.dismiss()

        time.sleep(5)
