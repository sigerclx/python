#功能：从扇贝背单词网上下载，生成到mp3path里
# http://media.shanbay.com/audio/us/hello.mp3 美式发音
# http://media.shanbay.com/audio/en/hello.mp3 英式发音

import csv
import os
import download
import time
import playsound
import searchwordApi
import os


#with open('eng31.csv',encoding='utf-8') as englishFile:

mydict=[]
line=[]
k=0
with open('eng.csv') as englishFile:
    englishReader = csv.reader(englishFile)
    for i in englishReader:
        #print(str(englishReader.line_num) + str(i[5]))
        if str(i[6])=="1":
            k=k+1
            word=str(i[5])
            wordmean=searchwordApi.getwordMean(word)
            #print(word)
            path=r'dict1/'+word+r'.mp3'
            #print(path)
            print(k)
            if os.path.exists(path)==False:
                print('单词找不到：'+word)
            if wordmean['mean'][0]==0:
                print(word)
                print('\n-------查不到该单词\n!')
            else:
                line=i
                line.append(wordmean['mean'])
                line=mydict.append(line)


writeFile=open('EnglishALl.csv','w',newline='')
csvWriter=csv.writer(writeFile)
for i in mydict:
    csvWriter.writerow(i)
writeFile.close()

#print(len(mydict))
#mydict= list(set(mydict))
#print(len(mydict))
            
            #playsound.playsound(mp3path+str(i[5]) +'.mp3', True)


