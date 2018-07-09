#! python3
# 天天基金网，爬数据

import logging
import requests
import webbrowser as web

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))

 
timeOut = 200

url=r'http://fund.eastmoney.com/js/fundcode_search.js'

try:
    res=requests.get(url,timeout=timeOut)
except Exception as err:
    print(url.ljust(30,' ')+' status : 超时 time > '+str(timeOut))

try:
    res.raise_for_status()
except Exception as exc:
    print('网站不可用：%s' %(exc))


jijinTxt = open('jijinTxt.txt','wb')

for chunk in res.iter_content(100000):
    jijinTxt.write(chunk)
    
jijinTxt.close()

# use_chrome_open_url('www.163.com')

logging.debug('End   of program'.center(30,'-'))
