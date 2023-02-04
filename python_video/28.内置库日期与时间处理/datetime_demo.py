"""
__author__ = 'hogwarts_xixi'
"""
import datetime
# 当前日期时间
# nowtime = datetime.datetime.now()
# print(nowtime)
# print(nowtime.day)
# print(nowtime.month)
# print(nowtime.year)
# # 转成时间戳
# print(nowtime.timestamp())
#
# print(datetime.datetime(2021, 10, 10))

# s = "2021-09-27 06:47:06"
# # 将字符串 转换为datetime实例
# s1 = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
# print(s1)
# print(type(s1))
# # 时间转成字符串
# result = s1.strftime('%a  %b  %d %H:%M')
# print(result)
mtimestamp = 1632725226.129461
# 时间戳-> 时间
s = datetime.datetime.fromtimestamp(mtimestamp)
print(s)
# 将时间->时间戳
print(s.timestamp())