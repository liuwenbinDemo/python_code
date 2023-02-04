#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure

def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach('''<body>这是一段htmlbody块</body>''', "html测试块", attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("/Users/juanxu/Documents/霍格沃兹培训/02录播课程/python/python010测试报告定制Allure/python008_alluredemo/resource/photo.jpg",
                  name="这是一个图片", attachment_type=allure.attachment_type.JPG)
def test_attach_video():
    allure.attach.file("/Users/juanxu/Documents/霍格沃兹培训/公开课/00训练营/app训练营/最好用的测试框架-pytest上.mp4",name="这是一个视频",
                       attachment_type=allure.attachment_type.MP4)


















"""
@allure.description('这条测试用例是用来说明allure的description')
def test_dynamic_description():
    assert 42 == int(6 * 7)
    allure.dynamic.description('A final description.')

@allure.title("这条测试是用来说明title")
def test_with_a_title():
    assert 2 + 2 == 4



def test_multiple_attachments():
    allure.attach.file('./resource/photo.jpg', attachment_type=allure.attachment_type.JPG)
    allure.attach('<head></head><body> 这是一个html页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
"""