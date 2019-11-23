# 集合
a = {'open','close','high'}  #集合石无序的
b= [1,2,3]
c= dict()
j=0
for i in a:
    c[i]=b[j]
    j=j+1
print (c)

# 集合运算
set1={1,2,3,4,5}
set2={6,7,8,9,10}
set3={1,3,5,7,9}
print('并集：', set1|set2)
print('交集:',set1&set2)
print('差' ,set3-set2)
print('对称差' ,set3^set2)
print('是否无交集' ,set1.isdisjoint(set2))