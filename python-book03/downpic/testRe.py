import re
strbody= '<div class="main-meta"> <span>分类：<a href="https://www.mzitu.com/xinggan/" rel="category tag">性感妹子</a></span> \
<img src="https://i5.meizitu.net/2019/08/06b01.jpg" alt > <div class="pagenavi"> ok bye'

pat1 = '(src=).+(.jpg)'
#<div class="pagenavi">
print (strbody)
result = re.search(pat1,strbody)
print (result.group())

str1='https://www.mzitu.com/197208/11'
print (str.split(str1,'/')[-1])

print(2%100)
i=0
for i in range(1,1000):
    print (i)
    if (i%100==0):
        print ('zhong')