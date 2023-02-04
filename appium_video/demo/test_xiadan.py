#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
from appium import webdriver
from time import sleep
import pytest
class TestXiaDan():
    _appPackage = "com.dangdang.buy2"
    _appActivity = ".activity.ActivityMainTab"

    @classmethod
    def setup_class(self):
        # _appPackage = "com.dangdang.buy2"
        # _appActivity = ".activity.ActivityMainTab"
        desire = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'deviceName': 'emulator-5554',
            'appPackage': self._appPackage,
            'appActivity': self._appActivity,
            'noReset': 'true'
        }
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire)
        self._driver.implicitly_wait(5)
    def setup(self):
        pass
        # self._driver.start_activity(self._appPackage, self._appActivity)

    @classmethod
    def teardown_class(self):
        self._driver.quit()

    def teardown(self):
        self._driver.back()
        self._driver.back()
        self._driver.back()

    # @pytest.mark.parametrize('searchkey', ['appium']) # ,'android', 'ios'
    @pytest.mark.parametrize('searchkey', yaml.safe_load(open("./datas.yaml"))) # ,'android', 'ios'
    @pytest.mark.skip
    def test_order(self, searchkey):
        """
        需要注意：
        登录（提前问题，绕过登录验证）
        noReset 设置
        添加一些步骤，比如单品页，结算页配送方式，优惠券的选择等
        查看物流，取消定单

        打开app
        搜索一个单品"连衣裙"
        点击第一个单品，添加购物车
        去购物车结算
        点击结算
        """
        self._driver.find_element_by_id("com.dangdang.buy2:id/home_search_hint_tv").click()
        self._driver.find_element_by_id("com.dangdang.buy2:id/search_edit_input").send_keys(searchkey)
        self._driver.find_element_by_id("com.dangdang.buy2:id/search_btn_search").click()
        assert self._driver.find_element_by_id("com.dangdang.buy2:id/tv_sale_count_sort").text == '销量'
        self._driver.find_element_by_id("com.dangdang.buy2:id/add_cart_tv").click()
        self._driver.find_element_by_id("com.dangdang.buy2:id/etv_cart").click()
        self._driver.find_element_by_id("com.dangdang.buy2:id/cart_balance_tv").click()
        self._driver.find_element_by_id("com.dangdang.buy2:id/checkout_button").click()
        sleep(2)
        print(self._driver.current_activity)
        assert 'H5PayActivity' in self._driver.current_activity
        sleep(5)
        print(self._driver.page_source)
        self._driver.find_element_by_accessibility_id("返回").click()
        self._driver.find_element_by_accessibility_id("是").click()
        sleep(3)


    @pytest.mark.skip
    def test_toast(self):
        self._driver.find_element_by_id("com.dangdang.buy2:id/tab_personal_iv").click()
        self._driver.find_element_by_id("com.dangdang.buy2:id/tv_agile_uesr_name").click()
        self._driver.find_element_by_id("com.dangdang.buy2:id/et_account").send_keys("18612466299")
        self._driver.find_element_by_id("com.dangdang.buy2:id/et_password").send_keys("123456")
        self._driver.find_element_by_id("com.dangdang.buy2:id/btn_login").click()
        print(self._driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)
        sleep(3)

    @pytest.mark.parametrize('a,b,c', yaml.safe_load(open("./datas_list.yaml"))) # ,'android', 'ios'
    def test_yaml(self,a,b,c):
        print(f"a = {a} ,b = {b} ,c = {c} ,")











