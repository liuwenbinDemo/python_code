# coding=utf-8
from time import sleep

from selenium import webdriver
# 导入Keys()类
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get('https://testerhome.com/')

driver.find_element_by_name('q').send_keys('seleniumm')
# 删除多余的一个m
driver.find_element_by_name('q').send_keys(Keys.BACK_SPACE)
sleep(3)
action = ActionChains(driver)
action.send_keys(Keys.SHIFT).send_keys('a').perform()
sleep(3)
# 输入空格键+教程
# driver.find_element_by_name('q').send_keys(Keys.SPACE)
# driver.find_element_by_name('q').send_keys(u'教程')
# # 全选输入框内容，使用control+A
# sleep(2)
# driver.find_element_by_name('q').send_keys(Keys.COMMAND, 'a')
# sleep(2)
# # 剪切输入框内容
# driver.find_element_by_name('q').send_keys(Keys.COMMAND, 'x')
# sleep(5)
# # 粘贴在文本框中
# driver.find_element_by_name('q').send_keys(Keys.COMMAND, 'v')
# sleep(5)
# # 回车搜索
# driver.find_element_by_name('q').send_keys(Keys.ENTER)

driver.quit()
