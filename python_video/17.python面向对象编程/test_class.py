# 创建一个人类
# 通过 class 关键字，进行定义了一个类
class Person:
    # 类变量
    name = 'default'
    age = 0
    gender = 'male'
    weight = 0

    # 构造方法， 在类实例化的被调用
    def __init__(self, name, age, gender, weight):
        # self。变量名的方式，访问的问题，叫做实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        print('__init__')

    # def set_param(self, name):
    #     self.name = name
    #
    # def set_age(self, age):
    #     self.age = age
    @classmethod
    def eat(self):
        print(f'{self.name}, eating')
        print('xxxxx')

    def play(self):
        print(f'{self.name}, playing')

    def jump(self):
        print(f'{self.name} ,jump')

# 类方法和实例方法
# 类方法是不能访问 实例方法
# 类方法需要添加一个装饰器classmethod
Person.eat()
# zs = Person('zhangsan', '20', '男', 130)
# zs.eat()
# 类变量和实例变量的区别，
# 类变量是需要类来访问， 实例变量是通过实例来访问的

# print(Person.name)
# Person.name = 'tom'
# print(Person.name)
#
zs = Person('zhangsan', '20', '男', 130)
# print(zs.name)
# zs.name = 'lili'
# print(zs.name)
# 类的实例化， 创建一个实例

# zs.set_param('zhangsan')
# zs.set_age(20)

print(f'zhangsan 的姓名是:{zs.name}, zhangsan 的年龄是：{zs.age}')

print(f'zhangsan 的性别是:{zs.gender}, zhangsan 的体重是：{zs.weight}')

ls = Person('lisi', '30', "男", 150)
ls.jump()
print(f'李四 的姓名是:{ls.name}, 李四 的年龄是：{ls.age}')

print(f'李四 的性别是:{ls.gender}, 李四 的体重是：{ls.weight}')
