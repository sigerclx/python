# 获取服务器的状态
import requests
import json
import configRead

def getStatus(url): #检测url给出状态反馈
        timeOut = int(configRead.readConfig('parameter','timeout'))
        try:
            res=requests.get(url,timeout=timeOut)
        except Exception as err:
            return ["超时 time >"+str(timeOut),"","","",""]

        try:
            display =res.json()
        except Exception as err:
            return ["无法连接","","",""]




        sysinfo=''
        syslist=[]
        disktmp =''

        if 'CPU' in display.keys():

            syslist.append(display['CPU']['CPU核心']+'C'+display['Memory']['总内存G']+'G')

            cpu1 = display['CPU']['CPU利用率'].strip('%')

            mem1 = display['Memory']['内存利用率'].strip('%')
            syslist.append(cpu1)
            syslist.append(mem1)
            

            disktmp = ''
            for i in display['Disk']:
                disknum1=display['Disk'][i][0].strip('G')
                disknum2=display['Disk'][i][1].strip('G')
                print('.',end='')
                diskstr = i + ':' +disknum1 + r'/'+disknum2+' '
                disktmp = disktmp + diskstr
            syslist.append(disktmp)
            syslist.append(display['version'])
            return syslist
            
        try:
            res.raise_for_status()
        except Exception as exc:
            #print('网站不可用：%s' %(exc))
            return ["无法连接","","",""]
