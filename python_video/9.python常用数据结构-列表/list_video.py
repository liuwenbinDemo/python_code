"""列表使用：创建"""
# 1、构造方法 list()
# li = list()
# print(type(li), li)
# li1 = list('hogwarts')
# print(type(li1), li1)
# 2、中括号填充元素 []
# li2 = [1, 2, 3]
# li3 = ['hogwarts', 'hello']
# li4 = [1, 3.14, 'hogwarts', [5, 6, 7]]
# print(li4)
# 3、列表推导式
# li5 = [i for i in range(1, 10) if i % 2 == 0]
# print(type(li5), li5)

"""列表使用：索引"""
# li6 = [1, 2, 3, 4, 5]
# 1、正向索引
# print(li6[2])
# 2、反向作引
# print(li6[-3])
"""列表使用：切片"""
"""列表使用：运算符"""
# 1、* 号
# li7 = [1]
# print(li7 * 5)
# 2、+ 号
# li8 = [1, 2, 3]
# li9 = [4, 5, 6]
# print(li8 + li9)
"""列表使用：成员检测"""
# 1、in
# li10 = [1, 2, 3]
# print(1 in li10)
# print(100 in li10)
#
# print(1 not in li10)
# print(100 not in li10)
# 2、not in
"""列表方法"""
# li11 = []
# append(item)
# li11.append(1)
# li11.append('hogwarts')

# extend(iterable)
# li11.extend('hello')
# print(len(li11), li11)
# li12 = ['a', 'b', 'c']
# li11.extend(li12)
# print(len(li11), li11)

# insert(index, item)
# li13 = [1, 2, 3, 4, 5]
# li13.insert(0, 'hogwarts')
# print(li13)
# li13.insert(3, 'hello python')
# print(li13)

# pop(index)
li14 = [1, 2, 3, 4, 5]
# print(li14)
# li14.pop(1)
# print(li14)
# data = li14.pop()
# print(data, li14)
#
# li14.pop(99)
# li15 = []
# li15.pop()

# remove(item)
# li16 = ['a', 'b', 'c']
# li16.remove('c')
# print(li16)

# li16.remove('d')

# sort()
# li18 = [1, 2, 4, 8, 7]
# li18.sort()
# print(li18)
# li18.sort(reverse=True)
# print(li18)
# li19 = ['Python', 'java', 'Go', 'R']
# li19.sort(key=len)
# print(li19)


# reverse()
# li20 = ['a', 'd', 'c']
# li20.reverse()
# print(li20)

"""列表嵌套"""
# li21 = [[1, 2, 3], ['hogwarts', 'hello', 'Python']]
# print(li21[1][2])
# li21[1].append('Go')
# print(li21)


"""列表推导式"""
# for循环
result = []
for i in range(1, 11):
    if i % 2 == 0:
        result.append(i ** 2)
print(result)

# 列表推导式
result2 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(result2)

