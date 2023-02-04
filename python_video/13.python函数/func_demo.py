# -*- coding: utf-8 -*-
# @Author : feier
# @File : func_demo.py

# 定义函数
def func_demo():
    # 函数体
    print("这是一个函数")


def func_with_params(a, b, c):
    '''
    这是一个携带参数和注释的函数
    '''
    print(f"传入的参数为：a={a},b={b},c={c}")

# 打印函数 comments 的内容
# print(func_with_params.__doc__)
# help(func_with_params)

# 定义空函数
def filter_char(s):
    '''
    功能：过滤敏感词
    '''
    # pass


def person(name, age, nationality="中国"):
    print(f"姓名为{name}")
    print(f"国籍为：{nationality}")
    if age >= 18:
        print(f"{name} 已成年")
    else:
        print(f"{name} 未成年")

# 指定参数默认值错误
# def wrong_demo(a=1, b, c):
#     pass

# 错误示范，默认值为空列表
# 默认值一定要用不可变对象，否则的话默认值可能会随着调用发生变化
# def wrong_demo2(a, b, c=[]):
#     c.append(a)
#     c.append(b)
#     print(a, b, c)

# wrong_demo2(1, 2)
# wrong_demo2(3, 4)

# 定义加法函数
def sum(a, b):
    result = a + b
    print(result)
    # 函数返回值
    return result, a, b

r = sum(1, 2)
print(r)

# 调用函数
# func_demo()
# 位置参数
# func_with_params(1, 2, 3)
# 位置参数错误例子，数量错误
# func_with_params(1, 2, 3, 4)
# func_with_params(2, 1, 3)
# 位置参数错误例子，顺序错误
# person(20, "lily")
# person("lily", 20)
# 关键字传参
# person(age=12, name="Tom",nationality="美国")

