#! python3
# P118 正则表达式

import re

# 第一个例子
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My phone num is 415-555-1234,and anthor is 432-666-5677')
print ('Phone number is :',mo.group())

# 例子2，分组
phoneNumRegex = re.compile(r'(\d{3})-\d{3}-\d{4}')
mo = phoneNumRegex.search('My phone num is 415-555-12-34,and anthor is 432-666-5677')

try:
    print ('Phone number is :',mo.group(2))
except IndexError:
    print ('Catch my frist error,current group is 1 = 432')

print(mo)
print(mo.group(0)) # mo.group(0) = mo.group() 相当于所有匹配串


# 例子3，所有匹配项findall()
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.findall('My phone num is 415-555-1234,and anthor is 432-666-5677')
print ('Phone number is :',mo)

# 例子4，.匹配除换行外的其他所有字符
phoneNumRegex = re.compile(r'.at')
mo = phoneNumRegex.findall('The cat in the hat sat on the flat mat.')
print ('Phone number is :',mo)

# 例子5，.*匹配任意字符，不包括回车
phoneNumRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo = phoneNumRegex.findall('First Name: jacky  Last Name: zhao ')
print ('Phone number is :',mo)

# 例子6，.*? 非贪心模式，匹配最短可能的字符串，，不包括回车
phoneNumRegex = re.compile(r'<.*?>')
mo = phoneNumRegex.search('< To server > no ip>')
print ('Phone number is :',mo.group())

# 例子7，.* 贪心模式，匹配最长可能的字符串，不包括回车
phoneNumRegex = re.compile(r'<.*>')
mo = phoneNumRegex.search('< To server > no ip>')
print ('Phone number is :',mo.group())

# 例子8，.* 加参数re.DOTALL可以任意字符，包括匹配回车
phoneNumRegex = re.compile(r'.*',re.DOTALL)
mo = phoneNumRegex.search('I \'am a student \n and I\'m a teacher,too.\n')
print ('Phone number is :',mo.group())

phoneNumRegex = re.compile(r'.*')
mo = phoneNumRegex.search('I \'am a student \n and I\'m a teacher,too.\n')
print ('Phone number is :',mo.group())

# 例子9，sub()方法替换要查找的模式文本
phoneNumRegex = re.compile(r'Agent \w+')
str1= 'Agent Alice gave the doc to Agent Bob'
str1= phoneNumRegex.sub('Jacky zhao',str1)
print(str1)
print('\n')

# 例子10，sub()方法替换要查找的模式文本,高级点替换警探的名字只保留第一个字母
phoneNumRegex = re.compile(r'Agent (\w)\w*')
str1= 'Agent Alice no1 gave the doc to Agent Bob no2'
str1= phoneNumRegex.sub(r'\1***',str1)  # \1 对应(\w) ，所以* 代替的 \w*
print(str1+'\n')






