#! python3
# 文件夹遍历

import pprint
import gushi
import random
import copy

import os,zipfile
import logging

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial %s' % (n))
    total = 1
    for i in range (n+1):
        total *= (i+1)
        logging.debug('i is '+ str(i) +', total is ' + str(total))
    logging.debug('End of factorial %s ' % (n))
    return total

print(factorial(2))

logging.debug('End of program')


