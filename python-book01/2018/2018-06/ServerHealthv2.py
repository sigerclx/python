#! python3
# 自动检测各服务器状态，包括CPU，内存，硬盘信息
# 

import logging
import requests
import ServerIP
import json
import pprint

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))

timeOut = 0.5



def getUrl(url): #检测url给出状态反馈
        try:
            res=requests.get(url,timeout=timeOut)
        except Exception as err:
            #print(url.ljust(30,' ')+' status : 超时 time > '+str(timeOut))
            return ["超时 time >"+str(timeOut),"","",""]

        try:
            display =res.json()
        except Exception as err:
            #print("无法连接")
            return ["无法连接","","",""]

        sysinfo=''
        syslist=[]
        disktmp =''
        if 'CPU' in display.keys():

            syslist.append(display['CPU']['CPU核心']+'C'+display['Memory']['总内存G']+'G')

            cpu1 = display['CPU']['CPU利用率'].strip('%')
            if int(cpu1)>70:
                cpu1 = '<font color=red>'+cpu1+'</font>'
            mem1 = display['Memory']['内存利用率'].strip('%')
            if int(mem1)>60:
                mem1 = '<font color=red>'+mem1+'</font>'
            syslist.append('CPU='+cpu1+'%')
            syslist.append('MEM='+mem1+'%')
            

            disktmp = 'DISK: '
            logging.debug(sysinfo)
            logging.debug(display['Disk'])
            logging.debug(display['Disk'].keys())
        
            for i in display['Disk']:
                disknum1=display['Disk'][i][0].strip('G')
                disknum2=display['Disk'][i][1].strip('G')
                if (int(disknum1) <30) and (int(disknum2)) >20:
                    disknum1 = '<font color=#FF8C00>'+disknum1+'</font>'
                elif (int(disknum1)<10) and (int(disknum2))>20:
                    disknum1 = '<font color=red>'+disknum1+'</font>'
                print(disknum1)
                diskstr = i + ':' +disknum1 + r'/'+display['Disk'][i][1]+' '
                disktmp = disktmp + diskstr
            syslist.append(disktmp)
            syslist.append(display['version'])
            return syslist
            
        try:
            res.raise_for_status()
        except Exception as exc:
            #print('网站不可用：%s' %(exc))
            return ["无法连接","","",""]

def listtohtml(mylist):
    webUrlFile=open('Serverlist.html','w',encoding='utf-8')
    webUrlFile.write(r'''
        <style type=text/css>
        table.gridtable
            {
                font-family: verdana,arial,sans-serif;
                font-size:14px;
                color:#333333;
                border-width: 1px;
                border-color: #666666;
            }
        table.gridtable th {
                border-width: 1px;
                padding: 1px;
                border-style: solid;
                border-color: #666666;
                background-color: #dedede;
            }
        table.gridtable td {
                border-width: 1px;
                padding: 6px;
                border-style: solid;
                border-color: #666666;
                background-color: #ffffff;}
                
        </style>''')

    webUrlFile.write('\n<table class=gridtable align=\'left\'>\n')

    for t1 in mylist:
        webUrlFile.write('<tr>')
        for t2 in t1:
            webUrlFile.write('<td>'+t2+'</td>')
        webUrlFile.write('<tr>\n')
    webUrlFile.write('</table>')
    webUrlFile.close()    

sites=list(ServerIP.ipDict.keys())
logging.debug(sites)

strInput ='!'
infomationList = []

while strInput!='':
        for i in range(len(sites)):
            
            #print(sites[i])
            #取得各台子的名称
            taiziStr = sites[i]
            
            for j in range(len(ServerIP.ipDict[sites[i]])):
                functionStr =ServerIP.ipDict[sites[i]][j][0]
                
                for k in range(1,len(ServerIP.ipDict[sites[i]][j])):
                    line=[]
                    url = r'http://'+ServerIP.ipDict[sites[i]][j][k]+r':9999/?key=getinfo'
                    line.append(taiziStr)
                    line.append(functionStr)
                    line.append(ServerIP.ipDict[sites[i]][j][k])
                    line = line + list(getUrl(url))
                    infomationList.append(line)
                    
            print('.')
        listtohtml(infomationList)
                
        print('Server health detection v0.1 按回车键结束')
        strInput=input()


logging.debug('End   of program'.center(30,'-'))
