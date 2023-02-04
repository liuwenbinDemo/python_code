"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/19 4:59 下午'
"""
import logging
import os

# 定义一个记录器
def get_logger():
    # create logger
    print(os.path.basename(__file__))
    # 记录器
    logger = logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    # 文件处理器
    ch = logging.FileHandler(filename='mylog.log', encoding="utf-8")
    ch.setLevel(logging.DEBUG)
    # create formatter
    # 定义格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return  logger

logger = get_logger()


def log_info(message):
    logger.info(message)

logger.debug('debug message')
# logger.info('info message')
log_info(" log info 方法")
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
