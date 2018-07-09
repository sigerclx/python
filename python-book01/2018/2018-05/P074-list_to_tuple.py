# 列表[]和元组()的转换
# list 和 tuple 之间的转换
# tuple 是只读的


aalist=[1,2,3]
aatuple = tuple(aalist)  # list转换为元组
print (aatuple)


bbtuple=['a','b','c']
aalist = list(bbtuple)  # 元组 转换为list 
print (aalist)

aalist[0]='aa'
print (aalist)
