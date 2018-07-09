#功能：从扇贝背单词网上下载，生成到mp3path里
# http://media.shanbay.com/audio/us/hello.mp3 美式发音
# http://media.shanbay.com/audio/en/hello.mp3 英式发音

import csv
import os
import download
import time
import playsound


mp3path = r'second2/'
downloadSite = r'http://media.shanbay.com/audio/us/'

with open(r'worddict.txt','r',encoding='utf-8') as englishFile:
    line = englishFile.readline()
    worddict=open(r'worddict1.txt','a',encoding='utf-8')
    while line:
        print(line)
        line=line.strip('\n')
        line=line.lower()
        filename = mp3path+ line +'.mp3'
        mp3url = downloadSite +line +'.mp3'
        res=download.downloadfile(mp3url,filename)
        if len(res)<1:
            print("发现错误了："+str(err))
            worddict.write(line)
            
        time.sleep(0.3)
        line = englishFile.readline()

englishFile.close()



##    for i in englishReader:
##        print(str(englishReader.line_num) + str(i[5]))
##        if str(i[6])=="1":
##            filename = mp3path+ str(i[5]) +'.mp3'
##            mp3url = downloadSite +str(i[5]) +'.mp3'
##            download.downloadfile(mp3url,filename)
##            time.sleep(0.3)
            
            #playsound.playsound(mp3path+str(i[5]) +'.mp3', True)


