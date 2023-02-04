# -*- coding: utf-8 -*-
# @Author : feier
# @File : lambda_demo.py

import math

# 常规写法
def circle_area(r):
    '''
    计算圆的面积
    r：半径
    '''
    result = math.pi*r*r
    return result

r = 10
# 用 lambda 表达式实现
result = lambda r:math.pi*r*r
# print(f"半径为 {r} 的圆的面积为 {circle_area(r)}")
print(f"半径为 {r} 的圆的面积为 {result(r)}")
# 不可以省略前面的变量
# print(lambda r:math.pi*r*r)

# 对获取到的信息进行排序
# 书籍信息
book_info = [
    ("python 零基础入门", 22.5),
    ("java 零基础入门", 20),
    ("软件测试零基础入门", 25)
]
print(book_info)

# 指定规则进行排序
# lambda x:(x[1]) 返回了列表中每个元组的第二个元素
book_info.sort(key=lambda x:x[1])
print(book_info)
