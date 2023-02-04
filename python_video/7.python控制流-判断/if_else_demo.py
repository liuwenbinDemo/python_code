# # 判断条件
# bob = "dev"
# if bob == "tester":
#     print("软件测试工程师")
# else的使用

# school = "hogwarts"
# if school == "hogwarts":
#     # 缩进问题
#     print("霍格沃兹测试开发")
# else:
#     print("测试开发")

# elif的使用
# food = "banana"
# color = "red"
# if food == "apple":
#     print("苹果")
#     if color == "red":
#         print("这是一个红色的苹果")
#
# # 分支嵌套需要注意缩进问题
# # 判断food == banana 且 color == red
# elif food == "banana" and color == "red":
#     print("香蕉")
#     if color == "red":
#         print("这是一个红色的香蕉")
#     else:
#         print("这是一个非红色的香蕉")
# elif food == "orange":
#     print("橘子")
# else:
#     print("food是其他食物")
#
# 三目运算符
a, b = 3, 2
# if a>b:
#     school = "hogwarts"
# else:
#     school = "hogwarts2"
# 赋值语句放在最前面  if 判断条件 else else需要赋值的内容
school = "hogwarts" if a>b else "hogwarts2"

print(school)
