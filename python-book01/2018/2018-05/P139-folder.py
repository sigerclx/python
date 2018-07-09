#! python3
# 目录操作
import os

print (os.getcwd())

os.chdir('d:\\')

print (os.getcwd())

os.chdir('D:\\doc\\工作\\python\\python-book01\\2018\\2018-05')

print (os.path.getsize('P118-regex.py'))

# 列出当前文件夹的所有文件
print (os.listdir(os.getcwd()))
