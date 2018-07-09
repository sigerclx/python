# 本程序找出infomationList中告警数据（根据config中的告警值），并组合成一个大字符串，以备在钉钉中发出
import configRead
def getAlarmDict(infomationList):
    cpuAlarm = int(configRead.readConfig('alarm','cpuAlarm2'))       # CPU 利用率超70%报警   
    memAlarm = int(configRead.readConfig('alarm','memAlarm2'))       # MEM 利用率超70%报警    
    diskAlarm1 = int(configRead.readConfig('alarm','diskAlarm1'))     # 磁盘 剩余空间低于30G 报橙色警
    diskAlarm2 = int(configRead.readConfig('alarm','diskAlarm2'))     # 磁盘 剩余空间低于10G 报红色警

    alarmLine=[] 
    alarmList=[] #正常服务器报警列表
    alarmStatus=[] #服务器状态服务报警列表

    timeOut = configRead.readConfig('parameter','timeout')
    timeOutStr = '超时 time >'+str(timeOut)
    for line in infomationList:
            
        if line[3]==timeOutStr:
                alarmLine.append(line[0])
                alarmLine.append(line[1])
                alarmLine.append(line[2])
                alarmLine.append('状态服务'+str(timeOut)+'秒超时')
                alarmStatus.append(alarmLine)
                alarmLine=[]
                continue
        if int(line[4])>cpuAlarm:
                alarmLine.append(line[0])
                alarmLine.append(line[1])
                alarmLine.append(line[2])
                alarmLine.append('CPU='+line[4])
                alarmList.append(alarmLine)
                alarmLine=[]
        if int(line[5])>memAlarm:
                alarmLine.append(line[0])
                alarmLine.append(line[1])
                alarmLine.append(line[2])
                alarmLine.append('MEM='+line[5])
                alarmList.append(alarmLine)
                alarmLine=[]
        alldisk = line[6].split(' ')
        for d in alldisk:
            if d=='':   #排除空值
                continue
            disk=d.split(':')
            diskAvliable=disk[1].split(r'/')
            if (int(diskAvliable[0])<diskAlarm2) and (int(diskAvliable[1])>6): #剔除光驱
                  alarmLine.append(line[0])
                  alarmLine.append(line[1])
                  alarmLine.append(line[2])
                  alarmLine.append(disk[0]+'剩余'+diskAvliable[0]+'G')
                  alarmList.append(alarmLine)
                  alarmLine=[]

    #组合大字符串
    alarmdict={}
    dingdingAlarmTxt1=''
    dingdingAlarmTxt2=''
    for i in alarmList:
        dingdingAlarmTxt1 = dingdingAlarmTxt1 + i[0]+' '+i[1] + '：\n ' +i[2] + ' ' +i[3]+'\n'
    for j in alarmStatus:
        dingdingAlarmTxt2 = dingdingAlarmTxt2 + j[0]+' '+j[1] + '：\n ' +j[2] + '\n' +j[3]+'\n'
    alarmdict.setdefault('ServerHealth',dingdingAlarmTxt1)
    alarmdict.setdefault('SeviceHealth',dingdingAlarmTxt2)
    return alarmdict
