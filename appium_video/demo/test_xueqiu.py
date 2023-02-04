#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import uiautomator2


class TestXueQiu:

    def test_demo(self):
        # 连接设备
        d = uiautomator2.connect()
        # info 获取设备信息
        print(d.info)
        # window_size() 获取屏幕尺寸
        print(d.window_size())
        # uiautoamtor2 current 获取当前页面的package和activity
        print(d.app_current())

    def test_demo1(self):
        # 连接设备
        d = uiautomator2.connect()
        # 启动应用 app_start
        d.app_start("com.xueqiu.android",
                    "com.xueqiu.android.common.MainActivity")
        d.app_wait("com.xueqiu.android")
        # 元素定位 文本定位，启动app
        # d(text="雪球股票").click()
        sleep(2)
        d.app_stop("com.xueqiu.android")

    def test_search(self):
        """
        打开雪球app
        点击搜索框
        输入【阿里巴巴】点第一个搜索结果
        点击第一个结果的 ’加自选’
        :return:
        """
        # 连接设备
        d = uiautomator2.connect()
        # 启动应用 app_start
        d.app_start("com.xueqiu.android",
                    "com.xueqiu.android.common.MainActivity")
        d.app_wait("com.xueqiu.android")
        # 向搜索框里面输入"alibaba" 文本信息
        d(resourceId="com.xueqiu.android:id/tv_search").send_keys("alibaba")
        # 点击搜索结果的"阿里巴巴"
        d(text='阿里巴巴').click()
        d(text='加自选').click()
        sleep(3)

        # 关闭应用
        d.app_stop("com.xueqiu.android")



