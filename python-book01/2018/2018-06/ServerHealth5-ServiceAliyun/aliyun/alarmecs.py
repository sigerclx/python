# -*- coding: utf8 -*-
#本模块只解决ecs到期报警信息的问题
import pprint
import aliyunecs
import tools
import configRead

def giveColor(string,color=1):
    if color==1:
        return '<font color=red><strong>' + string + '</strong></font>'
    else:
        return '<font color=#DAA520><strong>' + string + '</strong></font>'


def addLine(ecs,ip=False,color=False):
    #ip=False 是隐藏EIP
    #color=True是上色
    line=[]
    line.append(ecs[0])
    line.append(ecs[1])
    if ip!=False:
        line.append(ecs[2])
    line.append('到期日')
    line.append(ecs[7])
    return line

def dayIn(days):
    ecsDays=configRead.readConfig('aliyun','ecsAlarm')
    if days<ecsDays[-1]:
        return True
        
    for i in ecsDays:
        if days==i:
            return True
        
    return False

def getAlarmEcs():
    ecslists =aliyunecs.getAllaccountEcslist()

    alarmEcs=[]

    currentDay=tools.get_day()


    for i in ecslists:
        days=int(tools.day_cmp(i[7],currentDay))
        if ((dayIn(days)) and (i[12]==False)):
           alarmEcs.append(addLine(i))
    alarmEcs.sort(key=lambda ecs:ecs[3])

    return alarmEcs

#alarmEcs=getAlarmEcs()

#本模块只解决报警信息的问题
#tools.writelisttohtml(alarmEcs,'ecs.html')


#print(ecslist)



#print(aliyun.getEcs(client))
#pprint.pprint (response)
