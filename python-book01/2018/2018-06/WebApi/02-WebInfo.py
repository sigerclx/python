# coding:utf-8

import logging
import psutil   
import time
import json
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))


# 定义函数，两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'application/json;charset=utf-8')])

    d = parse_qs(environ['QUERY_STRING'])
    key = d.get('key', [''])[0] # 返回第一个age值.
        
    logging.debug('key='+key)

    
    if key=='getinfo':

        logging.debug(key)
        info=sysInfo()
        json_str = json.dumps(info,ensure_ascii=False,indent=4)
    
        return [json_str.encode('utf-8')]
    else:
        logging.debug('Noget')
        info = {"status": "none"}
        json_str = json.dumps(info,ensure_ascii=False,indent=4)
        return [json_str.encode('utf-8')]

    

def sysInfo():
    info={}
    
    line={}
    line.setdefault('CPU核心',str(psutil.cpu_count()))
    line.setdefault('CPU利用率',str(int(psutil.cpu_percent())) + '%')
    info['CPU']=line

    line={}
    line.setdefault('空闲内存G',str(round(psutil.virtual_memory().free/(1024.0*1024.0*1024.0), 2)))
    line.setdefault('总内存G',str(int(round(psutil.virtual_memory().total/(1024.0*1024.0*1024.0)))))
    line.setdefault('内存利用率',str(int((psutil.virtual_memory().total-psutil.virtual_memory().free)/float(psutil.virtual_memory().total)*100))+ '%')
    info['Memory'] =line
    	
    line={}
    
    io = psutil.disk_partitions()
    j=0
    for i in io:
        diskstr=[]
        o = psutil.disk_usage(i.device)
        disk='硬盘'+io[j][0].strip(r':\\')
        diskstr.append(str(int(o.free/(1024.0*1024.0*1024.0)))+"G") 
        diskstr.append(str(int(o.total/(1024.0*1024.0*1024.0)))+"G") 
        line.setdefault(disk+'可用容量',diskstr)
        j+=1

    info['Disk']=line
    return info

if __name__ == "__main__":
    port = 91
  
    httpd = make_server("0.0.0.0", port, application)
    print ("Health serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

