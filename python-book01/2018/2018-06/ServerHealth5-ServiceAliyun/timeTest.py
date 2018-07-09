import time
import datetime
import os
import tools
import configRead


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
    if first_time<second_time:
       first_time, second_time = second_time, first_time
    return (datetime.datetime.strptime(first_time,"%H:%M:%S") - datetime.datetime.strptime(second_time,"%H:%M:%S")).seconds



sleepsecond = configRead.readConfig('parameter','sleepsecond')
runtime = configRead.readConfig('parameter','runtime')


currentTime=tools.get_hour()
tools.recordLog(str(tools.time_cmp(currentTime,i)))
print('sleepsecond='+str(sleepsecond))
print(runtime)
for i in runtime:
    if tools.time_cmp(currentTime,i)<sleepsecond:
        print("运行时间到了")
    else:
        print("未到运行时间")
