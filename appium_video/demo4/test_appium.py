#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from time import sleep
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='com.xueqiu.android.common.MainActivity'
desired_caps['noReset']=True
desired_caps['dontStopAppOnReset'] = True
desired_caps['skipServerInstallation'] = True
desired_caps['unicodeKeyBoard'] = 'true'
desired_caps['resetKeyBoard'] = 'true'



driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
sleep(3)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
sleep(2)
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
sleep(2)
driver.find_element_by_xpath("//*[@text='阿里巴巴']").click()
sleep(2)
driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
sleep(2)
ele = driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
print(ele.text)

# print(driver.page_source)


# TouchAction(driver).press(x=700,y=2275).move_to(x=700,y=220).release().perform()

# print(driver.get_window_size())
# # print()
# width = driver.get_window_rect()['width']
# height = driver.get_window_rect()['height']
# x_ = width/2
# y_start = int(height*0.8)
# y_end = int(height*0.2)
#
# TouchAction(driver).long_press(x=x_,y=y_start).move_to(x=x_,y=y_end).release().perform()

# ele = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
# action = TouchAction(driver)
# TouchAction(driver).tap(ele).perform()
driver.quit()
# TouchAction(driver).press(x=219,y=514).release().perform()

# driver.implicitly_wait(10)
# driver.find_element_by_id("")
# driver.quit()
#
#
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='6.0'
# desired_caps['deviceName']='emulator-5554'
# desired_caps['appPackage']='io.appium.android.apis'
# desired_caps['appActivity']='io.appium.android.apis.ApiDemos'
# desired_caps['dontStopAppOnReset'] = True
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


# WebDriverWait(driver, 10,0.5).until(driver.find_element_by_id("com.android.settings:id/title"))
# WebDriverWait(driver, 10,0.5).until(lambda x:x.find_element_by_id("com.android.settings:id/title"))
# ele = WebDriverWait(driver, 10, 0.5).until(expected_conditions.visibility_of_element_located((MobileBy.ID,"com.android.settings:id/title")))
# print("888888")
# print(ele)
# print(ele.text)
# ele = driver.find_element_by_id("com.android.settings:id/title")
# print(ele.get_attribute("name"))
# print(ele.get_attribute("text"))
# print(ele.get_attribute("classname"))
# print(ele.get_attribute("resourceid"))
# enabled​、checkable​、checked
# print(ele.get_attribute("selected"))
# print(ele.get_attribute("checkable"))
# print(ele.get_attribute("checked"))
# print(ele.get_attribute("clickable"))
# a = ele.get_attribute("enabled")
# print(type(a))
#
# print(ele.get_attribute("long-clickable"))
# # print(ele.get_attribute("package"))
# print(ele.get_attribute("bounds"))
# print(ele.get_attribute("contentSize"))
# print(ele.get_attribute("selection-start"))
