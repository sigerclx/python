#! python3
# 文件夹遍历

import pprint
import gushi
import random
import copy

import os

for folderName,subFolders,fileNames in os.walk('D:\\doc\\工作\\python\\python-book01\\2018'):

    print('currentFolder:',folderName)
    for subfolder in subFolders:
        print('subFolder:',subfolder)
    for filename in fileNames:
        print('filename:',filename)

    print('')

