#-*- coding: utf-8 -*-
import configparser
import os
import winreg
import tools

# 读取config.ini 获取字典返回值 eval 把字符串转为字典
def readConfig(group,key):
    os.chdir(getPath())
    cp = configparser.SafeConfigParser()
    value =""
    try:
        cp.read('config.ini',encoding='utf-8')
        value = eval(cp.get(group,key))
    except Exception as err:
        tools.recordLog("read config err!"+ str(err))
        print("read config err!"+ str(err))
    return  value


def getPath():
    #获取服务执行程序的路径
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Services\ServerStatus")
        downloadPath =winreg.QueryValueEx(key,"ImagePath")
        path=os.path.dirname(downloadPath[0][1:])
    except Exception as err:
        path=r'c:\windows\system32'
        tools.recordLog('Path change err: '+ str(err))
    return path

#print(readConfig('parameter','sleepsecond'))
