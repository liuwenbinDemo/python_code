# -*- coding: utf-8 -*-
# @Author : feier
# @File : func_params.py

# *args 接收任意多个实际参数，并将其放到一个元组中
def print_language(*args):
    print(args)
    for i in args:
        print(i)


# 调用函数，把不同数量的参数传递进去，用位置参数
# print_language("python", "java")
# print_language("python", "java", "php", "go")

lan = ["python", "java", "php"]
# 等价为 print_language("python", "java", "php")
# print_language(*lan)

# 接收任意多个类似关键字参数一样显式赋值的实际参数
# 并将其放到一个字典中
def print_info(**kwargs):
    print(kwargs)

print_info(Tom=18, Lily=12)
print_info(Tom=18, Lily=12, Anna=16)

data = {
    "Tom":18,
    "Lily":12,
    "Jim":20
}
print_info(**data)
