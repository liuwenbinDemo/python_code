# # 单行字符串
# str_a = "this"
# # 多行字符串
# str_b = """
# this is a school
# 霍格沃兹测试开发
# """
# print(str_a)
# print(str_b)
#
# hogwarts = "hogwarts \\n school"
# print(hogwarts)
# 字符串格式化符号
# print("hogwarts teacher is %f"%1.2)
# format 的使用
# demo = "hogwarts is a {school}"
# 第一个参数放在0的位置，第二个参数放在1的位置
# demo_res = demo.format("very good", "school")
# demo_res = demo.format(school="very good")
# demo 是原始的变量内容
# print(demo)
# demo_res 是替换过后的变量内容
# print(demo_res)
# python3.6.5之后支持的一个语法
# name = "AD"
# 字符串前面添加f ，变量使用{变量名}
# print(f"my name is {name}")

# join的使用, 列表，根据想要的格式拼接成字符串
# a = ["a", "p", "p", "l", "e"]
# print("|".join(a))
# # split 的使用，将字符串根据规定的内容进行切分。以什么内容进行切分，那么这个内容也会没有
# b = "hogwarts school"
# print(b.split(" "))
# replace 将目标内容，替换为 想要替换的内容
# c = "my name is ad"
# print(c.replace("m", "M"))

d = " my name is ad "
print(d)