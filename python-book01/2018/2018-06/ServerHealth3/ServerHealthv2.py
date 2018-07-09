#! python3
# 自动检测各服务器状态，包括CPU，内存，硬盘信息
# 

import logging
import pprint
import configRead
import configparser
import tools            #个人常用过程模块，时间，日志
import getAlarm         #组织获取报警信息
import DingDingRobot    #钉钉报警
import getServerInfo    #获取服务器的状态信息

import htmlAlarm        #把list中需要报警的数字上色，还是返回list数据

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))



#导入config配置文件
ip=configRead.readConfig('server','ip')
sites=list(ip.keys())
logging.debug(sites)


infomationList = []   #搜集各服务器状态生成到这个list


#收集各服务器状态信息
for i in range(len(sites)):
    
    #print(sites[i])
    #取得各台子的名称
    taiziStr = sites[i]
    
    for j in range(len(ip[sites[i]])):
        functionStr =ip[sites[i]][j][0]
        
        for k in range(1,len(ip[sites[i]][j])):
            line=[]
            url = r'http://'+ip[sites[i]][j][k]+r':9999/?key=getinfo'
            line.append(taiziStr)
            line.append(functionStr)
            line.append(ip[sites[i]][j][k])
            line = line + list(getServerInfo.getStatus(url))
            infomationList.append(line)
            
    print('.')

#收集并发送报警
dingdingAlarmtxt = getAlarm.getAlarmstr(infomationList)


code = DingDingRobot.sendAlarm(dingdingAlarmtxt)
if code==0:
    print('send alarm ok!')
    tools.recordLog('send alarm ok!')
else:
    print('send err !')
    tools.recordLog('send alarm err!')
    

tools.recordLog(getAlarm.getAlarmstr(infomationList))

#报警数据上色，生成html
infomationList= htmlAlarm.color(infomationList) #上色

tools.listtohtml(infomationList)    #生成html





logging.debug('End   of program'.center(30,'-'))
