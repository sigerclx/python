import requests
import os
import re
 
'''
妹子图网站的特殊的地方在于网站服务器与图片服务器分开，
任何非网站服务器的对图片资源的请求都会被403  forbiden掉
因此需要在requests中设置代理服务器为网站服务器的ip，避开图片服务器的过滤
''' 
# 请求头设置模拟的浏览器版本
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# 创建链接对象

session = requests.session()
# 设置为短链接，防止连接数过多 程序报错
session.keep_alive = False
img_url= 'https://i5.meizitu.net/2019/08/06b11.jpg'
img = session.get(img_url, proxies={'http': '60.214.102.37'}, headers=headers)
        
with open("mm1.jpg", 'wb') as f:
    f.write(img.content)
              

