import csv
import os
import searchwordApi
import download
import time
import playsound

mp3path = r'second2/'

writefile=open('english.csv','w',newline='',encoding='utf-8')
writecsv=csv.writer(writefile)

with open('eng.csv',encoding='utf-8') as englishFile:
    englishReader = csv.reader(englishFile)


    for i in englishReader:
        line=i
        print(str(englishReader.line_num) + str(i[5]))
        if str(i[6])=="1":
            word= str(i[5])
            filename=mp3path+str(i[5])+'.mp3'
            wordmean=searchwordApi.getwordMean(word)
            if wordmean['mean']=='error':
                print(word+' is not found !')
                wordmean['mean']=''
        else:
            wordmean['mean']=''
            
            #print(wordmean['mean'][0])
        line.append(wordmean['mean'])
        writecsv.writerow(line)
            
        """    
        if len(wordmean['us_mp3'])<1:
            download.downloadfile(wordmean['en_mp3'],filename)
        else:
            download.downloadfile(wordmean['us_mp3'],filename)
        """
            
            #playsound.playsound(filename, True)
writefile.close()

