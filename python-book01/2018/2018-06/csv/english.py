import csv
import os
import download
import time
import playsound

mp3path = r'second2/'
downloadSite = r'http://media.shanbay.com/audio/us/'
with open('eng.csv',encoding='utf-8') as englishFile:
    englishReader = csv.reader(englishFile)


    for i in englishReader:
        print(str(englishReader.line_num) + str(i[5]))
        if str(i[6])=="1":
            filename = mp3path+ str(i[5]) +'.mp3'
            webmp3 = downloadSite +str(i[5]) +'.mp3'
            print(downloadSite)
            download.downloadfile(webmp3,filename)
            time.sleep(0.3)
            #playsound.playsound(mp3path+str(i[5]) +'.mp3', True)


