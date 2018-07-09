#! python3
# 自动检测各站点状态,需要读取webUrl,引用P190_CreateWeblist2
# 

import logging
import requests
import webUrl
import P190_CreateWeblist2

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))

timeOut = 0.5

def getUrl(url): #检测url给出状态反馈
        try:
            res=requests.get(url,timeout=timeOut)
        except Exception as err:
            print(url.ljust(30,' ')+' status : 超时 time > '+str(timeOut))
            return

        print(url.ljust(30,' ')+' status =',res.status_code,' time =',str(round(res.elapsed.total_seconds(),2)).ljust(4,' '),'秒')
        try:
            res.raise_for_status()
        except Exception as exc:
            #print('网站不可用：%s' %(exc))
            return

sites=list(webUrl.urlDict.keys())
logging.debug(sites)

strInput =''

while strInput=='':
        for i in range(len(sites)):
            
            print(sites[i])
            for j in range(len(webUrl.urlDict[sites[i]])):
                print(webUrl.urlDict[sites[i]][j][0]+':')
                for k in range(1,len(webUrl.urlDict[sites[i]][j])):
                    logging.debug(webUrl.urlDict[sites[i]][j][k])
                    url = r'http://'+webUrl.urlDict[sites[i]][j][k]
                    getUrl(url)

            print()
                
        print('Web health detection v0.13 按回车键继续，按其他键回车退出')
        strInput=input()


logging.debug('End   of program'.center(30,'-'))
