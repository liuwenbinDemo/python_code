# -*- coding: utf-8 -*-
# @Author : feier
# @File : assert_xml.py
from requests_xml import XMLSession
import xml.etree.ElementTree as ET

def test_xml():
    # 设置 session
    session = XMLSession()
    r = session.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
    # print(r.text)
    # links 可以拿到响应中所有的链接
    # print(r.xml.links)
    # # raw_xml 返回字节形式的响应内容
    # print(r.xml.raw_xml)
    # # text 返回标签中的内容
    # print(r.xml.text)

    # 通过 xpath
    # item = r.xml.xpath("//link", first=True)
    # # 因为返回的是对象，所以需要调用 text 属性获取具体的值
    # print(item.text)
    # item = r.xml.xpath("//link")
    # result = []
    # for i in item:
    #     print(i.text)
    #     result.append(i.text)
    # print(result)
    # assert "http://www.nasa.gov/" in result
    # item = r.xml.xpath("//pubDate")
    # for i in item:
    #     print(i.text)

    # 自己封装 xml 解析方法
    root = ET.fromstring(r.text)
    # 查找根元素
    item = root.findall(".")
    print(item)
    items = root.findall(".//link")
    result = []
    for i in items:
        print(i.text)
        result.append(i.text)
    assert "http://www.nasa.gov/" in result




