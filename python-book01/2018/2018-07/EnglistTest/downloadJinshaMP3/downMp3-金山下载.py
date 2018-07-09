#功能：利用金山API下载，生成到mp3path里
# 利用手输入的eng.csv里的单词列表，下载单词的mp3,放入dict文件夹


import csv
import os
import download
import time
import playsound
import searchwordApi


mp3path = r'dict/'
#with open('eng31.csv',encoding='utf-8') as englishFile:

k=0
with open('eng.csv') as englishFile:
    englishReader = csv.reader(englishFile)
    for i in englishReader:
        if str(i[6])=="1":
            k=k+1
            print('k='+str(k),end='')
            word=str(i[5])
            filename = mp3path+ str(i[5]) +'.mp3'
            
            mp3Url=searchwordApi.getwordMean(word)
            print(word)
            print(mp3Url)
            download.downloadfile(mp3Url['us_mp3'],filename)
            time.sleep(0.2)
            
            #playsound.playsound(mp3path+str(i[5]) +'.mp3', True)


