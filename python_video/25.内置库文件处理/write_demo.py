"""
__author__ = 'hogwarts_xixi'
"""
# # w+ 会清空，再写入，如果没有文件，会创建新文件
# with open('data1.txt','w+',encoding='utf-8') as f:
#     print(f.write('格兰芬多'))
#     # hello world!

# a+ 会在最末尾的位置，追加数据，不清空原来的内容
with open('data1.txt','a+',encoding='utf-8') as f:
    print(f.write('\n赫敏'))
    # hello world!