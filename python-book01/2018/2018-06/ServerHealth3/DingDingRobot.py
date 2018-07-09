#实现向钉钉机器人发送报警信息
import requests
import json
import tools

import configRead


# url = r'https://oapi.dingtalk.com/robot/send?access_token=f83e486b8996f287ae624746f36e472d127b79ab761c032cc09cad06dd12b416'  
def sendAlarm(msg):
    
    body = {"msgtype": "text","text": {"content": "测试"},"at": {"atMobiles": ["18678966660"], "isAtAll": "false"}}
    headers = {'content-type': "application/json"}
    if len(msg)<2:
       print('报警数据为空！') 
       msg='所有服务器状态正常'
       tools.recordLog(msg)

    body['text']["content"] =msg
    

    url =configRead.readConfig('dingding','url')
    body['at']["atMobiles"] =configRead.readConfig('dingding','atMobiles')
    

    # 这里有个细节，如果body需要json形式的话，需要做处理
    # 可以是data = json.dumps(body)
    response = requests.post(url, data = json.dumps(body), headers = headers)
    # 也可以直接将data字段换成json字段，2.4.3版本之后支持
    #print(response['errmsg'])
    res = eval(response.text)   # eval 转为字典，不能防注入
    if (response.status_code ==200) and (res['errcode'] ==0):
        tools.recordLog('DingDingCode:'+str(res['errcode'])+':'+res['errmsg'])
        return 0  #发送成功
    else:
        tools.recordLog('DingDingCode:'+str(res['errcode'])+':'+res['errmsg'])
        return 1  #发送失败


# 返回信息
#print (response.text)   ， 成功返回{"errcode":0,"errmsg":"ok"}
# 返回响应头
#print (response.status_code) ， 成功返回200
