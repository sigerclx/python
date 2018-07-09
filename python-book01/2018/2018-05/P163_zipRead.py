#! python3
# 文件夹遍历

import pprint
import gushi
import random
import copy

import os,zipfile

os.chdir('d:\\')
exampleZip = zipfile.ZipFile('2018-05.zip')
pprint.pprint(exampleZip.namelist())

fileInfo=exampleZip.getinfo('2018-05/myCats.py')
print(fileInfo.file_size);


# 解压缩

exampleZip.extractall()
exampleZip.close()
