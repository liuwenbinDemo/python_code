"""
__author__ = 'hogwarts_xixi'
"""
import datetime
# 时间格式
now = datetime.datetime.now()
# 转成字符串
c_time = now.strftime("%Y%m%d_%H%M%S")
print(c_time)

log_name = c_time+'.log'
with open(log_name, 'w+',encoding='utf-8') as f :
    # datetime [level] line: 13 this is a log message
    message = f"{now} [info] line: 14 this is a log message"
    f.write(message)