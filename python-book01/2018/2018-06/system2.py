#!/usr/bin/env python
# 获取电脑的基本信息
# !/usr/bin/env python  
# -*- coding: utf-8 -*-  
import pprint
import psutil  
import datetime  
import time
  
# 当前时间

def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

now_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))  
print (get_time_stamp())

# 查看cpu的信息  
print (u"物理CPU个数: %s" % psutil.cpu_count(logical=False))

print (get_time_stamp())

#cpu = (str)(psutil.cpu_percent(1)) + '%'

#print (u"cup使用率: %s" % psutil.cpu_percent())

# 查看内存信息,剩余内存.free  总共.total  
free = str(round(psutil.virtual_memory().free/(1024.0*1024.0*1024.0), 2))  
total = str(round(psutil.virtual_memory().total/(1024.0*1024.0*1024.0), 2))  
memory = int(psutil.virtual_memory().total-psutil.virtual_memory().free)/float(psutil.virtual_memory().total)  

print (u"物理内存： %s G" % total)  
print (u"剩余物理内存： %s G" % free ) 
print (u"物理内存使用率： %s %%" % int(memory*100)) 
print (get_time_stamp())

# 系统启动时间  
print (u"系统启动时间: %s" % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))  

# 系统用户  
users_count = len(psutil.users())  
users_list = ",".join([u.name for u in psutil.users()])  
print (u"当前有%s个用户，分别是 %s" % (users_count, users_list)) 
print (get_time_stamp())

# 网卡，可以得到网卡属性，连接数，当前流量等信息
       
net = psutil.net_io_counters()
bytes_sent = '{0:.2f} Mb'.format(net.bytes_recv / 1024/1024)  
bytes_rcvd = '{0:.2f} Mb'.format(net.bytes_sent / 1024/1024)  
print (u"网卡接收流量 %s 网卡发送流量 %s" % (bytes_rcvd, bytes_sent))  
print (get_time_stamp())

io = psutil.disk_partitions()
  

print ('-----------------------------磁盘信息---------------------------------------' ) 
pprint.pprint ("系统磁盘信息：")
#pprint.pprint (io)

j=0
for i in io:
    try:
        o = psutil.disk_usage(i.device)
    except Exception as err:
         print (err)
         pass
    print (io[j][0],end='')
    j+=1
    print (" 总容量："+str(int(o.total/(1024.0*1024.0*1024.0)))+"G",end='')  
    print ("已用容量："+str(int(o.used/(1024.0*1024.0*1024.0)))+"G",end='')  
    print ("可用容量："+str(int(o.free/(1024.0*1024.0*1024.0)))+"G" ) 
print ('-----------------------------进程信息-------------------------------------')







