#! python3
# 打开浏览器，访问url,指定谷歌浏览器打开

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
   


use_chrome_open_url('www.163.com')

logging.debug('End   of program'.center(30,'-'))

