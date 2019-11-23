import urllib.request
import re,time,os

linkUrl="https://www.mzitu.com/197835/1"
# headers 是用电脑浏览器打开该站，然后f12，network里再刷新该站，点击该网站，取得header，把user-agent复制出来，这样就能下载了
headers =("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
opener =urllib.request.build_opener()
opener.addheaders=[headers]
pat1 = '(<div class="main-image">).+(<div class="pagenavi">)'
pat2 ='(src=).+(.jpg)'
pat3 ='(href=").+( )'
i=1

for i in range(2):
    data = opener.open(linkUrl).read()
    data= str(data)
    #print (data)
    resultPage = re.search(pat1,data)   #下载当前url的页面
    resultImg = re.search(pat2,resultPage.group()) #过滤出含图片和下一个url
    resultLink = re.search(pat3,resultPage.group()) #过滤出下一个url
    linkUrl = str.split(resultLink.group(),"\"")[1]
    imgUrl =  str.split(resultImg.group(),"\"")[1]
    print (imgUrl,linkUrl)
    linkStr=str.split(linkUrl,'/')
    nameImg = linkStr[-2]+"_"+linkStr[-1]+".jpg"  # 利用下载路径生成图片名称，不会重复
    print(os.path.join("mm",nameImg))
    x=1
    try:
        urllib.request.urlretrieve(imgUrl,filename=nameImg)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            x+=1
            print (e.code)
        if hasattr(e,"reason"):
            x+=1
            print (e.reason)




'''

data = opener.open(url).read()
fhandle = open("mm1.html","wb")
fhandle.write(data)
fhandle.close()
'''