"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/19 4:29 下午'
"""
import logging
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('is when this event was logged.')

# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('is when this event was logged.')

logging.basicConfig(filename='myapp.log',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
logging.debug("这是debug日志")
logging.info("这是debug日志")