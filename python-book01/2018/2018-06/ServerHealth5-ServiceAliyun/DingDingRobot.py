#实现向钉钉机器人发送报警信息
import requests
import json
import tools

import globalvar as gl
import configRead


# url = r'https://oapi.dingtalk.com/robot/send?access_token=f83e486b8996f287ae624746f36e472d127b79ab761c032cc09cad06dd12b416'

def sendMsgtoDingDing(mydict,sendgroup,msg):
    body={
    "msgtype": "link", 
    "link":
    {
       "text":"群机器人是钉钉群的高级扩展功能。", 
       "title": "服务器状态信息", 
       "picUrl": "", 
       "messageUrl": "http://47.91.157.89:999/"
    }
    }
    headers = {'content-type': "application/json"}
    url=sendgroup[mydict][2]
            
    body['link']["text"] =msg
    body['link']["messageUrl"] =sendgroup[mydict][3]

    
    
    response = requests.post(url, data = json.dumps(body), headers = headers)
    res = eval(response.text)   # eval 转为字典，不能防注入
    if (response.status_code ==200) and (res['errcode'] ==0):
        tools.recordLog('DingDingCode:'+mydict+' '+str(res['errcode'])+':'+res['errmsg'])
        print(res['errmsg'])
        return 0  #发送成功
    else:
        tools.recordLog('DingDingCode:'+mydict+' '+str(res['errcode'])+':'+res['errmsg'])
        print(res['errmsg'])
        return int(res['errcode'])  #未发送或发送失败


#检查发送告警是否在允许的时间之内
def timeCheck(sendgroup,mydict):
    #sendgroup = configRead.readConfig('dingding','sendgroup')
    runTime =sendgroup[mydict][5]
    print(runTime)
    currentTime = tools.get_hour()
    print(currentTime)

    #在允许的时间段内扫描
    if (currentTime>=runTime[0]) and (currentTime<=runTime[1]):
        print(mydict+"时间命中")
        tools.recordLog(mydict+"时间命中")
        return True
    else:
        print(mydict+"时间没命中")
        tools.recordLog(mydict+"时间没有命中")
        tools.recordLog("runTime0"+runTime[0])
        tools.recordLog("runTime1"+runTime[1])
        print("runTime0"+runTime[0])
        print("runTime1"+runTime[1])
        return False    

    
def sendAlarm(msgDict,plan):

    #第一个body 是纯消息，不带链接
    #body = {"msgtype": "text","text": {"content": "测试"},"at": {"atMobiles": ["18678966660"], "isAtAll": "false"}} 
    
    sendgroup = configRead.readConfig('dingding','sendgroup')
    #count判断频率使用
    count= int(gl.getvalue('count'))+1
    gl.setvalue('count',str(count))
    print('count='+str(count))
    tools.recordLog('count='+str(count))

    for mydict in  sendgroup.keys():
        # (count % int(sendgroup[mydict][4]))==0 是执行频率 ，例如运维群每5分钟通知一次，那sendgroup[mydict][4]=5就好
        print(mydict+' 频率： '+sendgroup[mydict][4])

        if timeCheck(sendgroup,mydict)==False:
            continue

        print(mydict+' 尝试'+'plan='+str(plan))
        print('count='+str(count)+'余数：'+str((count % int(sendgroup[mydict][4]))))
                            
        #以下判断，当plan=1时，无条件执行扫描
        if ((sendgroup[mydict][0].upper()=='ON') and ((count % int(sendgroup[mydict][4]))==0)) or ((sendgroup[mydict][0].upper()=='ON') and (plan==1)):
            print(mydict+' 命中： '+'plan='+str(plan)+'\n')
            tools.recordLog(mydict+' 命中： '+'plan='+str(plan))
            tools.recordLog('count='+str(count)+' 命中'+str((count % int(sendgroup[mydict][4]))))
            
            if sendgroup[mydict][1].upper()=='SERVERHEALTH':
                msg =  msgDict['ServerHealth']
            elif sendgroup[mydict][1].upper()=='SEVICEHEALTH':
                msg =  msgDict['SeviceHealth']
            elif sendgroup[mydict][1].upper()=='ECSHEALTH':
                msg =  msgDict['ECSHealth']
                
            msg = msgPlan(msg,plan,sendgroup[mydict][1].upper())
            
            sendMsgtoDingDing(mydict,sendgroup,msg)
           

def msgPlan(msg,plan,fuwu):
    if (len(msg)<2) and (plan==1):
        print('计划扫描，所有服务器状态正常,按计划发送报告') 
        if fuwu=='ECSHEALTH':
            msg=''
            tools.recordLog('ECSHEALTH 暂没有ECS到期，无需报警')
        else:
            tools.recordLog('计划扫描: '+fuwu+' 所有服务器状态正常')
    elif (len(msg)<2) and (plan==0):
        print('定时扫描：'+fuwu+' 所有服务器状态正常,不发送报警') 
        msg=''
        tools.recordLog('定时扫描：'+fuwu+' 所有服务器状态正常,不发送报警')
    return msg
    




##    body['text']["content"] =msg
##    body['at']["atMobiles"] =configRead.readConfig('dingding','atMobiles')
##    body['at']["isAtAll"] =configRead.readConfig('dingding','isAtAll')
    
#gl.init()
    #报警的触发计数器
#gl.setvalue('count', '0')
#msg = {'ServerHealth':'','SeviceHealth':'','ECSHealth':''}
#sendAlarm(msg,0)    

#sendAlarm('xxxxxxxxxxxxx\nxxxxxxxxxxxxx\n',1)
# 返回信息
#print (response.text)   ， 成功返回{"errcode":0,"errmsg":"ok"}
# 返回响应头
#print (response.status_code) ， 成功返回200
