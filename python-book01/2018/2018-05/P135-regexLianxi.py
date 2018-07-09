#! python3
# P135 正则表达式 练习题

import re

# 第一个例子

phoneNumRegex = re.compile(r'[A-Z]\w+ Nakamato')
print(phoneNumRegex.search('sstat Nakamato'))
print(phoneNumRegex.search('Sstat Nakamato'))   # 只有这个匹配成功
print(phoneNumRegex.search('Mr.Nakamato'))
print(phoneNumRegex.search('Nakamato'))
print(phoneNumRegex.search('Wddf nakamato'))
print('\n')

# 第二个例子，检测强口令

pwd='Nakamato1'
phoneNumRegex = re.compile(r'[a-z]+')
print(phoneNumRegex.search(pwd)!=None)

phoneNumRegex = re.compile(r'[A-Z]+')
print(phoneNumRegex.search(pwd)!=None)

phoneNumRegex = re.compile(r'\d+')
print(phoneNumRegex.search(pwd)!=None)




