#! python3
# P148 古诗 把TXT的古诗作者，整理成字典存于gushi.py

import os
import pprint

gushiTXT = open('gushi.txt')

gushilines = gushiTXT.readlines()

gushi={}

for str1 in gushilines:
    str1=str1.strip('\n')
    str2 = str1.split(' ')
    str3= []
    str3.append(str2[1])
    str3.append(str2[2])
    print(str3)
    gushi[str2[0]]=str3

print(gushi)

file=open('gushi.py','w',encoding='utf-8')
file.write('gushi ='+pprint.pformat(gushi)+'\n')
file.close()


