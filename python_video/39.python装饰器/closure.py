"""
闭包函数： 霍格沃兹开学啦，要求打印每个学生的姓名、性别、年级
"""
# # 函数引用
# def hogwarts():
#     print("霍格沃兹测试学社")
# # hogwarts() # 函数的调用
# # print(hogwarts)
# # print("==========")
# # harry = hogwarts # 把函数对象赋值给一个变量
# # print(harry)
# peter = hogwarts
# print(peter)
# peter()

# def output_students(name, gender, grade):
#     print(f"霍格沃兹开学啦， 学生名称是{name}，性别是{gender}， 年级是{grade}年级")
#
# output_students("哈利", "男生", 2)
# output_students("罗恩", "男生", 2)
# output_students("赫敏", "女生", 2)

def students_grade(grade):
    # 闭包无法修改外部函数的局部变量
    grade = "2"
    print("外函数的年级为", grade)
    def output_students(name, gender):
        grade = "1"
        print("内函数的年级为", grade)
        # print(f"霍格沃兹开学啦， 学生名称是{name}，性别是{gender}， 年级是{grade}年级")
    return output_students


students_info = students_grade(1)
students_info("罗恩", "男生")
students_info("哈利", "男生")
students_info("赫敏", "女生")
