#! python3
# 打开浏览器，根据webUrl.py生成weblist.html

import pprint
import gushi
import random
import copy

import os,zipfile
import logging
import webbrowser as web
import webUrl

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)   # 加这句话，就是log全部禁止，不加，就可以log打印了
logging.debug('Start of program'.center(30,'-'))



#谷歌浏览器  
def use_chrome_open_url(url):  
    browser_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    web.register('chrome', None,web.BackgroundBrowser(browser_path))  
    web.get('chrome').open_new_tab(url)  
   

webUrlFile=open('weblist.html','w',encoding='utf-8')

logging.debug(len(webUrl.url))

logging.debug(list(webUrl.url.keys())[0])

webUrlFile.write(r'''
    <style type=text/css>
    table.gridtable
        {
            font-family: verdana,arial,sans-serif;
            font-size:14px;
            color:#333333;
            border-width: 1px;
            border-color: #666666;
        }
    table.gridtable th {
            border-width: 1px;
            padding: 8px;
            border-style: solid;
            border-color: #666666;
            background-color: #dedede;
        }
        table.gridtable td {
            border-width: 0px;
            padding: 8px;
            border-style: solid;
            border-color: #666666;
            background-color: #ffffff;}
    </style>''')


webUrlFile.write('\n<table class=gridtable align=\'left\'>\n')

for i in range(len(webUrl.url)):
    currentKey = str(list(webUrl.url.keys())[i])
    #logging.debug(webUrl.url[currentKey][0],currentKey)
    webUrlFile.write('<tr><td>'+currentKey+' : </td></tr>')
    webUrlFile.write('\n<td>后台</td>')
    
    #读写后台域名
    for k in range(len(webUrl.url[currentKey][0])):
        webUrlFile.write('<td><a href=\'http://'+webUrl.url[currentKey][0][k]+'\' target=_blank>'+webUrl.url[currentKey][0][k]+'</a></td>')
    webUrlFile.write('</tr>')
    webUrlFile.write('\n<td>API</td>')

    #读写API域名
    for h in range(len(webUrl.url[currentKey][1])):
        webUrlFile.write('<td><a href=\'http://'+webUrl.url[currentKey][1][h]+'\' target=_blank>'+webUrl.url[currentKey][1][h]+'</a></td>')
    webUrlFile.write('</tr>')
    
    webUrlFile.write('\n<td>Web</td>')
    
    #读写Web域名
    for j in range(len(webUrl.url[currentKey][2])):
        if j<8:
            webUrlFile.write('<td><a href=\'http://'+webUrl.url[currentKey][2][j]+'\' target=_blank>'+webUrl.url[currentKey][2][j]+'</a></td>')
        else:
            if j==8:
                webUrlFile.write('</tr>\n<tr><td></td>')
            webUrlFile.write('<td><a href=\'http://'+webUrl.url[currentKey][2][j]+'\' target=_blank>'+webUrl.url[currentKey][2][j]+'</a></td>')
    webUrlFile.write('</tr><tr><td></td></tr><tr><td></td></tr>\n')
    
webUrlFile.write('</table>')
    
    
webUrlFile.close()



logging.debug('End   of program'.center(30,'-'))

