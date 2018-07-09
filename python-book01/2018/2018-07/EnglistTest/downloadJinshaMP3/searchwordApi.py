# 利用金山词霸的api解析单词含义和美式，英式发音，音标等
# 主要是调用getwordMean(word)，获得单词含义，MP3下载路径（美式，美式为空用英式发音）
import requests
import os
import json
import pprint

def createUrl(word):
    url_1=r'http://dict-co.iciba.com/api/dictionary.php?w='
    url_2=r'&type=json&key=6FDE7DE576DE770A91C94917D29BF37C'
    #print(url_1+word+url_2)
    if word.strip()=='':
        return ''
    return (url_1+word+url_2)

def analysisJinShanJson(meanJson):
    meanlist={}
    
    symbols=meanJson['symbols'][0]
    #print("symbols="+str(symbols))
    try:
        parts=symbols['parts']
    except Exception as err:
        return {'mean':[0,'json error'+str(err)]}

    mean=[]
    line={}
    #获取各类词形的含义
    for u in parts:
        line.setdefault(u['part'],u['means'])
        mean.append(line)
        line={}

    meanlist.setdefault('mean',mean)
    if len(symbols['ph_am_mp3'])<1:
        meanlist.setdefault('us_mp3',symbols['ph_en_mp3']) #英式MP3下载地址
    else:
        meanlist.setdefault('us_mp3',symbols['ph_am_mp3']) #美式MP3下载地址

    #meanlist.setdefault('us_mp3',symbols['ph_am_mp3']) #美式MP3下载地址
    meanlist.setdefault('en',symbols['ph_en']) #英式音标
    meanlist.setdefault('en_mp3',symbols['ph_en_mp3']) #英式MP3下载地址

    return meanlist

    

   
def getwordMean(word): 
    timeOut = 10
    
    word=word.lower()
    try:
        url =createUrl(word).strip()
        if url=='':
            return {'mean':[0,'word is empty']}
        res=requests.get(url,timeout=timeOut)
        #print(res)
    except Exception as err:
        print(str(err))
        return {'mean':[0,'word api error']}

    try:
        wordMean =res.json()
        wordMean = analysisJinShanJson(wordMean)
    except Exception as err:
        print(str(err))
        return {'mean':[0,'json resolve error']}

    return wordMean


#print(getwordMean('watch'))
#print(getwordMean('mm'))
#print(getwordMean('hm'))
#print(getwordMean('noodles'))
#print(getwordMean('CD'))
#print(getwordMean('aargh'))
#print(getwordMean('mrs'))

#print(getwordMean('cinema'))
#print(getwordMean('letter'))


