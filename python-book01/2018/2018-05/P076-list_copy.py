# list的拷贝
# 对列表和字典，赋值只是引用
# 对字符串，整型，元组就是保存本身

import copy

print("是引用，一变全变")
str1 = [1,2,3,4]
str2 = str1  #是引用，一变全变

str1[1]=99
print (str1,str2)


print("是复制，各自独立")
str1 = [1,2,3,4]
str2 = copy.copy(str1)  #是复制，各自独立
str1[1]=99
print (str1,str2)

print("list第一级是复制，2级及以下是引用")
str1 = [1,2,3,[4,5,[6,7,8]]]
str2 = copy.copy(str1)  #list的第一级是复制，各自独立，2级及以下是引用
str1[1]=99
str1[3][1]=99
print (str1,str2)

print("list各级都是复制，各自独立")
str1 = [1,2,3,[4,5,[6,7,8]]]
str2 = copy.deepcopy(str1)  #是复制，各自独立
str1[1]=99
str1[3][1]=99
print (str1,str2)

