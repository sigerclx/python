# coding:utf-8

import pprint
import psutil  
import datetime  
import time
import json
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


# 定义函数，两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'application/json;charset=utf-8')])
    info={}
    info['物理CPU']=str(psutil.cpu_count(logical=False))
    info['cpu用量']=str(psutil.cpu_percent(1)) + '%'
    json_str = json.dumps(info,ensure_ascii=False,indent=4)
    return [json_str.encode('utf-8')]


if __name__ == "__main__":
    port = 90
    
    httpd = make_server("0.0.0.0", port, application)
    print ("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()
