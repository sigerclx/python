#功能：从扇贝背单词网上下载，生成到mp3path里
# http://media.shanbay.com/audio/us/hello.mp3 美式发音
# http://media.shanbay.com/audio/en/hello.mp3 英式发音

import csv
import os
import download
import time
import playsound
import searchwordApi


mp3path = r'dict/'
#with open('eng31.csv',encoding='utf-8') as englishFile:
downloadSite = r'http://media.shanbay.com/audio/us/'

k=0
with open('eng.csv') as englishFile:
    englishReader = csv.reader(englishFile)
    for i in englishReader:
        if str(i[6])=="1":
            k=k+1
            print('k='+str(k),end='')
            word=str(i[5])
            filename = mp3path+ str(i[5]) +'.mp3'
            mp3Url=downloadSite+filename
            print(word)
            print(mp3Url)
            download.downloadfile(mp3Url,filename)
            time.sleep(0.2)
            
            #playsound.playsound(mp3path+str(i[5]) +'.mp3', True)


