import os
#遍历目录，filename是一个List，而不是str
for folder,subfolder,filename in os.walk(r'yanzheng_pic'):
    print (filename)

print (filename)