# num = 1
# if num >= 1:
#     print("num <= 1")
# elif num > 100:
#     print("num < 100")
#
# list1 = [1,2,3]
# print(list1[0])
# #
# dict1 = {'name': 'tom'}
# print(dict1['age'])
#
# num = input('输入一个值：')
# print(int(num))


# def div(a, b):
#     return a / b
#
#
# # print(div(1, 0))
#
# f = open('data.txt')
# try:
#     print(div(1, 1))
#     list1 = [1, 2, 3]
#     print(list1[2])
#     f.readlines()
# except Exception as e:
#     print(e)
#     print("这里有一个异常")
# else:
#     print('没有异常的情况')
# finally:  # finally 最终都会被执行，无论 有一场还是没有异常的情况
#     print("finally")
#     f.close()


# def set_age(num):
#     if num <= 0 or num > 200:
#         raise ValueError(f"值错误{num}")
#
#     else:
#         print(f'设置的年龄位{num}')

# set_age(80)


class MyException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常：{msg}")


def set_age(num):
    if num <= 0 or num > 200:
        raise MyException(f"值错误{num}")


set_age(-10)
