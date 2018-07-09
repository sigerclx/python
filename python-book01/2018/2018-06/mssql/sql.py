import pymssql
import datetime
import time
# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称

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
    #first_time=int(first_time)
    #second_time =int(second_time)
    if (first_time==0) or (second_time==0):
        return 0
    #if first_time<second_time:
    #   first_time, second_time = second_time, first_time
    return (datetime.datetime.strptime(first_time,"%H:%M:%S") - datetime.datetime.strptime(second_time,"%H:%M:%S")).seconds


conn = pymssql.connect('183.111.122.191', 'sa', 'VTTthL5oLgyVckWdbd2EFw==', 'YT')

cursor = conn.cursor()

sqltext =r"""
SELECT top 1 
      [CreateTime]
  FROM [dbo].[LotteryHistoryNumCache]
  order by [CreateTime] desc
  """



try:
    cursor.execute(sqltext)
    row = cursor.fetchone()

    while row:

        currentTime=get_hour()
        print(currentTime)
        thisTime= row[0].strftime('%H:%M:%S')
        print(thisTime)
        print(time_cmp(currentTime,thisTime))
        row = cursor.fetchone()

except Exception as err:
    print(str(err))
finally:
    conn.close()

