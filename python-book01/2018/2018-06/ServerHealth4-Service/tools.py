import datetime
import time
import os
import configRead
import winreg

def recordLog(strmsg,filename='alarm.log'): #把strmsg写入日志
    os.chdir(getPath())
    try:
        logFile = open(filename,'a')
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write(strmsg+'\n')
    except Exception as err:
        logFile.write(get_time_stamp()+'  ') #写入日志
        logFile.write('log write err:'+str(err)+'\n')
        pass
    finally:
        logFile.close()
    return


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

def get_hour():
    ct = time.time()
    local_time = time.localtime(ct)
    hourtime = time.strftime("%H:%M:%S", local_time)
    return hourtime	

def time_cmp(first_time, second_time):
    
    if (first_time==0) or (second_time==0):
        return 0
    if first_time<second_time:
       first_time, second_time = second_time, first_time
    return (datetime.datetime.strptime(first_time,"%H:%M:%S") - datetime.datetime.strptime(second_time,"%H:%M:%S")).seconds

def getPath():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Services\ServerStatus")
        downloadPath =winreg.QueryValueEx(key,"ImagePath")
        path=os.path.dirname(downloadPath[0][1:])
    except Exception as err:
        path=r'c:\windows\system32'
        recordLog('Path change err: '+ str(err))
    return path
	
def writelisttohtml(mylist,htmlfile):
    #htmlfile = configRead.readConfig('parameter','webfile')

    try:
        webUrlFile=open(htmlfile,'w',encoding='utf-8')
    except Exception as err:
        recordLog(str(err))
        return
        
    try:
        webUrlFile.write(r'''
                
<head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                </head>
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

        webUrlFile.write('<h2>'+get_time_stamp()+'</h2>\n')
        webUrlFile.write('\n<table class=gridtable align=\'left\'>\n')

        for t1 in mylist:
                webUrlFile.write('<tr>')
                for t2 in t1:
                        webUrlFile.write('<td>'+t2+'</td>')
                webUrlFile.write('<tr>\n')
        webUrlFile.write('</table>')
    except Exception as err:
            recordLog("write to html error")
            recordLog(str(err))
    finally:
            webUrlFile.close()


def listtohtmlupdate(mylist):
    htmlfile = configRead.readConfig('parameter','webupdatefile')

    try:
        webUrlFile=open(htmlfile,'w',encoding='utf-8')
    except Exception as err:
        recordLog(str(err))
        return
        
    try:
        webUrlFile.write(r'''
                
<head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                </head>
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

        webUrlFile.write('<h2>'+get_time_stamp()+'</h2>\n')
        webUrlFile.write('\n<table class=gridtable align=\'left\'>\n')

        for t1 in mylist:
                webUrlFile.write('<tr>')
                for t2 in t1:
                        webUrlFile.write('<td>'+t2+'</td>')
                webUrlFile.write('<tr>\n')
        webUrlFile.write('</table>')
    except Exception as err:
            recordLog("write to html error")
            recordLog(str(err))
    finally:
            webUrlFile.close() 
