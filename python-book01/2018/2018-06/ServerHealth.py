#! python3
# 自动检测各服务器状态，包括CPU，内存，硬盘信息
# 

import logging
import requests
import ServerIP
import json

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))

timeOut = 0.5

def getUrl(url): #检测url给出状态反馈
        try:
            res=requests.get(url,timeout=timeOut)
        except Exception as err:
            #print(url.ljust(30,' ')+' status : 超时 time > '+str(timeOut))
            return ' status : 超时 time > '+str(timeOut)

        try:
            display =res.json()
        except Exception as err:
            #print("无法连接")
            return " status : 无法连接"

        sysinfo=''
        if 'CPU' in display.keys():
            sysinfo = 'Server:'+display['CPU']['CPU核心']+'C'+display['Memory']['总内存G']+'G, '
            logging.debug(sysinfo)
            sysinfo = sysinfo.ljust(15,' ') + 'CPU='+display['CPU']['CPU利用率'].ljust(3,' ')+' , '+'MEM='+display['Memory']['内存利用率']
            logging.debug(sysinfo)
            sysinfo = sysinfo.ljust(32,' ') + ' , DISK: '
            logging.debug(sysinfo)
            logging.debug(display['Disk'])
            logging.debug(display['Disk'].keys())

            for i in display['Disk']:
                diskstr = i.strip('硬盘')+ ':' +display['Disk'][i][0] + r'/'+display['Disk'][i][1]
                sysinfo = sysinfo + diskstr.ljust(12,' ')
            return sysinfo
            
        try:
            res.raise_for_status()
        except Exception as exc:
            #print('网站不可用：%s' %(exc))
            return '无法连接'

sites=list(ServerIP.ipDict.keys())
logging.debug(sites)

strInput =''

while strInput=='':
        for i in range(len(sites)):
            
            print(sites[i])
            for j in range(len(ServerIP.ipDict[sites[i]])):
                print(ServerIP.ipDict[sites[i]][j][0]+':')
                for k in range(1,len(ServerIP.ipDict[sites[i]][j])):
                    logging.debug(ServerIP.ipDict[sites[i]][j][k])
                    url = r'http://'+ServerIP.ipDict[sites[i]][j][k]+r':9999/?key=getinfo'
                    print(str(ServerIP.ipDict[sites[i]][j][k]).ljust(15,' ')+':'+str(getUrl(url)))

            print()
                
        print('Server health detection v0.1 按回车键继续，按其他键回车退出')
        strInput=input()


logging.debug('End   of program'.center(30,'-'))
