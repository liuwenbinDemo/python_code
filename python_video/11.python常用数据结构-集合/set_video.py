"""集合创建"""
# 1、通过使用`{}`填充元素
# set1 = {1, 2, 3}
# print(set1, type(set1))

# 2、通过构造方法 set(iterable)
# set2 = set('hogwarts')
# print(set2, type(set2))
# set3 = set([1, 2, 3])
# print(set3, type(set3))
# set4 = set()
# print(set4, type(set4))

# 3、通过集合推导式
# set5 = {i for i in range(5) if i % 2 == 0}
# print(set5, type(set5))


"""集合使用"""
# set6 = {1, 4, 6}
# # # 1、in
# print(1 in set6)
# # # 2、not in
# print(100 not in set6)


"""集合方法"""
set7 = set()
'''add(item)'''
# set7.add(1)
# set7.add(2)
# set7.add('hogwarts')
# print(set7, type(set7))
'''update(iterable)'''
# set7.update('hogwarts')
# print(set7, type(set7))
# set7.update([1, 2, 3])
# print(set7, type(set7))
'''remove(item)'''
# 1、元素存在
set8 = {1, 2, 'hogwarts'}
# set8.remove(1)
# print(set8)
# 2、元素不存在会报错
# set8.remove(100)

'''discard(item)'''
# 1、元素存在
# set8.discard(1)
# print(set8)
# # 2、元素不存在
# set8.discard(100)

'''pop()'''
# set9 = {1, 2, 'hogwarts'}
# set9.pop()
# print(set9)
'''clear()'''
# set10 = {1, 2, 3, 4, 5}
# set10.clear()
# print(set10)

"""集合运算"""
a = {1, 3, 2}
b = {5, 1, 4}
# 1、交集运算 intersection &
# print(a.intersection(b))
# print(a & b)
# 2、并集运算 union |
# print(a.union(b))
# print(a | b)

# 3、差集运算 difference -
# print(a.difference(b))
# print(a - b)

"""
集合推导式 
实例：寻找hogwartsss 与 hello world 的共相同字母
"""
set10 = set()
for s in 'hogwartsss':
    if s in 'hello world':
        set10.add(s)
print(set10)

set11 = {s for s in 'hogwartsss' if s in 'hello world'}
print(set11)