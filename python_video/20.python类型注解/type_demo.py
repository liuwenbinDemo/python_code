"""
__author__ = 'hogwarts_xixi'
"""
# 类型提示功能
# 用法一：为参数与返回数据指定类型
# def greeting(name: str,age) -> str:
#     return 'Hello '+name

# 用法二：为类型起别名
from typing import List

# Vector = List[float]
#
# def scale(scalar: float, vector: Vector) -> Vector:
#     print(scalar,vector)
#     return [scalar * num for num in vector]
#
#
# print(scale(1.1, [1.2, -4.2, 5.4]))

## 用法三：指定自定义类型

# class Student:
#     name: str
#     age: int
#     def get_money(self):
#         print("")
#
#
# def get_stu(name: str):
#     return Student()

from typing import List
a: List[int] = []
a= [1,2,'aaa']



