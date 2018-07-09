key1=[1,2,3]
str1=['a','b','c']
print (key1)
print (key1*2)
print (key1*3)
key2 = key1 + str1
print (key2)

del key1[2]
print (key1)
key1[1]='aab'
print (key1)

print()
print("列表查找")
str2=[13,2,23,5]
print (str2.index(5))

print()
print("列表插入")
key1.insert(1,'a1')
print (key1)

print()
print("列表追加")
key1.append('ccc')
print (key1)

print()
key1.remove('ccc')
print (key1)

print()
print("列表排序-升序")
str2=[13,2,23,5]
str2.sort()
print (str2)

print()
print("列表排序-降序")
str2=[13,2,23,5]
str2.sort(reverse=True)
print (str2)




