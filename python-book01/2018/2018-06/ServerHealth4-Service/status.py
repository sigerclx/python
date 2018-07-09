#encoding=utf-8  
#纯windows Service

"""
pyinstaller -F -c --hiddenimport win32timezone status.py

-F 是生成一个独立exe
-c 是控制台程序

生成04_windowsService.exe 后，

可用04_windowsService install 安装服务，在到服务里启动即可

用sc delete 服务名 删除服务
"""
import win32serviceutil
import win32service
import win32event
import os
import io
import logging
import inspect
import servicemanager
import sys
import psutil
import json
import globalvar as gl
import tools
import ServerHealth
import configRead
import time


class Serversinfo(win32serviceutil.ServiceFramework):   
 
    _svc_name_ = "ServerStatus"  #服务名 
    _svc_display_name_ = "Servers status robot"  #服务在windows系统中显示的名称
    _svc_description_ = "收集服务器信息，报警 "+tools.get_time_stamp()  #服务的描述

  
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)   
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
        self.run = True
          
    def _getLogger(self):
        this_file = inspect.getfile(inspect.currentframe())  
        dirpath = os.path.abspath(os.path.dirname(this_file))  
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))
        
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')  
        handler.setFormatter(formatter)  
        
        tools.recordLog(str(handler))
       
        return ""  
  
    def SvcDoRun(self):
        
        tools.recordLog("Service start")
        
        time2=0
        timeCha=0  #执行扫描的时间差
        mingzhongtime=''
        while self.run:
            tools.recordLog("Server status "+ gl.getvalue('version') + ' is running at '+ tools.get_time_stamp())
            sleepsecond = configRead.readConfig('parameter','sleepsecond')
            runtime = configRead.readConfig('parameter','runtime')
            print(sleepsecond)
            print(runtime)
            tools.recordLog(str(sleepsecond))
            tools.recordLog(str(runtime))
            currentTime=tools.get_hour()
            tools.recordLog(str(currentTime))

            #plan=1时，按计划扫描，=0时，按定时间隔扫描
            plan=1
            time1=tools.get_hour()
            for i in runtime:
                tools.recordLog(str(tools.time_cmp(currentTime,i)))
                tools.recordLog(str(i))
                print("计划扫描时间"+i)
                print('时间差1：'+str(timeCha))
                if tools.time_cmp(currentTime,i)<(int(sleepsecond)+int(timeCha)):
                    tools.recordLog("计划扫描命中："+i)
                    print("计划扫描命中："+i)
                    print("上次命中计划："+mingzhongtime)
                    if i!=mingzhongtime:
                        print('currentTime='+currentTime)
                        print("上次命中计划："+mingzhongtime)
                        ServerHealth.health(plan)
                        plan=0
                        mingzhongtime=i
                    
                    
            if plan==1:
                print("周期扫描命中"+currentTime)
                tools.recordLog("周期扫描命中"+currentTime)
                ServerHealth.health(0)
                
            time2=tools.get_hour()
            timeCha = tools.time_cmp(time1,time2)
            print('时间差2：'+str(timeCha))
            time.sleep(int(sleepsecond))
            
        
              
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)   
        win32event.SetEvent(self.hWaitStop)
        self.run = False
        tools.recordLog("Service stop ...")
        
  
if __name__=='__main__':
    gl.init()
    gl.setvalue('version', 'v0.11')

    #报警的触发计数器
    gl.setvalue('count', '0')
##    time2=0
##    timeCha=0
##    mingzhongtime=''
##    while 1:
##        tools.recordLog("Server status "+ gl.getvalue('version') + ' is running at '+ tools.get_time_stamp())
##        sleepsecond = configRead.readConfig('parameter','sleepsecond')
##        runtime = configRead.readConfig('parameter','runtime')
##        print(sleepsecond)
##        print(runtime)
##        tools.recordLog(str(sleepsecond))
##        tools.recordLog(str(runtime))
##        currentTime=tools.get_hour()
##        tools.recordLog(str(currentTime))
##
##        #plan=1时，按计划扫描，=0时，按定时间隔扫描
##        plan=1
##        time1=tools.get_hour()
##        for i in runtime:
##            tools.recordLog(str(tools.time_cmp(currentTime,i)))
##            tools.recordLog(str(i))
##            print("计划扫描时间"+i)
##            print('时间差1：'+str(timeCha))
##            if tools.time_cmp(currentTime,i)<(int(sleepsecond)+int(timeCha)):
##                tools.recordLog("计划扫描命中："+i)
##                print("计划扫描命中："+i)
##                print("上次命中计划："+mingzhongtime)
##                if i!=mingzhongtime:
##                    print('currentTime='+currentTime)
##                    print("上次命中计划："+mingzhongtime)
##                    ServerHealth.health(plan)
##                    plan=0
##                    mingzhongtime=i
##                
##                
##        if plan==1:
##            print("周期扫描命中"+currentTime)
##            tools.recordLog("周期扫描命中"+currentTime)
##            ServerHealth.health(0)
##            
##        time2=tools.get_hour()
##        timeCha = tools.time_cmp(time1,time2)
##        print('时间差2：'+str(timeCha))
##        time.sleep(int(sleepsecond))

    
    if len(sys.argv) == 1:
        try:
            evtsrc_dll = os.path.abspath(servicemanager.__file__)
            servicemanager.PrepareToHostSingle(Serversinfo)
            servicemanager.Initialize('Serversinfo', evtsrc_dll)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error as details:
            tools.recordLog(str(details))
            print(str(details))
            pass
    else:
        win32serviceutil.HandleCommandLine(Serversinfo)
