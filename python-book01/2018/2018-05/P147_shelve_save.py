#! python3
# 程序的中间值保存

import shelve

shelfFile = shelve.open('mydata')
colors=['Blue','White','Black']
shelfFile['colors']=colors
shelfFile.close

print(shelfFile['colors'])
