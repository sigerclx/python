import csv
import os
import time
import playsound
import random
import pprint
import sys

mp3path = r'second2/'

#打开我自己生成的单词表，导入到words并且返回
def openmyWordBook(filename='english.csv'):
    with open(filename,encoding='utf-8') as englishFile:
        englishReader = csv.reader(englishFile)


        words=[]
        line=[]
        for i in englishReader:
            #print(str(englishReader.line_num) + str(i[5]))
            if str(i[6])=="1":
                word= str(i[5])
                mp3= mp3path+word+'.mp3'
                mean= str(i[-1])
            line.append(word)
            line.append(mean)
            line.append(mp3.lower())
            words.append(line)
            line=[]
    return words

random.shuffle(openmyWordBook())

#pprint.pprint(words)

##for i in words:
##    print(i[2])


for i in words:
    playsound.playsound(i[2], True)
    inputPress=input("根据发音输入答案：")
    while inputPress.upper()!=i[0].upper():
        playsound.playsound(i[2], True)
        print(i[1])
        inputPress=input("根据发音输入答案：")
        print("inputPress="+inputPress)
        if inputPress=='q':
            sys.exit(0)
    print('回答正确')

        
        


