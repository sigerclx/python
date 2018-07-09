#! python3
# 远程取得API信息
# 

import logging
import requests
import json
import pprint
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))

timeOut = 5

def getUrl(url): #检测url给出状态反馈
        try:
            res=requests.get(url,timeout=timeOut)
        except Exception as err:
            print(url.ljust(30,' ')+' status : 超时 time > '+str(timeOut))
            return

        print(url.ljust(30,' ')+' status =',res.status_code,' time =',str(round(res.elapsed.total_seconds(),2)).ljust(4,' '),'秒')
        
        display =res.json()
        sysinfo=''
        if 'CPU' in display.keys():
            sysinfo = display['CPU']['CPU核心']+'C'+display['Memory']['总内存G']+'G'
            sysinfo = sysinfo + ' ['+display['CPU']['CPU利用率']+'] '+'['+display['Memory']['内存利用率']+']'

        

        try:
            res.raise_for_status()
        except Exception as exc:
            print('服务不可用：%s' %(exc))
            return

        return sysinfo
        
#getUrl(r'http://183.111.122.219:90/?age=1')
#print(getUrl(r'http://13.112.4.16:90/?age=113s'))
      
print(getUrl(r'http://127.0.0.1:91/?age=getinfo'))


logging.debug('End   of program'.center(30,'-'))
