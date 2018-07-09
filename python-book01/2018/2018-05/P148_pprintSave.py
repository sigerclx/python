#! python3
# P148 pprint.pformat保存变量

import pprint
import os

cats=[{'name':'Zophine','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
pprint.pprint(cats)


fileObj=open('myCats.py','w')
fileObj.write('cats='+pprint.pformat(cats)+'\n')
fileObj.close()


fileObj=open('myCats.py','r')
txt=fileObj.readlines()
print(txt[0])
