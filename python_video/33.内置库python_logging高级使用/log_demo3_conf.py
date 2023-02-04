"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/19 5:06 下午'
"""
import  logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("main")
logger.debug("这是debug日志")
