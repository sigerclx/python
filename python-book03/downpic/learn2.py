import requests
from bs4 import BeautifulSoup

# 定制请求头
headers = {'Referer':'https://www.mzitu.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36'}
main_img ='https://i5.meizitu.net/2019/08/06b18.jpg'
res = requests.get(main_img, headers=headers)
if res.status_code == 200:
    with open('3.jpg', 'wb') as f:
        f.write(res.content)
        print('成功保存图片')  