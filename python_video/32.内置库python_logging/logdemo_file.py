"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/7/19 4:27 下午'
"""
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')

logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')