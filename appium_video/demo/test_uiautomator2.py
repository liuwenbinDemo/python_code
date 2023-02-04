#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2

d = uiautomator2.connect("emulator-5554")
print(d.info)
print(d.device_info)
print(d.window_size())


class TestXueQiu:
    def test_search(self):
        print("搜索测试用例")
        d = uiautomator2.connect()
        # d(text="雪球股票").click()
        d.app_start("com.xueqiu.android", "com.xueqiu.android.common.MainActivity")
        d.app_wait("com.xueqiu.android")
        d(resourceId="com.xueqiu.android:id/tv_search").send_keys("alibaba")
        d(text="阿里巴巴").click()
        d(className="android.widget.RelativeLayout").\
            child(resourceId="com.xueqiu.android:id/add_attention").\
            click()

        message = d.toast.get_message(5.0, 10.0, '')
        # print(message)
        assert "添加成功" == message
        d.toast.reset()

        d.app_stop("com.xueqiu.android")


