#! python3
# 程序的中间值保存

import shelve

shelfFile = shelve.open('mydata')
print(shelfFile['colors'])
shelfFile.close


