"""字典使用：创建"""
# 1、使用大括号填充键值对
# dc1 = {"name": "Harry Potter", "age": 18}
# print(type(dc1), dc1)
# dc2 = {}
# print(type(dc2), dc2)
# 2、使用字典构造方法
# dc3 = dict()
# print(type(dc3), dc3)
# dc4 = dict([("name", "Harry Potter"), ("age", 18)])
# print(dc4, type(dc4))
# 3、使用字典推导式
# dc5 = {k: v for k, v in [("name", "Harry Potter"), ("age", 18)]}
# print(type(dc5), dc5)

"""字典使用：访问元素"""
# dc6 = {"name": "Harry Potter", "age": 18}
# 1、访问存在的key
# print(dc6['name'])

# 2、访问不存在的key，会报KeyError错误
# print(dc6['hobby'])

# dc6['age'] = 20
# print(dc6)
#
# dc6['hobby'] = 'Magic'
# print(dc6)


"""字典方法"""
# dc7 = {"name": "Harry Potter", "age": 18}
'''keys(),values(),items()'''
# print(dc7.keys())
# print(dc7.values())
# print(dc7.items())
#
# print(list(dc7.keys()))
# print(list(dc7.values()))
# print(list(dc7.items()))

'''get()'''
# dc8 = {"name": "Harry Potter", "age": 18}
# # 1、访问存在的key
# print(dc8.get('name'))
# print(dc8.get('age'))
# # 2、访问不存在的key
# print(dc8.get('hobby'))

'''update()'''
# dc9 = {"name": "Harry Potter", "age": 18}
# data = {"age": 20, "hobby": "magic"}
# dc9.update(data)
# print(dc9)

'''pop()'''
# dc10 = {"name": "Harry Potter", "age": 18}
# # 1、已经存在的key
# val = dc10.pop('age')
# print(val)
# print(dc10)
#
# # 2、不存在的key
# dc10.pop('hobby')

"""字典推导式 {k:v for k, v in ...}"""
# 例子2
# dc11 = {k: v for k, v in [("name", "Harry Potter"), ("age", 18)]}
# print(type(dc11), dc11)

# 例子2
# dc12 = {'a': 1, 'b': 2, 'c': 3}
#
# data = dict()
# for k, v in dc12.items():
#     if v > 1:
#         data[k] = v ** 2
# print(data)
#
# data2 = {k: v ** 2 for k, v in dc12.items() if v > 1}
# print(data2)

"""
给定一个字典对象，请使用字典推导式，将它的key和value分别进行交换。也就是key变成值，值变成key。

输入: {'a': 1, 'b': 2, 'c': 3}
输出: {1: 'a', 2: 'b', 3: 'c'}
"""
data = {'a': 1, 'b': 2, 'c': 3}
result = {v: k for k, v in data.items()}
print(data)
print(result)