import requests
import json

# url = r'https://oapi.dingtalk.com/robot/send?access_token=f83e486b8996f287ae624746f36e472d127b79ab761c032cc09cad06dd12b416'  
url = r'https://oapi.dingtalk.com/robot/send?access_token=2ec099ae725735a6e07567864c2c835aa4a7bcdb2eb4c4b789fdd17151b8f6dc'
body = {"msgtype": "text","text": {"content": "测试，聚银彩DB CPU > 95%\n测试，聚银彩DB MEM > 95\n"},"at": {"atMobiles": ["18678966660"], "isAtAll": "false"}}
headers = {'content-type': "application/json"}
 
#print type(body)
#print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
response = requests.post(url, data = json.dumps(body), headers = headers)
# 也可以直接将data字段换成json字段，2.4.3版本之后支持
# response  = requests.post(url, json = body, headers = headers)
 
# 返回信息
print (response.text)
# 返回响应头
print (response.status_code)
