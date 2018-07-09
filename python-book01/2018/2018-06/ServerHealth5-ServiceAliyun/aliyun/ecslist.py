# -*- coding: utf8 -*-
import pprint
import aliyunecs
import tools
import configRead

def giveColor(string,color=1):
    if color==1:
        return '<font color=red><strong>' + string + '</strong></font>'
    else:
        return '<font color=#DAA520><strong>' + string + '</strong></font>'


def addLine(ecs,ip=False,color=True):
    #ip=False 是隐藏EIP
    #color=True是上色
    line=[]
    line.append(ecs[0])
    line.append(ecs[1])
    if ip!=False:
        line.append(ecs[2])
    line.append(ecs[3])
    line.append(ecs[4])
    line.append(ecs[5])
    line.append(ecs[6])
    if color==True:
        line.append(giveColor(ecs[7],1))
    else:
        line.append(ecs[7])
    line.append(ecs[8])
    line.append(ecs[9])
    line.append(ecs[10])
    line.append(ecs[11])
    line.append(ecs[12])
    return line

def dayIn(days):
    ecsDays=configRead.readConfig('aliyun','ecsAlarm')
    if days<ecsDays[-1]:
        return True
        
    for i in ecsDays:
        if days==i:
            return True
        
    return False



def getEcslist():
    ecslists =aliyunecs.getAllaccountEcslist()
    ecslists.sort(key=lambda ecs:ecs[7])
    
    Ecslist=[]
    currentDay=tools.get_day()


    for i in ecslists:
        days=int(tools.day_cmp(i[7],currentDay))
        if ((dayIn(days)) and (i[12]==False)):
           Ecslist.append(addLine(i))
        else:
           Ecslist.append(addLine(i,False,False))
    
    Ecslist.insert(0,['账号','服务器','带宽','内网IP','CPU','MEM','到期日','类型','系统','状态','区域','是否过期'])
    Ecslist.append(['账号','服务器','带宽','内网IP','CPU','MEM','到期日','类型','系统','状态','区域','是否过期'])
    return Ecslist


#Ecslist=getEcslist()
#tools.writelisttohtml(Ecslist,'index.html')




