#! python3
# 自动检测各站点状态,需要读取webUrl

import pprint
import logging
import requests
import webbrowser as web
import webUrl

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))

def getUrl(url): #检测url给出状态反馈
        try:
            res=requests.get(url)
        except Exception as err:
            print(url.ljust(30,' ')+' status :  无法访问')
            return

        print(url.ljust(30,' ')+' status =',res.status_code,' time =',round(res.elapsed.total_seconds(),2))
        try:
            res.raise_for_status()
        except Exception as exc:
            #print('网站不可用：%s' %(exc))
            return

sites=list(webUrl.url.keys())

for i in range(len(sites)):

    
    print(sites[i])
    print('后台：')
    
    for k in range(len(webUrl.url[sites[i]][0])):
        logging.debug(webUrl.url[sites[i]][0][k])
        url = r'http://'+webUrl.url[sites[i]][0][k]
        getUrl(url)

    print('\nWeb：')
    for j in range(len(webUrl.url[sites[i]][2])):
        logging.debug(webUrl.url[sites[i]][2][j])
        url = r'http://'+webUrl.url[sites[i]][2][j]
        getUrl(url)

    print('\nAPI：')
    for h in range(len(webUrl.url[sites[i]][1])):
        logging.debug(webUrl.url[sites[i]][1][h])
        url = r'http://'+webUrl.url[sites[i]][1][h]
        getUrl(url)

    print()        
        



logging.debug('End   of program'.center(30,'-'))
