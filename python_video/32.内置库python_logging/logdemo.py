"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/19 4:22 下午'
"""
import logging
# logging 默认设置的级别 是warning
# 设置成哪个级别 ，就会打印这个级别 及以上级别的日志
logging.basicConfig(level=logging.DEBUG)

logging.debug("这是debug日志")
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
logging.error("这是一条error级别的日志")