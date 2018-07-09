# 字符串的各种玩法
import pyperclip
name = 'Jackyzhao'

#以xx开始
print (name.startswith('Jac'))

#以xx结束
print (name.endswith('ao'))

print ('Jac' in name)
print ('ack' in name)
print ('Ack' in name)


for i in name :
    print ('---'+i+'----')


# join()

print('|'.join(['a','b','c','d']))


# split()

print('1|-3|-4|-6|-7|-9|-0'.split('|-'))


# strip()去两边字符，默认空格

name = 'abcabc Jackyzhao abcabc'
print(name.strip('abc'))


# 拷贝字符串
pyperclip.copy("http://www.baidu.com")  # 拷贝进内存
print(pyperclip.paste())        # 把粘贴内容打印出来


