"""普通方法"""
# #1. 定义
# class MethodsDemo:
#     param_a = 0 #类变量
#     def normal_demo(self): # 定义一个类方法，第一个参数必须为self
#         """
#         普通方法
#         :return:
#         """
#         print("这是一个普通方法", self.param_a)
# # 2. 调用
# md = MethodsDemo()
# md.normal_demo()

"""
类方法
"""


# 定义
class MethodClass:

    CLASS_PARAM = 0

    def __init__(self):
        self.a = "abc"

    def demo_method(self):
        print("这是一个普通方法")

    def demo_method2(self):
        self.demo_method()
        print("这是一个普通方法")

    @classmethod
    def class_method(cls):
        # cls.demo_method() # 类方法内，不可以直接调用实例方法，实例变量
        cls.class_method2() # 类方法内，可以直接调用类变量与类方法
        print("这是一个类方法", cls.CLASS_PARAM)

    @classmethod
    def class_method2(cls):
        # cls.demo_method() # 类方法内，不可以直接调用实例方法，实例变量
        print("这是一个类方法2", cls.CLASS_PARAM)

# 调用
# MethodClass.class_method()
# 在调用过程中，类和实例都可以直接调用类方法
# demo = MethodClass()
# demo.class_method()
"""
静态方法
"""

class StaticMethod:

    @classmethod
    def class_method(cls):
        # cls.demo_method() # 类方法内，不可以直接调用实例方法，实例变量
        print("这是一个类方法")

    def demo_method(self):
        print("这是一个普通方法")

    # 定义： 1. 要使用staticmethod 装饰器 2. 这个方法是没有 self、 或者cls
    @staticmethod
    def static_demo(param1):
        print("这是一个静态方法", param1)

# 调用： 类.方法名
StaticMethod.static_demo("hogwarts")
demo = StaticMethod()
demo.static_demo("hogwarts2")



