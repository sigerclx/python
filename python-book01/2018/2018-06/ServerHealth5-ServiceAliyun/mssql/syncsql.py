import pymssql
import datetime
import time
import tools
# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称

def getSyncSeconds(list):
    
    #conn = pymssql.connect('183.111.122.191', 'sa', 'VTTthL5oLgyVckWdbd2EFw==', 'YT')
    conn = pymssql.connect(list[1], list[2],list[3], list[4])

    cursor = conn.cursor()

    sqltext =r"""
    SELECT top 1 
          [CreateTime]
      FROM [dbo].[LotteryHistoryNumCache]
      order by [CreateTime] desc
      """
    timeChayi='0'
    try:
        cursor.execute(sqltext,'timeout=6')
        row = cursor.fetchone()

        while row:

            currentTime=tools.get_hour()
            print(currentTime)
            thisTime= row[0].strftime('%H:%M:%S')
            print(thisTime)
            timeChayi= tools.time_cmp(currentTime,thisTime)
            print(timeChayi)
            row = cursor.fetchone()
            
    except Exception as err:
        print(str(err))
        timeChayi='Down'
    finally:
        cursor.close()
        conn.close()

    return timeChayi

##list1=["NBA同步", "183.111.122.155", "sa", "VTTthL5oLgyVckWdbd2EFw==", "Xinda"]
##list2=["JYC同步", "183.111.122.177", "sa", "VTTthL5oLgyVckWdbd2EFw==", "JYC"]
##list3=["YT同步", "183.111.122.191", "sa", "VTTthL5oLgyVckWdbd2EFw==", "YT"]
##		
##
##print(getSyncSeconds(list2))
