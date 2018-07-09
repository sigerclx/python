# 本程序找出list中告警数据（根据config中的告警值），并组合成一个大字符串，以备在钉钉中发出
import configRead
def color(infomationList,link=0):
    cpuAlarm1 = int(configRead.readConfig('alarm','cpuAlarm1'))       # CPU 利用率超60%报警
    cpuAlarm2 = int(configRead.readConfig('alarm','cpuAlarm2'))       # CPU 利用率超90%报警
    memAlarm1 = int(configRead.readConfig('alarm','memAlarm1'))       # MEM 利用率超70%报警
    memAlarm2 = int(configRead.readConfig('alarm','memAlarm2'))       # MEM 利用率超95%报警
    diskAlarm1 = int(configRead.readConfig('alarm','diskAlarm1'))     # 磁盘 剩余空间低于30G 报橙色警
    diskAlarm2 = int(configRead.readConfig('alarm','diskAlarm2'))     # 磁盘 剩余空间低于10G 报红色警
    
    alarmList=[]

    timeOut = configRead.readConfig('parameter','timeout')
    timeOut = '超时 time >'+str(timeOut)
    for line in infomationList:
        alarmLine=[]
        alarmLine.append(line[0])
        alarmLine.append(line[1])
        #link==0,不上链接
        if link!=0:
            alarmLine.append(giveLink(line[2]))
        alarmLine.append(line[3])
        
        
        if line[3]==timeOut:
            alarmList.append(alarmLine)
            continue

      
        CPU = line[4]
        MEM = line[5]
        
        #CPU 报警处理    
        if int(line[4])>cpuAlarm1:
            CPU= giveColor(line[4],2)
        elif int(line[4])>cpuAlarm2:
            CPU= giveColor(line[4],1)
            
        CPU= 'CPU='+CPU+'%'
        alarmLine.append(CPU)

        #MEM 报警处理
        if int(line[5])>memAlarm1:
            MEM= giveColor(line[5],2)
        elif int(line[5])>memAlarm2:
            MEM= giveColor(line[5],1)
        MEM= 'MEM='+MEM+'%'
        alarmLine.append(MEM)

        alldisk = line[6].split(' ')
        diskstr="DISK: "
        for d in alldisk:
            if d=='':   #排除空值
                continue
            disk=d.split(':')
            diskAvliable=disk[1].split(r'/')
            if (int(diskAvliable[0])<diskAlarm2) and (int(diskAvliable[1])>6): #剔除光驱  
                diskstr = diskstr + disk[0]+':'+ giveColor(diskAvliable[0],1) +r'/'+diskAvliable[1]+' '
            elif (int(diskAvliable[0])<diskAlarm1) and (int(diskAvliable[1])>6): #剔除光驱:
                diskstr = diskstr + disk[0]+':'+ giveColor(diskAvliable[0],2) +r'/'+diskAvliable[1]+' '
            else:
                diskstr = diskstr + disk[0]+':'+ diskAvliable[0] +r'/'+diskAvliable[1]+' '


        alarmLine.append(diskstr)
        alarmLine.append(line[7])
    
        alarmList.append(alarmLine)
    return alarmList


def giveColor(string,color=1):
    if color==1:
        return '<font color=red><strong>' + string + '</strong></font>'
    else:
        return '<font color=#DAA520><strong>' + string + '</strong></font>'
		
def giveLink(string):
    backstr= r'<a href=http://'+string+':9999/?key=getinfo target=_blank>'+string+'</a>&nbsp;&nbsp;||&nbsp;&nbsp;'
    backstr= backstr + r'<a href=http://'+string+':9999/?key=download target=_blank>升级</a>'
    return backstr
