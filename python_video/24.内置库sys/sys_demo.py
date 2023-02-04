# help(sys)
# print(dir(sys))

"""sys模块常用方法"""

# 返回 Python 解释器版本
# print(sys.version)

# 返回操作系统平台名称
# print(sys.platform)

# 返回外部向程序传递的参数

# 返回已导入的模块信息
# print(sys.modules)

# print(sys.modules.keys())
# 返回导包的搜索路径列表
# print(sys.path)

# 添加自定义路径到导包路径列表中
# import os.path
# import sys
#
# my_dir = os.path.dirname(os.path.abspath(__file__)) + "/hello"
# sys.path.append(my_dir)
#
# from path_demo import hello
# hello()
#
# print(sys.path)
import sys

"""sys模块常用方法"""
# 获取系统当前编码
# print(sys.getdefaultencoding())

# 运行时退出
# sys.exit()
# sys.exit(0)
# sys.exit("error")

import time
for i in range(10):
    if i == 6:
        print("exit...")
        sys.exit("正常退出了")
    print(f'running{i}...')
    time.sleep(1)
