"""
__author__ = 'hogwarts_xixi'
"""
# 第一步：（以只读模式）打开文件
f = open('data.txt', 'r', encoding='utf-8')

# 第二步：读取文件内容
# 换行符会占一个字符
# print(f.read(15))
# result = f.read()
# print(type(result))
# 读完一次之后，再次读取文件，内容将不是完整的，需要重新设置游标位置
# 设置游标的位置
# f.seek(0)
# result1 = f.readlines()
# print(type(result1))
# print(result1)
print(f.readline())
print(f.readline())


# 第三步：关闭文件
f.close()