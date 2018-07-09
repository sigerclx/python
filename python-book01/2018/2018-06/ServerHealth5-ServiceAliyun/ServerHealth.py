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
import globalvar as gl

import htmlAlarm        #把list中需要报警的数字上色，还是返回list数据
import alarmecs
import ecslist
import syncsql

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))


# 获取服务器健康信息
def getServerinfo():
    #导入config配置文件
    ip=configRead.readConfig('server','ip')
    #print(ip)
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
    return infomationList


def getsqlServer():
    #导入config配置文件
    sqlServerList=configRead.readConfig('DB','sqlserver')
    syncinfo=[]
    line=[]
    #print(sqlServerList)
    for i in sqlServerList['sync']:
        line.append(i[0])
        try:
            line.append(str(syncsql.getSyncSeconds(i)))
        except Exception as err:
            print(str(err))
            line='can\'t get info'
            tools.recordLog(str(err))
        syncinfo.append(line)
        line=[]
    tools.recordLog(str(syncinfo))
    htmlfile = configRead.readConfig('parameter','syncfile')
    tools.writelisttohtml(syncinfo,htmlfile)    #生成html

def health(plan=1):


    infomationList= getServerinfo()
    
    #过滤服务器状态报警
    dingdingAlarmDict = getAlarm.getAlarmDict(infomationList)
    dingdingAlarmDict.setdefault('ECSHealth','')
    
    
    #收集阿里服务器到期日报警

    #获取当前时间
    #
    escAlarmTime = configRead.readConfig('aliyun','AlarmTime')
    currentTime=tools.get_hour()
    print(currentTime)
    print(escAlarmTime)
    if ((currentTime>=escAlarmTime[0]) and (currentTime<=escAlarmTime[1])):
        print('ECS报警时段命中')
        print('报警时段:'+escAlarmTime[0] + escAlarmTime[1])
        currentDay = tools.get_day()
        print(currentDay)
        print(gl.getvalue('escSendday'))
        tools.recordLog('ECS报警时段命中')
        tools.recordLog(currentDay)
        tools.recordLog(gl.getvalue('escSendday'))
        if currentDay!=gl.getvalue('escSendday'):
            print('ECS收集，天不同')
            tools.recordLog('ECS收集信息，一天只能一次')
            try:
                ecsAlarmList = alarmecs.getAlarmEcs()
                print(ecsAlarmList)
                numAlarm=len(ecsAlarmList)
                print('有'+str(numAlarm)+'台ECS将要到期')
                tools.recordLog('有'+str(numAlarm)+'台ECS将要到期')
            except Exception as err:
                tools.recordLog("alarmecs.getAlarmEcs err : "+str(err))
                print(str(err))
            if numAlarm>0:
                print('ecs报警了')
                tools.recordLog('ecs>0报警了')
                gl.setvalue('escSendday', currentDay)
                dingdingAlarmDict['ECSHealth']='有'+str(numAlarm)+'台ECS将要到期'
                ecslists = ecslist.getEcslist()
                ecsfile = configRead.readConfig('aliyun','ecsfile')
                tools.writelisttohtml(ecslists,ecsfile)

    #print('打印MSG 字典')       
    #print(dingdingAlarmDict)       
    DingDingRobot.sendAlarm(dingdingAlarmDict,plan)

    tools.recordLog(str(dingdingAlarmDict))
    
    #报警数据上色，生成html
    infomationList1= htmlAlarm.color(infomationList,0) #上色
    htmlfile = configRead.readConfig('parameter','webfile')
    tools.writelisttohtml(infomationList1,htmlfile)    #生成html

    infomationList2= htmlAlarm.color(infomationList,1) #上色，带升级链接
    htmlfile = configRead.readConfig('parameter','webupdatefile')
    tools.writelisttohtml(infomationList2,htmlfile)    #生成html

    getsqlServer()
    tools.recordLog('同步数据获取完毕')


    logging.debug('End   of program'.center(30,'-'))


##gl.init()
##gl.setvalue('escSendday','')
##gl.setvalue('count','0')
##health(1)


