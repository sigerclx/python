# 字典数据类型的使用，键值对
import pprint
str1={'a':1,'b':[1,2,3],'c':3}
print (str1['b'])

#判断要找的key是否在字典数据里
print("\n判断要找的key是否在字典数据里")
if 'd' in str1.keys():
    print ("in")
else:
    print ("no")

#打印所有键值对
print ("\n打印所有键值对")
for v in str1.items():
    print (v)
    
#打印所有值
print ("\n打印所有值")
for v in str1.values():
    print (v)


#字典get方法  
print ("\n字典get方法")
print(str1.get('e'))
print(str1.get('e',0))
pprint.pprint(str1)

#字典Setdefault方法
#统计字典message里每个字符的出现次数，并打印
print ("\n统计字典message里每个字符的出现次数，并打印")
message='It was a bright cold day in April, and the clocks were striking thireen.'
count={}
for char in message:
    count.setdefault(char,0)
    count[char]=count[char]+1

pprint.pprint(count) #pprint.pprint(count)等价于print(pprint.pformat(count))

