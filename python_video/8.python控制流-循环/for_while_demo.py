# a = [1,2,3,4,5] # 元祖，字符串， 字典， 可迭代元素
# for i in a:
#     print(i)
# range(11) [0,1,2,3,...,10]
# 当range只传入一个参数的时候，传入的是 结束数值 ，遵循前闭后开原则
# 当range传入两个参数的时候，（开始数值， 结束数值） 2<=i<12
# # 当range传入三个参数的时候，（开始数值， 结束数值, 步长） 2<=i<12
# for i in range(2, 12, 3):
#     print(i)


# a = 1
# while a<6:
#     print(a)
#     a = a+1
#     # 1. 不要直接使用 2. 注意设定的跳出条件
#     if a == 3:
#         break

# list_a = [1,2,3,4,5,6]
# for i in list_a:
#     print(i)
#     #     # 1. 不要直接使用 2. 注意设定的跳出条件
#     if i == 3:
#         break

# b = 1
# while b<6:
#     if b == 3:
#         b = b+2.1
#         continue
#     b = b+1
# print(b)

# list_b = [1, 2, 3,4,5]
# for i in list_b:
#     if i == 3:
#         continue
#     print(i)

# 计算1~100 求和
# 使用分支结构实现1~100之间的偶数求和
# sum = 0
# for i in range(1, 101):
#     # 对i取余，如果余数为0，则证明i为偶数
#     if i%2 == 0:
#         sum = sum + i
#         print(sum)
# 不使用分支结构实现1~100之间的偶数求和
# sum = 0
# for i in range(0, 101, 2):
#     sum = sum+i
#     print(sum)

# 猜数字游戏
# 计算机出一个1~100之间的随机数由人来猜
# 计算机根据人猜的数字分别
# 给出提示大一点/小一点/猜对了
# 计算机产生的数字，
import random

computer_num = random.randint(1, 100)
# print("computer_num", computer_num)

while True:
    people_num = int(input("请输入数字："))
    # 当计算机数字大于人猜的数字的时候，提示大一点
    if computer_num>people_num:
        print("大一点")
    elif computer_num<people_num:
        print("小一点")
    else:
        print("猜对啦")
        break
