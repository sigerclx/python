#! python3
# 打开浏览器，根据webUrl.py生成weblist.html

import pprint
import logging
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

logging.debug(len(webUrl.urlDict))

logging.debug(list(webUrl.urlDict.keys())[0])

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
            padding: 1px;
            border-style: solid;
            border-color: #666666;
            background-color: #dedede;
        }
    table.gridtable td {
            border-width: 1px;
            padding: 6px;
            border-style: solid;
            border-color: #666666;
            background-color: #ffffff;}
            
    </style>''')


webUrlFile.write('\n<table class=gridtable align=\'left\'>\n')

sites=list(webUrl.urlDict.keys())
column = 9 # 超过6列就折行显示

for i in range(len(sites)):
    webUrlFile.write('<tr><td style=\'border-style:none\'>'+sites[i]+' : </td></tr>\n<tr>')
    for j in range(len(webUrl.urlDict[sites[i]])):
        webUrlFile.write('<td>'+webUrl.urlDict[sites[i]][j][0]+'</td>')
 
        for p in range(1,len(webUrl.urlDict[sites[i]][j])):
            url = r'http://'+webUrl.urlDict[sites[i]][j][p]
            webUrlFile.write('<td><a href=\''+url+'\' target=_blank>'+webUrl.urlDict[sites[i]][j][p]+'</a></td>')
            yushu = int(p % column)
            if p>=column and yushu==0 and p!=(len(webUrl.urlDict[sites[i]][j])-1):
                webUrlFile.write('</tr><tr><td style=\'border-style:none\'></td>')
            
        webUrlFile.write('</tr>')
            
    webUrlFile.write('</tr>')
webUrlFile.write('</table>')
webUrlFile.close()



logging.debug('End   of program'.center(30,'-'))

